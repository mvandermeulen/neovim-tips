# Title: Auto indent
# Category: Indentation
# Tags: indent, auto, format
---
Use `==` to auto-indent current line, or `{number}==` to auto-indent multiple lines.

```vim
==   " auto-indent current line
5==  " auto-indent 5 lines
```

**Source:** Community contributed
***
# Title: Quickly Reindent Code Blocks
# Category: indentation
# Tags: code-formatting, editing, movement
---
Powerful commands to reindent code blocks using text objects and motion commands

```vim
" Reindent inner block
=i{

" Reindent block including braces
=a{

" Reindent with cursor on brace
=%
```

```lua
-- Reindent inner block
vim.cmd('normal =i{')

-- Reindent block including braces
vim.cmd('normal =a{')

-- Reindent with cursor on brace
vim.cmd('normal =%%')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Auto_indent_on_finishing_a_code_block)
***
# Title: Increment/Decrement Block Indentation
# Category: indentation
# Tags: code-formatting, editing, movement
---
Easily increase or decrease indentation for code blocks using motion commands

```vim
" Increase indent of inner block
>i{

" Decrease indent of inner block
<i{
```

```lua
-- Increase indent of inner block
vim.cmd('normal >i{')

-- Decrease indent of inner block
vim.cmd('normal <i{')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Auto_indent_on_finishing_a_code_block)
***
# Title: Improve PHP and HTML Indentation Support
# Category: indentation
# Tags: php, html, filetype, indent
---
Custom indent script to handle mixed PHP and HTML files, providing better indentation support for files with embedded HTML in PHP

```vim
" Better indent support for PHP with HTML
function! GetPhpHtmlIndent(lnum)
  if exists('*HtmlIndent')
    let html_ind = HtmlIndent()
  else
    let html_ind = HtmlIndentGet(a:lnum)
  endif
  let php_ind = GetPhpIndent()
  
  if php_ind > -1
    return php_ind
  endif
  
  if html_ind > -1
    if getline(a:lnum) =~ "^<?" && (0< searchpair('<?', '', '?>', 'nWb')
          \ || 0 < searchpair('<?', '', '?>', 'nW'))
      return -1
    endif
    return html_ind
  endif
  
  return -1
endfunction

setlocal indentexpr=GetPhpHtmlIndent(v:lnum)
setlocal indentkeys+=<>>
```

```lua
local function get_php_html_indent(lnum)
  local html_ind = vim.fn['HtmlIndentGet'](lnum)
  local php_ind = vim.fn['GetPhpIndent']()
  
  if php_ind > -1 then
    return php_ind
  end
  
  if html_ind > -1 then
    local line = vim.fn.getline(lnum)
    if line:match('^<?') and (
      vim.fn.searchpair('<?', '', '?>', 'nWb') > 0 or
      vim.fn.searchpair('<?', '', '?>', 'nW') > 0
    ) then
      return -1
    end
    return html_ind
  end
  
  return -1
end

-- Set up for PHP files
vim.api.nvim_create_autocmd('FileType', {
  pattern = 'php',
  callback = function()
    vim.bo.indentexpr = 'v:lua.get_php_html_indent(v:lnum)'
    vim.bo.indentkeys = vim.bo.indentkeys .. ',<>'
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Better_indent_support_for_php_with_html)
***
# Title: Easy Indentation with Cursor Position Preserved
# Category: indentation
# Tags: key-mapping, indent, cursor-preservation
---
Indent lines in normal and insert mode while keeping the cursor in the same relative position

```vim
"Indent forward in normal mode
nmap <C-Tab> a<C-t><Esc>

"Indent backward in normal mode
nmap <C-S-Tab> a<C-d><Esc>

"Indent forward in insert mode
imap <C-Tab> <C-t>

"Indent backward in insert mode
imap <C-S-Tab> <C-d>
```

```lua
-- Indent forward in normal mode
vim.keymap.set('n', '<C-Tab>', 'a<C-t><Esc>', { desc = 'Indent line forward' })

-- Indent backward in normal mode
vim.keymap.set('n', '<C-S-Tab>', 'a<C-d><Esc>', { desc = 'Indent line backward' })

-- Indent forward in insert mode
vim.keymap.set('i', '<C-Tab>', '<C-t>', { desc = 'Indent line forward' })

-- Indent backward in insert mode
vim.keymap.set('i', '<C-S-Tab>', '<C-d>', { desc = 'Indent line backward' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Easy_indenting_in_insert_and_normal_mode_with_no_cursor_displacement)
***
# Title: Flexible Indentation and Tab Settings
# Category: indentation
# Tags: tabs, formatting, indentation
---
Configure indentation to use 4 spaces instead of tabs, with flexible shift width settings

```vim
" Indentation using 4 spaces
set shiftwidth=4
set softtabstop=4
set expandtab
```

```lua
-- Configure indentation
vim.opt.shiftwidth = 4
vim.opt.softtabstop = 4
vim.opt.expandtab = true
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Example_vimrc)
***
# Title: Preserve Indent Across Blank Lines
# Category: indentation
# Tags: indent, autoindent, blank-lines
---
Automatically maintain indentation when creating new lines, even when traversing blank lines. Useful for maintaining consistent code structure and readability.

```vim
function! IndentIgnoringBlanks(child)
  let lnum = v:lnum
  while v:lnum > 1 && getline(v:lnum-1) == ""
    normal k
    let v:lnum = v:lnum - 1
  endwhile
  if a:child == ""
    if ! &l:autoindent
      return 0
    elseif &l:cindent
      return cindent(v:lnum)
    endif
  else
    exec "let indent=".a:child
    if indent != -1
      return indent
    endif
  endif
  if v:lnum == lnum && lnum != 1
    return -1
  endif
  let next = nextnonblank(lnum)
  if next == lnum
    return -1
  endif
  if next != 0 && next-lnum <= lnum-v:lnum
    return indent(next)
  else
    return indent(v:lnum-1)
  endif
endfunction
```

```lua
function _G.indent_ignoring_blanks(child)
  local lnum = vim.v.lnum
  while lnum > 1 and vim.fn.getline(lnum - 1) == "" do
    vim.cmd('normal! k')
    lnum = lnum - 1
  end

  if child == "" then
    if not vim.bo.autoindent then
      return 0
    elseif vim.bo.cindent then
      return vim.fn.cindent(lnum)
    end
  else
    local indent = vim.fn.eval(child)
    if indent ~= -1 then
      return indent
    end
  end

  if lnum == vim.v.lnum and vim.v.lnum ~= 1 then
    return -1
  end

  local next = vim.fn.nextnonblank(lnum)
  if next == lnum then
    return -1
  end

  if next ~= 0 and next - lnum <= lnum - vim.v.lnum then
    return vim.fn.indent(next)
  else
    return vim.fn.indent(vim.v.lnum - 1)
  end
end

-- Usage
vim.cmd('command! -bar IndentIgnoringBlanks lua _G.setup_indent_ignoring_blanks()')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Get_the_correct_indent_for_new_lines_despite_blank_lines)
***
# Title: Disable Auto-Indentation for Specific File Types
# Category: indentation
# Tags: file-type, configuration, editing
---
Create a custom indent script to disable auto-indentation for specific file types like HTML

```vim
let b:did_indent = 1
```

```lua
-- In ~/.config/nvim/after/indent/html.lua
vim.g.did_indent = 1
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/How_to_stop_auto_indenting)
***
# Title: Disable Auto-Indentation for Current File
# Category: indentation
# Tags: configuration, editing
---
Quickly turn off auto-indentation for the current buffer

```vim
:setlocal noautoindent nocindent nosmartindent indentexpr=
```

```lua
-- Disable auto-indentation for current buffer
vim.opt_local.autoindent = false
vim.opt_local.cindent = false
vim.opt_local.smartindent = false
vim.opt_local.indentexpr = ''
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/How_to_stop_auto_indenting)
***
# Title: Reindent Code Blocks Efficiently
# Category: indentation
# Tags: code-formatting, text-editing, navigation
---
Indent entire code blocks relative to matching braces quickly

```vim
" Indent block with matching brace
=%

" Increase/decrease block indent
>%
<%
```

```lua
-- These commands work identically in Neovim
-- Cursor should be on { or } when using
-- =% indents block with matching brace
-- >% increases block indent
-- <% decreases block indent
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Indent_a_code_block)
***
# Title: Select and Manipulate Code Blocks by Indentation
# Category: indentation
# Tags: text-objects, selection, editing
---
Create text objects that select code blocks based on indentation levels, allowing easy manipulation of entire indented sections

```vim
"Place in vimrc
onoremap <silent>ai :<C-U>cal <SID>IndTxtObj(0)<CR>
onoremap <silent>ii :<C-U>cal <SID>IndTxtObj(1)<CR>
vnoremap <silent>ai :<C-U>cal <SID>IndTxtObj(0)<CR><Esc>gv
vnoremap <silent>ii :<C-U>cal <SID>IndTxtObj(1)<CR><Esc>gv

function! s:IndTxtObj(inner)
  let curline = line(".")
  let lastline = line("$")
  let i = indent(line(".")) - &shiftwidth * (v:count1 - 1)
  let i = i < 0 ? 0 : i
  if getline(".") !~ "^\\s*$"
    "... rest of the function implementation ...
  endif
endfunction
```

```lua
local function ind_txt_obj(inner)
  local curline = vim.fn.line('.')
  local lastline = vim.fn.line('$')
  local indent_level = vim.fn.indent(curline) - vim.o.shiftwidth * (vim.v.count1 - 1)
  indent_level = indent_level < 0 and 0 or indent_level

  if vim.fn.getline('.') ~= '' then
    -- Implement selection logic similar to Vimscript function
    -- This would require translating the complex line selection logic
  end
end

-- Set up keymappings
vim.keymap.set({'o', 'v'}, 'ai', function() ind_txt_obj(false) end, { silent = true })
vim.keymap.set({'o', 'v'}, 'ii', function() ind_txt_obj(true) end, { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Indent_text_object)
***
# Title: Indent with Tabs, Align with Spaces
# Category: indentation
# Tags: whitespace, formatting, code-style
---
Configure Vim to use tabs for indentation and spaces for alignment, allowing flexible tab width while maintaining text alignment

```vim
set noexpandtab
set copyindent
set preserveindent
set softtabstop=0
set shiftwidth=4
set tabstop=4
```

```lua
vim.opt.expandtab = false
vim.opt.copyindent = true
vim.opt.preserveindent = true
vim.opt.softtabstop = 0
vim.opt.shiftwidth = 4
vim.opt.tabstop = 4
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Indent_with_tabs,_align_with_spaces)
***
# Title: Smart Tabs for Consistent Indentation
# Category: indentation
# Tags: tabs, spaces, code-formatting
---
Use tabs only for indentation levels while using spaces for text alignment, maintaining consistent code appearance across different tab widths

```vim
" Recommended to use Smart Tabs plugin
:set noet sts=0 sw=4 ts=4
:set cindent
:set cinoptions=(0,u0,U0
```

```lua
-- Recommended to use Smart Tabs plugin
vim.opt.expandtab = false
vim.opt.softtabstop = 0
vim.opt.shiftwidth = 4
vim.opt.tabstop = 4
vim.opt.cindent = true
vim.opt.cinoptions = '(0,u0,U0'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Indent_with_tabs,_align_with_spaces)
***
# Title: Preserve Indentation When Typing Hash
# Category: indentation
# Tags: indent, configuration, insert-mode
---
Prevent Vim from removing indentation when typing # at the start of a line, especially useful for comments in various programming languages

```vim
set cindent
set cinkeys-=0#
set indentkeys-=0#

" Alternative mapping for smartindent
:inoremap # X<BS>#
```

```lua
-- Preserve indentation for lines starting with #
vim.opt.cindent = true
vim.cmd('set cinkeys-=0#')
vim.cmd('set indentkeys-=0#')

-- Alternative mapping
vim.keymap.set('i', '#', function()
  local line = vim.api.nvim_get_current_line()
  local cursor = vim.api.nvim_win_get_cursor(0)
  vim.api.nvim_buf_set_text(0, cursor[1]-1, cursor[2], cursor[1]-1, cursor[2], {'#'})
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Keep_indent_for_new_lines)
***
# Title: Use Filetype-Based Indentation
# Category: indentation
# Tags: filetype, configuration, best-practices
---
Prefer filetype-based indentation over generic smartindent, which provides more accurate and language-specific indentation rules

```vim
filetype indent on
set autoindent
```

```lua
-- Enable filetype-specific indentation
vim.cmd('filetype indent on')
vim.opt.autoindent = true
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Prevent_autoindent_from_removing_indentation)
***
# Title: Quickly Reindent Entire File or Selected Text
# Category: indentation
# Tags: formatting, code-style, text-editing
---
Use 'cc' or 'S' to start insert mode on a new line with correct indentation, avoiding manual indent issues

```vim
" No direct vimscript mapping needed, just use built-in commands
```

```lua
-- Use built-in Vim commands 'cc' or 'S' to start insert mode
-- with correct indentation on a blank line
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Restoring_indent_after_typing_hash)
***
# Title: Smart Dedent to Previous Indent Level
# Category: indentation
# Tags: indent-management, python-integration, insert-mode
---
Provides a smart way to dedent to the previous meaningful indent level, instead of just moving by fixed shiftwidth increments

```vim
function! DedentToPrevious()
python << EOF
import vim
tabsize = int(vim.eval("&ts"))
l = vim.current.line
rest = l.lstrip()
indent = l[:-len(rest)]
if indent != "":
    cur_size = len(indent.replace("\t", " "*tabsize))
    idx = vim.current.window.cursor[0]-2
    while idx >= 0:
        ll = vim.current.buffer[idx]
        indent = ll[:-len(ll.lstrip())]
        if len(indent.replace("\t", " "*tabsize)) < cur_size:
            vim.current.line = indent+rest
            break
        idx -= 1
EOF
endfunction

" Replace Ctrl-D in insert mode with smart dedent
imap <C-d> <C-o>:call DedentToPrevious()<CR>
```

```lua
function _G.smart_dedent()
    local tabsize = vim.o.tabstop
    local current_line = vim.api.nvim_get_current_line()
    local rest = current_line:match("^%s*(.*)$")
    local current_indent = current_line:match("^(%s*)")
    
    if current_indent ~= "" then
        local cur_size = #(current_indent:gsub("\t", string.rep(" ", tabsize)))
        local current_line_nr = vim.api.nvim_win_get_cursor(0)[1]
        
        for idx = current_line_nr - 2, 0, -1 do
            local prev_line = vim.api.nvim_buf_get_lines(0, idx, idx+1, false)[1]
            local prev_indent = prev_line:match("^(%s*)")
            local prev_indent_size = #(prev_indent:gsub("\t", string.rep(" ", tabsize)))
            
            if prev_indent_size < cur_size then
                vim.api.nvim_set_current_line(prev_indent .. rest)
                break
            end
        end
    end
end

-- Map Ctrl-D to smart dedent in insert mode
vim.keymap.set('i', '<C-d>', '<Cmd>lua _G.smart_dedent()<CR>', { noremap = true, silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Return_to_previous_indent)
***
# Title: Quick Block Indentation Commands
# Category: indentation
# Tags: code-formatting, text-objects, block-editing
---
Efficient ways to reindent code blocks in Vim, using text object navigation

```vim
" Reindent inner block
=i{

" Reindent block including braces
=a{

" Increase/decrease block indent
>i{
<i{
```

```lua
-- Lua equivalents (these work the same in Neovim)
-- Can be used in visual mode or with text objects
-- Use = for auto-reindent
-- Use > or < for manual indent changes
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip597)
***
# Title: Block Indentation with Brace Matching
# Category: indentation
# Tags: code-formatting, matching-pairs, text-objects
---
Use % to match braces and indent entire code blocks with single commands

```vim
" Indent block including matching brace
=%

" Increase/decrease block indent
>%
<%
```

```lua
-- Lua equivalents work identically in Neovim
-- These commands leverage Vim's text object and matching capabilities
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip597)
***
