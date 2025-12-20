# Title: Silent and no-remap mappings
# Category: Key Mappings
# Tags: noremap, silent, mapping, recursive
---
Use `noremap` and `<silent>` modifiers to create safe, non-recursive mappings that don't echo commands.
Or:

```vim
:nnoremap <silent> <leader>w :w<CR>
:inoremap jk <Esc>
" noremap prevents recursive mapping, silent suppresses command echo
" Use noremap by default to avoid unexpected behavior
```

```lua
vim.keymap.set('n', '<leader>w', '<Cmd>w<CR>', { silent = true })
vim.keymap.set('i', 'jk', '<Esc>')
```

**Source:** Community contributed
***
# Title: Expression mappings
# Category: Key Mappings
# Tags: expr, expression, mapping, dynamic
---
Use `<expr>` mappings to create dynamic key behaviors that evaluate expressions.
Or:

```vim
:inoremap <expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"
:inoremap <expr> <CR> pumvisible() ? "\<C-y>" : "\<CR>"
:nnoremap <expr> n 'Nn'[v:searchforward]
" Tab for completion navigation, Enter to accept
```

```lua
vim.keymap.set('i', '<Tab>', function()
    return vim.fn.pumvisible() == 1 and '<C-n>' or '<Tab>'
end, { expr = true })
vim.keymap.set('i', '<CR>', function()
    return vim.fn.pumvisible() == 1 and '<C-y>' or '<CR>'
end, { expr = true })
vim.keymap.set('n', 'n', function()
    return vim.v.searchforward == 1 and 'n' or 'N'
end, { expr = true })
```

**Source:** Community contributed
***
# Title: Script-local mappings
# Category: Key Mappings
# Tags: script, local, SID, unique
---
Use `<SID>` (Script ID) to create mappings that call script-local functions, avoiding global namespace pollution.
Or:

```vim
:nnoremap <silent> <F5> :call <SID>CompileAndRun()<CR>
function! s:CompileAndRun()
    " Script-local function
    execute '!gcc % -o %:r && ./%:r'
endfunction
" <SID> ensures function is only accessible from this script
```

```lua
local function compile_and_run()
    vim.cmd('!ggc % -o %:r && ./%:r')
end

vim.keymap.set('n', '<F5>', compile_and_run, { silent = true })
```

**Source:** Community contributed
***
# Title: Abbreviations vs mappings
# Category: Key Mappings
# Tags: abbreviation, iabbrev, expand, text
---
Use abbreviations for text expansion that only triggers after whitespace, unlike mappings which are immediate.
Or:

```vim
:iabbrev teh the
:iabbrev @@ your.email@domain.com
:iabbrev dts <C-r>=strftime('%Y-%m-%d')<CR>
" Abbreviations expand after whitespace/punctuation
" Mappings activate immediately when typed
```

```lua
vim.keymap.set('ia', 'teh', 'the')
vim.keymap.set('ia', '@@', 'your.email@domain.com')
vim.keymap.set('ia', 'dts', function() 
    return os.date('%Y-%m-%d')
end, { expr = true })
```

**Source:** Community contributed
***
# Title: Mapping special characters
# Category: Key Mappings
# Tags: special, characters, escape, literal
---
Use proper escaping and notation for mapping special characters like quotes, backslashes, and pipes.
Or:

```vim
:nnoremap <leader>" ciw"<C-r>""<Esc>
:nnoremap <leader>' ciw'<C-r>"'<Esc>
:nnoremap <leader>\ :nohlsearch<CR>
" Surround word with quotes, backslash to clear search
```

```lua
vim.keymap.set('n', '<leader>"', 'ciw"<C-r>""<Esc>')
vim.keymap.set('n', "<leader>'", "ciw'<C-r>\"'<Esc>")
vim.keymap.set('n', '<leader>\\', '<Cmd>nohlsearch<CR>')
```

**Source:** Community contributed
***
# Title: Recursive abbreviations
# Category: Key Mappings
# Tags: abbreviation, recursive, noreabbrev, expand
---
Use `noreabbrev` to prevent recursive abbreviation expansion, similar to noremap for mappings.
Or:

```vim
:abbreviate W w
:noreabbrev Wq wq
:abbreviate Q q
" 'W' expands to 'w', but 'Wq' won't recursively expand the 'W' part
```

```lua
vim.keymap.set('ca', 'W', 'w')
vim.keymap.set('ca', 'Wq', 'wq')
vim.keymap.set('ca', 'Q', 'q')
```

**Source:** Community contributed
***
# Title: Visual mode mappings
# Category: Key Mappings
# Tags: visual, vnoremap, selection, range
---
Use visual mode mappings to operate on selections with custom key combinations.
Or:

```vim
:vnoremap <leader>s :sort<CR>
:vnoremap <leader>u :!uniq<CR>
:vnoremap * y/\V<C-r>"<CR>
:vnoremap # y?\V<C-r>"<CR>
" Sort selection, remove duplicates, search for selection
```

```lua
vim.keymap.set('v', '<leader>s', '<Cmd>sort<CR>')
vim.keymap.set('v', '<leader>u', '<Cmd>!uniq<CR>')
vim.keymap.set('v', '*', 'y/\\V<C-r>"<CR>')
vim.keymap.set('v', '#', 'y?\\V<C-r>"<CR>')
```

**Source:** Community contributed
***
# Title: Command-line mappings
# Category: Key Mappings
# Tags: cnoremap, command, line, navigation
---
Use command-line mode mappings to improve command-line editing with familiar key bindings.
Or:

```vim
:cnoremap <C-a> <Home>
:cnoremap <C-e> <End>
:cnoremap <C-b> <Left>
:cnoremap <C-f> <Right>
:cnoremap <C-d> <Delete>
" Emacs-style command line navigation
```

```lua
vim.keymap.set('c', '<C-a>', '<Home>')
vim.keymap.set('c', '<C-e>', '<End>')
vim.keymap.set('c', '<C-b>', '<Left>')
vim.keymap.set('c', '<C-f>', '<Right>')
vim.keymap.set('c', '<C-d>', '<Delete>')
```

**Source:** Community contributed
***
# Title: Operator-pending mappings
# Category: Key Mappings
# Tags: onoremap, operator, pending, motion
---
Use operator-pending mappings to create custom text objects and motions.
Or:

```vim
:onoremap in( :<C-u>normal! f(vi(<CR>
:onoremap an( :<C-u>normal! f(va(<CR>
:onoremap in{ :<C-u>normal! f{vi{<CR>
" Creates 'in(' and 'an(' text objects
" Now you can use din( to delete inside next parentheses
```

```lua
vim.keymap.set('o', 'in(', '<Cmd><C-u>normal! f(vi(<CR>')
vim.keymap.set('o', 'an(', '<Cmd><C-u>normal! f(va(<CR>')
vim.keymap.set('o', 'in{', '<Cmd><C-u>normal! f{va{<CR>')
```

**Source:** Community contributed
***
# Title: Terminal mode mappings
# Category: Key Mappings
# Tags: tnoremap, terminal, mode, escape
---
Use terminal mode mappings to control built-in terminal behavior and key bindings.
Or:

```vim
:tnoremap <Esc> <C-\><C-n>
:tnoremap <C-w>h <C-\><C-n><C-w>h
:tnoremap <C-w>j <C-\><C-n><C-w>j
:tnoremap <C-w>k <C-\><C-n><C-w>k
:tnoremap <C-w>l <C-\><C-n><C-w>l
" Escape to exit terminal mode, window navigation
```

```lua
vim.keymap.set('t', '<Esc>', '<C-\\><C-n>')
vim.keymap.set('t', '<C-w>h', '<C-\\><C-n><C-w>h')
vim.keymap.set('t', '<C-w>j', '<C-\\><C-n><C-w>j')
vim.keymap.set('t', '<C-w>k', '<C-\\><C-n><C-w>k')
vim.keymap.set('t', '<C-w>l', '<C-\\><C-n><C-w>l')
```

**Source:** Community contributed
***
# Title: Multiple key mappings
# Category: Key Mappings
# Tags: multiple, keys, sequence, chain
---
Create mappings that respond to multiple key sequences or provide alternative bindings.
Or:

```vim
:nnoremap <leader>fs :w<CR>
:nnoremap <leader>ff :find<Space>
:nnoremap <leader>fb :buffer<Space>
:nnoremap <C-s> :w<CR>
:inoremap <C-s> <Esc>:w<CR>a
" Multiple ways to save: <leader>fs and <C-s>
```

```lua
vim.keymap.set('n', '<leader>fs', '<Cmd>w<CR>')
vim.keymap.set('n', '<leader>ff', '<Cmd>find<Space>')
vim.keymap.set('n', '<leader>fb', '<Cmd>buffer<Space>')
vim.keymap.set('n', '<C-s>', '<Cmd>w<Space>')
vim.keymap.set('i', '<C-s>', '<Esc><Cmd>w<CR>a')
```

**Source:** Community contributed
***
# Title: Mapping with arguments
# Category: Key Mappings
# Tags: arguments, parameters, count, range
---
Use `<count>` and ranges in mappings to create flexible key bindings that accept numeric arguments.
Or:

```vim
:nnoremap <silent> <leader>d :<C-u>call DeleteLines(v:count1)<CR>
function! DeleteLines(count)
    execute 'normal! ' . a:count . 'dd'
endfunction
" 3<leader>d deletes 3 lines
```

```lua
local function delete_lines(count)
    vim.cmd('normal! ' .. count .. 'dd')
end

vim.keymap.set('n', '<leader>d' function() 
    delete_lines(vim.v.count1)
end)

-- Or even like this
vim.keymap.set('n', '<leader>d' function() 
    vim.cmd('normal! ' .. vim.v.count1 .. 'dd')
end, { silent = true })
```

**Source:** Community contributed
***
# Title: Auto-pair mappings
# Category: Key Mappings
# Tags: autopair, brackets, quotes, matching
---
Create smart bracket and quote auto-pairing with conditional mappings.
Or:

```vim
:inoremap <expr> ( getline('.')[col('.')-2] =~ '\w' ? '(' : '()<Left>'
:inoremap <expr> { getline('.')[col('.')-2] =~ '\w' ? '{' : '{}<Left>'
:inoremap <expr> [ '[]<Left>'
:inoremap <expr> " '""<Left>'
" Smart auto-pairing that considers context
```

```lua
vim.keymap.set('i', '(', function()
  local line = vim.fn.getline('.')
  local col = vim.fn.col('.')
  local char = line:sub(col - 1, col - 1)
  
  if char:match('%w') then
    return '('
  else
    return '()<Left>'
  end
end, { expr = true })

vim.keymap.set('i', '{', function()
  local line = vim.fn.getline('.')
  local col = vim.fn.col('.')
  local char = line:sub(col - 1, col - 1)
  
  if char:match('%w') then
    return '{'
  else
    return '{}<Left>'
  end
end, { expr = true })

vim.keymap.set('i', '[', '[]<Left>', { expr = true })
vim.keymap.set('i', '"', '""<Left>', { expr = true })
```

**Source:** Community contributed
***
# Title: Context-aware mappings
# Category: Key Mappings
# Tags: context, aware, conditional, filetype
---
Create mappings that behave differently based on file type, mode, or cursor context.
Or:

```vim
:autocmd FileType python nnoremap <buffer> <F5> :!python %<CR>
:autocmd FileType javascript nnoremap <buffer> <F5> :!node %<CR>
:autocmd FileType sh nnoremap <buffer> <F5> :!bash %<CR>
" Same key, different behavior per file type
```

```lua
vim.api.nvim_create_autocmd('FileType', {
    pattern = 'python',
    callback = function()
        vim.keymap.set('n', '<F5>', '<Cmd>python %<CR>', { buffer = true })
    end
})
vim.api.nvim_create_autocmd('FileType', {
    pattern = 'javascript',
    callback = function()
        vim.keymap.set('n', '<F5>', '<Cmd>node %<CR>', { buffer = true })
    end
})
vim.api.nvim_create_autocmd('FileType', {
    pattern = 'sh',
    callback = function()
        vim.keymap.set('n', '<F5>', '<Cmd>bash %<CR>', { buffer = true })
    end
})
```

**Source:** Community contributed
***
# Title: Buffer-local keymaps with Lua
# Category: Key Mappings
# Tags: lua, buffer, local, keymap, nvim_buf_set_keymap
---
Create buffer-specific keymaps in Lua that only apply to the current buffer without affecting global mappings.

```lua
-- Set keymap for current buffer (buffer 0):
vim.keymap.set('n', '<leader>r', ':!python %<CR>', {
  buffer = 0,
  desc = 'Run current file'
})

-- In autocommand for specific filetype:
vim.api.nvim_create_autocmd('FileType', {
  pattern = 'lua',
  callback = function(args)
    vim.keymap.set('n', '<leader>x', ':source %<CR>', {
      buffer = args.buf,
      desc = 'Source Lua file'
    })
  end,
})

-- In LspAttach autocommand:
vim.api.nvim_create_autocmd('LspAttach', {
  callback = function(args)
    local opts = { buffer = args.buf }
    vim.keymap.set('n', 'gd', vim.lsp.buf.definition, opts)
    vim.keymap.set('n', 'K', vim.lsp.buf.hover, opts)
    vim.keymap.set('n', '<leader>rn', vim.lsp.buf.rename, opts)
  end,
})
```

**Source:** Community contributed
***
# Title: Quick Spellcheck Mappings
# Category: advanced_mappings
# Tags: spelling, autocorrect, navigation
---
Create convenient mappings for spell checking and navigating spelling errors in Vim/Neovim

```vim
map <F5> :setlocal spell! spelllang=en_us<CR>
" Jump to next misspelled word
map <F6> ]s
" Jump to previous misspelled word
map <F7> [s
" Suggest corrections
map <F8> z=
```

```lua
vim.keymap.set('n', '<F5>', function()
  vim.opt.spell = not vim.opt.spell
  vim.opt.spelllang = 'en_us'
end, { desc = 'Toggle Spell Check' })

vim.keymap.set('n', '<F6>', ']s', { desc = 'Next Spelling Error' })
vim.keymap.set('n', '<F7>', '[s', { desc = 'Previous Spelling Error' })
vim.keymap.set('n', '<F8>', 'z=', { desc = 'Spelling Suggestions' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/A_rough_mapping_to_spellcheck_the_buffer)
***
# Title: Visible Screen ROT13 Mapping with Cursor Preservation
# Category: advanced_mappings
# Tags: key-mapping, text-transformation, cursor-position
---
ROT13 encode only the visible screen while maintaining cursor position

```vim
map <F3> mzHVLg?`z
```

```lua
vim.keymap.set('n', '<F3>', 'mzHVLg?`z', { desc = 'ROT13 visible screen with cursor position' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/A_simple_%22boss_key%22_mapping_or_panic_button)
***
# Title: Conditional Abbreviation Expansion with Prompt
# Category: advanced_mappings
# Tags: abbreviation, interactive-expansion, user-prompt
---
Create an abbreviation that asks for confirmation before expanding, giving users control over automatic text expansion

```vim
function! s:Ask(abbr,expansion,defprompt)
  let answer = confirm("Expand '" . a:abbr . "'?", "&Yes\n&No", a:defprompt)
  return answer == 1 ? a:expansion : a:abbr
endfunction

iabbrev <expr> for <SID>Ask('for', "for () {\n}", 2)
```

```lua
local function ask_expand(abbr, expansion, defprompt)
  local choice = vim.fn.confirm(string.format("Expand '%s'?", abbr), "&Yes\n&No", defprompt)
  return choice == 1 and expansion or abbr
end

vim.cmd.iabbrev{
  args = {'<expr>', 'for', string.format('<cmd>lua return require"user.utils".ask_expand("for", "for () {\n}", 2)<CR>')}
}
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Abbreviation_that_prompts_whether_to_expand_it_or_not)
***
# Title: Conditional Date Abbreviation Expansion
# Category: advanced_mappings
# Tags: abbreviation, insert-mode, custom-mapping
---
Create a flexible abbreviation for inserting dates that can be selectively expanded using a custom shortcut key

```vim
iabbrev date^A <c-r>=strftime("%F")<CR>
inoremap <c-b> <c-v><c-a><c-]>
```

```lua
vim.cmd('iabbrev date^A <c-r>=strftime("%F")<CR>')
vim.keymap.set('i', '<c-b>', '<c-v><c-a><c-]>', { desc = 'Expand date abbreviation' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Abbreviations_only_on_shortcut)
***
# Title: Quick Python Documentation in Vim
# Category: advanced_mappings
# Tags: python, documentation, buffer-management
---
Easily access Python documentation for words/modules under cursor using pydoc, with flexible display options

```vim
nnoremap <buffer> K :<C-u>let save_isk = &iskeyword |
    \ set iskeyword+=. |
    \ execute "!pydoc " . expand("<cword>") |
    \ let &iskeyword = save_isk<CR>
```

```lua
vim.keymap.set('n', 'K', function()
  local save_iskeyword = vim.opt.iskeyword:get()
  vim.opt.iskeyword:append('.')
  vim.fn.system('pydoc ' .. vim.fn.expand('<cword>'))
  vim.opt.iskeyword = save_iskeyword
end, { buffer = true, desc = 'Show Python documentation' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Access_Python_Help)
***
# Title: Cross-Platform Clipboard Key Mappings
# Category: advanced_mappings
# Tags: key-mapping, clipboard, productivity
---
Add familiar clipboard shortcuts for copy, cut, and paste in insert and visual modes

```vim
" Clipboard shortcuts
:inoremap <C-v> <ESC>"+pa
:vnoremap <C-c> "+y
:vnoremap <C-d> "+d
```

```lua
-- Clipboard shortcuts
vim.keymap.set('i', '<C-v>', '<ESC>"+pa')
vim.keymap.set('v', '<C-c>', '"+y')
vim.keymap.set('v', '<C-d>', '"+d')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Accessing_the_system_clipboard)
***
# Title: Quick HTML Anchor Creation from Two Lines
# Category: advanced_mappings
# Tags: key-mapping, html, text-transformation
---
Convert two lines (URL and title) into a single HTML anchor tag using a simple F7 mapping

```vim
" Convert two lines (URL then TITLE) to one line: <a href=URL>TITLE</a>
map <F7> <Esc>I<a href="<Esc>A"><Esc>gJA</a><Esc>
```

```lua
vim.keymap.set('n', '<F7>', function()
  -- Get the current line and next line
  local url_line = vim.fn.getline('.')
  local title_line = vim.fn.getline(vim.fn.line('.') + 1)
  
  -- Create HTML anchor tag
  local link = string.format('<a href="%s">%s</a>', url_line:match('^%s*(.-)%s*$'), title_line:match('^%s*(.-)%s*$'))
  
  -- Replace lines with anchor tag
  vim.fn.setline('.', link)
  vim.fn.deleteline(vim.fn.line('.') + 1)
end, { desc = 'Convert two lines to HTML anchor tag' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Add_a_full_link-tag_with_automatic_title)
***
# Title: Automatic Closing Characters with Smart Insertion
# Category: advanced_mappings
# Tags: insert-mode, auto-completion, key-mapping
---
Automatically insert closing brackets, braces, and parentheses with intelligent behavior for different scenarios

```vim
inoremap {      {}<Left>
inoremap {<CR>  {<CR>}<Esc>O
inoremap {{     {
inoremap {}     {}

inoremap        (  ()<Left>
inoremap <expr> )  strpart(getline('.'), col('.')-1, 1) == ")" ? "\<Right>" : ")"
```

```lua
vim.keymap.set('i', '{', function()
  local line = vim.fn.getline('.')
  local col = vim.fn.col('.')
  vim.fn.feedkeys('{}\27hi', 'n')
end)

vim.keymap.set('i', '(', function()
  local line = vim.fn.getline('.')
  local col = vim.fn.col('.')
  vim.fn.feedkeys('()\27hi', 'n')
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Add_closing_brace_automatically_on_code_blocks)
***
# Title: Conditional Closing Character Insertion
# Category: advanced_mappings
# Tags: insert-mode, conditional-mapping, text-editing
---
Insert closing characters only when cursor is at end of line, preventing unnecessary auto-completion

```vim
function! ConditionalPairMap(open, close)
  let line = getline('.')
  let col = col('.')
  if col < col('$') || stridx(line, a:close, col + 1) != -1
    return a:open
  else
    return a:open . a:close . repeat("\<left>", len(a:close))
  endif
endf
inoremap <expr> ( ConditionalPairMap('(', ')')
inoremap <expr> { ConditionalPairMap('{', '}')
inoremap <expr> [ ConditionalPairMap('[', ']')
```

```lua
local function conditional_pair_map(open, close)
  local line = vim.fn.getline('.')
  local col = vim.fn.col('.')
  if col < vim.fn.col('$') or line:find(close, col + 1) then
    return open
  else
    return open .. close .. string.rep('\27h', #close)
  end
end

vim.keymap.set('i', '(', function() return conditional_pair_map('(', ')') end, { expr = true })
vim.keymap.set('i', '{', function() return conditional_pair_map('{', '}') end, { expr = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Add_closing_brace_automatically_on_code_blocks)
***
# Title: Auto-Generate Function Headers Quickly
# Category: advanced_mappings
# Tags: key-mapping, text-insertion, productivity
---
Create a custom function to automatically insert standardized function headers with a single keystroke, saving time and maintaining consistent documentation

***
# Title: Align #endif with Corresponding #if Directive
# Category: advanced_mappings
# Tags: preprocessor, code-alignment, mapping
---
Quickly insert and align #endif with its corresponding #if directive in C/C++ code

```vim
inoremap <buffer> #en X<BS><Esc>?#if<CR>"zy0^Og0"zpDa#endif<CR>X<BS><Esc>?#end?-1<CR>^"zy0^O0"zpDa
```

```lua
vim.keymap.set('i', '#en', function()
  -- Simplified implementation of finding and aligning #endif
  local line = vim.api.nvim_get_current_line()
  local cursor = vim.api.nvim_win_get_cursor(0)
  
  -- Insert #endif and attempt to align with corresponding #if
  vim.api.nvim_put({'#endif'}, 'l', true, true)
end, { buffer = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Align_endif_with_corresponding_if_or_ifdef_directive)
***
# Title: Auto-Insert Function Headers
# Category: advanced_mappings
# Tags: code-generation, documentation, automation
---
Quick alternative ways to exit insert mode without reaching for the Escape key

```vim
" Quick exit insert mode mappings
:imap jj <Esc>
:imap jk <Esc>
:imap kj <Esc>
:imap ;; <Esc>
```

```lua
-- Alternative escape key mappings in Neovim
vim.keymap.set('i', 'jj', '<Esc>', { noremap = true })
vim.keymap.set('i', 'jk', '<Esc>', { noremap = true })
vim.keymap.set('i', 'kj', '<Esc>', { noremap = true })
vim.keymap.set('i', ';;', '<Esc>', { noremap = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Alternative_to_hitting_Esc)
***
# Title: Use Ctrl-[ as Escape Alternative
# Category: advanced_mappings
# Tags: key-mapping, insert-mode, keyboard-shortcut
---
Equivalent to Escape key for quickly exiting insert mode, especially useful on different keyboard layouts

```vim
" Use Ctrl-[ as Escape alternative
" (Already built-in, no additional mapping needed)
```

```lua
-- Ctrl-[ works as Escape by default in Neovim
-- No additional configuration required
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Alternative_to_hitting_Esc)
***
# Title: Advanced HTML Tag Completion
# Category: advanced_mappings
# Tags: html, auto-insert, mapping
---
Sophisticated HTML tag completion with auto-indentation and flexible insertion

```vim
function s:CompleteTags()
  inoremap <buffer> > ></<C-x><C-o><Esc>:startinsert!<CR><C-O>?</<CR>
  inoremap <buffer> ><CR> ></<C-x><C-o><Esc>:startinsert!<CR><C-O>?</<CR><CR><Tab><CR><Up><C-O>$
endfunction
autocmd BufRead,BufNewFile *.html,*.js,*.xml call s:CompleteTags()
```

```lua
local function complete_tags()
  vim.keymap.set('i', '>', function()
    return '>' .. '</' .. vim.fn['complete'](vim.fn.col('.'), vim.fn['compl#omnifunc']())
  end, { buffer = true, expr = true })
  
  vim.keymap.set('i', '><CR>', function()
    return '>' .. '</' .. vim.fn['complete'](vim.fn.col('.'), vim.fn['compl#omnifunc']()) .. '\n\t\n'
  end, { buffer = true, expr = true })
end

vim.api.nvim_create_autocmd({'BufRead', 'BufNewFile'}, {
  pattern = {'*.html', '*.js', '*.xml'},
  callback = complete_tags
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Auto_closing_an_HTML_tag)
***
# Title: Auto-Close Quotes in HTML/XML Attributes
# Category: advanced_mappings
# Tags: auto-completion, editing, html, xml
---
Automatically insert matching quotes and position cursor between them when typing HTML/XML attribute values

```vim
inoremap " ""<LEFT>
inoremap ' ''<LEFT>
```

```lua
vim.keymap.set('i', '"', '""<Left>', { desc = 'Auto-close double quotes' })
vim.keymap.set('i', "'", "''<Left>", { desc = 'Auto-close single quotes' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Auto_end-quote_html/xml_attribute_values_as_you_type_in_insert_mode)
***
# Title: Auto-Close Brackets and Braces
# Category: advanced_mappings
# Tags: auto-completion, editing
---
Quickly insert matching brackets, parentheses, and braces with cursor positioned inside

```vim
imap () ()<LEFT>
imap [] []<LEFT>
imap {} {}<LEFT>
imap <> <><LEFT>
```

```lua
vim.keymap.set('i', '(', '()<Left>', { desc = 'Auto-close parentheses' })
vim.keymap.set('i', '[', '[]<Left>', { desc = 'Auto-close square brackets' })
vim.keymap.set('i', '{', '{}<Left>', { desc = 'Auto-close curly braces' })
vim.keymap.set('i', '<', '<><Left>', { desc = 'Auto-close angle brackets' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Auto_end-quote_html/xml_attribute_values_as_you_type_in_insert_mode)
***
# Title: Automatic Closing Characters for Brackets and Quotes
# Category: advanced_mappings
# Tags: auto-completion, insert-mode, key-mapping
---
Insert closing braces only when the cursor is at the end of the line, preventing unwanted auto-completions

```vim
function! ConditionalPairMap(open, close)
  let line = getline('.')
  let col = col('.')
  if col < col('$') || stridx(line, a:close, col + 1) != -1
    return a:open
  else
    return a:open . a:close . repeat("\<left>", len(a:close))
  endif
endf
inoremap <expr> ( ConditionalPairMap('(', ')')
inoremap <expr> { ConditionalPairMap('{', '}')
```

```lua
local function conditional_pair_map(open, close)
  local line = vim.fn.getline('.')
  local col = vim.fn.col('.')
  if col < vim.fn.col('$') or line:find(close, col + 1) then
    return open
  else
    return open .. close .. string.rep('<Left>', #close)
  end
end

vim.keymap.set('i', '(', function() return conditional_pair_map('(', ')') end, { expr = true })
vim.keymap.set('i', '{', function() return conditional_pair_map('{', '}') end, { expr = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Autoappend_closing_characters)
***
# Title: Auto-close Brackets and Braces in Insert Mode
# Category: advanced_mappings
# Tags: auto-completion, insert-mode, key-mapping
---
Automatically insert closing characters like (), {}, [] with smart behavior for different scenarios

```vim
inoremap {      {}<Left>
inoremap {<CR>  {<CR>}<Esc>O
inoremap {{     {
inoremap {}     {}

inoremap        (  ()<Left>
inoremap <expr> )  strpart(getline('.'), col('.')-1, 1) == ")" ? "\<Right>" : ")"
```

```lua
vim.keymap.set('i', '{', '{}<Left>', { desc = 'Auto-insert closing brace' })
vim.keymap.set('i', '{<CR>', '{<CR>}<Esc>O', { desc = 'Auto-insert closing brace on new line' })

vim.keymap.set('i', '(', '()<Left>', { desc = 'Auto-insert closing parenthesis' })
vim.keymap.set('i', ')', function()
  local line = vim.fn.getline('.')
  local col = vim.fn.col('.')
  return line:sub(col, col) == ')' and '<Right>' or ')'
end, { expr = true, desc = 'Smart closing parenthesis' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Automatically_append_closing_characters)
***
# Title: Conditional Pair Mapping for Closing Characters
# Category: advanced_mappings
# Tags: auto-completion, insert-mode, smart-mapping
---
Insert closing characters only when cursor is at end of line to avoid unnecessary interruptions

```vim
function! ConditionalPairMap(open, close)
  let line = getline('.')
  let col = col('.')
  if col < col('$') || stridx(line, a:close, col + 1) != -1
    return a:open
  else
    return a:open . a:close . repeat("\<left>", len(a:close))
  endif
endf
inoremap <expr> ( ConditionalPairMap('(', ')')
inoremap <expr> { ConditionalPairMap('{', '}')
inoremap <expr> [ ConditionalPairMap('[', ']')
```

```lua
local function conditional_pair_map(open, close)
  local line = vim.fn.getline('.')
  local col = vim.fn.col('.')
  if col < vim.fn.col('$') or line:find(close, col + 1) then
    return open
  else
    return open .. close .. string.rep('<Left>', #close)
  end
end

vim.keymap.set('i', '(', function() return conditional_pair_map('(', ')') end, { expr = true })
vim.keymap.set('i', '{', function() return conditional_pair_map('{', '}') end, { expr = true })
vim.keymap.set('i', '[', function() return conditional_pair_map('[', ']') end, { expr = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Automatically_append_closing_characters)
***
# Title: Automatically Create and Update Cscope Database
# Category: advanced_mappings
# Tags: cscope, code-navigation, project-management
---
Check for problematic backspace key mappings and diagnose insert mode mapping issues

```vim
" Check backspace mappings
:verbose imap <BS>
:verbose imap ^H
```

```lua
-- Check backspace mappings
vim.cmd('verbose imap <BS>')
vim.cmd('verbose imap ^H')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Backspace_and_delete_problems)
***
# Title: Custom Jump List Selection Function
# Category: advanced_mappings
# Tags: jump-list, custom-function, navigation
---
Create dynamic code snippet expansions using postfix abbreviations, allowing quick insertion of boilerplate code by typing the array/variable name followed by an abbreviation

```vim
:ab ff <Esc>^d$ifor(int i=0;i<<Esc>pi.length;i++){<CR><CR>}//end for loop over array <Esc>pi[i]<Esc>==k==k==ji<Tab>
```

```lua
-- Example of creating an abbreviation in Lua
vim.cmd.abbreviate('ff', '<Esc>^d$ifor(int i=0;i<<Esc>pi.length;i++){<CR><CR>}//end for loop over array <Esc>pi[i]<Esc>==k==k==ji<Tab>')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Basic_postfix_abbreviations)
***
# Title: Quickly Launch and Edit Remote Batch Job Results
# Category: advanced_mappings
# Tags: job-management, remote-execution, file-editing
---
Provides a workflow for launching remote jobs and quickly editing their output files using custom key mappings

```vim
" F7: Execute current file after saving and making executable
map <F7> :w<Bar>:!(chmod +x %; %)<CR>

" F12: Edit most recent file matching a pattern
map <F12> :exec EditMostRecentFile()<CR>

function! EditMostRecentFile()
  let g:pattern = input("EditMostRecentFile. Pattern of files ? (".g:recent." )")
  if g:pattern != ""
    let g:recent = g:pattern
  endif
  let shell_cmd = "ls -t ".g:recent."| head -1"
  exec "e ".system(shell_cmd)
endfunction
```

```lua
-- F7: Execute current file after saving and making executable
vim.keymap.set('n', '<F7>', function()
  vim.cmd('w')
  vim.fn.system('chmod +x ' .. vim.fn.expand('%'))
  vim.fn.system(vim.fn.expand('%'))
end, { desc = 'Save and execute current file' })

-- F12: Edit most recent file matching a pattern
vim.keymap.set('n', '<F12>', function()
  local pattern = vim.fn.input('EditMostRecentFile. Pattern of files? ')
  if pattern ~= '' then
    local shell_cmd = 'ls -t ' .. (pattern or '*') .. ' | head -1'
    local recent_file = vim.fn.trim(vim.fn.system(shell_cmd))
    vim.cmd('edit ' .. recent_file)
  end
end, { desc = 'Open most recent file' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Batch_jobs_launching_%26_listings_viewing_using_VIM)
***
# Title: Smart Bracket and Parenthesis Insertion for Perl
# Category: advanced_mappings
# Tags: auto-completion, insert-mode, language-specific
---
Intelligent bracket insertion for Perl, automatically handling different contexts like block creation and hash syntax

```vim
function! InsertBrackets()
  let fileType = &ft
  if fileType == 'perl'
    let col = col('.') - 1
    if !col || getline('.')[col - 1] !~ '\k' && getline('.')[col - 1] !~ '\$' && getline('.')[col - 1] !~ '@' && getline('.')[col - 1] !~ '%' && getline('.')[col - 1] !~ '#'
      return "{\<CR>\<BS>}\<Esc>ko"
    else
      return "{}\<Esc>i\<c-o>:echo \<CR>"
    endif
  else
    return "{\<CR>\<BS>}\<Esc>ko"
  endif
endfunction
```

```lua
function _G.insert_brackets()
  local filetype = vim.bo.filetype
  if filetype == 'perl' then
    local col = vim.fn.col('.') - 1
    local line = vim.fn.getline('.')
    local prev_char = line:sub(col, col)
    
    if col == 0 or not prev_char:match('[%w$@%_%#]') then
      return '{\n}\27ko'
    else
      return '{}\27i'
    end
  else
    return '{\n}\27ko'
  end
end

vim.keymap.set('i', '{', '<C-R>=v:lua.insert_brackets()<CR>', { expr = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Brackets_and_parentheses_in_Perl)
***
# Title: TortoiseSVN Commands from Vim
# Category: advanced_mappings
# Tags: version-control, external-commands, subversion
---
Create custom mappings to invoke TortoiseSVN commands directly from Vim, allowing quick access to diff, log, blame, and revision graph without leaving the editor

```vim
" Diff current file with SVN version
map <silent> ,tdiff :w<CR>:silent !"C:\Progra~1\TortoiseSVN\bin\TortoiseProc.exe" /command:diff /path:"%" /notempfile /closeonend

" Show SVN log for current file
map <silent> ,tlog :w<CR>:silent !"C:\Progra~1\TortoiseSVN\bin\TortoiseProc.exe" /command:log /path:"%" /notempfile /closeonend

" Show blame for current file
function! TortoiseBlame()
  let filename = expand("%")
  let linenum = line(".")
  silent execute('!C:\Progra~1\TortoiseSVN\bin\TortoiseProc.exe /command:blame /path:"' . filename . '" /line:' . linenum . ' /notempfile /closeonend')
endfunction

map <silent> ,tblame :call TortoiseBlame()<CR>
```

```lua
-- Diff current file with SVN version
vim.keymap.set('n', '<leader>td', function()
  vim.cmd.write()
  vim.fn.system('"C:\\Progra~1\\TortoiseSVN\\bin\\TortoiseProc.exe" /command:diff /path:"' .. vim.fn.expand('%') .. '" /notempfile /closeonend')
end, { silent = true })

-- Show SVN log for current file
vim.keymap.set('n', '<leader>tl', function()
  vim.cmd.write()
  vim.fn.system('"C:\\Progra~1\\TortoiseSVN\\bin\\TortoiseProc.exe" /command:log /path:"' .. vim.fn.expand('%') .. '" /notempfile /closeonend')
end, { silent = true })

-- Show blame for current file at current line
vim.keymap.set('n', '<leader>tb', function()
  local filename = vim.fn.expand('%')
  local linenum = vim.fn.line('.')
  vim.cmd.write()
  vim.fn.system(string.format('"C:\\Progra~1\\TortoiseSVN\\bin\\TortoiseProc.exe" /command:blame /path:"%s" /line:%d /notempfile /closeonend', filename, linenum))
end, { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Call_TortoiseSVN_commands_from_within_Vim)
***
# Title: Visual Selection Case Conversion
# Category: advanced_mappings
# Tags: case-conversion, text-transformation, visual-mode
---
Provides flexible commands to convert case styles within visual selections or entire lines, supporting both CamelCase and snake_case transformations

```vim
function! s:Camelize(range) abort
  if a:range == 0
    s#\(\%(\_l\+\)\%(_\)\@=\)\|_\(\l\)#\u\1\2#g
  else
    s#\%V\(\%(\_l\+\)\%(_\)\@=\)\|_\(\l\)\%V#\u\1\2#g
  endif
endfunction

command! -range CamelCase silent! call <SID>Camelize(<range>)
```

```lua
function CamelCase(range)
  local start_line, end_line
  if range == 0 then
    -- Convert entire line
    vim.cmd('s#\v(\l+)_|(\l)#\u\1\2#g')
  else
    -- Convert within visual selection
    vim.cmd('s#\%V\v(\l+)_|(\l)\%V#\u\1\2#g')
  end
end

-- Create a Lua command
vim.api.nvim_create_user_command('CamelCase', function()
  CamelCase(vim.fn.line('v') == vim.fn.line('.') and 0 or 1)
end, { range = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/CamelCase)
***
# Title: Flexible Case Conversion Commands
# Category: advanced_mappings
# Tags: text-manipulation, custom-commands, regex
---
Create custom commands for converting case within entire buffer or visual selection

```vim
function! s:Camelize(range) abort
  if a:range == 0
    s#\(\%(\<\l\+\)\%(_\)\@=\)\|_\(\l\)#\u\1\2#g
  else
    s#\%V\(\%(\<\l\+\)\%(_\)\@=\)\|_\(\l\)\%V#\u\1\2#g
  endif
endfunction

command! -range CamelCase silent! call <SID>Camelize(<range>)
```

```lua
local function camelize(range)
  local cmd = range == 0 and
    's#\(\%(\<\l\+\)\%(_\)\@=\)\|_\(\l\)#\u\1\2#g' or
    's#\%V\(\%(\<\l\+\)\%(_\)\@=\)\|_\(\l\)\%V#\u\1\2#g'
  
  vim.cmd(cmd)
end

vim.api.nvim_create_user_command('CamelCase', function(opts)
  camelize(opts.range)
end, { range = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/CamelCase_to_under_lined_and_vice_versa)
***
# Title: Camel/Snake Case Conversion Functions
# Category: advanced_mappings
# Tags: text-transformation, custom-function, visual-mode
---
Create reusable functions to convert case styles that work line-wise and in visual selections

```vim
function! s:Camelize(range) abort
  if a:range == 0
    s#\(\%\(\<\l\+\)\%(_\)\@=\)\|_\(\l\)#\u\1\2#g
  else
    s#\%V\(\%\(\<\l\+\)\%(_\)\@=\)\|_\(\l\)\%V#\u\1\2#g
  endif
endfunction

command! -range CamelCase silent! call <SID>Camelize(<range>)
```

```lua
local function camelize(range)
  local cmd = range == 0 and 
    's#\(\%\(\<\l\+\)\%(_\)\@=\)\|_\(\l\)#\u\1\2#g' or
    's#\%V\(\%\(\<\l\+\)\%(_\)\@=\)\|_\(\l\)\%V#\u\1\2#g'
  
  vim.cmd(cmd)
end

vim.api.nvim_create_user_command('CamelCase', function(opts)
  camelize(opts.range)
end, { range = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Camel_case)
***
# Title: Easily Capitalize Words and Regions
# Category: advanced_mappings
# Tags: text-manipulation, case-conversion, editing
---
Provides custom mappings to capitalize words, lines, and visual selections with intuitive gc (capitalize) commands

```vim
if (&tildeop)
  nmap gcw guw~l
  nmap gcW guW~l
  nmap gciw guiw~l
  nmap gciW guiW~l
  nmap gcis guis~l
  nmap gc$ gu$~l
  nmap gcgc guu~l
  nmap gcc guu~l
  vmap gc gu~l
else
  nmap gcw guw~h
  nmap gcW guW~h
  nmap gciw guiw~h
  nmap gciW guiW~h
  nmap gcis guis~h
  nmap gc$ gu$~h
  nmap gcgc guu~h
  nmap gcc guu~h
  vmap gc gu~h
endif
```

```lua
-- Capitalize every word on current line
vim.keymap.set('n', 'gcc', function()
  vim.cmd('s/\v<(.)((\w*))>/\u\1\L\2/g')
end)

-- Capitalize words in visual selection
vim.keymap.set('x', 'gc', function()
  vim.cmd('s/\%V\v<(.)((\w*))>/\u\1\L\2/g')
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Capitalize_words_and_regions_easily)
***
# Title: Capitalize Words Without Moving Cursor
# Category: advanced_mappings
# Tags: case-modification, text-editing, mapping
---
Quick mapping to capitalize words in-place during insert or normal mode without cursor movement

```vim
"Normal mode mappings:
nmap <F7> mzg~iw`z
nmap <F8> mzgUiw`z

"Insert mode mappings:
imap <F8> _<Esc>mzwbgUiw`zi<Del>
```

```lua
-- Normal mode mappings
vim.keymap.set('n', '<F7>', 'mzg~iw`z', { desc = 'Toggle word case' })
vim.keymap.set('n', '<F8>', 'mzgUiw`z', { desc = 'Capitalize word' })

-- Insert mode mappings
vim.keymap.set('i', '<F8>', '_<Esc>mzwbgUiw`zi<Del>', { desc = 'Capitalize word in insert mode' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Capitalize_words_in_insert_and_normal_modes_without_moving_the_cursor)
***
# Title: Quick Directory Change Mapping
# Category: advanced_mappings
# Tags: key-mapping, navigation, productivity
---
Create a quick mapping to change directory to the current file's location and optionally display the new path

```vim
" Quick directory change mapping
nnoremap <leader>cd :cd %:p:h<CR>

" With path display
nnoremap <leader>cd :cd %:p:h<CR>:pwd<CR>
```

```lua
-- Quick directory change mapping
vim.keymap.set('n', '<leader>cd', ':cd %:p:h<CR>', { desc = 'Change to current file directory' })

-- With path display
vim.keymap.set('n', '<leader>cd', function()
  vim.cmd('cd %:p:h')
  vim.cmd('pwd')
end, { desc = 'Change to current file directory and show path' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Change_to_directory_of_the_opened_file)
***
# Title: Quick Word Replacement with Last Yanked Text
# Category: advanced_mappings
# Tags: text-objects, registers, editing
---
Use 'S' to quickly replace the current word with the last yanked text, allowing rapid word replacement across a file

```vim
nnoremap S diw"0P
```

```lua
vim.keymap.set('n', 'S', function()
  vim.cmd('normal! diw"0P')
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Change_visual_mode_paste_command_behaviour)
***
# Title: Quick Web Search from Vim
# Category: advanced_mappings
# Tags: search, web-integration, key-mapping
---
Easily search the web for the word under cursor or selected text using different search engines

```vim
" Search Google for current word
nmap gF vviWgF
vmap <silent> gF y:sil! !start C:/progra~1/intern~1/iexplore.exe -nohome http://www.google.com/search?hl=en&q=<C-R>0<CR>
```

```lua
-- Search Google for current word
vim.keymap.set('n', 'gF', function()
  local word = vim.fn.expand('<cword>')
  vim.fn.system('xdg-open "https://www.google.com/search?q=' .. word .. '"')
end, { desc = 'Search Google for word under cursor' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Check_spelling_and_phrases_using_Google_search)
***
# Title: Quick System Clipboard Keymaps
# Category: advanced_mappings
# Tags: clipboard, key-mapping, productivity
---
Add convenient keymaps to interact with system clipboard in different modes

```vim
" Paste in insert mode
:inoremap <C-v> <ESC>"+pa
" Copy in visual mode
:vnoremap <C-c> "+y
" Cut in visual mode
:vnoremap <C-d> "+d
```

```lua
-- Paste in insert mode
vim.keymap.set('i', '<C-v>', '<ESC>"+pa', { noremap = true })

-- Copy in visual mode
vim.keymap.set('v', '<C-c>', '"+y', { noremap = true })

-- Cut in visual mode
vim.keymap.set('v', '<C-d>', '"+d', { noremap = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Clipboard)
***
# Title: Toggle Clojure Comments Easily
# Category: advanced_mappings
# Tags: commenting, language-specific, key-mapping
---
A quick function to toggle comments for Clojure files, allowing easy commenting and uncommenting of lines

```vim
map <Leader>. :call ClojureCommentUncomment()<CR>
function! ClojureCommentUncomment()
  let search_saved = @/
  if getline('.') =~ '^;'
    s/^;//  " remove ';' at beginning of line
  else
    s/^/;/  " insert ';' at beginning of line
  endif
  let @/ = search_saved
endfunction
```

```lua
vim.keymap.set('n', '<leader>.', function()
  local line = vim.api.nvim_get_current_line()
  if line:match('^;') then
    -- Uncomment: remove leading semicolon
    vim.api.nvim_set_current_line(line:gsub('^;', ''))
  else
    -- Comment: add semicolon at the beginning
    vim.api.nvim_set_current_line('; ' .. line)
  end
end, { desc = 'Toggle Clojure comment' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Clojure_Tips)
***
# Title: SQL Command History Management in Vim
# Category: advanced_mappings
# Tags: sql, command-history, buffer-management
---
Advanced function to manage SQL command history, automatically saving and tracking SQL statements in a separate history file

```vim
fu! VimSQL()
  setf sql
  nnoremap <C-K> :<C-U>
  exe "let linenum=".v:count<CR>:1,$-1d<CR><C-W>j:exe linenum."y"<CR><C-W>kP
  let linenum=line("$")
  1,$-1w! >> ~/.sqlplus.history
  e ~/.sqlplus.history
  execute ":$-".(linenum-1)",$m0"
  %!uniq
  if line("$")>100
    101,$d
  endif
  b#
  set splitbelow
  sp ~/.sqlplus.history
  au! BufEnter afiedt.buf
endf
au BufEnter afiedt.buf call VimSQL()
```

```lua
local function vim_sql()
  vim.bo.filetype = 'sql'
  vim.keymap.set('n', '<C-K>', function()
    local linenum = vim.v.count
    -- Similar logic would be implemented using vim.api and vim.fn functions
    -- Exact translation requires more complex Lua mapping
  end)
end

vim.api.nvim_create_autocmd('BufEnter', {
  pattern = 'afiedt.buf',
  callback = vim_sql
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Command-history_facilities_for_Oracle/sqlplus_user)
***
# Title: Quickly Comment/Uncomment Multiple Lines
# Category: advanced_mappings
# Tags: commenting, code-editing, key-mapping
---
Dynamically comment or uncomment lines based on file type using a single function and mapping

```vim
function! Comment()
  let ft = &filetype
  if ft == 'python' || ft == 'sh' || ft == 'ruby'
    silent s/^/\#/
  elseif ft == 'javascript' || ft == 'c' || ft == 'cpp'
    silent s:^:\/\/:g
  elseif ft == 'vim'
    silent s:^:":g
  endif
endfunction

function! Uncomment()
  let ft = &filetype
  if ft == 'python' || ft == 'sh' || ft == 'ruby'
    silent s/^\#//
  elseif ft == 'javascript' || ft == 'c' || ft == 'cpp'
    silent s:^\/\/::g
  elseif ft == 'vim'
    silent s:^"::g
  endif
endfunction

map <C-a> :call Comment()<CR>
map <C-b> :call Uncomment()<CR>
```

```lua
function _G.comment_lines()
  local ft = vim.bo.filetype
  local comment_map = {
    python = '#', 
    sh = '#', 
    ruby = '#',
    javascript = '//', 
    c = '//', 
    cpp = '//'
  }
  local comment_char = comment_map[ft] or '#'
  
  -- Use visual line mode to get selected lines
  local start_line = vim.fn.line("'<")
  local end_line = vim.fn.line("'>")
  
  for line = start_line, end_line do
    vim.fn.setline(line, comment_char .. vim.fn.getline(line))
  end
end

function _G.uncomment_lines()
  local ft = vim.bo.filetype
  local comment_map = {
    python = '#', 
    sh = '#', 
    ruby = '#',
    javascript = '//', 
    c = '//', 
    cpp = '//'
  }
  local comment_char = comment_map[ft] or '#'
  
  local start_line = vim.fn.line("'<")
  local end_line = vim.fn.line("'>")
  
  for line = start_line, end_line do
    local current_line = vim.fn.getline(line)
    if current_line:match('^' .. vim.pesc(comment_char)) then
      vim.fn.setline(line, current_line:gsub('^' .. vim.pesc(comment_char), ''))
    end
  end
end

-- Set key mappings
vim.keymap.set('v', '<C-a>', ':lua _G.comment_lines()<CR>', { noremap = true, silent = true })
vim.keymap.set('v', '<C-b>', ':lua _G.uncomment_lines()<CR>', { noremap = true, silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Comment_%26_Uncomment_multiple_lines_in_Vim)
***
# Title: Automatic Code Block Commenting
# Category: advanced_mappings
# Tags: autocomplete, code-generation, mapping
---
Automatically adds end-of-block comments for code blocks, reducing manual commenting for large functions

```vim
function CurlyBracket()
  let l:startline = line(".")
  let l:result1 = searchpair('{', '', '}', 'bW')
  if (result1 > 0)
    let l:linenum = line(".")
    let l:string1 = substitute(getline(l:linenum), '^\s*\(.*\)\s*$', '\1', "")
    let l:my_string = substitute(l:string1, '\s*{[^{]*$', '', "")
    let l:my_strlen = strlen(l:my_string)
    if (l:my_strlen > 30)
      let l:my_string = strpart(l:my_string,0,30)."..."
    endif

    if ((l:startline - l:linenum) > 10)
      exe "normal a /* " . l:my_string . " */"
    endif
  endif
endfunction
```

```lua
function _G.CurlyBracket()
  local startline = vim.fn.line('.')
  local result1 = vim.fn.searchpair('{', '', '}', 'bW')
  if result1 > 0 then
    local linenum = vim.fn.line('.')
    local string1 = vim.fn.substitute(vim.fn.getline(linenum), '^\\s*\\(.*\\)\\s*$', '\\1', '')
    local my_string = vim.fn.substitute(string1, '\\s*{[^{]*$', '', '')
    local my_strlen = #my_string
    
    if my_strlen > 30 then
      my_string = string.sub(my_string, 1, 30) .. '...'
    end

    if (startline - linenum) > 10 then
      vim.cmd('normal a /* ' .. my_string .. ' */')
    end
  end
end

-- Add autocmd for specific file types
vim.api.nvim_create_autocmd({'BufNewFile', 'BufRead'}, {
  pattern = {'*.c', '*.cc', '*.h', '*.cpp', '*.java'},
  callback = function()
    vim.keymap.set('i', '}<CR>', '<Esc>:lua CurlyBracket()<CR>a', { buffer = true })
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Comment_your_code_blocks_automatically)
***
# Title: Dynamic Commenting Operator for Different Filetypes
# Category: advanced_mappings
# Tags: commenting, text-manipulation, operators
---
Create a flexible commenting/uncommenting operator that automatically detects comment syntax based on filetype

```vim
function! CommentStr()
  if &ft == 'cpp' || &ft == 'java' || &ft == 'javascript'
    return '//'
  elseif &ft == 'vim'
    return '"'
  elseif &ft == 'python' || &ft == 'perl' || &ft == 'sh' || &ft == 'R'
    return '#'
  elseif &ft == 'lisp'
    return ';'
  endif
  return ''
endfunction

nnoremap <Leader>c <Esc>:set opfunc=DoCommentOp<CR>g@
nnoremap <Leader>C <Esc>:set opfunc=UnCommentOp<CR>g@
```

```lua
local function get_comment_string()
  local ft = vim.bo.filetype
  local comment_map = {
    cpp = '//', java = '//', javascript = '///',
    vim = '"', python = '#', perl = '#', 
    sh = '#', R = '#', lisp = ';'
  }
  return comment_map[ft] or ''
end

-- Similar mapping logic would be implemented using vim.keymap.set
-- This demonstrates the core concept of dynamic comment detection
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Commenting_with_opfunc)
***
# Title: Quick Java Compilation and Execution Mappings
# Category: advanced_mappings
# Tags: java, compilation, key-mapping
---
Set up function key mappings to quickly compile and run Java files, with support for both current and alternate files

```vim
" Compile current file with F9, run with F10
" Compile alternate file with F11, run with F12
map <F9> :set makeprg=javac\ %<CR>:make<CR>
map <F10> :!echo %|awk -F. '{print $1}'|xargs java<CR>
map <F11> :set makeprg=javac\ #<CR>:make<CR>
map <F12> :!echo #|awk -F. '{print $1}'|xargs java<CR>
```

```lua
vim.keymap.set('n', '<F9>', function()
  vim.o.makeprg = 'javac %'
  vim.cmd('make')
end, { desc = 'Compile current Java file' })

vim.keymap.set('n', '<F10>', function()
  local filename = vim.fn.expand('%:r')
  vim.cmd('!java ' .. filename)
end, { desc = 'Run current Java file' })

-- Similar mappings can be added for F11 and F12 for alternate file
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Compile_Java_with_Sun_JDK_javac)
***
# Title: Compile File with F7 Keybinding
# Category: advanced_mappings
# Tags: compilation, key-mapping, build-automation
---
Add a function to save and compile the current file using F7, with automatic directory handling

```vim
function! Make()
  let curr_dir = expand('%:h')
  if curr_dir == ''
    let curr_dir = '.'
  endif
  execute 'lcd ' . curr_dir
  execute 'make %:r.o'
  execute 'lcd -'
endfunction
nnoremap <F7> :update<CR>:call Make()<CR>
```

```lua
function _G.make_current_file()
  local curr_dir = vim.fn.expand('%:h')
  if curr_dir == '' then curr_dir = '.' end
  vim.cmd('lcd ' .. curr_dir)
  vim.cmd('make %:r.o')
  vim.cmd('lcd -')
end

vim.keymap.set('n', '<F7>', function()
  vim.cmd('update')
  _G.make_current_file()
end, { desc = 'Save and compile current file' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Compiling_the_actual_file_with_gcc)
***
# Title: Quick MSDN Documentation Lookup
# Category: advanced_mappings
# Tags: key-mapping, web-search, documentation
---
Quickly open MSDN documentation for a word under cursor using Google's 'I'm Feeling Lucky' search

```vim
nmap <F1> :silent ! start iexplore "http://www.google.com/search?hl=en&btnI=I%27m+Feeling+Lucky&q=site%3Amsdn.microsoft.com%20<cWORD>"<CR>
```

```lua
vim.keymap.set('n', '<F1>', function()
  local word = vim.fn.expand('<cWORD>')
  local url = string.format("http://www.google.com/search?hl=en&btnI=I'm+Feeling+Lucky&q=site:msdn.microsoft.com %s", word)
  vim.fn.system(string.format("start iexplore '%s'", url))
end, { desc = 'Quick MSDN Documentation Lookup' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Context_sensitive_access_to_MSDN_help)
***
# Title: Auto-continue Python module omnicompletion
# Category: advanced_mappings
# Tags: python, completion, key-mapping
---
Automatically trigger omnicompletion after inserting a dot in Python files, improving module completion workflow

```vim
imap <silent> <expr> <buffer> <CR> pumvisible() ? "<CR><C-R>=(col('.')-1&&match(getline(line('.')), '\.',
      \ col('.')-2) == col('.')-2)?"\<lt>C-X>\<lt>C-O>":""<CR>"
      \ : "<CR>"
```

```lua
vim.keymap.set('i', '<CR>', function()
  if vim.fn.pumvisible() == 1 then
    local line = vim.fn.getline('.')
    local col = vim.fn.col('.') - 1
    if col > 0 and line:sub(col, col) == '.' then
      return vim.api.nvim_replace_termcodes('<C-X><C-O>', true, false, true)
    end
  end
  return vim.api.nvim_replace_termcodes('<CR>', true, false, true)
  end, 
  { expr = true, buffer = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Continue_omnicompletion_for_python_modules)
***
# Title: Move Lines Up/Down with Alt Keys
# Category: advanced_mappings
# Tags: key-mapping, line-manipulation, productivity
---
Easily move entire lines or selected blocks up or down in normal, insert, and visual modes using Alt+j/k

```vim
nnoremap <A-j> :m .+1<CR>==
nnoremap <A-k> :m .-2<CR>==
inoremap <A-j> <Esc>:m .+1<CR>==gi
inoremap <A-k> <Esc>:m .-2<CR>==gi
vnoremap <A-j> :m '>+1<CR>gv=gv
vnoremap <A-k> :m '<-2<CR>gv=gv
```

```lua
vim.keymap.set('n', '<A-j>', ':m .+1<CR>==', { noremap = true, silent = true })
vim.keymap.set('n', '<A-k>', ':m .-2<CR>==', { noremap = true, silent = true })
vim.keymap.set('i', '<A-j>', '<Esc>:m .+1<CR>==gi', { noremap = true, silent = true })
vim.keymap.set('i', '<A-k>', '<Esc>:m .-2<CR>==gi', { noremap = true, silent = true })
vim.keymap.set('v', '<A-j>', ':m ">+1<CR>gv=gv', { noremap = true, silent = true })
vim.keymap.set('v', '<A-k>', ':m "<-2<CR>gv=gv', { noremap = true, silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Copy_multiple_lines/words_to_a_specified_position)
***
# Title: Custom Search Text Object for Older Vim
# Category: advanced_mappings
# Tags: search, mapping, text-objects
---
Create a custom 's' mapping to easily copy, change, or operate on search matches in Vim versions before 7.4

```vim
" Search text object mappings
vnoremap <silent> s //e<C-r>=&selection=='exclusive'?'+1':''<CR><CR>
    \:<C-u>call histdel('search',-1)<Bar>let @/=histget('search',-1)<CR>gv
omap s :normal vs<CR>
```

```lua
-- Lua equivalent (requires vim.keymap.set)
vim.keymap.set('v', 's', function()
  -- Implement search text object logic
  -- Note: More complex to replicate exact Vimscript behavior
  -- Recommend using built-in gn in Neovim 0.7+
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Copy_or_change_search_hit)
***
# Title: Flexible Mappings for GUI and Console Vim
# Category: advanced_mappings
# Tags: key-mapping, conditional-mapping, cross-environment
---
Create a function that dynamically sets different key mappings for GUI and console Vim, reducing configuration complexity

```vim
function! ModeMapping(guiLhs, termLhs, rhs, ...)
  let mapCommand='map'
  if (a:0 > 0)
    let mapCommand=a:1
  endif
  if (has("gui_running"))
    execute mapCommand . " " . a:guiLhs . " " . a:rhs
  else
    execute mapCommand . " " . a:termLhs . " " . a:rhs
  endif
endfunction
```

```lua
function _G.ModeMapping(guiLhs, termLhs, rhs, mapCommand)
  mapCommand = mapCommand or 'map'
  if vim.g.gui_running then
    vim.cmd(mapCommand .. ' ' .. guiLhs .. ' ' .. rhs)
  else
    vim.cmd(mapCommand .. ' ' .. termLhs .. ' ' .. rhs)
  end
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Create_one_mapping_for_both_console_and_GUI)
***
# Title: Create Custom Text Objects in Vim/Neovim
# Category: advanced_mappings
# Tags: text-objects, custom-mapping, operator-pending
---
Demonstrates how to create custom text objects for selecting and operating on specific regions like folds or indent levels

```vim
" Visual mode mapping for 'a fold'
vnoremap af :<C-U>silent! normal! [zV]z<CR>

" Operator-pending mode mapping
omap af :normal Vaf<CR>
```

```lua
-- Visual mode mapping for 'a fold'
vim.keymap.set('v', 'af', function()
  vim.cmd.silent('normal! [zV]z')
end, { desc = 'Select entire fold' })

-- Operator-pending mode mapping
vim.keymap.set('o', 'af', function()
  vim.cmd.normal('Vaf')
end, { desc = 'Operate on entire fold' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Creating_new_text_objects)
***
# Title: Remap Help Navigation for AZERTY Keyboards
# Category: advanced_mappings
# Tags: keyboard-layout, help-navigation, key-mapping
---
Provides a mapping solution for AZERTY keyboard users to navigate Vim help, which typically uses Ctrl+] to follow links

```vim
" Map F9 to navigate help links
nmap <F9> <C-]>
map! <F9> <C-]>
```

```lua
-- Map F9 to navigate help links in all modes
vim.keymap.set({'n', 'i', 'c'}, '<F9>', '<C-]>', { desc = 'Navigate help links' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Die_Hilfe_mit_einem_AZERTY_Klavier_durchfahren)
***
# Title: Disable Accidentally Triggered F1 Help Key
# Category: advanced_mappings
# Tags: key-mapping, usability, keyboard-shortcut
---
Prevent accidental F1 key presses from opening help, which can be disruptive during editing

```vim
" Disable F1 help key in normal and insert modes
:nmap <F1> <nop>
:imap <F1> <Esc>
```

```lua
-- Disable F1 help key in Neovim
vim.keymap.set('n', '<F1>', '<Nop>')
vim.keymap.set('i', '<F1>', '<Esc>')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Disable_F1_built-in_help_key)
***
# Title: Contextual F1 Help with Smart Behavior
# Category: advanced_mappings
# Tags: key-mapping, help, context-aware
---
Intelligent F1 mapping that opens help for word under cursor or closes help buffer

```vim
function! MapF1()
  if &buftype == "help"
    exec 'quit'
  else
    exec 'help'
  endif
endfunction
noremap <F1> :call MapF1()<CR>
```

```lua
function _G.smart_help()
  if vim.bo.buftype == "help" then
    vim.cmd('quit')
  else
    vim.cmd('help')
  end
end

vim.keymap.set('n', '<F1>', _G.smart_help)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Disable_F1_built-in_help_key)
***
# Title: Disable Unwanted Built-in Vim Commands
# Category: advanced_mappings
# Tags: key-mapping, customization
---
Quick single-key mapping to toggle between .cpp and .h files in the same directory

```vim
map <F4> :e %:p:s,.h$,.X123X,:s,.cpp$,.h,:s,.X123X$,.cpp,<CR>
```

```lua
vim.keymap.set('n', '<F4>', function()
  local current_file = vim.fn.expand('%:p')
  local new_file = current_file:gsub('\.h$', '.X123X'):gsub('\.cpp$', '.h'):gsub('\.X123X$', '.cpp')
  vim.cmd('edit ' .. new_file)
end, { desc = 'Toggle between source and header' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Easily_switch_between_source_and_header_file)
***
# Title: Multi-Language Comment/Uncomment Mappings
# Category: advanced_mappings
# Tags: comments, language-specific, text-editing
---
Flexible mappings to comment/uncomment lines across different programming languages using single-key shortcuts

```vim
" Language-specific comment mappings
map ,# :s/^/#/<CR>
map ,/ :s/^/\/\//<CR>
map ,> :s/^/> /<CR>
map ,' :s/^/'/<CR>
map ,c :s/^/\/\/\|^--\|^> \|^[#"%!;]//<CR>
```

```lua
-- Lua equivalent using Neovim keymap API
local function comment_line(comment_char)
  vim.api.nvim_command(string.format('s/^/%s/', comment_char))
end

vim.keymap.set('n', ',#', function() comment_line('#') end)
vim.keymap.set('n', ',/', function() comment_line('//') end)
vim.keymap.set('n', ',>', function() comment_line('> ') end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Easy_(un)commenting_out_of_source_code)
***
# Title: Smart Toggle Line Comment
# Category: advanced_mappings
# Tags: comments, toggle, text-editing
---
A single function to toggle comments on the current line, handling both single-line and multi-line comment styles

```vim
function! Komment()
  if getline('.') =~ '\/\*'
    let hls=@/
    s/^\/\*//
    s/*\/$//
    let @/=hls
  else
    let hls=@/
    s/^/\/*/
    s/$/*\//
    let @/=hls
  endif
endfunction
map k :call Komment()<CR>
```

```lua
local function toggle_comment()
  local line = vim.api.nvim_get_current_line()
  local is_commented = line:match('^/%*') and line:match('%*/$')
  
  if is_commented then
    -- Uncomment
    line = line:gsub('^/%*', ''):gsub('%*/$', '')
  else
    -- Comment
    line = '/*' .. line .. '*/'
  end
  
  vim.api.nvim_set_current_line(line)
end

vim.keymap.set('n', 'k', toggle_comment)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Easy_(un)commenting_out_of_source_code)
***
# Title: Easy Block Selection with Alt+Left Mouse
# Category: advanced_mappings
# Tags: mouse-selection, key-mapping, visual-mode
---
Remap Q to quickly play back the macro recorded in the q register, making macro replay more convenient

```vim
noremap Q @q
```

```lua
vim.keymap.set('n', 'Q', '@q', { desc = 'Play macro from q register' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Easy_playback_of_recorded_keys)
***
# Title: Macro Playback with Function Keys
# Category: advanced_mappings
# Tags: macro, key-mapping, productivity
---
Map function keys to specific macro registers for quick and easy macro replay

```vim
nmap <F2> @a
```

```lua
vim.keymap.set('n', '<F2>', '@a', { desc = 'Play macro from a register' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Easy_playback_of_recorded_keys)
***
# Title: Convenient Macro Playback Mapping
# Category: advanced_mappings
# Tags: key-mapping, macros, productivity
---
Map space key to quickly replay a macro from the q register

```vim
" Map space to replay macro in q register
:nnoremap <Space> @q
```

```lua
vim.keymap.set('n', '<Space>', '@q', { desc = 'Replay macro from q register' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Edit_a_previously_recorded_macro)
***
# Title: Toggle Word Completion with F12 Key
# Category: advanced_mappings
# Tags: key-mapping, autocomplete, mode-switching
---
Create a flexible mapping to toggle word completion and paste mode, providing a quick way to switch between editing modes

```vim
" Toggle word completion and paste mode
fun! SetComplete()
  call DoWordComplete()
  set nopaste
  nunmap <F12>
  iunmap <F12>
  nmap <F12> :call UnsetComplete()<CR>
  imap <F12> <Esc>:call UnsetComplete()<CR>a
  echo
endfun

fun! UnsetComplete()
  call EndWordComplete()
  set paste
  nunmap <F12>
  iunmap <F12>
  nmap <F12> :call SetComplete()<CR>
  imap <F12> <Esc>:call SetComplete()<CR>a
  echo
endfun

nmap <F12> :call UnsetComplete()<CR>
imap <F12> <Esc>:call UnsetComplete()<CR>a
```

```lua
local function set_complete()
  vim.fn.DoWordComplete()
  vim.o.paste = false
  vim.keymap.del('n', '<F12>')
  vim.keymap.del('i', '<F12>')
  vim.keymap.set('n', '<F12>', unset_complete)
  vim.keymap.set('i', '<F12>', '<Esc>:lua unset_complete()<CR>a')
end

local function unset_complete()
  vim.fn.EndWordComplete()
  vim.o.paste = true
  vim.keymap.del('n', '<F12>')
  vim.keymap.del('i', '<F12>')
  vim.keymap.set('n', '<F12>', set_complete)
  vim.keymap.set('i', '<F12>', '<Esc>:lua set_complete()<CR>a')
end

-- Initial mapping
vim.keymap.set('n', '<F12>', unset_complete)
vim.keymap.set('i', '<F12>', '<Esc>:lua unset_complete()<CR>a')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Enhance_the_word_complete.vim_script)
***
# Title: Quick Escape Key Alternatives in Insert Mode
# Category: advanced_mappings
# Tags: key-mapping, insert-mode, productivity
---
Quickly execute a normal mode command accidentally typed in insert mode by using a custom mapping that switches to normal mode, undoes the last insertion, and executes the command

```vim
inoremap <somekey> <Esc>u@.

autocmd CursorHoldI * call feedkeys("\<C-G>u", 'tn')
```

```lua
vim.keymap.set('i', '<somekey>', '<Esc>u@.', { desc = 'Execute normal mode command from insert mode' })

vim.api.nvim_create_autocmd('CursorHoldI', {
  callback = function()
    vim.fn.feedkeys('\<C-G>u', 'tn')
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Execute_accidentally_inserted_commands)
***
# Title: Execute Files and URLs from Buffer Text
# Category: advanced_mappings
# Tags: windows, file-operations, key-mapping
---
Quickly open files, URLs, or execute commands directly from the current buffer text on Windows

```vim
" Execute current file
nmap \xf :silent !start rundll32 url.dll,FileProtocolHandler %:p <CR>

" Execute string under cursor
nmap \x :silent !start rundll32 url.dll,FileProtocolHandler <cWORD> <CR>

" Execute string with current file's path
nmap \xl :silent !start rundll32 url.dll,FileProtocolHandler %:p:h/<cWORD> <CR>
```

```lua
-- Execute current file
vim.keymap.set('n', '<leader>xf', function()
  vim.fn.system('rundll32 url.dll,FileProtocolHandler ' .. vim.fn.expand('%:p'))
end, { silent = true })

-- Execute string under cursor
vim.keymap.set('n', '<leader>x', function()
  vim.fn.system('rundll32 url.dll,FileProtocolHandler ' .. vim.fn.expand('<cWORD>'))
end, { silent = true })

-- Execute string with current file's path
vim.keymap.set('n', '<leader>xl', function()
  vim.fn.system('rundll32 url.dll,FileProtocolHandler ' .. vim.fn.expand('%:p:h') .. '/' .. vim.fn.expand('<cWORD>'))
end, { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Execute_commands_from_buffer_text_under_Windows)
***
# Title: Expand Existing Abbreviation Quickly
# Category: advanced_mappings
# Tags: abbreviation, key-mapping, text-expansion
---
Provides a quick way to expand existing abbreviations in Vim, allowing for dynamic text replacement

```vim
map <C-X><C-X> diw:exe "normal i".@"<CR>
```

```lua
vim.keymap.set('n', '<C-X><C-X>', function()
  -- Delete current word and replace with its expanded version
  vim.cmd('normal! diw""P')
end, { desc = 'Expand existing abbreviation' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Expand_existing_abbreviation)
***
# Title: Alternative Abbreviation Expansion Method
# Category: advanced_mappings
# Tags: abbreviation, text-manipulation, key-mapping
---
A more robust method for expanding abbreviations, especially when the abbreviation is at the end of a line

```vim
nno <C-X><C-X> ciw@<Esc>"_s<C-R>"<Esc>b
```

```lua
vim.keymap.set('n', '<C-X><C-X>', function()
  -- Change inner word, then paste register content
  vim.cmd('normal! ciw@')
  vim.cmd('normal! "+p')
end, { desc = 'Expand abbreviation at line end' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Expand_existing_abbreviation)
***
# Title: Smart Tab Insertion with Context
# Category: advanced_mappings
# Tags: insert-mode, key-mapping, indentation
---
Dynamically insert tabs or spaces based on cursor position and file context

```vim
" Insert spaces at line start, real tabs elsewhere
inoremap <Silent> <Tab> <C-R>=(col('.') > (matchend(getline('.'), '^\s*') + 1))?'<C-V><C-V><Tab>':'<Tab>'<CR>
```

```lua
vim.keymap.set('i', '<Tab>', function()
  local col = vim.fn.col('.')
  local line = vim.fn.getline('.')
  local non_white_idx = line:find('%S')
  
  if non_white_idx and col > non_white_idx then
    return vim.api.nvim_replace_termcodes('<Tab>', true, false, true)
  else
    return vim.api.nvim_replace_termcodes('<C-V><Tab>', true, false, true)
  end
, { expr = true, silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Expandtabs)
***
# Title: Execute External Commands with Key Mapping
# Category: advanced_mappings
# Tags: key-mapping, external-commands, workflow
---
Map a key to run external commands quickly, with automatic execution by adding <CR>

```vim
map <F6> :!p4 edit %<CR>
```

```lua
vim.keymap.set('n', '<F6>', function() vim.cmd('!p4 edit %') end, { desc = 'Run external command on current file' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/External_commands_on_Windows)
***
# Title: Run Python Scripts from Vim
# Category: advanced_mappings
# Tags: key-mapping, python, external-commands
---
Quick mapping to execute the current Python file

```vim
map <F5> <Esc>:!python %<CR>
```

```lua
vim.keymap.set('n', '<F5>', function() vim.cmd('!python %') end, { desc = 'Run current Python file' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/External_commands_on_Windows)
***
# Title: Debug Code Abbreviations for PHP
# Category: advanced_mappings
# Tags: debugging, abbreviation, php
---
Quick insert of debug print statements and variable inspection

```vim
iab phpb exit("<hr>Debug ");
iab phpv echo "<hr><pre>";var_dump($a);exit("debug ");
iab phpallv print_r(get_defined_vars());
```

```lua
vim.cmd([[iabbrev phpb exit("<hr>Debug ");]])
vim.cmd([[iabbrev phpv echo "<hr><pre>";var_dump($a);exit("debug ");]])
vim.cmd([[iabbrev phpallv print_r(get_defined_vars());]])
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Fast_jump_to_next_variable_on_the_same_line_(php_programmers_))
***
# Title: Quick One-Key Session Command Mapping
# Category: advanced_mappings
# Tags: key-mapping, command-execution, productivity
---
Dynamically map the last executed command to a function key for quick repeated execution

```vim
function MapLastCommandToKeys(keysToMapTo)
  exe "unmap ".a:keysToMapTo
  exe "map ".a:keysToMapTo." :".histget("cmd")."<CR>"
endfunction

function PrepareMap(keysToMapTo)
  exe "map ".a:keysToMapTo." :call MapLastCommandToKeys('".a:keysToMapTo."')<CR>"
endfunction

" Map F1-F12 for quick command repetition
let i=1
while i<13
  call PrepareMap('<F'.i.'>')
  let i=i+1
endwhile
```

```lua
local function map_last_command_to_keys(keys_to_map_to)
  vim.cmd('unmap ' .. keys_to_map_to)
  vim.cmd('map ' .. keys_to_map_to .. ' :' .. vim.fn.histget('cmd') .. '<CR>')
end

local function prepare_map(keys_to_map_to)
  vim.cmd('map ' .. keys_to_map_to .. ' :lua map_last_command_to_keys("' .. keys_to_map_to .. '")<CR>')
end

-- Map F1-F12 for quick command repetition
for i = 1, 12 do
  prepare_map('<F' .. i .. '>')
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Fast_one_session_mapping)
***
# Title: Quick Word Search Across Project
# Category: advanced_mappings
# Tags: mapping, search, productivity
---
Create a mapping to search for word under cursor in all files and open quickfix window

```vim
map <F4> :execute "vimgrep /" . expand("<cword>") . "/j **" <Bar> cw<CR>
```

```lua
vim.keymap.set('n', '<F4>', function()
  vim.cmd('execute "vimgrep /' .. vim.fn.expand('<cword>') .. '/j **" | cw')
end, { noremap = true, silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Find_in_files_within_Vim)
***
# Title: Custom Backspace Function for Edge Cases
# Category: advanced_mappings
# Tags: key-mapping, custom-function, editing
---
Check and remove unintended insert mode mappings for backspace key

```vim
" Check backspace mappings
:verbose imap <BS>
:verbose imap ^H

" Clear problematic mapping
:iunmap <BS>
```

```lua
-- Check backspace mappings
vim.cmd('verbose imap <BS>')
vim.cmd('verbose imap ^H')

-- Clear problematic mapping
vim.keymap.del('i', '<BS>')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Fix_delete_in_terminals_that_send_incorrect_delete_code)
***
# Title: Fix Meta-Keys in Terminal Vim
# Category: advanced_mappings
# Tags: key-mapping, terminal-config, meta-keys
---
Add a quick keybinding to reset syntax highlighting when it breaks

```vim
noremap <F12> <Esc>:syntax sync fromstart<CR>
inoremap <F12> <C-o>:syntax sync fromstart<CR>
```

```lua
vim.keymap.set('n', '<F12>', ':syntax sync fromstart<CR>', { noremap = true })
vim.keymap.set('i', '<F12>', '<C-o>:syntax sync fromstart<CR>', { noremap = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Fix_syntax_highlighting)
***
# Title: Fix x Command in Virtual Edit Mode
# Category: advanced_mappings
# Tags: key-mapping, virtual-edit, editing
---
Modify the x command to jump to end of line when in virtual edit mode, ensuring consistent character deletion behavior

```vim
" redefine x for virtualEdit so that past end of line, it jumps left to end-of-line
function! Redefine_x_ForVirtualEdit()
  if &ve != "" && col('.') >= col('$')
    normal $
  endif
endfu!
silent! unmap x
:nnoremap <silent>x x:call Redefine_x_ForVirtualEdit()<CR>
```

```lua
vim.api.nvim_create_user_command('RedefineXForVirtualEdit', function()
  if vim.o.virtualedit ~= '' and vim.fn.col('.') >= vim.fn.col('$') then
    vim.cmd('normal! $')
  end
end, {})

vim.keymap.set('n', 'x', function()
  vim.cmd('normal! x')
  vim.cmd.RedefineXForVirtualEdit()
end, { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Fix_the_x_command_in_virtualedit_mode)
***
# Title: Custom Folding Key Mappings
# Category: advanced_mappings
# Tags: folding, key-mapping, navigation
---
Remap Shift-Left/Right to close and open folds, simplifying fold navigation

```vim
nnoremap <S-Left> zo
inoremap <S-Left> <C-O>zo
nnoremap <S-Right> zc
inoremap <S-Right> <C-O>zc
```

```lua
vim.keymap.set({'n', 'i'}, '<S-Left>', 'zo', { desc = 'Open fold' })
vim.keymap.set({'n', 'i'}, '<S-Right>', 'zc', { desc = 'Close fold' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Folding_for_plain_text_files_based_on_indentation)
***
# Title: Manual XML Formatting Mapping
# Category: advanced_mappings
# Tags: xml, formatting, key-mapping
---
Create a custom key mapping to format XML files on demand using xmllint

```vim
map @@x !%xmllint --format --recover -^M
```

```lua
vim.keymap.set('n', '@@x', ':%!xmllint --format --recover -<CR>', { desc = 'Format XML document' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Format_your_xml_document_using_xmllint)
***
# Title: Easy French Character Mappings
# Category: advanced_mappings
# Tags: internationalization, character-mapping, input-method
---
Provides a systematic way to input French accented characters using simple key combinations in insert and command modes

```vim
" French character mappings
map! ;z à
map! ;a â
map! ;b ä
map! ;c ç
map! ;d è
map! ;e ê
map! ;f ë
map! ;g é
imap ;q «  »<Esc>hi
```

```lua
-- French character mappings in Neovim
vim.keymap.set({'i', 'c'}, ';z', 'à', { desc = 'Insert à' })
vim.keymap.set({'i', 'c'}, ';a', 'â', { desc = 'Insert â' })
vim.keymap.set({'i', 'c'}, ';c', 'ç', { desc = 'Insert ç' })
vim.keymap.set('i', ';q', '«  »<Esc>hi', { desc = 'Insert French quotation marks' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/French_character_maps)
***
# Title: Automate Java Getter/Setter Generation
# Category: advanced_mappings
# Tags: java, code-generation, mapping
---
Create a custom mapping to quickly generate Java getter and setter methods for class variables

```vim
map jgs mawv/ <CR>"ty/ <CR>wvwh"ny/getters<CR>$a<CR><CR><Esc>xxapublic
<Esc>"tpa<Esc>"npbiget<Esc>l~ea()<CR>{<CR><Tab>return
<Esc>"npa;<CR>}<Esc>=<CR><Esc>/setters<CR>$a<CR><CR><Esc>xxapublic void
<Esc>"npbiset<Esc>l~ea(<Esc>"tpa <Esc>"npa)<CR>{<CR><Tab>this.<Esc>"npa=
<Esc>"npa;<CR>}<Esc>=<CR>`ak
```

```lua
-- Lua equivalent requires more complex implementation
-- Recommended to use a dedicated plugin like 'java_getset.vim'
function generate_getter_setter()
  -- Example implementation would parse current line
  -- Extract variable type and name
  -- Generate getter and setter methods
end

-- Potential key mapping
vim.keymap.set('n', '<leader>jgs', generate_getter_setter, { desc = 'Generate Java Getter/Setter' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Generate_Java_setters_and_getters_automatically)
***
# Title: Generate PHP Accessor and Setter Methods
# Category: advanced_mappings
# Tags: php, code-generation, mapping
---
Quickly generate getter and setter methods for class variables using Vim mappings

```vim
" Public Accessors
map <F3> :s/\(\(\w\)\(\w\+\)\).*/public function get\u\2\3(){
	return \$this->\1;
}/<CR>
" Public Setters
map <S-F3> :s/\(\(\w\)\(\w\+\)\).*/public function set\u\2\3(\$\1){\r	\$this->\1 = \$\1;\r}/<CR>
```

```lua
-- Lua equivalent for generating PHP accessors/setters
local function generate_getter()
  vim.cmd('s/\(\(\w\)\(\w\+\)\).*/public function get\u\2\3(){
	return $this->' .. vim.fn.expand('<cword>') .. ';
}/')
end

local function generate_setter()
  vim.cmd('s/\(\(\w\)\(\w\+\)\).*/public function set\u\2\3($' .. vim.fn.expand('<cword>') .. '){
	$this->' .. vim.fn.expand('<cword>') .. ' = $' .. vim.fn.expand('<cword>') .. ';
}/')
end

-- Set keymaps
vim.keymap.set('n', '<F3>', generate_getter, { desc = 'Generate PHP Getter' })
vim.keymap.set('n', '<S-F3>', generate_setter, { desc = 'Generate PHP Setter' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Generate_accessor_and_setter_methods_from_variable_names)
***
# Title: Access Python Documentation in Vim
# Category: advanced_mappings
# Tags: python, documentation, key-mapping
---
Quickly access Python library documentation using pydoc directly from Vim, with support for single words and module methods

```vim
nnoremap <buffer> K :<C-u>let save_isk = &iskeyword |
    \ set iskeyword+=. |
    \ execute "!pydoc " . expand("<cword>") |
    \ let &iskeyword = save_isk<CR>
```

```lua
vim.keymap.set('n', 'K', function()
  local save_isk = vim.o.iskeyword
  vim.o.iskeyword = vim.o.iskeyword .. '.'
  vim.cmd('!pydoc ' .. vim.fn.expand('<cword>'))
  vim.o.iskeyword = save_isk
end, { buffer = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Get_help_on_Python_libraries)
***
# Title: Quick PHP Function Inline Help
# Category: advanced_mappings
# Tags: mapping, help, php
---
Create a custom mapping to fetch PHP function documentation in a new window using lynx

```vim
map <C-F1> "vyiw:new<CR>:execute "r!lynx -dump http://localhost/phpman/function.".@v.".html"<CR>:1<CR>
```

```lua
vim.keymap.set('n', '<C-F1>', function()
  -- Yank the word under cursor
  local word = vim.fn.expand('<cword>')
  
  -- Open new window and fetch PHP function documentation
  vim.cmd('new')
  vim.fn.system('lynx -dump http://localhost/phpman/function.' .. word .. '.html')
  vim.cmd('1')
end, { desc = 'Get PHP function inline help' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Get_inline_help_for_PHP_functions)
***
# Title: Prevent Accidental Key Presses
# Category: advanced_mappings
# Tags: key-mapping, error-prevention, usability
---
Remap problematic keys to prevent unintended actions or disable them entirely

```vim
" Prevent F1 key from interrupting in insert mode
inoremap <F1> <Nop>

" Normalize Shift+Arrow key behavior
nnoremap <S-Up> V
nnoremap <S-Down> V
```

```lua
-- Prevent F1 key from interrupting in insert mode
vim.keymap.set('i', '<F1>', '<Nop>')

-- Normalize Shift+Arrow key behavior
vim.keymap.set('n', '<S-Up>', 'V')
vim.keymap.set('n', '<S-Down>', 'V')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Handle_common_command_typos)
***
# Title: Toggle Option Flags Dynamically
# Category: advanced_mappings
# Tags: key-mapping, configuration, options
---
Create a flexible function to toggle Vim option flags, allowing easy runtime configuration of settings

```vim
function ToggleFlag(option,flag)
  exec ('let lopt = &' . a:option)
  if lopt =~ (".*" . a:flag . ".*")
    exec ('set ' . a:option . '-=' . a:flag)
  else
    exec ('set ' . a:option . '+=' . a:flag)
  endif
endfunction

" Example mappings
map <silent> <F8> :call ToggleFlag("guioptions","m")<CR>
map <silent> <F9> :call ToggleFlag("guioptions","T")<CR>
```

```lua
function _G.toggle_flag(option, flag)
  local current_opts = vim.api.nvim_get_option(option)
  if current_opts:find(flag) then
    vim.api.nvim_set_option(option, current_opts:gsub(flag, ''))
  else
    vim.api.nvim_set_option(option, current_opts .. flag)
  end
end

-- Example mappings
vim.keymap.set('n', '<F8>', function() _G.toggle_flag('guioptions', 'm') end)
vim.keymap.set('n', '<F9>', function() _G.toggle_flag('guioptions', 'T') end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Handy_option_flag_toggler)
***
# Title: Cycle Numeric Options Intelligently
# Category: advanced_mappings
# Tags: configuration, key-mapping, options
---
Create a mapping that repeats the last edit while maintaining the original cursor position, mimicking Emacs behavior

```vim
" Restore cursor position after dot repeat
noremap . mz.`z
```

```lua
-- Restore cursor position after dot repeat
vim.keymap.set('n', '.', function()
  local cursor_pos = vim.fn.getpos('.')
  vim.cmd('normal! .')
  vim.fn.setpos('.', cursor_pos)
end, { desc = 'Repeat last edit without moving cursor' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Have_._restore_the_cursor_position_a_la_emacs_in_viper_mode)
***
# Title: Create Granular Undo Breakpoints in Insert Mode
# Category: advanced_mappings
# Tags: undo, insert-mode, key-mapping
---
Create a toggle mapping to highlight lines exceeding text width, with fallback to 80 characters if no textwidth is set

```vim
nnoremap <silent> <Leader>l
      \ :if exists('w:long_line_match') <Bar>
      \   silent! call matchdelete(w:long_line_match) <Bar>
      \   unlet w:long_line_match <Bar>
      \ elseif &textwidth > 0 <Bar>
      \   let w:long_line_match = matchadd('ErrorMsg', '\%>'.&tw.'v.\+', -1) <Bar>
      \ else <Bar>
      \   let w:long_line_match = matchadd('ErrorMsg', '\%>80v.\+', -1) <Bar>
      \ endif<CR>
```

```lua
vim.keymap.set('n', '<Leader>l', function()
  local match_id = vim.w.long_line_match
  
  if match_id then
    vim.fn.matchdelete(match_id)
    vim.w.long_line_match = nil
  else
    local tw = vim.o.textwidth
    if tw > 0 then
      vim.w.long_line_match = vim.fn.matchadd('ErrorMsg', '\%>' .. tw .. 'v.\+', -1)
    else
      vim.w.long_line_match = vim.fn.matchadd('ErrorMsg', '\%>80v.\+', -1)
    end
  end
end, { desc = 'Toggle long line highlighting' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Highlight_long_lines)
***
# Title: Toggle Line Length Highlighting
# Category: advanced_mappings
# Tags: key-mapping, highlighting, configuration
---
Create a toggle mapping to highlight lines exceeding textwidth or a default of 80 columns

```vim
nnoremap <silent> <Leader>l
      \ :if exists('w:long_line_match') <Bar>
      \   silent! call matchdelete(w:long_line_match) <Bar>
      \   unlet w:long_line_match <Bar>
      \ elseif &textwidth > 0 <Bar>
      \   let w:long_line_match = matchadd('ErrorMsg', '\%>'.&tw.'v.\+', -1) <Bar>
      \ else <Bar>
      \   let w:long_line_match = matchadd('ErrorMsg', '\%>80v.\+', -1) <Bar>
      \ endif<CR>
```

```lua
local function toggle_line_length_highlight()
  local match_exists = vim.w.long_line_match ~= nil
  
  if match_exists then
    vim.fn.matchdelete(vim.w.long_line_match)
    vim.w.long_line_match = nil
  else
    local textwidth = vim.o.textwidth
    local match_col = textwidth > 0 and textwidth or 80
    vim.w.long_line_match = vim.fn.matchadd('ErrorMsg', '\%>' .. match_col .. 'v.\+', -1)
  end
end

vim.keymap.set('n', '<Leader>l', toggle_line_length_highlight, { desc = 'Toggle line length highlight' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Highlight_text_beyond_80_columns)
***
# Title: Create Custom Language Keymaps
# Category: advanced_mappings
# Tags: key-mapping, internationalization, language-input
---
Create custom keymaps for different languages or special character inputs, with support for UTF-8 and multiple encodings

```vim
" Keymap file structure example
let b:keymap_name="cz"
highlight lCursor ctermbg=red guibg=red

loadkeymap
" Mapping examples
sz ß  " German eszet mapping
:a ä   " Umlaut mapping
```

```lua
-- Lua equivalent for creating custom keymaps
-- Note: Neovim keymap creation is more flexible
vim.g.keymap_name = "cz"
vim.api.nvim_set_hl(0, 'lCursor', { bg = 'red' })

-- Custom language mappings can be set using vim.keymap.set
-- with buffer-local option for specific language inputs
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/How_to_make_a_keymap)
***
# Title: Quick Comment/Uncomment for Web Languages
# Category: advanced_mappings
# Tags: key-mapping, commenting, filetype-specific
---
Provides language-specific comment/uncomment mappings for HTML, JS, and CSS using localleader key

```vim
" HTML
autocmd BufNewFile,BufRead *.html nnoremap <buffer> <localleader>c I<!-- <esc>A --><esc>
autocmd BufNewFile,BufRead *.html nnoremap <buffer> <localleader>uc 0/- <cr>lv0d$v3hd
" JS
autocmd FileType javascript nnoremap <buffer> <localleader>c I// <esc>
autocmd FileType javascript nnoremap <buffer> <localleader>uc 0v2ld
" CSS
autocmd BufNewFile,BufRead *.css nnoremap <buffer> <localleader>c I/* <esc>A */<esc>
autocmd BufNewFile,BufRead *.css nnoremap <buffer> <localleader>uc 0v2ld$v2hd
```

```lua
vim.api.nvim_create_autocmd({'BufNewFile', 'BufRead'}, {
  pattern = '*.html',
  callback = function()
    vim.keymap.set('n', '<localleader>c', 'I<!-- <esc>A --><esc>', {buffer = true})
    vim.keymap.set('n', '<localleader>uc', '0/- <cr>lv0d$v3hd', {buffer = true})
  end
})

vim.api.nvim_create_autocmd('FileType', {
  pattern = 'javascript',
  callback = function()
    vim.keymap.set('n', '<localleader>c', 'I// <esc>', {buffer = true})
    vim.keymap.set('n', '<localleader>uc', '0v2ld', {buffer = true})
  end
})

vim.api.nvim_create_autocmd({'BufNewFile', 'BufRead'}, {
  pattern = '*.css',
  callback = function()
    vim.keymap.set('n', '<localleader>c', 'I/* <esc>A */<esc>', {buffer = true})
    vim.keymap.set('n', '<localleader>uc', '0v2ld$v2hd', {buffer = true})
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Html,_Javascript_and_Css_comment/uncomment_mapping)
***
# Title: Toggle Whitespace Ignore in Diff
# Category: advanced_mappings
# Tags: diff, toggle, whitespace
---
Add a keymapping to toggle whitespace ignore in diff mode, providing flexible comparison options

```vim
if &diff
    map gs :call IwhiteToggle()<CR>
    function! IwhiteToggle()
        if &diffopt =~ 'iwhite'
            set diffopt-=iwhite
        else
            set diffopt+=iwhite
        endif
    endfunction
endif
```

```lua
if vim.o.diff then
    vim.keymap.set('n', 'gs', function()
        if vim.o.diffopt:find('iwhite') then
            vim.o.diffopt = vim.o.diffopt:gsub(',iwhite', '')
        else
            vim.o.diffopt = vim.o.diffopt .. ',iwhite'
        end
    end, { desc = 'Toggle whitespace ignore in diff' })
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Ignore_white_space_in_vimdiff)
***
# Title: Improve Completion Popup Menu Navigation
# Category: advanced_mappings
# Tags: completion, key-mapping, insert-mode
---
Enhanced completion menu navigation with intuitive key mappings for selecting and accepting completions

```vim
inoremap <expr> <Esc>      pumvisible() ? "\<C-e>" : "\<Esc>"
inoremap <expr> <CR>       pumvisible() ? "\<C-y>" : "\<CR>"
inoremap <expr> <Down>     pumvisible() ? "\<C-n>" : "\<Down>"
inoremap <expr> <Up>       pumvisible() ? "\<C-p>" : "\<Up>"
inoremap <expr> <PageDown> pumvisible() ? "\<PageDown>\<C-p>\<C-n>" : "\<PageDown>"
inoremap <expr> <PageUp>   pumvisible() ? "\<PageUp>\<C-p>\<C-n>" : "\<PageUp>"
```

```lua
vim.keymap.set('i', '<Esc>', function()
  return vim.fn.pumvisible() == 1 and '<C-e>' or '<Esc>'
end, { expr = true })

vim.keymap.set('i', '<CR>', function()
  return vim.fn.pumvisible() == 1 and '<C-y>' or '<CR>'
end, { expr = true })

vim.keymap.set('i', '<Down>', function()
  return vim.fn.pumvisible() == 1 and '<C-n>' or '<Down>'
end, { expr = true })

vim.keymap.set('i', '<Up>', function()
  return vim.fn.pumvisible() == 1 and '<C-p>' or '<Up>'
end, { expr = true })

vim.keymap.set('i', '<PageDown>', function()
  return vim.fn.pumvisible() == 1 and '<PageDown><C-p><C-n>' or '<PageDown>'
end, { expr = true })

vim.keymap.set('i', '<PageUp>', function()
  return vim.fn.pumvisible() == 1 and '<PageUp><C-p><C-n>' or '<PageUp>'
end, { expr = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Improve_completion_popup_menu)
***
# Title: Insert-Mode Only Caps Lock Toggle
# Category: advanced_mappings
# Tags: key-mapping, insert-mode, productivity
---
Create a Caps Lock functionality that only works in insert mode, toggled by Ctrl-^

```vim
" Toggle insert-mode only Caps Lock
for c in range(char2nr('A'), char2nr('Z'))
  execute 'lnoremap ' . nr2char(c+32) . ' ' . nr2char(c)
  execute 'lnoremap ' . nr2char(c) . ' ' . nr2char(c+32)
endfor

" Automatically turn off when leaving insert mode
autocmd InsertLeave * set iminsert=0
```

```lua
-- Toggle insert-mode only Caps Lock
for i = string.byte('a'), string.byte('z') do
  local lower = string.char(i)
  local upper = string.char(i - 32)
  vim.keymap.set('l', lower, upper, { noremap = true })
  vim.keymap.set('l', upper, lower, { noremap = true })
end

-- Automatically turn off when leaving insert mode
vim.api.nvim_create_autocmd('InsertLeave', {
  callback = function()
    vim.o.iminsert = 0
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Insert-mode_only_Caps_Lock)
***
# Title: Quickly Insert Non-Commented Lines
# Category: advanced_mappings
# Tags: mapping, comments, formatting
---
Override automatic comment insertion when using 'o' or 'O' to open new lines

```vim
nnoremap go o<Esc>S
nnoremap gO O<Esc>S
```

```lua
vim.keymap.set('n', 'go', 'o<Esc>S', { desc = 'Insert line below without comments' })
vim.keymap.set('n', 'gO', 'O<Esc>S', { desc = 'Insert line above without comments' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Insert_a_non_commented_line_despite_formatoptions)
***
# Title: Quickly Insert Single Character
# Category: advanced_mappings
# Tags: key-mapping, editing, productivity
---
Provides an efficient way to insert a single character without switching to insert mode repeatedly

```vim
nnoremap s :exec "normal i".nr2char(getchar())."\e"<CR>
nnoremap S :exec "normal a".nr2char(getchar())."\e"<CR>
```

```lua
vim.keymap.set('n', 's', function()
  local char = vim.fn.nr2char(vim.fn.getchar())
  vim.api.nvim_put({char}, '', true, true)
end, { desc = 'Insert single char before cursor' })

vim.keymap.set('n', 'S', function()
  local char = vim.fn.nr2char(vim.fn.getchar())
  vim.api.nvim_put({char}, '', false, true)
end, { desc = 'Insert single char after cursor' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Insert_a_single_character)
***
# Title: Repeatable Single Character Insertion
# Category: advanced_mappings
# Tags: key-mapping, repeat, editing
---
Enhanced version that supports repeating character insertion with count

```vim
function! RepeatChar(char, count)
  return repeat(a:char, a:count)
endfunction
nnoremap s :<C-U>exec "normal i".RepeatChar(nr2char(getchar()), v:count1)<CR>
nnoremap S :<C-U>exec "normal a".RepeatChar(nr2char(getchar()), v:count1)<CR>
```

```lua
vim.keymap.set('n', 's', function()
  local count = vim.v.count1
  local char = vim.fn.nr2char(vim.fn.getchar())
  vim.api.nvim_put({string.rep(char, count)}, '', true, true)
end, { desc = 'Insert repeatable single char before cursor' })

vim.keymap.set('n', 'S', function()
  local count = vim.v.count1
  local char = vim.fn.nr2char(vim.fn.getchar())
  vim.api.nvim_put({string.rep(char, count)}, '', false, true)
end, { desc = 'Insert repeatable single char after cursor' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Insert_a_single_character)
***
# Title: Create Aligned Comment Boxes Quickly
# Category: advanced_mappings
# Tags: comment, mapping, productivity
---
Quickly insert a formatted comment box that spans 100 columns, useful for section headers or documentation

```vim
map ,co O#====================================================================================================<CR>#<CR>#====================================================================================================<Esc>100\|Dkk100\|DjA
```

```lua
vim.keymap.set('n', ',co', function()
  -- Create a 100-column comment box
  vim.api.nvim_put({'#' .. string.rep('=', 100), '#', '#' .. string.rep('=', 100)}, 'l', true, true)
  vim.cmd('normal! kk100|D')
end, { desc = 'Insert comment box' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Insert_comment_boxes_in_your_code)
***
# Title: Insert Empty Line in Normal Mode
# Category: advanced_mappings
# Tags: normal-mode, line-manipulation, productivity
---
Quickly insert an empty line above or below the current line without entering insert mode

```vim
" Insert line below
nmap ,o o<Esc>k
" Insert line above
nmap ,O O<Esc>j
```

```lua
vim.keymap.set('n', ',o', 'o<Esc>k', { desc = 'Insert line below' })
vim.keymap.set('n', ',O', 'O<Esc>j', { desc = 'Insert line above' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Insert_in_normal_mode)
***
# Title: Insert Space Without Moving Cursor
# Category: advanced_mappings
# Tags: text-alignment, normal-mode, cursor-preservation
---
Insert a space at the current cursor position without moving the cursor, useful for manual text alignment

```vim
nnoremap <Space> i<Space><Esc>
```

```lua
vim.keymap.set('n', '<Space>', 'i<Space><Esc>', { desc = 'Insert space at cursor' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Insert_in_normal_mode)
***
# Title: Add Blank Line Without Moving Cursor
# Category: advanced_mappings
# Tags: key-mapping, cursor-position, navigation
---
Insert a blank line above or below current line while keeping cursor in place

```vim
nnoremap <C-J> m`o<Esc>``
nnoremap <C-K> m`O<Esc>``
```

```lua
vim.keymap.set('n', '<C-J>', 'm`o<Esc>``', { desc = 'Insert line below, keep cursor' })
vim.keymap.set('n', '<C-K>', 'm`O<Esc>``', { desc = 'Insert line above, keep cursor' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Insert_newline_without_entering_insert_mode)
***
# Title: Advanced Single Character Insertion with Repeat
# Category: advanced_mappings
# Tags: key-mapping, editing, repeat
---
Insert multiple single characters with count support and repeatability

```vim
function! RepeatChar(char, count)
  return repeat(a:char, a:count)
endfunction

nnoremap s :<C-U>exec "normal i".RepeatChar(nr2char(getchar()), v:count1)<CR>
nnoremap S :<C-U>exec "normal a".RepeatChar(nr2char(getchar()), v:count1)<CR>
```

```lua
vim.keymap.set('n', 's', function()
  local count = vim.v.count1
  local char = vim.fn.nr2char(vim.fn.getchar())
  vim.cmd('normal! i' .. string.rep(char, count))
end)

vim.keymap.set('n', 'S', function()
  local count = vim.v.count1
  local char = vim.fn.nr2char(vim.fn.getchar())
  vim.cmd('normal! a' .. string.rep(char, count))
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Insert_one_character_only)
***
# Title: Quick Dictionary Lookup in Vim
# Category: advanced_mappings
# Tags: key-mapping, external-tool, dictionary
---
Use F12 to quickly look up words in a dictionary file using agrep, with support for whole word and partial matches

```vim
" Whole word lookup (exact match)
map <F12> b"*yw<Esc>:! c:/bin/agrep -wih <C-R>* "c:/dict/an-cs.txt"<CR>

" Partial pattern lookup
map <S-F12> b"*yw<Esc>:! c:/bin/agrep -ih <C-R>* "c:/dict/an-cs.txt"<CR>
```

```lua
-- Whole word lookup (exact match)
vim.keymap.set('n', '<F12>', function()
  local word = vim.fn.expand('<cword>')
  vim.cmd('!c:/bin/agrep -wih ' .. word .. ' "c:/dict/an-cs.txt"')
end)

-- Partial pattern lookup
vim.keymap.set('n', '<S-F12>', function()
  local word = vim.fn.expand('<cword>')
  vim.cmd('!c:/bin/agrep -ih ' .. word .. ' "c:/dict/an-cs.txt"')
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Integrate_Vim_with_a_dictionary)
***
# Title: Custom AutoCAD MTEXT Editing Menu in Vim
# Category: advanced_mappings
# Tags: integration, custom-menu, external-tools
---
Create a custom menu for AutoCAD MTEXT editing with special character and formatting insertions

```vim
"AutoCad menu for MTEXT editation
"Menu for inserting special AutoCAD text formatting codes

imenu &AutoCad.Insert.Space \~
vmenu &AutoCad.Insert.Space <Esc>`<i\~<Esc>%

imenu &AutoCad.Colour.Red \C1;
vmenu &AutoCad.Colour.Red <Esc>`>a\C7;<Esc>`<i\C1;<Esc>%
```

```lua
-- Lua equivalent for custom AutoCAD MTEXT menu
local function create_autocad_menu()
  vim.api.nvim_create_user_command('AutoCadInsertSpace', function()
    vim.cmd('normal! i~')
  end, {})
  
  vim.api.nvim_create_user_command('AutoCadInsertRedColor', function()
    vim.cmd('normal! i\C1;')
  end, {})
end

-- Call the function to set up the menu
create_autocad_menu()
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Integrate_gvim_with_AutoCad_MTEXT)
***
# Title: Quick File Upload with FTPeel Integration
# Category: advanced_mappings
# Tags: ftp, file-upload, external-integration
---
Create a custom mapping to quickly upload the current file to FTPeel on macOS using AppleScript

```vim
" FTPeel MagicMirror support
fun! MagicMirrorIt()
  let path = substitute(expand("%:p"), '/', ":", "g")
  let nice_path = substitute(path, "^:", "", "")
  execute('!osascript -e "tell application \"FTPeel\" to open \"' . nice_path . '\""')
endfun
map <C-S> :call MagicMirrorIt()<CR>
```

```lua
function MagicMirrorIt()
  local path = vim.fn.expand('%:p'):gsub('/', ':')
  local nice_path = path:gsub('^:', '')
  vim.cmd(string.format('!osascript -e "tell application \"FTPeel\" to open \"%s\""', nice_path))
end

vim.keymap.set('n', '<C-S>', MagicMirrorIt, { desc = 'Upload file to FTPeel' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Integrate_with_FTPeel_on_Mac_OS_X)
***
# Title: Quick Internet Search for Word Under Cursor
# Category: advanced_mappings
# Tags: key-mapping, web-search, productivity
---
Quickly search the internet for the word under the cursor using a custom key mapping

```vim
" Search Google for word under cursor
nmap gF vviWgF
vmap <silent> gF y:sil! !start C:/progra~1/intern~1/iexplore.exe -nohome http://www.google.com/search?hl=en&q=<C-R>0<CR>
```

```lua
-- Search Google for word under cursor
vim.keymap.set('n', 'gF', function()
  local word = vim.fn.expand('<cword>')
  local url = string.format('http://www.google.com/search?hl=en&q=%s', word)
  vim.fn.system(string.format('start %s', url))
end, { desc = 'Search Google for word under cursor' })

-- Visual mode version
vim.keymap.set('v', 'gF', function()
  local selected_text = vim.fn.getvisualtext()
  local url = string.format('http://www.google.com/search?hl=en&q=%s', selected_text)
  vim.fn.system(string.format('start %s', url))
end, { desc = 'Search Google for selected text' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Internet_search_for_the_current_word)
***
# Title: Open Web Links Under Cursor
# Category: advanced_mappings
# Tags: key-mapping, url-handling, web
---
Quickly open URLs or web links directly from Vim

```vim
" Open URL under cursor
nmap gF viWgF
vmap <silent> gF y:sil! !start C:/progra~1/intern~1/iexplore.exe <C-R>=escape(@0,"#%")<CR><CR>
```

```lua
-- Open URL under cursor
vim.keymap.set('n', 'gF', function()
  local url = vim.fn.expand('<cfile>')
  if url ~= '' then
    vim.fn.system(string.format('start %s', url))
  end
end, { desc = 'Open URL under cursor' })

-- Visual mode version
vim.keymap.set('v', 'gF', function()
  local selected_text = vim.fn.getvisualtext()
  if selected_text ~= '' then
    vim.fn.system(string.format('start %s', selected_text))
  end
end, { desc = 'Open selected URL' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Internet_search_for_the_current_word)
***
# Title: Quickly Introduce and Extract Variables
# Category: advanced_mappings
# Tags: refactoring, text-manipulation, key-mapping
---
A quick mapping to extract a complex expression into a named variable, useful for code refactoring and readability

```vim
" map \v to put x = y on the line above cursor
map <Leader>v 0wh:put .<CR>a = <Esc>pa<CR><Esc>
```

```lua
vim.keymap.set('n', '<leader>v', function()
  -- Go to start of line
  vim.cmd('0wh:put .')
  vim.cmd('a = ')
  vim.cmd('normal! p')
  vim.cmd('normal! o')
end, { desc = 'Extract expression to variable' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Introduce_variable)
***
# Title: Invert Number Row Keys for Faster Typing
# Category: advanced_mappings
# Tags: key-mapping, productivity, typing
---
Swap number row keys to type symbols more easily without using Shift key, potentially improving typing speed and comfort

```vim
" map each number to its shift-key character
" Insert mode mappings
inoremap 1 !
inoremap 2 @
inoremap 3 #
inoremap 4 $
inoremap 5 %
inoremap 6 ^
inoremap 7 &
inoremap 8 *
inoremap 9 (
inoremap 0 )
inoremap - _

" Reverse mappings
inoremap ! 1
inoremap @ 2
inoremap # 3
inoremap $ 4
inoremap % 5
inoremap ^ 6
inoremap & 7
inoremap * 8
inoremap ( 9
inoremap ) 0
inoremap _ -
```

```lua
-- Lua equivalent for number row key inversion
local function setup_key_inversion()
  local maps = {
    ['1'] = '!', ['2'] = '@', ['3'] = '#', ['4'] = '$', ['5'] = '%',
    ['6'] = '^', ['7'] = '&', ['8'] = '*', ['9'] = '(', ['0'] = ')',
    ['-'] = '_'
  }

  for k, v in pairs(maps) do
    vim.keymap.set('i', k, v)
    vim.keymap.set('i', v, k)
  end
end

setup_key_inversion()
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Invert_the_number_row_keys_for_faster_typing)
***
# Title: Invoke Function with Count Prefix
# Category: advanced_mappings
# Tags: function-mapping, custom-commands, count-prefix
---
Create a mapping that allows invoking a function with a numeric count prefix, similar to built-in Vim commands

```vim
function! Foo(count)
  echo 'FOO: ' . a:count
endfunction

command! -nargs=1 FooCmd call Foo(<args>)
map ,a :<C-U>FooCmd(v:count)<CR>
```

```lua
function _G.foo(count)
  print(string.format('FOO: %d', count))
end

vim.api.nvim_create_user_command('FooCmd', function(opts)
  _G.foo(tonumber(opts.args))
end, { nargs = 1 })

vim.keymap.set('n', ',a', function()
  local count = vim.v.count > 0 and vim.v.count or 1
  vim.cmd('FooCmd ' .. count)
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Invoke_a_function_with_a_count_prefix)
***
# Title: Write Current Key Mappings to File
# Category: advanced_mappings
# Tags: mapping, export, configuration
---
Redirect and save all current key mappings to a text file for reference or backup

```vim
:redir! > vim_keys.txt
:silent verbose map
:redir END
```

```lua
-- Lua equivalent for saving key mappings
vim.cmd('redir! > vim_keys.txt')
vim.cmd('silent verbose map')
vim.cmd('redir END')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Is_there_any_way_to_write_currently_mapped_keys_in_Vim_to_a_file%3F)
***
# Title: Custom Jump List Navigation Function
# Category: advanced_mappings
# Tags: navigation, custom-function, jump-list
---
Create a custom function to interactively select and navigate jump list locations

```vim
function! GotoJump()
  jumps
  let j = input("Please select your jump: ")
  if j != ''
    let pattern = '\v\c^\+'
    if j =~ pattern
      let j = substitute(j, pattern, '', 'g')
      execute "normal " . j . "\<c-i>"
    else
      execute "normal " . j . "\<c-o>"
    endif
  endif
endfunction

" Optional mapping
nmap <Leader>j :call GotoJump()<CR>
```

```lua
function _G.goto_jump()
  vim.cmd('jumps')
  local j = vim.fn.input('Please select your jump: ')
  if j ~= '' then
    local pattern = '^+'
    if j:match(pattern) then
      j = j:gsub('^+', '')
      vim.cmd('normal! ' .. j .. '\<c-i>')
    else
      vim.cmd('normal! ' .. j .. '\<c-o>')
    end
  end
end

-- Set up mapping
vim.keymap.set('n', '<Leader>j', _G.goto_jump, { desc = 'Navigate jump list' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Jumping_to_previously_visited_locations)
***
# Title: Disable Alt Key Menu Shortcuts in Vim
# Category: advanced_mappings
# Tags: key-mapping, configuration, input-handling
---
Disable Alt key menu shortcuts to allow custom Alt key mappings, which is useful for creating alternative key bindings

```vim
set winaltkeys=no
```

```lua
vim.o.winaltkeys = 'no'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Key_maps_using_the_Alt_modifier)
***
# Title: Custom Alt Key Mappings for Special Characters
# Category: advanced_mappings
# Tags: key-mapping, custom-bindings
---
Create Alt key combinations to quickly insert special characters or symbols that might be hard to type directly

```vim
" Alt key character mappings
" <M-`> 0
" <M-q> \
" <M-w> |
" <M-f> [
" <M-g> ]
```

```lua
-- Alt key character mappings
vim.keymap.set('n', '<M-`>', '0', { desc = 'Insert 0' })
vim.keymap.set('n', '<M-q>', '\\', { desc = 'Insert backslash' })
vim.keymap.set('n', '<M-w>', '|', { desc = 'Insert pipe' })
vim.keymap.set('n', '<M-f>', '[', { desc = 'Insert left bracket' })
vim.keymap.set('n', '<M-g>', ']', { desc = 'Insert right bracket' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Key_maps_using_the_Alt_modifier)
***
# Title: Quick Global Substitution Mapping
# Category: advanced_mappings
# Tags: substitution, key-mapping, productivity
---
Create a fast mapping to initiate a global search and replace with confirmation

```vim
:map <F4> :%s///gc<Left><Left><Left>
```

```lua
vim.keymap.set('n', '<F4>', ':%s///gc<Left><Left><Left>', { desc = 'Global substitution with confirmation' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Keystroke_Saving_Substituting_and_Searching)
***
# Title: Launch and View Remote Batch Job Results
# Category: advanced_mappings
# Tags: remote-jobs, key-mapping, file-operations
---
Quickly launch remote batch jobs and view their most recent output file with custom key mappings

```vim
" F7: Execute current file after saving and making executable
" F12: Edit most recent file matching a pattern
map <F7> :w<Bar>:!(chmod +x %; %)<CR>
map <F12> :exec EditMostRecentFile()<CR>

function! EditMostRecentFile()
  let g:pattern = input("EditMostRecentFile. Pattern of files ? (".g:recent." )")
  if g:pattern != ""
    let g:recent = g:pattern
  endif
  let shell_cmd = "ls -t ".g:recent."| head -1"
  exec "e ".system(shell_cmd)
endfunction
```

```lua
vim.keymap.set('n', '<F7>', function()
  vim.cmd('w')
  os.execute('chmod +x ' .. vim.fn.expand('%') .. ' && ' .. vim.fn.expand('%'))
end, { desc = 'Save and execute current file' })

local function edit_most_recent_file()
  local pattern = vim.fn.input('EditMostRecentFile. Pattern of files? ('.. (vim.g.recent or '*') .. '): ')
  if pattern ~= '' then
    vim.g.recent = pattern
  end
  local shell_cmd = 'ls -t ' .. (vim.g.recent or '*') .. '| head -1'
  local recent_file = vim.fn.system(shell_cmd):gsub('%s+', '')
  vim.cmd('edit ' .. recent_file)
end

vim.keymap.set('n', '<F12>', edit_most_recent_file, { desc = 'Edit most recent file' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Launch_remote_batch_jobs_and_view_results_in_Vim)
***
# Title: Quick Compile Mapping with F7
# Category: advanced_mappings
# Tags: compile, key-mapping, build-tools
---
Add a convenient key mapping to save and compile the current buffer in its directory

```vim
function! Make()
  let curr_dir = expand('%:h')
  if curr_dir == ''
    let curr_dir = '.'
  endif
  execute 'lcd ' . curr_dir
  execute 'make %:r.o'
  execute 'lcd -'
endfunction
nnoremap <F7> :update<CR>:call Make()<CR>
```

```lua
function _G.compile_current_buffer()
  local curr_dir = vim.fn.expand('%:h')
  if curr_dir == '' then curr_dir = '.' end
  
  vim.cmd('lcd ' .. curr_dir)
  vim.cmd('make %:r.o')
  vim.cmd('lcd -')
end

vim.keymap.set('n', '<F7>', function()
  vim.cmd('update')
  _G.compile_current_buffer()
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Make-compile_current_buffer)
***
# Title: Windows-style Word Navigation Shortcuts
# Category: advanced_mappings
# Tags: key-mapping, navigation, windows-compatibility
---
Add Ctrl+Left/Right navigation to move between words like in Windows, supporting normal, visual, and insert modes

```vim
"Edit mapping (make cursor keys work like in Windows: <C-Left><C-Right>
"Move to next word.
nnoremap <C-Left> b
vnoremap <C-S-Left> b
nnoremap <C-S-Left> gh<C-O>b
inoremap <C-S-Left> <C-\><C-O>gh<C-O>b

nnoremap <C-Right> w
vnoremap <C-S-Right> w
nnoremap <C-S-Right> gh<C-O>w
inoremap <C-S-Right> <C-\><C-O>gh<C-O>w
```

```lua
-- Windows-style word navigation
vim.keymap.set('n', '<C-Left>', 'b', { desc = 'Move back a word' })
vim.keymap.set('v', '<C-S-Left>', 'b', { desc = 'Select and move back a word' })
vim.keymap.set('n', '<C-S-Left>', 'gh<C-O>b', { desc = 'Move back a word in select mode' })
vim.keymap.set('i', '<C-S-Left>', '<C-\><C-O>gh<C-O>b', { desc = 'Move back a word in insert mode' })

vim.keymap.set('n', '<C-Right>', 'w', { desc = 'Move forward a word' })
vim.keymap.set('v', '<C-S-Right>', 'w', { desc = 'Select and move forward a word' })
vim.keymap.set('n', '<C-S-Right>', 'gh<C-O>w', { desc = 'Move forward a word in select mode' })
vim.keymap.set('i', '<C-S-Right>', '<C-\><C-O>gh<C-O>w', { desc = 'Move forward a word in insert mode' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Make_C-Left_C-Right_behave_as_in_Windows)
***
# Title: Handle Shift-Tab for Unindent and Completion
# Category: advanced_mappings
# Tags: key-mapping, input, terminal-compatibility
---
Configure Shift-Tab to work correctly across different terminals and use it for unindenting or tab completion

```vim
" Map Shift-Tab to unindent or tab completion
:map <Esc>[Z <s-tab>
:ounmap <Esc>[Z

" More robust method
:exe 'set t_kB=' . nr2char(27) . '[Z'
```

```lua
-- Lua equivalent for handling Shift-Tab
vim.keymap.set({'n', 'i', 'v'}, '<S-Tab>', function()
  -- Implement unindent or tab completion logic
  vim.cmd('normal! <<')
end, { desc = 'Unindent or tab completion' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Make_Shift-Tab_work)
***
# Title: Quick Omni and User Completion
# Category: advanced_mappings
# Tags: completion, key-mapping, productivity
---
Add mappings to quickly open omni and user completion menus with smart behavior

```vim
" Open omni completion menu
inoremap <expr> <C-Space> (pumvisible() ? (col('.') > 1 ? '<Esc>i<Right>' : '<Esc>i') : '') .
            \ '<C-x><C-o><C-r>=pumvisible() ? "\<lt>C-n>\<lt>C-p>\<lt>Down>" : ""<CR>'
" Open user completion menu
inoremap <expr> <S-Space> (pumvisible() ? (col('.') > 1 ? '<Esc>i<Right>' : '<Esc>i') : '') .
            \ '<C-x><C-u><C-r>=pumvisible() ? "\<lt>C-n>\<lt>C-p>\<lt>Down>" : ""<CR>'
```

```lua
-- Open omni completion menu
vim.keymap.set('i', '<C-Space>', function()
  local col = vim.fn.col('.')
  local prefix = (vim.fn.pumvisible() == 1) and
    ((col > 1) and '<Esc>i<Right>' or '<Esc>i') or ''
  
  return prefix .. '<C-x><C-o><C-r>=pumvisible() ? "\<lt>C-n>\<lt>C-p>\<lt>Down>" : ""<CR>'
  end, { expr = true })

-- Open user completion menu
vim.keymap.set('i', '<S-Space>', function()
  local col = vim.fn.col('.')
  local prefix = (vim.fn.pumvisible() == 1) and
    ((col > 1) and '<Esc>i<Right>' or '<Esc>i') or ''
  
  return prefix .. '<C-x><C-u><C-r>=pumvisible() ? "\<lt>C-n>\<lt>C-p>\<lt>Down>" : ""<CR>'
  end, { expr = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Make_Vim_completion_popup_menu_work_just_like_in_an_IDE)
***
# Title: Auto-Close Brackets & Navigate Out
# Category: advanced_mappings
# Tags: insert-mode, auto-completion, brackets
---
Automatically insert closing brackets and provide easy navigation out of them in insert mode

```vim
inoremap ( ()<Esc>i
inoremap [ []<Esc>i
inoremap { {<CR>}<Esc>O

" Jump out of brackets
inoremap <C-j> <Esc>:call search(BC_GetChar(), "W")<CR>a
```

```lua
-- Auto-close brackets and navigate
vim.keymap.set('i', '(', '()<Esc>i', { desc = 'Auto-close parentheses' })
vim.keymap.set('i', '[', '[]<Esc>i', { desc = 'Auto-close square brackets' })
vim.keymap.set('i', '{', '{<CR>}<Esc>O', { desc = 'Auto-close curly braces' })

-- Navigation out of brackets
vim.keymap.set('i', '<C-j>', '<Esc>/', { desc = 'Navigate out of brackets' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Making_Parenthesis_And_Brackets_Handling_Easier)
***
# Title: Create Custom Option Toggle Function
# Category: advanced_mappings
# Tags: key-mapping, function, customization
---
Remapping CapsLock to Escape or Ctrl can significantly improve typing efficiency and reduce hand strain in Vim/Neovim

```vim
" No native Vim mapping, uses OS-level remapping
```

```lua
-- Recommended to use AutoHotkey, SharpKeys, or OS-level key remapping
-- In Neovim, you can alternatively create a custom mapping
vim.keymap.set('n', '<CapsLock>', '<Esc>', { noremap = true, silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Map_CapsLock_key_to_Esc)
***
# Title: Conditional Key Remapping with AutoHotkey
# Category: advanced_mappings
# Tags: key-mapping, workflow, conditional-mapping
---
Create application-specific key mappings that only activate in certain contexts like Vim or VSCode

```vim
" No native Vim equivalent
```

```lua
-- While Neovim doesn't directly support this, you can use autocmds
vim.api.nvim_create_autocmd('FileType', {
  pattern = 'vim',
  callback = function()
    vim.keymap.set('n', '<CapsLock>', '<Esc>', { buffer = true })
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Map_CapsLock_key_to_Esc)
***
# Title: Map Ctrl-Backspace to Delete Previous Word
# Category: advanced_mappings
# Tags: key-mapping, insert-mode, editing
---
Allows using Ctrl-Backspace to delete the previous word in insert mode, similar to terminal/readline behavior

```vim
" Map Ctrl-Backspace to delete the previous word in insert mode
imap <C-BS> <C-W>

" For terminal compatibility
noremap! <C-BS> <C-w>
noremap! <C-h> <C-w>
```

```lua
-- Map Ctrl-Backspace to delete previous word
vim.keymap.set('i', '<C-BS>', '<C-W>', { desc = 'Delete previous word' })

-- More readline-like behavior
vim.keymap.set('i', '<C-w>', '<C-\><C-o>dB', { desc = 'Delete previous WORD' })
vim.keymap.set('i', '<C-BS>', '<C-\><C-o>db', { desc = 'Delete previous word' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Map_Ctrl-Backspace_to_delete_previous_word)
***
# Title: Ctrl-S: Smart File Saving Shortcut
# Category: advanced_mappings
# Tags: key-mapping, file-operations, productivity
---
Create a custom Ctrl-S mapping that saves existing files or opens a file browser for new files, working in multiple modes

```vim
" Smart save command
command -nargs=0 -bar Update if &modified
    if empty(bufname('%'))
        browse confirm write
    else
        confirm write
    endif
endif

" Normal mode mapping
nnoremap <silent> <C-S> :<C-u>Update<CR>

" Insert mode mapping
inoremap <c-s> <c-o>:Update<CR>
```

```lua
-- Create Update command
vim.api.nvim_create_user_command('Update', function()
    if vim.bo.modified then
        if vim.api.nvim_buf_get_name(0) == '' then
            vim.cmd('browse confirm write')
        else
            vim.cmd('confirm write')
        end
    end
end, {})

-- Key mappings
vim.keymap.set('n', '<C-S>', '<Cmd>Update<CR>', { silent = true })
vim.keymap.set('i', '<C-S>', '<C-o>:Update<CR>', { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Map_Ctrl-S_to_save_current_or_new_files)
***
# Title: Flexible Caps Lock Mapping with AutoHotkey
# Category: advanced_mappings
# Tags: key-mapping, customization
---
Advanced key mapping to use Caps Lock as Ctrl when held, and Escape when tapped

```vim
" No direct Vimscript implementation
```

```lua
-- Conceptual implementation
-- Requires external tool like AutoHotkey
-- Provides context-aware key remapping
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Map_caps_lock_to_escape_in_Windows)
***
# Title: Remap Caps Lock to Escape on macOS
# Category: advanced_mappings
# Tags: keyboard-layout, productivity, key-mapping
---
Remap Caps Lock key to Escape in system settings, which is especially useful for Vim/Neovim users who frequently use the Escape key

```lua
-- No direct Neovim code, this is a system-level configuration
-- Go to System Settings > Keyboard > Modifier Keys
-- Select 'Escape' for Caps Lock key
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Map_caps_lock_to_escape_in_macOS)
***
# Title: Remap Extra Keys on Non-US Keyboards
# Category: advanced_mappings
# Tags: key-mapping, internationalization, keyboard-layout
---
Customize keyboard mappings for non-US keyboard layouts to improve navigation and typing efficiency

```vim
" German keyboard example
map ü <C-]>
map ö [
map ä ]
map Ö {
map Ä }
map ß /
```

```lua
-- German keyboard example
vim.keymap.set('n', 'ü', '<C-]>', { desc = 'Custom mapping for ]' })
vim.keymap.set('n', 'ö', '[', { desc = 'Custom mapping for [' })
vim.keymap.set('n', 'ä', ']', { desc = 'Custom mapping for ]' })
vim.keymap.set('n', 'Ö', '{', { desc = 'Custom mapping for {' })
vim.keymap.set('n', 'Ä', '}', { desc = 'Custom mapping for }' })
vim.keymap.set('n', 'ß', '/', { desc = 'Custom mapping for /' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Map_extra_keys_on_non_US_keyboards)
***
# Title: Turkish Keyboard Layout Optimization
# Category: advanced_mappings
# Tags: key-mapping, productivity, keyboard-layout
---
Optimize keyboard layout by remapping less accessible keys to more convenient actions

```vim
" Turkish keyboard layout optimization
nmap ş <cr>
let mapleader = "ğ"
```

```lua
-- Turkish keyboard layout optimization
vim.keymap.set('n', 'ş', '<CR>', { desc = 'Remap Enter key' })
vim.g.mapleader = 'ğ'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Map_extra_keys_on_non_US_keyboards)
***
# Title: Map Semicolon to Command Mode
# Category: advanced_mappings
# Tags: key-mapping, productivity, command-line
---
Quickly enter command mode by mapping semicolon to colon, reducing the need to press shift

```vim
" Map semicolon to enter command mode
nnoremap ; :
vnoremap ; :
```

```lua
-- Map semicolon to enter command mode
vim.keymap.set('n', ';', ':', { desc = 'Enter command mode quickly' })
vim.keymap.set('v', ';', ':', { desc = 'Enter command mode in visual mode' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Map_semicolon_to_colon)
***
# Title: Preserve Original Semicolon Functionality
# Category: advanced_mappings
# Tags: key-mapping, workaround
---
Remap double semicolon to preserve original semicolon functionality for repeat f/t commands

```vim
" Double semicolon to get original semicolon behavior
noremap ;; ;
```

```lua
-- Double semicolon to get original semicolon behavior
vim.keymap.set('n', ';;', ';', { desc = 'Repeat last f/t motion' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Map_semicolon_to_colon)
***
# Title: Fast Keycode Mapping in Terminal Vim
# Category: advanced_mappings
# Tags: key-mapping, terminal, performance
---
Create targeted key mappings for specific Vim editing modes, allowing more precise and context-aware shortcuts

```vim
" Normal mode mapping
nnoremap <F2> :lchdir %:p:h<CR>:pwd<CR>

" Insert mode mapping
imap <F3> <C-R>=strftime('%c')<CR>
```

```lua
-- Normal mode mapping
vim.keymap.set('n', '<F2>', ':lchdir %:p:h<CR>:pwd<CR>', { desc = 'Change to current file directory' })

-- Insert mode mapping
vim.keymap.set('i', '<F3>', function() return vim.fn.strftime('%c') end, { expr = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mapping_keys_in_Vim_-_Tutorial)
***
# Title: Find Unused Keys for Custom Mappings
# Category: advanced_mappings
# Tags: key-mapping, configuration, vim-tips
---
Learn how to identify and use unused key sequences for custom mappings without conflicting with existing Vim functionality

```vim
" Check existing maps
:map
:map!
" Check verbose mapping details
:verbose map ,
```

```lua
-- Check existing maps
vim.cmd('map')
vim.cmd('map!')
-- Check verbose mapping details
vim.cmd('verbose map ,')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mapping_keys_in_Vim_-_Tutorial_(Part_2))
***
# Title: Use Symbolic Key Notation for Mappings
# Category: advanced_mappings
# Tags: key-mapping, notation
---
Use symbolic key notation for more readable and consistent key mappings across different environments

```vim
" Examples of symbolic key notation
:map <C-R> :somecommand<CR>
:map <S-F2> :anothercommand<CR>
```

```lua
-- Examples of symbolic key notation
vim.keymap.set('n', '<C-R>', ':somecommand<CR>')
vim.keymap.set('n', '<S-F2>', ':anothercommand<CR>')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mapping_keys_in_Vim_-_Tutorial_(Part_2))
***
# Title: Avoid Mapping Frequently Used Navigation Keys
# Category: advanced_mappings
# Tags: key-mapping, performance, navigation
---
Prevent mapping keys like 'j', 'k', 'l', 'h' at the start of custom mappings to avoid input delays

```vim
" Bad example (avoid)
:nmap jx :somecommand<CR>
" Good practice: use less common prefix
:nmap <leader>jx :somecommand<CR>
```

```lua
-- Avoid mapping frequently used navigation keys
-- Use a leader key or less common prefix
vim.keymap.set('n', '<leader>jx', ':somecommand<CR>')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mapping_keys_in_Vim_-_Tutorial_(Part_2))
***
# Title: Use <Leader> for Plugin-Friendly Key Mappings
# Category: advanced_mappings
# Tags: key-mapping, configuration, plugins
---
Use <Leader> to create consistent and customizable key mappings across plugins, allowing users to easily configure their preferred leader key

```vim
let mapleader = '_'
nnoremap <Leader>f :call <SID>JumpToFile()<CR>
```

```lua
vim.g.mapleader = '_'
vim.keymap.set('n', '<Leader>f', function() -- implement JumpToFile function end, { desc = 'Jump to file' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mapping_keys_in_Vim_-_Tutorial_(Part_3))
***
# Title: Create Unique Plugin Mappings with <Plug>
# Category: advanced_mappings
# Tags: key-mapping, plugins, customization
---
Use <Plug> to create unique, user-configurable key mappings in plugins that won't conflict with existing mappings

```vim
noremap <unique> <Plug>ScriptFunc :call <SID>VimScriptFn()<CR>
nmap _p <Plug>ScriptFunc
```

```lua
vim.keymap.set('n', '<Plug>ScriptFunc', function() -- implement VimScriptFn end, { unique = true })
vim.keymap.set('n', '_p', '<Plug>ScriptFunc')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mapping_keys_in_Vim_-_Tutorial_(Part_3))
***
# Title: Create Mode-Specific Key Mappings in Vim
# Category: advanced_mappings
# Tags: key-mapping, mode-specific, configuration
---
Learn how to create key mappings that work only in specific Vim modes like normal, insert, visual, etc. This allows for more precise and targeted key configurations.

```vim
" Normal mode mapping
nnoremap <F2> :lchdir %:p:h<CR>:pwd<CR>

" Insert mode mapping
imap <F3> <C-R>=strftime('%c')<CR>
```

```lua
-- Normal mode mapping
vim.keymap.set('n', '<F2>', ':lchdir %:p:h<CR>:pwd<CR>', { desc = 'Change to current file directory' })

-- Insert mode mapping
vim.keymap.set('i', '<F3>', function()
  return vim.fn.strftime('%c')
end, { expr = true, desc = 'Insert current timestamp' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mapping_keys_tutorial)
***
# Title: Safely List and Manage Vim Key Mappings
# Category: advanced_mappings
# Tags: key-mapping, configuration, debugging
---
Use built-in Vim commands to list, inspect, and manage key mappings across different modes, helping you understand and debug your configuration.

```vim
" List mappings by mode
:nmap   " Normal mode mappings
:imap   " Insert mode mappings
:vmap   " Visual mode mappings

" Remove a specific mapping
:unmap <F2>
```

```lua
-- List mappings in Neovim
-- Use :nmap, :imap etc. directly or use lua API
vim.cmd('nmap')  -- List normal mode mappings

-- To remove a mapping
vim.keymap.del('n', '<F2>')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mapping_keys_tutorial)
***
# Title: Swap ; and : for Faster Command Entry
# Category: advanced_mappings
# Tags: key-mapping, productivity, command-line
---
Swap semicolon and colon to reduce finger strain when entering commands, with an additional mapping to quickly edit command history

```vim
" Swap ; and : keys
silent! nunmap ;
silent! nunmap :
nnoremap <unique> ; :
nnoremap <unique> : ;

" Quick command-line editing
cnoremap <expr> ; (getcmdpos() == 1 && getcmdtype() =~ '\v^:') ? '<C-F>A' : ';'
```

```lua
-- Swap ; and : keys
vim.keymap.set('n', ';', ':', { unique = true })
vim.keymap.set('n', ':', ';', { unique = true })

-- Quick command-line editing
vim.keymap.set('c', ';', function()
  if vim.fn.getcmdpos() == 1 and vim.fn.getcmdtype():match('^:') then
    return '<C-F>A'
  else
    return ';'
  end
, { expr = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mapping_to_enter_colon_commands)
***
# Title: Visual Mode Smart Paste Without Register Overwrite
# Category: advanced_mappings
# Tags: visual-mode, registers, clipboard
---
Provides a smart paste mapping in visual mode that preserves the original copied text in the register

```vim
xnoremap <silent> p p:let @"=@0<CR>
```

```lua
vim.keymap.set('x', 'p', 'p<cmd>let @"=@0<CR>', { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mappings_and_commands_for_visual_mode)
***
# Title: Insert Mode Alt Key Mappings for Quick Editing
# Category: advanced_mappings
# Tags: key-mapping, insert-mode, productivity
---
A set of Alt key mappings in insert mode to quickly perform normal mode actions without leaving insert mode, reducing mode switching overhead

```vim
" Basic motion mappings in insert mode

imap <A-h> <Left>
imap <A-j> <Down>
imap <A-k> <Up>
imap <A-l> <Right>

" Other useful insert mode mappings
imap <A-o> <C-o>
imap <A-w> <C-o>:w<CR>
```

```lua
-- Lua equivalents for Alt key mappings
vim.keymap.set('i', '<A-h>', '<Left>', { desc = 'Move left in insert mode' })
vim.keymap.set('i', '<A-j>', '<Down>', { desc = 'Move down in insert mode' })
vim.keymap.set('i', '<A-k>', '<Up>', { desc = 'Move up in insert mode' })
vim.keymap.set('i', '<A-l>', '<Right>', { desc = 'Move right in insert mode' })

vim.keymap.set('i', '<A-o>', '<C-o>', { desc = 'Execute single normal mode command' })
vim.keymap.set('i', '<A-w>', '<C-o>:w<CR>', { desc = 'Save file from insert mode' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mappings_to_facilitate_the_creation_of_text)
***
# Title: Advanced Command and Function Mapping Techniques
# Category: advanced_mappings
# Tags: command-line, function-mapping, scripting
---
Demonstrates how to create flexible Vim commands and mappings that can handle ranges, registers, and optional arguments

```vim
fun! TestOne(reg,bang,args) range
  call Dfunc("TestOne(reg<".a:reg.">bang=".a:bang." q-args=".a:args.") firstline=".a:firstline." lastline=".a:lastline)
  call Dret("TestOne")
endfun

com! -range -register -bang TestOne <line1>,<line2>call TestOne("<reg>",<bang>0,<q-args>)
nnoremap \aa :TestOne<CR>
```

```lua
function _G.test_one(reg, bang, args, first_line, last_line)
  -- Equivalent logic for processing command arguments
  vim.pretty_print({
    reg = reg, 
    bang = bang, 
    args = args, 
    first_line = first_line, 
    last_line = last_line
  })
end

-- Create command using Lua API
vim.api.nvim_create_user_command('TestOne', function(opts)
  _G.test_one(opts.reg or '', opts.bang, opts.args, opts.line1, opts.line2)
end, {
  range = true,
  register = true,
  bang = true
})

-- Create mapping
vim.keymap.set('n', '\\aa', ':TestOne<CR>')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Maps,_Commands,_and_Functions_-_some_examples_of_their_interplay)
***
# Title: Enhanced Mouse Interaction in Vim
# Category: advanced_mappings
# Tags: mouse, visual-mode, key-mapping
---
Improve mouse functionality in Vim, adding block selection and paste behavior similar to other text editors

```vim
"Mouse visual block selection (like MS Word)
set mouse=ra

"For GUI Vim
if has("gui_running")
  nmap <A-LeftMouse> ms<LeftMouse><C-v>`so
  imap <A-LeftMouse> <Esc><C-v>`^ms<Esc>gi<LeftMouse><C-o><C-v>`so
else
  "Paste toggle in console Vim
  nmap <F7> :set paste! paste?<CR>
  set pastetoggle=<F7> mouse=rnv
endif
```

```lua
-- Enhanced mouse interaction in Neovim
vim.opt.mouse = 'ra'

-- GUI-specific mappings
if vim.g.neovide or vim.g.nvui then
  vim.keymap.set({'n', 'i'}, '<A-LeftMouse>', function()
    vim.cmd('normal! ms`[v`]')
  end)
end

-- Paste toggle
vim.keymap.set({'n', 'i', 'v'}, '<F7>', function()
  vim.o.paste = not vim.o.paste
  print('Paste mode: ' .. (vim.o.paste and 'ON' or 'OFF'))
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mighty_Mouse)
***
# Title: Simulate Shift-Arrow Text Selection in Terminals
# Category: advanced_mappings
# Tags: terminal, key-mapping, visual-mode
---
Add mappings to enable text selection using Ctrl-arrows in terminals where Shift-arrows don't work correctly

```vim
" Simulate shift-arrows with control-arrows
inoremap <Esc>[A <C-O>vk
vnoremap <Esc>[A k
inoremap <Esc>[B <C-O>vj
vnoremap <Esc>[B j
inoremap <Esc>[C <C-O>vl
vnoremap <Esc>[C l
inoremap <Esc>[D <C-O>vh
vnoremap <Esc>[D h
```

```lua
-- Simulate shift-arrows with control-arrows
vim.keymap.set({'i', 'v'}, '<Esc>[A', function() 
  if vim.fn.mode() == 'i' then
    vim.cmd('normal! vk')
  else
    vim.cmd('normal! k')
  end
end, { desc = 'Select up in terminal' })

-- Similar mappings for other directions can be added accordingly
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mimic_shift-arrow_to_select_text_in_terminals_without_shift-arrow)
***
# Title: Break Undo Chain with Modifier Keys
# Category: advanced_mappings
# Tags: undo, key-mapping, editing
---
Use <C-g>u to create undo breakpoints for more granular undo operations in insert mode

```vim
inoremap <BS> <c-g>u<BS>
inoremap <CR> <c-g>u<CR>
inoremap <del> <c-g>u<del>
inoremap <c-w> <c-g>u<c-w>
```

```lua
vim.keymap.set('i', '<BS>', '<C-g>u<BS>', { desc = 'Undo break on backspace' })
vim.keymap.set('i', '<CR>', '<C-g>u<CR>', { desc = 'Undo break on enter' })
vim.keymap.set('i', '<Del>', '<C-g>u<Del>', { desc = 'Undo break on delete' })
vim.keymap.set('i', '<C-w>', '<C-g>u<C-w>', { desc = 'Undo break on word delete' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Modified_undo_behavior)
***
# Title: Explicit Undo Chain Break with <End>
# Category: advanced_mappings
# Tags: undo, key-mapping, editing
---
Map <End> key to explicitly break the undo chain in insert mode

```vim
inoremap <End> <C-g>u<End>
```

```lua
vim.keymap.set('i', '<End>', '<C-g>u<End>', { desc = 'Break undo chain at end of line' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Modified_undo_behavior)
***
# Title: Disable Middle Mouse Button Paste
# Category: advanced_mappings
# Tags: mouse, clipboard, input-prevention
---
Prevent accidental middle mouse button pastes in Vim/Neovim by mapping the middle mouse button to do nothing

```vim
:map <MiddleMouse> <Nop>
:imap <MiddleMouse> <Nop>

:map <2-MiddleMouse> <Nop>
:imap <2-MiddleMouse> <Nop>
:map <3-MiddleMouse> <Nop>
:imap <3-MiddleMouse> <Nop>
:map <4-MiddleMouse> <Nop>
:imap <4-MiddleMouse> <Nop>
```

```lua
-- Disable middle mouse button paste in all modes
vim.keymap.set({'n', 'i', 'v', 'x', 's', 'c', 't'}, '<MiddleMouse>', '<Nop>')
vim.keymap.set({'n', 'i', 'v', 'x', 's', 'c', 't'}, '<2-MiddleMouse>', '<Nop>')
vim.keymap.set({'n', 'i', 'v', 'x', 's', 'c', 't'}, '<3-MiddleMouse>', '<Nop>')
vim.keymap.set({'n', 'i', 'v', 'x', 's', 'c', 't'}, '<4-MiddleMouse>', '<Nop>')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mouse_wheel_for_scroll_only_-_disable_middle_button_paste)
***
# Title: Virtual Cursor Movement in Insert Mode
# Category: advanced_mappings
# Tags: insert-mode, cursor-movement, virtualedit
---
Allows moving cursor virtually up/down in insert mode, automatically padding with spaces when moving beyond line length

```vim
"cursor down/up existing lines
imap <S-Down> _<Esc>mz:set ve=all<CR>i<Down>_<Esc>my`zi<Del><Esc>:set ve=<CR>`yi<Del>
imap <S-Up> _<Esc>mz:set ve=all<CR>i<Up>_<Esc>my`zi<Del><Esc>:set ve=<CR>`yi<Del>
"cursor down with a new line
imap <S-CR> _<Esc>mz:set ve=all<CR>o<C-o>`z<Down>_<Esc>my`zi<Del><Esc>:set ve=<CR>`yi<Del>
```

```lua
vim.keymap.set('i', '<S-Down>', function()
  local cursor = vim.api.nvim_win_get_cursor(0)
  vim.o.virtualedit = 'all'
  vim.cmd.normal('i<Down>')
  vim.o.virtualedit = ''
  vim.api.nvim_win_set_cursor(0, cursor)
end, { desc = 'Virtual cursor down in insert mode' })

vim.keymap.set('i', '<S-Up>', function()
  local cursor = vim.api.nvim_win_get_cursor(0)
  vim.o.virtualedit = 'all'
  vim.cmd.normal('i<Up>')
  vim.o.virtualedit = ''
  vim.api.nvim_win_set_cursor(0, cursor)
end, { desc = 'Virtual cursor up in insert mode' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Move_cursor_up/down_virtually_in_insert_mode)
***
# Title: Move Function Parameters with Macros
# Category: advanced_mappings
# Tags: macro, editing, function-parameters
---
Quickly move function parameters within a function call using custom key mappings

```vim
"Move after next comma
nmap ,mc "zdiWxf,a <Esc>"zp

"Move until next parenthesis
nmap ,mp "zdiWxf)hi, <Esc>"zpx
```

```lua
-- Move parameter after next comma
vim.keymap.set('n', ',mc', function()
  vim.cmd('normal! "zdiWxf,a ')
  vim.cmd('normal! "zp')
end, { desc = 'Move parameter after comma' })

-- Move parameter to end of parameters
vim.keymap.set('n', ',mp', function()
  vim.cmd('normal! "zdiWxf)hi, ')
  vim.cmd('normal! "zpx')
end, { desc = 'Move parameter to end' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Move_function_parameters_with_macro)
***
# Title: Easily Move Lines Up or Down
# Category: advanced_mappings
# Tags: navigation, editing, key-mapping
---
Provides intuitive Alt+j/k mappings to move lines up or down in normal, insert, and visual modes, with automatic re-indentation

```vim
nnoremap <A-j> :m .+1<CR>==
nnoremap <A-k> :m .-2<CR>==
inoremap <A-j> <Esc>:m .+1<CR>==gi
inoremap <A-k> <Esc>:m .-2<CR>==gi
vnoremap <A-j> :m '>+1<CR>gv=gv
vnoremap <A-k> :m '<-2<CR>gv=gv
```

```lua
vim.keymap.set('n', '<A-j>', ':m .+1<CR>==', { noremap = true, silent = true })
vim.keymap.set('n', '<A-k>', ':m .-2<CR>==', { noremap = true, silent = true })
vim.keymap.set('i', '<A-j>', '<Esc>:m .+1<CR>==gi', { noremap = true, silent = true })
vim.keymap.set('i', '<A-k>', '<Esc>:m .-2<CR>==gi', { noremap = true, silent = true })
vim.keymap.set('v', '<A-j>', ':m ">+1<CR>gv=gv', { noremap = true, silent = true })
vim.keymap.set('v', '<A-k>', ':m "<-2<CR>gv=gv', { noremap = true, silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Moving_lines_up_or_down_in_a_file)
***
# Title: Quick Toggle for Vim Options
# Category: advanced_mappings
# Tags: key-mapping, configuration, options
---
Provides a single-key interface to toggle various Vim options quickly, reducing the number of mappings and simplifying option management

```vim
" Map leader+o to open toggle options menu
map <Leader>o :ToggleOptions<CR>

function! ToggleOptionsMenu()
  let l:char = s:Char_menu( "{w}rap, {W}rapscan, {l}ist, {b}inary, {m}odifiable, {d}iff, {v}irtualedit, uhe{x}" )
  if l:char ==# 'w'
    set wrap!
    set wrap?
  elseif l:char ==# 'd'
    if &diff
      set nodiff foldcolumn=0
    else
      diffthis
    endif
    set diff?
  endif
endfunction
```

```lua
-- Lua equivalent of toggle options menu
local function toggle_options()
  local options = {
    w = function() vim.wo.wrap = not vim.wo.wrap end,
    d = function()
      if vim.wo.diff then
        vim.wo.diff = false
        vim.wo.foldcolumn = '0'
      else
        vim.cmd('diffthis')
      end
    end
  }

  local char = vim.fn.getchar()
  local option_func = options[vim.fn.nr2char(char)]
  if option_func then option_func() end
end

-- Map leader+o to toggle options
vim.keymap.set('n', '<Leader>o', toggle_options, { desc = 'Toggle Vim Options' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Not_So_Quick_generic_option_toggling)
***
# Title: Open Online Documentation for Word Under Cursor
# Category: advanced_mappings
# Tags: documentation, browser-integration, key-mapping
---
Create custom keymaps to open Windows HTML Help files with the word under cursor or selected text

```vim
nnoremap <C-F1> :silent! !cmd.exe /c start keyhh.exe -#klink "<C-R><C-W>" "$ASANY9\docs\dbmaen9.chm"<CR><CR>
vnoremap <C-F1> :<C-U>let old_reg=@"<CR>gvy:silent!!cmd.exe /cstart keyhh.exe -#klink "<C-R><C-R>"" "$ASANY9\docs\dbmaen9.chm"<CR><CR>:let @"=old_reg<CR>:echo ""<CR>
```

```lua
vim.keymap.set('n', '<C-F1>', function()
  local word = vim.fn.expand('<cword>')
  vim.fn.system(string.format('cmd.exe /c start keyhh.exe -#klink "%s" "$ASANY9\\docs\\dbmaen9.chm"', word))
end, { silent = true })

vim.keymap.set('v', '<C-F1>', function()
  local old_reg = vim.fn.getreg('"')
  vim.cmd('normal! gvy')
  local selected = vim.fn.getreg('"')
  vim.fn.system(string.format('cmd.exe /c start keyhh.exe -#klink "%s" "$ASANY9\\docs\\dbmaen9.chm"', selected))
  vim.fn.setreg('"', old_reg)
end, { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_Windows_Help_files_on_a_specific_topic)
***
# Title: Insert Multiple Blank Lines Easily
# Category: advanced_mappings
# Tags: key-mapping, editing, productivity
---
Quickly insert multiple blank lines with a customizable mapping that ensures at least one blank line before and after

```vim
" Open multiple lines (insert empty lines) before or after current line
function! OpenLines(nrlines, dir)
  let nrlines = a:nrlines < 3 ? 3 : a:nrlines
  let start = line('.') + a:dir
  call append(start, repeat([''], nrlines))
  if a:dir < 0
    normal! 2k
  else
    normal! 2j
  endif
endfunction

" Mappings to open multiple lines and enter insert mode
nnoremap <Leader>o :<C-u>call OpenLines(v:count, 0)<CR>S
nnoremap <Leader>O :<C-u>call OpenLines(v:count, -1)<CR>S
```

```lua
-- Function to insert multiple blank lines
function _G.open_lines(nrlines, dir)
  nrlines = nrlines < 3 and 3 or nrlines
  local start = vim.fn.line('.') + dir
  
  -- Insert blank lines
  local blank_lines = vim.fn['repeat']({''}. nrlines)
  vim.fn.append(start, blank_lines)
  
  -- Adjust cursor position
  if dir < 0 then
    vim.cmd('normal! 2k')
  else
    vim.cmd('normal! 2j')
  end
end

-- Key mappings
vim.keymap.set('n', '<Leader>o', function()
  local count = vim.v.count > 0 and vim.v.count or 1
  _G.open_lines(count, 0)
  vim.cmd('startinsert')
end, { desc = 'Insert blank lines below' })

vim.keymap.set('n', '<Leader>O', function()
  local count = vim.v.count > 0 and vim.v.count or 1
  _G.open_lines(count, -1)
  vim.cmd('startinsert')
end, { desc = 'Insert blank lines above' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_multiple_lines)
***
# Title: Quick HTML/URL Preview in Browser
# Category: advanced_mappings
# Tags: browser-preview, file-operations, web-development
---
Easily open the current HTML file or URL in a browser directly from Vim/Neovim using flexible key mappings

```vim
" Open current file in default browser
nnoremap <F5> :update<Bar>silent !xdg-open %:p &<CR>

" Open URL under cursor in browser
nnoremap <F8> :silent !xdg-open <cfile> &<CR>
```

```lua
-- Open current file in default browser
vim.keymap.set('n', '<F5>', function()
  vim.cmd.update()
  vim.fn.system('xdg-open ' .. vim.fn.expand('%:p') .. ' &')
end, { desc = 'Open current file in browser' })

-- Open URL under cursor in browser
vim.keymap.set('n', '<F8>', function()
  vim.fn.system('xdg-open ' .. vim.fn.expand('<cfile>') .. ' &')
end, { desc = 'Open URL under cursor in browser' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Opening_current_Vim_file_in_your_Windows_browser)
***
# Title: Dynamic Key Handler with Multiple Contexts
# Category: advanced_mappings
# Tags: key-mapping, function-handler, conditional-execution
---
Execute a recorded macro on all lines matching a specific pattern

```vim
" Run macro 'q' on lines containing 'pattern'
:g/pattern/normal @q
```

```lua
-- Run macro 'q' on lines containing 'pattern'
vim.cmd('g/pattern/normal @q')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Power_of_g)
***
# Title: Exit Insert Mode Without Moving Cursor
# Category: advanced_mappings
# Tags: insert-mode, cursor-position, key-mapping
---
Provides a way to exit insert mode without the default cursor movement behavior, using a quick key sequence

```vim
set timeoutlen=300
inoremap fj <Esc>l
inoremap jf <Esc>l
```

```lua
vim.opt.timeoutlen = 300
vim.keymap.set('i', 'fj', '<Esc>l')
vim.keymap.set('i', 'jf', '<Esc>l')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Prevent_escape_from_moving_the_cursor_one_character_to_the_left)
***
# Title: Prevent Accidental Command Typos
# Category: advanced_mappings
# Tags: key-mapping, error-prevention, productivity
---
Correct common command-line typos and prevent unintended actions by remapping frequently mistyped commands

```vim
" Correct common command-line typos
cabbrev Q quit
cabbrev W write

" Prevent accidentally holding Shift
cabbrev q!@ q!
cabbrev wq!@ wq!
```

```lua
-- Lua equivalent for command typo correction
vim.cmd('cabbrev Q quit')
vim.cmd('cabbrev W write')
vim.cmd('cabbrev q!@ q!')
vim.cmd('cabbrev wq!@ wq!')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Prevent_the_cursor_from_jumping_around_when_pressing_%22V%22_for_visual_mode)
***
# Title: Run and Preview Interpreter Output in Split Window
# Category: advanced_mappings
# Tags: scripting, interpreter, output-preview, development
---
Allows running selected code snippets in an interpreter and displaying output in a preview window, useful for quick script testing and debugging

```vim
function! Ruby_eval_vsplit() range
  let src = tempname()
  let dst = tempname()
  execute ': ' . a:firstline . ',' . a:lastline . 'w ' . src
  execute ':silent ! ruby ' . src . ' > ' . dst . ' 2>&1'
  execute ':pclose!'
  execute ':redraw!'
  execute ':vsplit'
  execute 'normal \<C-W>l'
  execute ':e! ' . dst
  execute ':set pvw'
  execute 'normal \<C-W>h'
endfunction

vmap <silent> <F7> :call Ruby_eval_vsplit()<CR>
nmap <silent> <F7> mzggVG<F7>`z
imap <silent> <F7> <Esc><F7>a
```

```lua
function _G.ruby_eval_vsplit(first_line, last_line)
  local src = vim.fn.tempname()
  local dst = vim.fn.tempname()
  
  -- Write selected lines to temp file
  vim.cmd(string.format(':%d,%dw %s', first_line, last_line, src))
  
  -- Run Ruby and capture output
  os.execute(string.format('ruby %s > %s 2>&1', src, dst))
  
  -- Open preview window with results
  vim.cmd('pclose!')
  vim.cmd('redraw!')
  vim.cmd('vsplit')
  vim.cmd('wincmd l')
  vim.cmd('edit! ' .. dst)
  vim.cmd('set pvw')
  vim.cmd('wincmd h')
end

-- Mappings
vim.keymap.set('v', '<F7>', function()
  local first_line = vim.fn.line("'<")
  local last_line = vim.fn.line("'>")
  _G.ruby_eval_vsplit(first_line, last_line)
end, { silent = true })

vim.keymap.set('n', '<F7>', function()
  vim.cmd('normal! mzggVG')
  _G.ruby_eval_vsplit(1, vim.fn.line('$'))
  vim.cmd('normal! `z')
end, { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Preview_output_from_interpreter_in_new_window)
***
# Title: Handle Numeric Keypad Escape Sequences
# Category: advanced_mappings
# Tags: key-mapping, terminal, input-handling
---
Map escape sequences from numeric keypad to corresponding numbers and operations

```vim
" Mapping escape sequences to numeric keypad keys
:inoremap <Esc>Oq 1
:inoremap <Esc>Or 2
:inoremap <Esc>Os 3
:inoremap <Esc>Ot 4
:inoremap <Esc>Ou 5
:inoremap <Esc>Ov 6
:inoremap <Esc>Ow 7
:inoremap <Esc>Ox 8
:inoremap <Esc>Oy 9
:inoremap <Esc>Op 0
```

```lua
-- Lua equivalent for handling numeric keypad escape sequences
local function map_keypad_sequences()
  vim.keymap.set('i', '<Esc>Oq', '1', { noremap = true })
  vim.keymap.set('i', '<Esc>Or', '2', { noremap = true })
  vim.keymap.set('i', '<Esc>Os', '3', { noremap = true })
  vim.keymap.set('i', '<Esc>Ot', '4', { noremap = true })
  vim.keymap.set('i', '<Esc>Ou', '5', { noremap = true })
  vim.keymap.set('i', '<Esc>Ov', '6', { noremap = true })
  vim.keymap.set('i', '<Esc>Ow', '7', { noremap = true })
  vim.keymap.set('i', '<Esc>Ox', '8', { noremap = true })
  vim.keymap.set('i', '<Esc>Oy', '9', { noremap = true })
  vim.keymap.set('i', '<Esc>Op', '0', { noremap = true })
end

-- Call the function to set up mappings
map_keypad_sequences()
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/PuTTY_numeric_keypad_mappings)
***
# Title: Quick Markdown Preview with External Tools
# Category: advanced_mappings
# Tags: markdown, preview, external-tools
---
Create a key mapping to quickly convert Markdown to HTML and open in a browser for instant preview

```vim
map ^P :w!<CR>:w!/home/user/tmp/vim-markdown.md<CR>:!pandoc -s -f markdown -t html -o /home/user/tmp/vim-markdown.html /home/user/tmp/vim-markdown.md<CR>:!dillo /home/user/tmp/vim-markdown.html > /dev/null 2> /dev/null&<CR><CR>
```

```lua
vim.keymap.set('n', '<C-p>', function()
  -- Save current file
  vim.cmd('write')
  
  -- Define temporary paths
  local tmp_md = '/home/user/tmp/vim-markdown.md'
  local tmp_html = '/home/user/tmp/vim-markdown.html'
  
  -- Write current buffer to temp markdown file
  vim.fn.writefile(vim.api.nvim_buf_get_lines(0, 0, -1, false), tmp_md)
  
  -- Convert markdown to HTML using pandoc
  os.execute(string.format('pandoc -s -f markdown -t html -o %s %s', tmp_html, tmp_md))
  
  -- Open in browser (can replace 'dillo' with preferred browser)
  os.execute(string.format('dillo %s > /dev/null 2> /dev/null &', tmp_html))
end, { desc = 'Quick Markdown Preview' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Quick_Markdown_Preview)
***
# Title: Quick Insert Mode Commands via Double Letters
# Category: advanced_mappings
# Tags: key-mapping, insert-mode, productivity
---
Map double uppercase letters to perform quick normal mode actions without leaving insert mode, improving editing efficiency

```vim
" Quick movements
" Go to first non-blank text
inoremap II <Esc>I
" Go to end of line
inoremap AA <Esc>A
" Open new line above
inoremap OO <Esc>O

" Line modifications
" Change right of cursor
inoremap CC <Esc>C
" Change whole line
inoremap SS <Esc>S
" Delete current line
inoremap DD <Esc>dd
" Undo
inoremap UU <Esc>u
```

```lua
-- Quick movements and line modifications
local function setup_insert_mode_mappings()
  vim.keymap.set('i', 'II', '<Esc>I', { desc = 'Go to first non-blank text' })
  vim.keymap.set('i', 'AA', '<Esc>A', { desc = 'Go to end of line' })
  vim.keymap.set('i', 'OO', '<Esc>O', { desc = 'Open new line above' })
  vim.keymap.set('i', 'CC', '<Esc>C', { desc = 'Change right of cursor' })
  vim.keymap.set('i', 'SS', '<Esc>S', { desc = 'Change whole line' })
  vim.keymap.set('i', 'DD', '<Esc>dd', { desc = 'Delete current line' })
  vim.keymap.set('i', 'UU', '<Esc>u', { desc = 'Undo' })
end

setup_insert_mode_mappings()
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Quick_command_in_insert_mode)
***
# Title: Quick Insert Character at End of Line
# Category: advanced_mappings
# Tags: key-mapping, insert-mode, productivity
---
Quickly add a character (like semicolon or quote) at the end of the current line without moving the cursor

```vim
imap <silent><F2> <Esc>v`^me<Esc>gi<C-o>:call Ender()<CR>

function Ender()
  let endchar = nr2char(getchar())
  execute "normal \<End>a".endchar
  normal `e
endfunction
```

```lua
vim.keymap.set('i', '<F2>', function()
  -- Record current position
  local current_line = vim.fn.line('.')
  local current_col = vim.fn.col('.')
  
  -- Move to end of line and prompt for character
  local endchar = vim.fn.nr2char(vim.fn.getchar())
  vim.cmd('normal! A' .. endchar)
  
  -- Return to original position
  vim.fn.cursor(current_line, current_col)
end, { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Quick_insert_character_at_end-of-line)
***
# Title: Custom Toolbar URL Launcher
# Category: advanced_mappings
# Tags: toolbar, custom-mapping, windows
---
Replace existing toolbar icon to launch selected URL in browser using visual mode

```vim
vnoremenu 1.140 ToolBar.New "wy:!start explorer <C-R>w<CR>
```

```lua
vim.keymap.set('v', '<ToolBar>New', function()
  local selected_text = vim.fn.getreg('"')
  vim.fn.system('start explorer ' .. selected_text)
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Quick_launch_html_and_other_Windows_documents)
***
# Title: Dynamic File Preview in Index/Listing
# Category: advanced_mappings
# Tags: file-preview, custom-mapping, dynamic-loading
---
Create a custom mapping to quickly preview files from an index or listing, with version-aware implementation

```vim
nnoremap <buffer> <Space> :exec "let alist=readfile(expand('%:p:h').'/'.substitute(getline('.'), '\(^.*\|\s*\)\|\(\s\s*$\)', '', 'g'))\|echo join(alist,\"\n\")"<CR>
```

```lua
vim.keymap.set('n', '<Space>', function()
  local filename = vim.fn.expand('%:p:h') .. '/' .. vim.fn.substitute(vim.fn.getline('.'), '\(^.*\|\s*\)\|\(\s\s*$\)', '', 'g')
  local lines = vim.fn.readfile(filename)
  print(table.concat(lines, '\n'))
end, { buffer = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Quick_peek_at_files)
***
# Title: Quick Braces Insertion in Insert Mode
# Category: advanced_mappings
# Tags: key-mapping, programming, productivity
---
Quickly insert opening and closing braces with automatic indentation, saving keystrokes when programming

```vim
" Opening and closing braces
imap <C-F> {<CR>}<C-O>O
```

```lua
-- Quick braces insertion
vim.keymap.set('i', '<C-f>', '{<CR>}<C-o>O', { desc = 'Insert braces with auto-indent' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Quick_way_to_insert_opening_and_closing_braces_for_programmers)
***
# Title: Quick Word/Line Change with Auto-Exit
# Category: advanced_mappings
# Tags: key-mapping, editing-workflow, custom-mapping
---
Custom mappings to quickly change text and exit insert mode with Space or Enter

```vim
nmap pw :inoremap <Space> <Space><Esc>:iunmap <Space><CR><CR> cw
nmap p$ :inoremap <CR> <CR><Esc>:iunmap <CR><CR><CR> c$
```

```lua
-- Lua equivalent with modern Neovim mapping
vim.keymap.set('n', 'pw', function()
  vim.api.nvim_buf_set_keymap(0, 'i', '<Space>', '<Space><Esc>', {noremap = true, silent = true})
  vim.cmd('normal! cw')
end, { desc = 'Change word and exit with Space' })

vim.keymap.set('n', 'p$', function()
  vim.api.nvim_buf_set_keymap(0, 'i', '<CR>', '<CR><Esc>', {noremap = true, silent = true})
  vim.cmd('normal! c$')
end, { desc = 'Change to line end and exit with Enter' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Quickly_change_word_or_line)
***
# Title: Quick Single Word Insertion Mapping
# Category: advanced_mappings
# Tags: key-mapping, insert-mode, workflow
---
Create a custom mapping to quickly insert a single word and automatically exit insert mode

```vim
nmap <buffer> <silent> ,w :exec ":imap \<space\> \<space\>\<esc\>,BB"<CR>i
nmap <buffer> <silent> ,BB :exec ":iunmap \<space\>"<CR>
```

```lua
vim.keymap.set('n', ',w', function()
  -- Temporarily map space to exit insert mode
  vim.keymap.set('i', ' ', function()
    vim.cmd('stopinsert')
    vim.keymap.del('i', ' ')
  end, { buffer = true })
  vim.cmd('startinsert')
end, { desc = 'Quick word insertion' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Quickly_insert_a_single_word)
***
# Title: Toggle Less-like Scrolling Mode
# Category: advanced_mappings
# Tags: scrolling, key-mapping, mode-toggle
---
Adds a toggle to switch between normal editing and pager-like scrolling, allowing easy navigation without moving the cursor

```vim
function! LessMode()
  if g:lessmode == 0
    let g:lessmode = 1
    noremap <script> d <C-D>
    noremap <script> j <C-E>
    noremap <script> u <C-U>
    noremap <script> k <C-Y>
  else
    let g:lessmode = 0
    unmap d
    unmap j
    unmap u
    unmap k
  endif
endfunction

let g:lessmode = 0
nnoremap <F5> :call LessMode()<CR>
inoremap <F5> <Esc>:call LessMode()<CR>
```

```lua
local less_mode = false

local function toggle_less_mode()
  less_mode = not less_mode
  if less_mode then
    vim.keymap.set('n', 'd', '<C-D>')
    vim.keymap.set('n', 'j', '<C-E>')
    vim.keymap.set('n', 'u', '<C-U>')
    vim.keymap.set('n', 'k', '<C-Y>')
    print('Less mode on')
  else
    vim.keymap.unset('n', 'd')
    vim.keymap.unset('n', 'j')
    vim.keymap.unset('n', 'u')
    vim.keymap.unset('n', 'k')
    print('Less mode off')
  end
end

vim.keymap.set('n', '<F5>', toggle_less_mode)
vim.keymap.set('i', '<F5>', '<Esc>' .. toggle_less_mode)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Quickly_switch_between_pager-like_and_editor-like_scroll)
***
# Title: Convert Quoted Printable Email to Plain Text
# Category: advanced_mappings
# Tags: email, text-conversion, key-mapping
---
Quick mapping to decode quoted printable encoded emails in Vim, converting special encodings to readable text

```vim
nnoremap <Leader>Q :%s/=\(\x\x\<BAR>\n\)/\=submatch(1)=='
'?'':nr2char('0x'.submatch(1))/ge<CR>
vnoremap <Leader>Q :s/=\(\x\x\<BAR>\n\)/\=submatch(1)=='
'?'':nr2char('0x'.submatch(1))/ge<CR>
```

```lua
vim.keymap.set('n', '<Leader>Q', function()
  vim.cmd([[%s/=\(\x\x\|\n\)/\=submatch(1) == '\n' ? '' : nr2char('0x' . submatch(1))/ge]])
end, { desc = 'Convert Quoted Printable to Plain Text' })

vim.keymap.set('v', '<Leader>Q', function()
  vim.cmd([[s/=\(\x\x\|\n\)/\=submatch(1) == '\n' ? '' : nr2char('0x' . submatch(1))/ge]])
end, { desc = 'Convert Selected Quoted Printable to Plain Text' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Quoted_Printable_to_Plain)
***
# Title: Simple RCS Version Control Mappings
# Category: advanced_mappings
# Tags: version-control, rcs, key-mapping
---
Quick mappings for basic RCS version control operations directly from Vim, allowing check-in and check-out of files with function keys

```vim
map <F1> :write %<CR>:!ci -l %<CR>:edit!<CR>
map <F2> :!co -l %<CR>:edit!<CR>
```

```lua
vim.keymap.set('n', '<F1>', function()
  vim.cmd.write()
  os.execute('ci -l ' .. vim.fn.expand('%'))
  vim.cmd.edit({ bang = true })
end, { desc = 'RCS Check-in' })

vim.keymap.set('n', '<F2>', function()
  os.execute('co -l ' .. vim.fn.expand('%'))
  vim.cmd.edit({ bang = true })
end, { desc = 'RCS Check-out' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Really_basic_RCS_interaction_from_within_vim)
***
# Title: Prevent Accidental Text Deletion in Insert Mode
# Category: advanced_mappings
# Tags: insert-mode, undo, key-mapping
---
Add an undo breakpoint before Ctrl-U and Ctrl-W deletions to make them undoable

```vim
inoremap <c-u> <c-g>u<c-u>
inoremap <c-w> <c-g>u<c-w>
```

```lua
vim.keymap.set('i', '<C-u>', '<C-g>u<C-u>', { desc = 'Undo-breakpoint before line deletion' })
vim.keymap.set('i', '<C-w>', '<C-g>u<C-w>', { desc = 'Undo-breakpoint before word deletion' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Recover_from_accidental_Ctrl-U)
***
# Title: Create Recursive Vim Mappings for Repetitive Editing
# Category: advanced_mappings
# Tags: macro, mapping, automation, editing
---
Recursive mappings allow you to create powerful, self-repeating editing commands that can automatically process multiple lines or perform complex transformations

```vim
" Example 1: Recursive mapping to process file names
:map z Iwc <Esc>lyawA><Esc>pa.log<CR>echo "HelloWorld"<Esc>jz

" Example 2: Recursive mapping to increment numbers
:map z 2^Ajz
```

```lua
-- Lua implementation requires more explicit handling
-- This demonstrates the concept rather than direct translation
function RecursiveFileProcessing()
  -- Move to start of line
  vim.cmd('normal! Iwc ')
  -- Copy word
  vim.cmd('normal! lyaw')
  -- Append log and echo
  vim.cmd('normal! A> echo "HelloWorld"')
  -- Move to next line
  vim.cmd('normal! j')
end

-- Can be mapped using more modern Neovim mapping
vim.keymap.set('n', 'z', RecursiveFileProcessing)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Recursive_mappings)
***
# Title: Remap CapsLock to Escape or Ctrl in Neovim
# Category: advanced_mappings
# Tags: key-mapping, productivity, input-optimization
---
Efficiently remap CapsLock key to Escape or Ctrl to improve keyboard ergonomics and reduce hand movement in Neovim

```lua
-- Remap CapsLock to Escape using AutoHotkey (Windows)
-- In Neovim init.lua
vim.keymap.set('i', '<C-c>', '<Esc>', { desc = 'Alternative escape method' })

-- For system-wide remapping, use AutoHotkey or Keyboard Manager
-- Example Lua mapping to simulate CapsLock behavior
local function caps_escape()
  if vim.fn.mode() == 'i' then
    return '<Esc>'
  else
    return '<C-\>'
  end
end

vim.keymap.set({'i', 'n'}, '<CapsLock>', caps_escape, { expr = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Remap_CapsLock_or_other_keys_without_reboot_in_Windows)
***
# Title: Context-Specific Key Remapping with AutoHotkey
# Category: advanced_mappings
# Tags: key-mapping, conditional-mapping, workflow
---
Efficiently copy and replace text at multiple locations using yanking and dot command

```vim
# Copy word: yiw
# Replace word: ciw<C-R>0<Esc>
# Repeat replacements with '.'
```

```lua
-- Copy word: 'yiw'
-- Replace word: 'ciw' .. vim.fn.getreg('0') .. '<Esc>'
-- Use '.' to repeat replacements
-- Leverage vim.fn.getreg() to access registers in Lua
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Repeat_last_change)
***
# Title: Repeat Last Command at Start of Change
# Category: advanced_mappings
# Tags: key-mapping, editing, productivity
---
Modify the dot (.) command to return cursor to start of previous change, making repetitive editing across multiple lines easier

```vim
nmap . .`[
```

```lua
vim.keymap.set('n', '.', function()
  vim.cmd('normal! .`[')
end, { desc = 'Repeat last command and return to change start' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Repeat_last_command_and_put_cursor_at_start_of_change)
***
# Title: Quick Word/Selection Replacement Mappings
# Category: advanced_mappings
# Tags: clipboard, key-mapping, visual-mode
---
Efficient method to replace multiple words or text objects using change and register recall

```vim
" Replace words consistently with repeatability
" yiw (yank word)
" ciw<C-r>0 (change inner word, paste from register 0)
" . (repeat last change)
```

```lua
-- Note: This workflow is inherently Vim-like and works similarly in Neovim
-- 1. yank word with yiw
-- 2. Move to target word
-- 3. Use ciw<C-r>0 to replace
-- 4. Use . to repeat
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Replacing_a_string_with_default_buffer_contents)
***
# Title: Quickfix-Powered Code Review Workflow
# Category: advanced_mappings
# Tags: code-review, workflow, quickfix, collaboration
---
Create a systematic code review process using Vim's quickfix list to track and navigate review comments across files

```vim
function SavePosition()
  let g:file_name=expand("%:t")
  let g:line_number=line(".")
  let g:reviewer_initials="KG" " Your initials
endfunction

function InsertComment()
  execute "normal i". g:file_name . ":" . g:line_number . ": " . g:reviewer_initials . " - "
  startinsert
endfunction
nmap ,sp :call SavePosition()<CR>
nmap ,ic :call InsertComment()<CR>
```

```lua
function _G.save_position()
  vim.g.file_name = vim.fn.expand('%:t')
  vim.g.line_number = vim.fn.line('.')
  vim.g.reviewer_initials = 'KG' -- Your initials
end

function _G.insert_comment()
  local cmd = string.format('normal i%s:%d: %s - ', 
    vim.g.file_name, vim.g.line_number, vim.g.reviewer_initials)
  vim.cmd(cmd)
  vim.cmd('startinsert')
end

vim.keymap.set('n', ',sp', _G.save_position, {})
vim.keymap.set('n', ',ic', _G.insert_comment, {})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Review_code_effectively_using_quickfix)
***
# Title: Quick Number Conversion Under Cursor
# Category: advanced_mappings
# Tags: mapping, number-conversion, utility
---
Add a custom mapping to quickly convert and display the number under the cursor between decimal and hexadecimal formats

```vim
nnoremap gn :call DecAndHex(expand("<cWORD>"))<CR>
```

```lua
vim.keymap.set('n', 'gn', function()
  local word = vim.fn.expand('<cWORD>')
  local dec = tonumber(word)
  local hex = tonumber(word, 16)
  
  if dec then
    print(string.format('%d -> 0x%X', dec, dec))
  elseif hex then
    print(string.format('0x%X -> %d', hex, hex))
  else
    print('Not a valid number')
  end
end, { desc = 'Convert number under cursor' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip448)
***
# Title: Use Ctrl-O for Single Normal Mode Command in Insert Mode
# Category: advanced_mappings
# Tags: key-mapping, insert-mode, productivity
---
Ctrl-O allows executing a single normal mode command while in insert mode without fully exiting, preventing cursor movement issues

```vim
:imap <F5> <C-o>:set number!<CR>
```

```lua
vim.keymap.set('i', '<F5>', '<C-o>:set number!<CR>', { desc = 'Toggle line numbers in insert mode' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip459)
***
# Title: Flexible Insert Mode Command Execution
# Category: advanced_mappings
# Tags: key-mapping, command-execution, productivity
---
Multiple approaches to running commands in insert mode: multiple Ctrl-O, using | for multiple commands, or defining a custom function

```vim
:map <F5> :set number!<CR>
:imap <F5> <c-o><F5>
```

```lua
vim.keymap.set('n', '<F5>', ':set number!<CR>')
vim.keymap.set('i', '<F5>', '<c-o><F5>', { desc = 'Execute normal mode F5 from insert mode' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip459)
***
# Title: Quick XML Element Creation Mapping
# Category: advanced_mappings
# Tags: xml, text-expansion, insert-mode
---
Rapidly create XML elements from any word in insert mode by typing the word followed by three commas

```vim
imap ,,, <Esc>diwi<<Esc>pa><CR></<Esc>pa><Esc>kA
```

```lua
vim.keymap.set('i', ',,,', function()
  -- Get current word
  local word = vim.fn.expand('<cword>')
  -- Delete word and create XML element
  vim.cmd('normal! diw')
  vim.api.nvim_put({string.format('<%s>', word)}, '', true, true)
  vim.cmd('normal! o')
  vim.api.nvim_put({string.format('</%s>', word)}, '', true, true)
  vim.cmd('normal! k')
end, { buffer = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip465)
***
# Title: Quick Single Character Insertion
# Category: advanced_mappings
# Tags: key-mapping, editing, efficiency
---
Quickly insert a single character without switching to insert mode, with support for character repetition

```vim
function! RepeatChar(char, count)
  return repeat(a:char, a:count)
endfunction
nnoremap s :<C-U>exec "normal i".RepeatChar(nr2char(getchar()), v:count1)<CR>
nnoremap S :<C-U>exec "normal a".RepeatChar(nr2char(getchar()), v:count1)<CR>
```

```lua
function RepeatChar(char, count)
  return string.rep(char, count)
end

vim.keymap.set('n', 's', function()
  local count = vim.v.count1
  local char = vim.fn.nr2char(vim.fn.getchar())
  vim.cmd('normal! i' .. string.rep(char, count))
end)

vim.keymap.set('n', 'S', function()
  local count = vim.v.count1
  local char = vim.fn.nr2char(vim.fn.getchar())
  vim.cmd('normal! a' .. string.rep(char, count))
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip466)
***
# Title: Advanced Word Swapping Mapping
# Category: advanced_mappings
# Tags: text-manipulation, key-mapping
---
Custom mapping to swap words without changing cursor position, supporting complex word exchanges

```vim
nnoremap <silent> gw "_yiw:s/\(%#\w\+\)\(\W\+\)\(\w\+\)/\3\2\1/<CR><c-o><c-l>:nohlsearch<CR>
```

```lua
vim.keymap.set('n', 'gw', function()
  local current_word = vim.fn.expand('<cword>')
  local next_word = vim.fn.expand('<cword>')
  -- Implement word swapping logic
  -- This is a simplified placeholder
end, { desc = 'Swap current word with next' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip47)
***
# Title: Restore Cursor Position After Repeat Command
# Category: advanced_mappings
# Tags: cursor-movement, key-mapping, editing
---
Modify the dot (.) repeat command to maintain cursor position after repeating the last edit, similar to Emacs behavior

```vim
"make . not move the cursor
noremap . mz.`z
```

```lua
vim.keymap.set('n', '.', function()
  local mark = vim.fn.getpos('.')
  vim.cmd('normal! .')
  vim.fn.setpos('.', mark)
end, { desc = 'Repeat last edit without moving cursor' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip474)
***
# Title: Alternative Cursor Position Preservation Mapping
# Category: advanced_mappings
# Tags: cursor-movement, key-mapping
---
An alternative method to preserve cursor position after repeating a command, using a different mark technique

```vim
noremap . .'^
```

```lua
vim.keymap.set('n', '.', function()
  vim.cmd('normal! .')
  vim.cmd('normal! `[')
end, { desc = 'Repeat last edit with minimal cursor movement' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip474)
***
# Title: Quick Word Replacement Without Typing
# Category: advanced_mappings
# Tags: word-replace, registers, key-mapping
---
Efficiently replace words using registers without manual retyping, allowing fast word substitution across multiple occurrences

```vim
" Copy word to register b
noremap gy lb"bye

" Replace word with register b (with space)
noremap go lb"bPldwi <Esc>hbye

" Replace word with register b (without space)
noremap gp lb"bPldwhbyw
```

```lua
-- Copy word to register b
vim.keymap.set('n', 'gy', 'lb"bye', { desc = 'Yank word to register b' })

-- Replace word with register b (with space)
vim.keymap.set('n', 'go', 'lb"bPldwi <Esc>hbye', { desc = 'Replace word with register b and add space' })

-- Replace word with register b (without space)
vim.keymap.set('n', 'gp', 'lb"bPldwhbyw', { desc = 'Replace word with register b' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip479)
***
# Title: Numeric Keypad Escape Sequence Mapping
# Category: advanced_mappings
# Tags: key-mapping, terminal, input
---
Map PuTTY numeric keypad escape sequences to actual numbers in Vim

```vim
" Map numeric keypad escape sequences
:inoremap <Esc>Oq 1
:inoremap <Esc>Or 2
:inoremap <Esc>Os 3
:inoremap <Esc>Ot 4
:inoremap <Esc>Ou 5
:inoremap <Esc>Ov 6
:inoremap <Esc>Ow 7
:inoremap <Esc>Ox 8
:inoremap <Esc>Oy 9
:inoremap <Esc>Op 0
```

```lua
-- Map numeric keypad escape sequences
vim.keymap.set('i', '<Esc>Oq', '1')
vim.keymap.set('i', '<Esc>Or', '2')
vim.keymap.set('i', '<Esc>Os', '3')
vim.keymap.set('i', '<Esc>Ot', '4')
vim.keymap.set('i', '<Esc>Ou', '5')
vim.keymap.set('i', '<Esc>Ov', '6')
vim.keymap.set('i', '<Esc>Ow', '7')
vim.keymap.set('i', '<Esc>Ox', '8')
vim.keymap.set('i', '<Esc>Oy', '9')
vim.keymap.set('i', '<Esc>Op', '0')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip503)
***
# Title: Open Windows Help Files with Custom Keymapping
# Category: advanced_mappings
# Tags: windows, help, key-mapping
---
Create custom keymappings to quickly open Windows HTML help files for specific topics, using either current word or visual selection

```vim
nnoremap <C-F1> :silent! !cmd.exe /c start keyhh.exe -#klink "<C-R><C-W>" "$ASANY9\docs\dbmaen9.chm"<CR><CR>
vnoremap <C-F1> :<C-U>let old_reg=@"<CR>gvy:silent!!cmd.exe /cstart keyhh.exe -#klink "<C-R><C-R>"" "$ASANY9\docs\dbmaen9.chm"<CR><CR>:let @"=old_reg<CR>:echo ""<CR>
```

```lua
vim.keymap.set('n', '<C-F1>', function()
  vim.cmd.silent('!cmd.exe /c start keyhh.exe -#klink "' .. vim.fn.expand('<cword>') .. '" "$ASANY9\\docs\\dbmaen9.chm"')
end)

vim.keymap.set('v', '<C-F1>', function()
  local old_reg = vim.fn.getreg('"')
  vim.cmd.normal{'gvy'}
  local selected_text = vim.fn.getreg('"')
  vim.cmd.silent('!cmd.exe /c start keyhh.exe -#klink "' .. selected_text .. '" "$ASANY9\\docs\\dbmaen9.chm"')
  vim.fn.setreg('"', old_reg)
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip506)
***
# Title: Dynamic Search Mode Cycling
# Category: advanced_mappings
# Tags: search, custom-mapping, productivity
---
Create a custom F4 mapping to cycle through different search result display modes

```vim
function! s:SearchMode()
  if !exists('s:searchmode') || s:searchmode == 0
    nnoremap <silent> n n:call <SID>MaybeMiddle()<CR>
    let s:searchmode = 1
  elseif s:searchmode == 1
    nnoremap n nzz
    let s:searchmode = 2
  else
    nunmap n
    let s:searchmode = 0
  endif
endfunction
```

```lua
local function search_mode()
  local modes = {
    [0] = function()
      vim.keymap.set('n', 'n', function()
        local winline = vim.fn.winline()
        local winheight = vim.fn.winheight(0)
        if winline == 1 or winline == winheight then
          vim.cmd('normal! zz')
        end
        vim.cmd('normal! n')
      end)
    end,
    [1] = function()
      vim.keymap.set('n', 'n', 'nzz')
    end,
    [2] = function()
      vim.keymap.del('n', 'n')
    end
  }

  local current_mode = vim.g.search_mode or 0
  local next_mode = (current_mode + 1) % 3
  
  modes[next_mode]()
  vim.g.search_mode = next_mode
end

-- Bind to F4
vim.keymap.set('n', '<F4>', search_mode)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip528)
***
# Title: Configure Shift-Tab Key Behavior in Vim
# Category: advanced_mappings
# Tags: key-mapping, terminal-compatibility
---
Solve issues with Shift-Tab key mapping across different terminals and systems, enabling consistent key behavior

```vim
" Map Shift-Tab to work correctly
map <Esc>[Z <s-tab>
ounmap <Esc>[Z

" Alternatively, set terminal key code
exe 'set t_kB=' . nr2char(27) . '[Z'
```

```lua
-- Map Shift-Tab in Neovim
vim.keymap.set({'n', 'i', 'v'}, '<S-Tab>', '<C-d>', { desc = 'Unindent or navigate back' })

-- Set terminal key code for compatibility
vim.o.t_kB = vim.fn.nr2char(27) .. '[Z'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip529)
***
# Title: Smart Table Navigation with Custom Field Movement
# Category: advanced_mappings
# Tags: navigation, table-editing, custom-function
---
Provides a custom function to intelligently move between table columns, automatically padding lines and handling variable field lengths

```vim
func! NextField(fieldsep,minlensep,padstr,offset)
  let curposn = col(".")
  let linenum = line(".")
  let prevline = getline(linenum-1)
  let curline = getline(linenum)
  let nextposn = matchend(prevline,a:fieldsep,curposn-a:minlensep)+1
  let padding = ""
  if nextposn > strlen(prevline) || linenum == 1 || nextposn == 0
    echo "last field or no fields on line above"
    return
  endif
  echo ""
  if nextposn > strlen(curline)
    if &modifiable == 0
      return
    endif
    let i = strlen(curline)
    while i < nextposn - 1
      let i = i + 1
      let padding = padding . a:padstr
    endwhile
    call setline(linenum,substitute(curline,"$",padding,""))
  endif
  call cursor(linenum,nextposn+a:offset)
  return
endfunc
```

```lua
function _G.next_field(fieldsep, minlensep, padstr, offset)
  local curposn = vim.fn.col('.')
  local linenum = vim.fn.line('.')
  local prevline = vim.fn.getline(linenum - 1)
  local curline = vim.fn.getline(linenum)
  
  local nextposn = vim.fn.matchend(prevline, fieldsep, curposn - minlensep) + 1
  
  if nextposn > #prevline or linenum == 1 or nextposn == 0 then
    print('last field or no fields on line above')
    return
  end
  
  if nextposn > #curline then
    if vim.o.modifiable == false then
      return
    end
    
    local padding = string.rep(padstr, nextposn - #curline)
    vim.fn.setline(linenum, curline .. padding)
  end
  
  vim.fn.cursor(linenum, nextposn + offset)
end

-- Example mapping
vim.keymap.set({'n', 'i'}, '<S-Tab>', function()
  _G.next_field(' {2,}', 2, ' ', 0)
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip547)
***
# Title: Smart Table Editing with Tab Navigation
# Category: advanced_mappings
# Tags: navigation, text-editing, tables
---
Dynamically map Tab and Shift-Tab to navigate between table fields in both insert and normal modes, with automatic padding and alignment

```vim
" In table.vim script
map <Tab> :call NextField()<CR>
map <S-Tab> :call PreviousField()<CR>
```

```lua
-- Lua equivalent (conceptual)
function _G.next_table_field()
  -- Implement field navigation logic
end

vim.keymap.set({'n', 'i'}, '<Tab>', _G.next_table_field)
vim.keymap.set({'n', 'i'}, '<S-Tab>', _G.previous_table_field)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip554)
***
# Title: Quick File Save Mapping
# Category: advanced_mappings
# Tags: key-mapping, file-operations, productivity
---
Create a quick leader key mapping to save files only when changes have been made, avoiding unnecessary writes

```vim
noremap <Leader>s :update<CR>
```

```lua
vim.keymap.set('n', '<leader>s', ':update<CR>', { desc = 'Save file if modified' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip582)
***
# Title: Enhanced Block Selection with Matchit
# Category: advanced_mappings
# Tags: selection, text-objects, code-navigation
---
Replace words quickly with last yanked text using a custom mapping

```vim
" Replace current word with last yanked text
nnoremap S diw"0P
```

```lua
-- Lua equivalent for word stamping
vim.keymap.set('n', 'S', function()
  vim.cmd('normal! diw"0P')
end, { noremap = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip605)
***
# Title: Create Custom Keymaps for Language Mapping
# Category: advanced_mappings
# Tags: key-mapping, internationalization, custom-keymap
---
Create custom keymaps for different languages, allowing translation of keyboard inputs with flexible mapping options

```vim
" Example keymap for Czech with UTF-8
let b:keymap_name = "cz"
highlight lCursor ctermbg=red guibg=red

loadkeymap
" Key mappings go here
A <Char-0x00C1>  " Map A to Á
```

```lua
-- Lua equivalent for custom keymap
vim.g.keymap_name = "cz"
vim.cmd.highlight("lCursor ctermbg=red guibg=red")

-- Note: Full keymap loading requires Vim script
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip619)
***
# Title: Quick C Debugging Print Statement Macro
# Category: advanced_mappings
# Tags: debugging, key-mapping
---
Quickly insert fprintf debugging statements with file and line information for easier tracking and removal

```vim
nmap _if ofprintf(0<C-d>stderr, "{%s} {%d} - \n", __FILE__, __LINE__);<Esc>F\i
```

```lua
vim.keymap.set('n', '_if', function()
  local debug_stmt = string.format('fprintf(0stderr, "{%%s} {%%d} - \n", __FILE__, __LINE__);
')
  vim.api.nvim_put({ debug_stmt }, 'l', true, true)
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip625)
***
# Title: Execute Files and URLs from Buffer Text in Windows
# Category: advanced_mappings
# Tags: windows, file-execution, key-mapping
---
Create mappings to quickly open files, URLs, or execute commands directly from buffer text in Vim/Neovim on Windows

```vim
" eXecute File being edited
nmap \xf :silent !start rundll32 url.dll,FileProtocolHandler %:p <CR>

"eXecute string below cursor
nmap \x :silent !start rundll32 url.dll,FileProtocolHandler <cWORD> <CR>

" eXecute string below cursor after prepending it with path to file
nmap \xl :silent !start rundll32 url.dll,FileProtocolHandler %:p:h/<cWORD> <CR>
```

```lua
-- Execute current file
vim.keymap.set('n', '\xf', function()
  vim.cmd.silent('!start rundll32 url.dll,FileProtocolHandler ' .. vim.fn.expand('%:p'))
end, { desc = 'Open current file' })

-- Execute word under cursor
vim.keymap.set('n', '\x', function()
  vim.cmd.silent('!start rundll32 url.dll,FileProtocolHandler ' .. vim.fn.expand('<cWORD>'))
end, { desc = 'Execute word under cursor' })

-- Execute word with current file path
vim.keymap.set('n', '\xl', function()
  vim.cmd.silent('!start rundll32 url.dll,FileProtocolHandler ' .. vim.fn.expand('%:p:h') .. '/' .. vim.fn.expand('<cWORD>'))
end, { desc = 'Execute word with file path' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip628)
***
# Title: Auto-Insert Closing Characters with Smart Behavior
# Category: advanced_mappings
# Tags: insert-mode, autocomplete, key-mapping
---
Automatically insert closing characters like parentheses, braces, and quotes with intelligent handling of different scenarios

```vim
inoremap {      {}<Left>
inoremap {<CR>  {<CR>}<Esc>O
inoremap {{     {
inoremap {}     {}

inoremap (  ()<Left>
inoremap <expr> )  strpart(getline('.'), col('.')-1, 1) == ")" ? "\<Right>" : ")"
```

```lua
-- Lua equivalent for closing characters
vim.keymap.set('i', '{', '{}<Left>', { desc = 'Auto-insert closing brace' })
vim.keymap.set('i', '{<CR>', '{<CR>}<Esc>O', { desc = 'Auto-insert closing brace on new line' })
vim.keymap.set('i', '{{', '{', { desc = 'Prevent double brace insertion' })
vim.keymap.set('i', '{}', '{}', { desc = 'Allow empty braces' })

vim.keymap.set('i', '(', '()<Left>', { desc = 'Auto-insert closing parenthesis' })
vim.keymap.set('i', ')', function()
  local line = vim.fn.getline('.')
  local col = vim.fn.col('.')
  return line:sub(col, col) == ')' and '<Right>' or ')'
end, { expr = true, desc = 'Smart closing parenthesis handling' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip630)
***
# Title: Run Windows Program with K Keymap
# Category: advanced_mappings
# Tags: key-mapping, command-execution, windows
---
Quickly disable built-in Vim key commands that you find annoying or accidentally trigger

```vim
:map K <Nop>
```

```lua
vim.keymap.set('n', 'K', '<Nop>', { desc = 'Disable built-in K command' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip643)
***
# Title: Quick Abbreviation Expansion Mapping
# Category: advanced_mappings
# Tags: abbreviation, mapping, productivity
---
Provides a quick way to expand existing abbreviations with a custom keybinding

```vim
map <C-X><C-X> diw:exe "normal i".@"<CR>
```

```lua
vim.keymap.set('n', '<C-X><C-X>', function()
  -- Alternative implementation that works better
  vim.cmd('ciw@')
  vim.cmd('normal! "_s\<C-R>"')
  vim.cmd('normal! b')
end, { desc = 'Expand existing abbreviation' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip649)
***
# Title: Automatic Comment Mapping for Different Filetypes
# Category: advanced_mappings
# Tags: comments, filetype, autocmd, mapping
---
Check for existing backspace mappings and remove them if they're causing issues

```vim
" Check backspace mappings
:verbose imap <BS>

" Remove problematic mapping
:iunmap <BS>
```

```lua
-- Check backspace mappings
vim.cmd('verbose imap <BS>')

-- Remove problematic mapping
vim.keymap.del('i', '<BS>')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip68)
***
# Title: Clipboard Keymappings for macOS
# Category: advanced_mappings
# Tags: clipboard, key-mapping, productivity
---
Create convenient keymappings for copying and pasting using system clipboard

```vim
map <F2> :.w !pbcopy<CR><CR>
map <F3> :r !pbpaste<CR>
```

```lua
vim.keymap.set('n', '<F2>', ':.w !pbcopy<CR><CR>', { desc = 'Copy current line' })
vim.keymap.set('n', '<F3>', ':r !pbpaste<CR>', { desc = 'Paste from clipboard' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip687)
***
# Title: Easy French Character Input Mappings
# Category: advanced_mappings
# Tags: internationalization, text-input, character-mapping
---
Create intuitive mappings for quickly inserting French accented characters in insert and command modes

```vim
" French character mappings
map! ;z à
map! ;a â
map! ;b ä
map! ;c ç
map! ;d è
map! ;e ê
map! ;f ë
map! ;g é
imap ;q «  »<Esc>hi
```

```lua
-- French character mappings for Neovim
vim.keymap.set({'i', 'c'}, ';z', 'à', { desc = 'Insert à' })
vim.keymap.set({'i', 'c'}, ';a', 'â', { desc = 'Insert â' })
vim.keymap.set({'i', 'c'}, ';c', 'ç', { desc = 'Insert ç' })
vim.keymap.set('i', ';q', '«  »<Esc>hi', { desc = 'Insert French quotation marks' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip697)
***
# Title: Generate Code Templates with Vim
# Category: advanced_mappings
# Tags: code-generation, text-templates, productivity
---
Create powerful text templates with variable substitution using a custom Perl script to generate repetitive code structures quickly

```vim
vnoremap <F6> :!perl E:\Devtools\vim\vimfiles\template\truler.pl<CR>
```

```lua
vim.keymap.set('v', '<F6>', function()
  -- Example implementation would require adapting the Perl script
  -- or creating a similar Lua/Neovim function for template processing
  vim.cmd('!perl E:\\Devtools\\vim\\vimfiles\\template\\truler.pl')
end, { desc = 'Process code template' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip710)
***
# Title: Create Context-Aware Mappings for GUI and Console
# Category: advanced_mappings
# Tags: key-mapping, conditional-mapping, cross-platform
---
Dynamically create mappings that adapt between GUI and console Vim based on the current environment, reducing configuration duplication

```vim
function! ModeMapping(guiLhs, termLhs, rhs, ...)
  let mapCommand='map'
  if (a:0 > 0)
    let mapCommand=a:1
  endif
  if (has("gui_running"))
    echo mapCommand . " " . a:guiLhs . " " . a:rhs
  else
    echo mapCommand . " " . a:termLhs . " " . a:rhs
  endif
endfunction
```

```lua
function _G.mode_mapping(gui_lhs, term_lhs, rhs, map_command)
  map_command = map_command or 'map'
  if vim.g.gui_running then
    vim.cmd(map_command .. ' ' .. gui_lhs .. ' ' .. rhs)
  else
    vim.cmd(map_command .. ' ' .. term_lhs .. ' ' .. rhs)
  end
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip713)
***
# Title: Quick Uuencode/Decode Text in Vim
# Category: advanced_mappings
# Tags: encoding, text-processing, key-mapping
---
Provides convenient key mappings to uuencode and uudecode text in normal and visual modes, useful for email attachments and text encoding

```vim
nnoremap <silent> <Leader>ue :%!uuencode -m /dev/stdout<CR>
nnoremap <silent> <Leader>ud :%!uudecode -o /dev/stdout<CR>
vnoremap <silent> <Leader>ue !uuencode -m /dev/stdout<CR>
vnoremap <silent> <Leader>ud !uudecode -o /dev/stdout<CR>
```

```lua
vim.keymap.set('n', '<Leader>ue', ':%!uuencode -m /dev/stdout<CR>', { silent = true })
vim.keymap.set('n', '<Leader>ud', ':%!uudecode -o /dev/stdout<CR>', { silent = true })
vim.keymap.set('v', '<Leader>ue', '!uuencode -m /dev/stdout<CR>', { silent = true })
vim.keymap.set('v', '<Leader>ud', '!uudecode -o /dev/stdout<CR>', { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip749)
***
# Title: Advanced CapsLock Key Behavior
# Category: advanced_mappings
# Tags: key-mapping, custom-behavior, productivity
---
Create a custom CapsLock key that acts as Escape when tapped, and Ctrl when held with another key

```vim
" No direct Vim implementation
```

```lua
-- Conceptual Lua implementation would require external utility like AutoHotkey
-- Demonstrates advanced key remapping potential
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip75)
***
# Title: Advanced Pasted Text Selection with Preserve Mode
# Category: advanced_mappings
# Tags: text-selection, registers, visual-mode
---
Dynamically select pasted text while preserving the original visual mode (character, line, or block)

```vim
nnoremap <expr> gp '`[' . strpart(getregtype(), 0, 1) . '`]'
```

```lua
vim.keymap.set('n', 'gp', function() 
  return '`[' .. vim.fn.strpart(vim.fn.getregtype(), 0, 1) .. '`]'
end, { expr = true, desc = 'Select pasted text with original mode' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip759)
***
