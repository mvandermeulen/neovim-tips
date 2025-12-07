# Title: AES256 File Encryption with GPG
# Category: advanced_tricks
# Tags: encryption, security, file-operations
---
Use GPG to encrypt and decrypt files with AES256 encryption directly from Vim

```vim
function Scramble()
  %!gpg -q --cipher-algo aes256 --symmetric --armor 2>/dev/null
endfunction

function Unscramble()
  %!gpg -q --cipher-algo aes256 --decrypt --armor 2>/dev/null
endfunction
```
```lua
function _G.encrypt_file()
  vim.cmd('%!gpg -q --cipher-algo aes256 --symmetric --armor 2>/dev/null')
end

function _G.decrypt_file()
  vim.cmd('%!gpg -q --cipher-algo aes256 --decrypt --armor 2>/dev/null')
end

vim.keymap.set('n', '<F7>', _G.encrypt_file, { desc = 'Encrypt file' })
vim.keymap.set('n', '<F8>', _G.decrypt_file, { desc = 'Decrypt file' })
```

**Source:** ** https://vim.fandom.com/wiki/AES256_encryption_in_Vim
***
# Title: Auto Highlight Current Word When Idle
# Category: advanced_tricks
# Tags: highlighting, search, cursor-tracking
---
Automatically highlight all occurrences of the word under the cursor when idle, useful for exploring unfamiliar source code

```vim
" Highlight all instances of word under cursor
nnoremap z/ :if AutoHighlightToggle()<Bar>set hls<Bar>endif<CR>
function! AutoHighlightToggle()
  let @/ = ''
  if exists('#auto_highlight')
    au! auto_highlight
    augroup! auto_highlight
    setl updatetime=4000
    echo 'Highlight current word: off'
    return 0
  else
    augroup auto_highlight
      au!
      au CursorHold * let @/ = '\V\<'.escape(expand('<cword>'), '\').'\'>
    augroup end
    setl updatetime=500
    echo 'Highlight current word: ON'
    return 1
  endif
endfunction
```
```lua
local function auto_highlight_toggle()
  -- Toggle highlighting of current word
  local ns = vim.api.nvim_create_namespace('auto_highlight')
  
  if vim.b.auto_highlight then
    -- Turn off highlighting
    vim.api.nvim_buf_clear_namespace(0, ns, 0, -1)
    vim.b.auto_highlight = false
    vim.o.updatetime = 4000
    print('Highlight current word: off')
  else
    -- Turn on highlighting
    vim.api.nvim_create_autocmd('CursorHold', {
      group = vim.api.nvim_create_augroup('AutoHighlight', { clear = true }),
      callback = function()
        local word = vim.fn.expand('<cword>')
        vim.fn.setreg('/', '\V\<' .. vim.fn.escape(word, '\') .. '\>')
        vim.o.hlsearch = true
      end
    })
    vim.o.updatetime = 500
    vim.b.auto_highlight = true
    print('Highlight current word: ON')
  end
end

-- Optional: Create a keymap to toggle
vim.keymap.set('n', 'z/', auto_highlight_toggle, { desc = 'Toggle auto word highlight' })
```

**Source:** ** https://vim.fandom.com/wiki/Auto_highlight_current_word_when_idle
***
# Title: Decode MIME Base64 and Quoted-Printable Encoding
# Category: advanced_tricks
# Tags: encoding, perl, text-processing
---
Add custom commands to decode MIME-encoded text directly in Vim using Perl modules

```vim
command! -range=% Decode64 :w | <line1>,<line2>delete | let foo = @"
 \ | perl use MIME::Base64 (); my $foo=VIM::Eval(foo); my ($r, $c)=$curwin->Cursor(); $curbuf->Append($r-1, split '\n', MIME::Base64::decode($foo));

command! -range=% DecodeQP :w | <line1>,<line2>delete | let foo = @"
 \ | perl use MIME::QuotedPrint (); my $foo=VIM::Eval(foo); my ($r, $c)=$curwin->Cursor(); $curbuf->Append($r-1, split '\n', MIME::QuotedPrint::decode_qp($foo));
```
```lua
-- Note: Requires Vim compiled with Perl support
vim.api.nvim_create_user_command('Decode64', function()
  local lines = vim.api.nvim_buf_get_lines(0, 0, -1, false)
  local decoded_lines = vim.fn.system('perl -MMIME::Base64 -e "print decode_base64(join(\'\', <>))"', lines)
  vim.api.nvim_buf_set_lines(0, 0, -1, false, vim.split(decoded_lines, '\n'))
end, {})

vim.api.nvim_create_user_command('DecodeQP', function()
  local lines = vim.api.nvim_buf_get_lines(0, 0, -1, false)
  local decoded_lines = vim.fn.system('perl -MMIME::QuotedPrint -e "print decode_qp(join(\'\', <>))"', lines)
  vim.api.nvim_buf_set_lines(0, 0, -1, false, vim.split(decoded_lines, '\n'))
end, {})
```

**Source:** ** https://vim.fandom.com/wiki/Decode_MIME_text_using_Perl_in_Vim
***
# Title: Enhanced Hex Mode Editing in Vim
# Category: advanced_tricks
# Tags: hex-editing, binary-files, file-manipulation
---
Provides an improved method for editing binary files in hex mode using xxd, with easy toggling and automatic conversion

```vim
" Toggle hex mode command
command -bar Hexmode call ToggleHex()

function ToggleHex()
  let l:modified=&mod
  let l:oldreadonly=&readonly
  let &readonly=0
  let l:oldmodifiable=&modifiable
  let &modifiable=1
  if !exists("b:editHex") || !b:editHex
    let b:oldft=&ft
    let b:oldbin=&bin
    setlocal binary
    silent :e
    let &ft="xxd"
    let b:editHex=1
    %!xxd
  else
    let &ft=b:oldft
    if !b:oldbin
      setlocal nobinary
    endif
    let b:editHex=0
    %!xxd -r
  endif
  let &mod=l:modified
  let &readonly=l:oldreadonly
  let &modifiable=l:oldmodifiable
endfunction

" Mapping to toggle hex mode
nnoremap <C-H> :Hexmode<CR>
```
```lua
local function toggle_hex()
  local modified = vim.o.modified
  local readonly = vim.o.readonly
  local modifiable = vim.o.modifiable

  vim.o.readonly = false
  vim.o.modifiable = true

  if not vim.b.edit_hex then
    vim.b.old_ft = vim.o.filetype
    vim.b.old_bin = vim.o.binary
    vim.o.binary = true
    vim.cmd('silent e')
    vim.o.filetype = 'xxd'
    vim.b.edit_hex = true
    vim.cmd('%!xxd')
  else
    vim.o.filetype = vim.b.old_ft
    if not vim.b.old_bin then
      vim.o.binary = false
    end
    vim.b.edit_hex = false
    vim.cmd('%!xxd -r')
  end

  vim.o.modified = modified
  vim.o.readonly = readonly
  vim.o.modifiable = modifiable
end

-- Create command and mapping
vim.api.nvim_create_user_command('Hexmode', toggle_hex, {})
vim.keymap.set('n', '<C-H>', ':Hexmode<CR>', { noremap = true, silent = true })
```

**Source:** ** https://vim.fandom.com/wiki/Improved_hex_editing
***
# Title: Preview HTML Text in Vim Buffer
# Category: advanced_tricks
# Tags: text-extraction, web-preview, buffer-management
---
Extract and view the text content of an HTML file or URL directly in a Vim buffer using a text-based browser

```vim
function! ViewHtmlText(url)
  if !empty(a:url)
    new
    setlocal buftype=nofile bufhidden=hide noswapfile
    execute 'r !elinks ' . a:url . ' -dump -dump-width ' . winwidth(0)
    1d
  endif
endfunction

" Mappings for different preview scenarios
nnoremap <Leader>H :update<Bar>call ViewHtmlText(expand('%:p'))<CR>
vnoremap <Leader>h y:call ViewHtmlText(@@)<CR>
nnoremap <Leader>h :call ViewHtmlText(@+)<CR>
```
```lua
function _G.view_html_text(url)
  if url ~= '' then
    vim.cmd('new')
    vim.api.nvim_buf_set_option(0, 'buftype', 'nofile')
    vim.api.nvim_buf_set_option(0, 'bufhidden', 'hide')
    vim.api.nvim_buf_set_option(0, 'swapfile', false)
    
    local output = vim.fn.system('elinks ' .. url .. ' -dump -dump-width ' .. vim.fn.winwidth(0))
    vim.api.nvim_buf_set_lines(0, 0, 1, false, vim.split(output, '\n'))
    vim.cmd('normal! gg')
  end
end

-- Mappings for different preview scenarios
vim.keymap.set('n', '<Leader>H', function()
  vim.cmd.update()
  _G.view_html_text(vim.fn.expand('%:p'))
end)

vim.keymap.set('v', '<Leader>h', function()
  local selected_text = vim.fn.getreg('*')
  _G.view_html_text(selected_text)
end)

vim.keymap.set('n', '<Leader>h', function()
  _G.view_html_text(vim.fn.getreg('+'))
end)
```

**Source:** ** https://vim.fandom.com/wiki/Preview_file_on_localhost
***
