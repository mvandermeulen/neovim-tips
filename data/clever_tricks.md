# Title: Swap two characters
# Category: Clever Tricks
# Tags: character, swap, transpose
---
Use `xp` to swap current character with next character.

```vim
xp  " swap characters
```

**Source:** Community contributed
***
# Title: Auto-indent entire document
# Category: Clever Tricks
# Tags: indent, format, document, auto
---
Use `gg=G` to auto-indent entire document from top to bottom.

```vim
gg=G  " auto-indent entire file
```

**Source:** Community contributed
***
# Title: Auto-indent current block
# Category: Clever Tricks
# Tags: indent, block, braces, auto
---
Use `=%` when cursor is on opening brace to auto-indent entire block.

```vim
=%  " auto-indent current block/braces
```

**Source:** Community contributed
***
# Title: Open file under cursor
# Category: Clever Tricks
# Tags: file, open, cursor, path
---
Use `gf` to open file whose name is under cursor. Use `gF` to go to specific line number.

```vim
gf   " open file under cursor
gF   " open file and go to line number
```

**Source:** Community contributed
***
# Title: Line completion in insert mode
# Category: Clever Tricks
# Tags: completion, line, insert, auto
---
Use `Ctrl+X Ctrl+L` in insert mode to complete entire lines from current buffer.

```vim
" In insert mode:
Ctrl+X Ctrl+L  " complete entire line
```

**Source:** Community contributed
***
# Title: Quick substitute word
# Category: Clever Tricks
# Tags: substitute, word, replace
---
Use `ciw{newword}` to change inner word. Position cursor anywhere in word and type replacement.

```vim
ciwfoo  " change word to 'foo'
```

**Source:** Community contributed
***
# Title: Split line at cursor
# Category: Clever Tricks
# Tags: split, line, break
---
Use `i` followed by `Enter` then `Esc`, or more efficiently `r` followed by `Enter` to break line at cursor.

```vim
i<Enter><Esc>  " split line at cursor
```

**Source:** Community contributed
***
# Title: Quick number increment
# Category: Clever Tricks
# Tags: number, increment, math
---
Use `Ctrl+a` to increment number under cursor, `Ctrl+x` to decrement. Works with decimals and hex.

```vim
Ctrl+a  " increment number
Ctrl+x  " decrement number
```

**Source:** Community contributed
***
# Title: Visual line selection shortcut
# Category: Clever Tricks
# Tags: visual, line, selection
---
Use `V` to select entire line immediately, then `j`/`k` to extend selection.

```vim
Vjjj  " select current line + 3 below
```

**Source:** Community contributed
***
# Title: Change until character
# Category: Clever Tricks
# Tags: change, until, character
---
Use `ct{char}` to change text up to but not including character, or `cf{char}` to include the character.

```vim
ct;  " change until semicolon
cf;  " change including semicolon
```

**Source:** Community contributed
***
# Title: Center line after jump
# Category: Clever Tricks
# Tags: center, jump, navigation
---
Append `zz` after navigation commands to center the line. Works with searches, line jumps, etc.

```vim
42Gzz   " jump to line 42 and center
/foozz  " search for 'foo' and center
```

**Source:** Community contributed
***
# Title: G-commands - search variations
# Category: Clever Tricks
# Tags: search, variations, boundaries
---
Use `g*` and `g#` to search for word under cursor without word boundaries (matches partial words).

```vim
g*  " search forward for word without boundaries
g#  " search backward for word without boundaries
```

**Source:** Community contributed
***
# Title: G-commands - undo branches
# Category: Clever Tricks
# Tags: undo, branch, time, state
---
Use `g-` and `g+` to navigate through undo branches by time.

```vim
g-  " go to older text state
g+  " go to newer text state
```

**Source:** Community contributed
***
# Title: G-commands - screen line movement
# Category: Clever Tricks
# Tags: screen, line, wrap, movement
---
Use `gj` and `gk` to move by screen lines when text is wrapped, `g0` and `g$` for screen line start/end.

```vim
gj  " move down by screen line (with wrap)
gk  " move up by screen line (with wrap)
g0  " go to start of screen line
g$  " go to end of screen line
```

**Source:** Community contributed
***
# Title: G-commands - middle of line
# Category: Clever Tricks
# Tags: middle, line, screen, text
---
Use `gm` to go to middle of screen line and `gM` to go to middle of text line.

```vim
gm  " go to middle of screen line
gM  " go to middle of text line
```

**Source:** Community contributed
***
# Title: G-commands - case conversion
# Category: Clever Tricks
# Tags: case, convert, upper, lower
---
Use `gU{motion}` for uppercase, `gu{motion}` for lowercase, and `g~{motion}` to toggle case.

```vim
gUw   " uppercase word
guu   " lowercase current line
g~iw  " toggle case of word under cursor
```

**Source:** Community contributed
***
# Title: G-commands - join without space
# Category: Clever Tricks
# Tags: join, line, space
---
Use `gJ` to join lines without inserting a space between them.

```vim
gJ  " join lines without adding space
```

**Source:** Community contributed
***
# Title: G-commands - search and select
# Category: Clever Tricks
# Tags: search, select, visual, pattern
---
Use `gn` to find and visually select next search match, `gN` for previous match.

```vim
/pattern<Enter>  " search for pattern first
gn               " select next match
gN               " select previous match
```

**Source:** Community contributed
***
# Title: G-commands - put and leave cursor
# Category: Clever Tricks
# Tags: put, paste, cursor, position
---
Use `gp` and `gP` to put text and leave cursor after the pasted text.

```vim
gp  " put after and leave cursor at end
gP  " put before and leave cursor at end
```

**Source:** Community contributed
***
# Title: G-commands - format keeping cursor
# Category: Clever Tricks
# Tags: format, cursor, position, text
---
Use `gw{motion}` to format text while keeping cursor position unchanged.

```vim
gwap  " format paragraph, keep cursor position
```

**Source:** Community contributed
***
# Title: G-commands - sleep
# Category: Clever Tricks
# Tags: sleep, delay, pause
---
Use `gs` to make Neovim sleep for specified seconds (useful in scripts).

```vim
3gs  " sleep for 3 seconds
gs   " sleep for 1 second (default)
```

**Source:** Community contributed
***
# Title: G-commands - execute application
# Category: Clever Tricks
# Tags: execute, application, file, system
---
Use `gx` to execute the default application for the file/URL under cursor.

```vim
gx  " open file/URL under cursor with default app
```

**Source:** Community contributed
***
# Title: G-commands - virtual replace
# Category: Clever Tricks
# Tags: virtual, replace, mode, character
---
Use `gR` to enter virtual replace mode, `gr{char}` to replace character without affecting layout.

```vim
gR    " enter virtual replace mode
grx   " replace character with 'x' virtually
```

**Source:** Community contributed
***
# Title: G-commands - select modes
# Category: Clever Tricks
# Tags: select, mode, visual, block
---
Use `gh` for select mode, `gH` for select line mode, `g Ctrl+h` for select block mode.

```vim
gh       " start select mode
gH       " start select line mode
g Ctrl+h " start select block mode
```

**Source:** Community contributed
***
# Title: G-commands - repeat substitute
# Category: Clever Tricks
# Tags: substitute, repeat, global, command
---
Use `g&` to repeat the last `:substitute` command on all lines.

```vim
:s/old/new/   " substitute on current line
g&            " repeat substitute on all lines
```

**Source:** Community contributed
***
# Title: G-commands - display command output
# Category: Clever Tricks
# Tags: display, command, output, history
---
Use `g<` to display the output of the previous command.

```vim
g<  " display previous command output
```

**Source:** Community contributed
***
# Title: G-commands - mark navigation without jumplist
# Category: Clever Tricks
# Tags: mark, navigation, jumplist
---
Use `g'` and `` g` `` to jump to marks without changing the jumplist.

```vim
g'a  " jump to mark 'a' without affecting jumplist
g`a  " jump to exact position of mark 'a' without jumplist
```

**Source:** Community contributed
***
# Title: Repeat last Ex command with @:
# Category: Clever Tricks
# Tags: repeat, ex, command, macro, colon
---
Use `@:` to repeat the last Ex command, similar to how `@@` repeats macros.

```vim
:substitute/old/new/g
@:  " repeat the last substitute command
```

**Source:** Community contributed
***
# Title: Enhanced repeat with cursor positioning
# Category: Clever Tricks
# Tags: repeat, cursor, position, change, dot
---
Map `.` followed by `` ` `` to repeat last command and return cursor to start of change.

```vim
" Vimscript:
nnoremap <leader>. .`[

" Now after making a change:
<leader>.  " repeat change and go to start position
```
```lua
-- Lua:
vim.keymap.set('n', '<leader>.', '.`[', { desc = 'Repeat change and return to start' })
```

**Source:** Community contributed
***
# Title: List lines matching last search
# Category: Clever Tricks
# Tags: search, list, global, pattern, last
---
Use `:g//` to list all lines containing the last search pattern without specifying the pattern again.

```vim
/function   " search for 'function'
:g//        " list all lines containing 'function'
:g//p       " same as above (print is default)
```

**Source:** Community contributed
***
# Title: Save each line to separate files
# Category: Clever Tricks
# Tags: file, save, line, separate, export
---
Use `:g/^/exe` to save each line to a separate file with incremental names.

```vim
:let i = 1 | g/^/exe 'w! line' . i . '.txt' | let i = i + 1
" Saves each line to line1.txt, line2.txt, etc.
```

**Source:** Community contributed
***
# Title: Alternative substitute delimiters
# Category: Clever Tricks
# Tags: substitute, delimiter, slash, alternative
---
Use any character as delimiter in substitute commands to avoid escaping slashes in paths.

```vim
:s#/path/to/old#/path/to/new#g  " using # as delimiter
:s|/usr/bin|/usr/local/bin|g    " using | as delimiter
:s@old@new@g                    " using @ as delimiter
```

**Source:** Community contributed
***
# Title: Calculation with expression register
# Category: Clever Tricks
# Tags: calculation, expression, register, math, evaluate
---
Use `=` register to evaluate mathematical expressions and insert results.

```vim
" In insert mode:
Ctrl+r =2+3*4<Enter>    " inserts 14
Ctrl+r =sqrt(16)<Enter> " inserts 4.0
Ctrl+r =strftime("%Y")<Enter>  " inserts current year
```

**Source:** Community contributed
***
# Title: Scroll windows together
# Category: Clever Tricks
# Tags: scroll, window, together, bind, sync
---
Use `:set scrollbind` in multiple windows to scroll them together synchronously.

```vim
" Vimscript:
" In first window:
:set scrollbind

" In second window:
:set scrollbind

" Now both windows scroll together
" To disable:
:set noscrollbind
```
```lua
-- Lua:
-- In first window:
vim.wo.scrollbind = true

-- In second window:
vim.wo.scrollbind = true

-- To disable:
vim.wo.scrollbind = false
```

**Source:** Community contributed
***
# Title: Change directory to current file
# Category: Clever Tricks
# Tags: directory, current, file, cd, path
---
Use `:cd %:h` to change directory to the directory of the current file.

```vim
" Vimscript:
:cd %:h     " change to current file's directory
:pwd        " verify current directory
:lcd %:h    " change local directory for current window only
```
```lua
-- Lua:
vim.cmd('cd ' .. vim.fn.expand('%:h'))  -- change to current file's directory
vim.cmd('pwd')  -- verify current directory
vim.cmd('lcd ' .. vim.fn.expand('%:h'))  -- change local directory for current window only

-- Or using Lua API:
vim.fn.chdir(vim.fn.expand('%:h'))
```

**Source:** Community contributed
***
# Title: File encoding in status line
# Category: Clever Tricks
# Tags: encoding, status, line, file, format
---
Add file encoding to status line to see current file's character encoding.

```vim
" Vimscript:
:set statusline=%f\ [%{&fileencoding?&fileencoding:&encoding}]\ %y
" Shows filename, encoding, and filetype
```
```lua
-- Lua:
vim.opt.statusline = '%f [%{&fileencoding?&fileencoding:&encoding}] %y'
-- Shows filename, encoding, and filetype
```

**Source:** Community contributed
***
# Title: Create word frequency table
# Category: Clever Tricks
# Tags: word, frequency, table, count, analysis
---
Create a word frequency analysis using Vim commands and external tools.

```vim
" Create word frequency table:
:%s/\W\+/\r/g | sort | uniq -c | sort -nr
" Or using Vim's internal commands:
:g/./normal 0"ay$
```

**Source:** Community contributed
***
# Title: Search for lines NOT matching pattern
# Category: Clever Tricks
# Tags: search, not, matching, invert, negative
---
Use `:v/pattern/` or `:g!/pattern/` to work with lines that do NOT match a pattern.

```vim
:v/TODO/d       " delete lines NOT containing TODO
:g!/function/p  " print lines NOT containing 'function'
:v/^$/d         " delete non-empty lines (keep only empty lines)
```

**Source:** Community contributed
***
# Title: Swap assignment statement sides
# Category: Clever Tricks
# Tags: swap, assignment, left, right, substitute
---
Use substitute with groups to swap left and right sides of assignment statements.

```vim
" Swap variable assignment (a = b becomes b = a):
:%s/\(\w\+\)\s*=\s*\(\w\+\)/\2 = \1/g

" Swap in selected region:
:'<,'>s/\(\w\+\)\s*=\s*\(\w\+\)/\2 = \1/g
```

**Source:** Community contributed
***
# Title: Z-commands - spelling corrections
# Category: Clever Tricks
# Tags: spelling, correction, dictionary
---
Use `z=` for spelling suggestions, `zg` to add word to dictionary, `zw` to mark as misspelled, `zG`/`zW` for temporary marks.

```vim
z=  " show spelling suggestions for word under cursor
zg  " add word to personal dictionary (good)
zw  " mark word as misspelled (wrong)
zG  " temporarily mark word as correct
zW  " temporarily mark word as incorrect
```

**Source:** Community contributed
***
# Title: Toggle text case inside a HTML tag
# Category: Clever Tricks
# Tags: edit, case, tag
---
Use `g~it` to change the case of the text inside a html tag. Cursor should be between opening and closing HTML tag.

```vim
" turns <b>important</b> into <b>IMPORTANT</b>
g~it
```

**Source:** Community contributed
***
# Title: Create HTML Links with Automatic Title Fetch
# Category: clever_tricks
# Tags: html, web-development, automation
---
Automatically generate HTML anchor tags by fetching page titles from URLs, saving time when creating links

```vim
" Prompt user to enter URL and optional TARGET.
nnoremap <Leader>al :call AddLink()<CR>
function! AddLink()
  let url = input('URL to add? ')
  if empty(url)
    return
  endif
  let target = input('Target for this link? ')
  if !empty(target)
    let target = ' target="' . target . '"'
  endif
  let html = system('wget -q -O - ' . shellescape(url))
  let regex = '\c.*head.*<title[^>]*>\_s*\zs.\_*\ze\_s*<\/title>'
  let title = substitute(matchstr(html, regex), "\n", ' ', 'g')
  if empty(title)
    let title = 'Unknown'
  endif
  put ='<a href="' . url . '"' . target . '>' . title . '</a>'
endfunction
```
```lua
function _G.add_html_link()
  local url = vim.fn.input('URL to add? ')
  if url == '' then return end

  local target = vim.fn.input('Target for this link? ')
  local target_attr = target ~= '' and ' target="' .. target .. '"' or ''

  local html = vim.fn.system('wget -q -O - ' .. vim.fn.shellescape(url))
  local title = html:match('<title[^>]*>%s*(.-)%s*</title>') or 'Unknown'
  title = title:gsub('
', ' ')

  local link = string.format('<a href="%s"%s>%s</a>', url, target_attr, title)
  vim.api.nvim_put({link}, 'l', true, false)
end

-- Map the function
vim.keymap.set('n', '<leader>al', _G.add_html_link, { desc = 'Add HTML link with title' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Add_a_full_link-tag_with_automatic_title)
***
# Title: Insert Filename as Classname in Insert Mode
# Category: clever_tricks
# Tags: insert-mode, abbreviation, filename
---
Quickly insert the current filename (without path/extension) while in insert mode using an abbreviation

```vim
" Insert classname (filename minus path and extension).
iab <buffer> <unique> ,f <C-r>=expand('%:t:r')<CR>
```
```lua
-- Create buffer-local abbreviation to insert filename
vim.cmd('iab <buffer> <unique> ,f ' .. vim.fn.expand('%:t:r'))
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Add_classname_based_on_filename_while_in_input_mode)
***
# Title: Quick LaTeX Environment Creation in Vim
# Category: clever_tricks
# Tags: latex, text-insertion, custom-commands
---
Create custom commands to easily insert LaTeX environments with tab completion and optional insert mode functionality

```vim
command -complete=custom,ListE -nargs=1 -range E normal <line1>ggO\begin{<args>}<Esc><line2>ggjo\end{<args>}<Esc><line1>ggv<line2>ggjj=
command -complete=custom,ListE -nargs=1 Ei execute "normal \<Esc>i\begin{<args>}\<CR>\end{<args>}<Esc>O<Space>" | startinsert

function ListE(A,L,P)
  return "align*\nenumerate\nitemize\nfigure\ntabular\nbmatrix\npmatrix\ncases\n\ndocument\narray\nproof"
endfunction

" Optional insert mode mapping
imap <buffer> <C-Space> <Esc>:Ei<Space>
```
```lua
vim.api.nvim_create_user_command('E', function(opts)
  local env = opts.args
  local line1 = vim.fn.line('.')
  vim.cmd('normal! O\\begin{' .. env .. '}\<Esc>')
  vim.cmd('normal! j o\\end{' .. env .. '}\<Esc>')
  vim.cmd('normal! ' .. line1 .. 'ggv' .. (line1+1) .. 'ggjj=')
end, {
  nargs = 1,
  complete = function()
    return {'align*', 'enumerate', 'itemize', 'figure', 'tabular', 'bmatrix', 'pmatrix', 'cases', 'document', 'array', 'proof'}
  end
})

-- Insert mode mapping
vim.keymap.set('i', '<C-Space>', '<Esc>:Ei<Space>', { buffer = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Auctex-style_environment_creation_in_LaTeX)
***
# Title: Calculate Math Expressions In-Editor
# Category: clever_tricks
# Tags: calculation, external-tool, visual-mode
---
Use BC (basic calculator) to evaluate mathematical expressions directly within Vim, supporting complex calculations and trigonometric functions

```vim
function! CalcBC()
  let has_equal = 0
  let @e = substitute(@e, "\n", "", "g")
  let @e = substitute(@e, '\s*$', "", "g")
  if @e =~ "=$"
    let @e = substitute(@e, '=$', "", "")
    let has_equal = 1
  endif
  let @e = substitute(@e, '\csin\s*(', "s (", "")
  let @e = substitute(@e, '\ccos\s*(', "c (", "")
  let answer = substitute(system("echo " . @e . " | bc -l"), "\n", "", "")
  if has_equal == 1
    normal `>
    exec "normal a" . answer
  else
    echo "answer = " . answer
  endif
endfunction

vnoremap ;bc "ey:call CalcBC()<CR>
```
```lua
function _G.calc_bc()
  local text = vim.fn.getreg('e')
  text = text:gsub('\n', ''):gsub('%s*$', '')
  
  local has_equal = text:match('=$')
  if has_equal then
    text = text:gsub('=$', '')
  end
  
  text = text:gsub('sin%s*%(', 's (')
  text = text:gsub('cos%s*%(', 'c (')
  
  local result = vim.fn.system(string.format('echo "%s" | bc -l', text)):gsub('\n', '')
  
  if has_equal then
    vim.cmd('normal! `>')
    vim.fn.setreg('e', result)
    vim.cmd('normal! p')
  else
    print('answer = ' .. result)
  end
end

vim.keymap.set('v', ';bc', '"ey:lua _G.calc_bc()<CR>', { noremap = true, silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Calculate_equations_from_within_vim)
***
# Title: Inline Visual Mode Calculator
# Category: clever_tricks
# Tags: calculation, visual-mode, command-line
---
Perform mathematical calculations directly in Vim using visual mode and bc calculator, with options to replace or append results

```vim
function MyCalc(str)
  if exists("g:MyCalcRounding")
    return system("echo 'x=" . a:str . ";d=.5/10^" . g:MyCalcPresition
          \. ";if (x<0) d=-d; x+=d; scale=" . g:MyCalcPresition . ";print x/1' | bc -l")
  else
    return system("echo 'scale=" . g:MyCalcPresition . " ; print " . a:str . "' | bc -l")
  endif
endfunction

" Control precision and rounding
let g:MyCalcPresition = 2
let g:MyCalcRounding = 1

" Replace current line or visual block with calculation result
map <silent> <Leader>c :s/.*/\=MyCalc(submatch(0))/<CR>:noh<CR>
vmap <silent> <Leader>c :B s/.*/\=MyCalc(submatch(0))/<CR>:noh<CR>
```
```lua
local function my_calc(str)
  local precision = vim.g.MyCalcPresition or 2
  local cmd = string.format("echo 'scale=%d; print %s' | bc -l", precision, str)
  local result = vim.fn.system(cmd):gsub("\n", "")
  return result
end

-- Calculator mappings
vim.keymap.set({'n', 'v'}, '<leader>c', function()
  local mode = vim.fn.mode()
  if mode == 'v' or mode == 'V' or mode == '\22' then
    local start_pos = vim.fn.getpos("'<")
    local end_pos = vim.fn.getpos("'>")
    local lines = vim.fn.getline(start_pos[2], end_pos[2])
    
    for i, line in ipairs(lines) do
      local calc_result = my_calc(line)
      vim.fn.setline(start_pos[2] + i - 1, calc_result)
    end
  else
    local line = vim.fn.getline('.')
    local calc_result = my_calc(line)
    vim.fn.setline('.', calc_result)
  end
end, { desc = 'Calculator: Replace line/selection with result' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Calculator_Editing)
***
# Title: Toggle File Path Slashes Quickly
# Category: clever_tricks
# Tags: file-paths, search-replace, mapping
---
Easily convert between backslashes and forward slashes in file paths, especially useful for cross-platform file handling

```vim
function! ToggleSlash(independent) range
  let from = ''
  for lnum in range(a:firstline, a:lastline)
    let line = getline(lnum)
    let first = matchstr(line, '[/\\]')
    if !empty(first)
      if a:independent || empty(from)
        let from = first
      endif
      let opposite = (from == '/' ? '\\' : '/')
      call setline(lnum, substitute(line, from, opposite, 'g'))
    endif
  endfor
endfunction
command! -bang -range ToggleSlash <line1>,<line2>call ToggleSlash(<bang>1)
noremap <silent> <F8> :ToggleSlash<CR>
```
```lua
function _G.toggle_slashes(independent, first_line, last_line)
  for lnum = first_line, last_line do
    local line = vim.fn.getline(lnum)
    local first = line:match('[/\\]')
    if first then
      local from = independent and first or (from or first)
      local opposite = from == '/' and '\\' or '/'
      vim.fn.setline(lnum, line:gsub(vim.pesc(from), opposite))
    end
  end
end

vim.api.nvim_create_user_command('ToggleSlash', function(opts)
  local first_line = opts.line1
  local last_line = opts.line2
  local independent = opts.bang
  _G.toggle_slashes(independent, first_line, last_line)
end, { range = true, bang = true })

vim.keymap.set('n', '<F8>', ':ToggleSlash<CR>', { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Change_between_backslash_and_forward_slash)
***
# Title: Convert Between Hex and Decimal Quickly
# Category: clever_tricks
# Tags: conversion, number-manipulation, command-line
---
Provides multiple methods to convert between hex and decimal numbers in Vim/Neovim, including command-line and mapping-based approaches

```vim
" Convert decimal to hex
command! -nargs=? -range Dec2hex call s:Dec2hex(<line1>, <line2>, '<args>')
function! s:Dec2hex(line1, line2, arg) range
  if empty(a:arg)
    let cmd = 's/\<\d\+\>/\=printf("0x%x",submatch(0)+0)/g'
    execute a:line1 . ',' . a:line2 . cmd
  else
    echo printf('%x', a:arg + 0)
  endif
endfunction
```
```lua
-- Convert decimal to hex
vim.api.nvim_create_user_command('Dec2hex', function(opts)
  local arg = opts.args
  local range = {opts.line1, opts.line2}
  
  if arg == '' then
    local cmd = 's/\d\+/\=printf("0x%x", submatch(0) + 0)/g'
    vim.cmd(range[1] .. ',' .. range[2] .. cmd)
  else
    print(string.format('%x', tonumber(arg)))
  end
end, { nargs = '?', range = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Convert_between_hex_and_decimal)
***
# Title: Convert Between Hex and Decimal Numbers
# Category: clever_tricks
# Tags: conversion, numbers, utilities
---
Easily convert between decimal and hexadecimal numbers in Vim/Neovim using built-in functions and custom commands

```vim
" Convert decimal to hex
function! Dec2hex(arg)
  return printf('%x', a:arg + 0)
endfunction

" Convert hex to decimal
function! Hex2dec(arg)
  return (a:arg =~? '^0x') ? a:arg + 0 : ('0x'.a:arg) + 0
endfunction
```
```lua
-- Convert decimal to hex
function _G.dec_to_hex(arg)
  return string.format('%x', tonumber(arg))
end

-- Convert hex to decimal
function _G.hex_to_dec(arg)
  return tonumber(arg:match('^0x') and arg or '0x' .. arg)
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Convert_decimal_to_hex)
***
# Title: Quick Number Base Conversion
# Category: clever_tricks
# Tags: number-conversion, utility, command-line
---
Use built-in Vim functions to quickly convert numbers between bases in command mode or insert mode

```vim
" Convert hex to decimal in command mode
:echo str2nr('0x0a2f', 16)

" Convert decimal to hex string
:echo printf('%x', 1234)

" Insert converted number in insert mode
" <C-R>=0x09ab<Enter> inserts 2475
" <C-R>=printf('0x%04x',2475)<Enter> inserts 0x09ab
```
```lua
-- Convert hex to decimal
print(tonumber('0x0a2f', 16))

-- Convert decimal to hex string
print(string.format('%x', 1234))

-- For insert mode conversion, use vim.fn.input() or lua's string formatting
-- Example in Neovim lua command mode
vim.fn.feedkeys('i' .. string.format('0x%04x', 2475), 'n')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Convert_numbers_hex/decimal_via_menu)
***
# Title: Advanced Number Increment/Decrement
# Category: clever_tricks
# Tags: number-manipulation, search, editing
---
Enhanced Ctrl-A/Ctrl-X to increment/decrement numbers across lines, with backward search option

```vim
function! AddSubtract(char, back)
  let pattern = &nrformats =~ 'alpha' ? '[[:alpha:][:digit:]]' : '[[:digit:]]'
  call search(pattern, 'cw' . a:back)
  execute 'normal! ' . v:count1 . a:char
  silent! call repeat#set(":\<C-u>call AddSubtract('" .a:char. "', '" .a:back. "')\<CR>")
endfunction
nnoremap <silent>         <C-a> :<C-u>call AddSubtract("\<C-a>", '')<CR>
nnoremap <silent> <Leader><C-a> :<C-u>call AddSubtract("\<C-a>", 'b')<CR>
nnoremap <silent>         <C-x> :<C-u>call AddSubtract("\<C-x>", '')<CR>
nnoremap <silent> <Leader><C-x> :<C-u>call AddSubtract("\<C-x>", 'b')<CR>
```
```lua
local function add_subtract(char, back)
  local pattern = vim.o.nrformats:match('alpha') and '[%w]' or '[%d]'
  vim.fn.search(pattern, 'cw' .. back)
  vim.cmd('normal! ' .. (vim.v.count1 or 1) .. char)
end

vim.keymap.set('n', '<C-a>', function() add_subtract('\<C-a>', '') end, { silent = true })
vim.keymap.set('n', '<leader><C-a>', function() add_subtract('\<C-a>', 'b') end, { silent = true })
vim.keymap.set('n', '<C-x>', function() add_subtract('\<C-x>', '') end, { silent = true })
vim.keymap.set('n', '<leader><C-x>', function() add_subtract('\<C-x>', 'b') end, { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Cool_trick_to_change_numbers)
***
# Title: Quickly Create Perl Subroutines in Vim
# Category: clever_tricks
# Tags: mapping, text-insertion, productivity
---
Adds a mapping to create a new Perl subroutine with the word under the cursor, placing it at the end of the file or before special tokens

```vim
nnoremap <Leader>ns :call Newsub()<CR>
function! Newsub()
  let word = "sub " . expand("<cword>") . "{}"
  let ln = search("__.*__", 'nW')
  if ln == 0
    call append('$', word)
  else
    call append(ln-1, word)
  endif
endfunction
```
```lua
vim.keymap.set('n', '<Leader>ns', function()
  local word = expand('<cword>')
  local line_num = vim.fn.search('__.*__', 'nW')
  
  if line_num == 0 then
    -- Append to end of file
    vim.fn.append('$', 'sub ' .. word .. '{}')
  else
    -- Insert before special token
    vim.fn.append(line_num - 1, 'sub ' .. word .. '{}')
  end
end, { desc = 'Create new Perl subroutine' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Create_new_subroutines)
***
# Title: Repeat Last Change Efficiently
# Category: clever_tricks
# Tags: productivity, editing, normal-mode
---
Use the dot (.) command to repeat the last change in normal mode, which can dramatically speed up repetitive editing tasks

```vim
# Example use cases:
# After deleting a word with 'dw', press '.' to delete another word
# After joining lines with 'J', press '.' to join more lines
```
```lua
-- Dot command works the same in Neovim
-- Simply press '.' to repeat the last normal mode change
-- Can be used with a count, e.g. '5.' to repeat 5 times
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Dot_makes_life_easier)
***
# Title: Evaluate Expressions Across Vim Modes
# Category: clever_tricks
# Tags: expression-evaluation, key-mapping, calculator
---
Use Ctrl-R= to evaluate expressions in insert, command, and normal modes, enabling quick calculations and dynamic value insertion

```vim
" Map Ctrl-R= to work in normal mode for expression evaluation
map <CTRL-R>= :echo
```
```lua
-- Lua equivalent for mapping expression evaluation
vim.keymap.set({'n', 'i', 'c'}, '<C-r>=', function()
  local expr = vim.fn.input('Expression: ')
  return vim.fn.eval(expr)
end, { expr = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Evaluate_an_expression_in_any_mode)
***
# Title: Evaluate Python Expressions in Vim
# Category: clever_tricks
# Tags: python, scripting, evaluation
---
Provides a flexible way to evaluate Python expressions directly within Vim, allowing complex calculations and transformations of current line content

```vim
python << EOL
import vim

def EvaluateCurrentLine(*args):
  cur_str = vim.current.line
  action, symb = None, None
  for i in args:
    if i in ["r","p"]: action = i
    else: symb = i
  try: start = cur_str.rindex(symb)+len(symb)
  except: start = 0
  result = eval(cur_str[start:],globals())
  if action == "r":
    vim.current.line = cur_str[:start]+str(result)
  else:
    print result
EOL
command -narg=* PyEv python EvaluateCurrentLine(<f-args>)
```
```lua
function _G.evaluate_current_line(...)
  local cur_str = vim.api.nvim_get_current_line()
  local action, symb = nil, nil
  for _, arg in ipairs({...}) do
    if arg == 'r' or arg == 'p' then
      action = arg
    else
      symb = arg
    end
  end
  
  local start = 0
  if symb then
    local idx = cur_str:reverse():find(symb:reverse())
    start = idx and (#cur_str - idx + 1) or 0
  end
  
  local ok, result = pcall(load('return ' .. cur_str:sub(start + 1)))
  if ok then
    if action == 'r' then
      vim.api.nvim_set_current_line(cur_str:sub(1, start) .. tostring(result))
    else
      print(result)
    end
  end
end

vim.api.nvim_create_user_command('PyEv', function(opts)
  _G.evaluate_current_line(unpack(opts.fargs))
end, { nargs = '*' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Evaluate_current_line_using_Python)
***
# Title: Execute Python Code Inside Vim Buffer
# Category: clever_tricks
# Tags: python, scripting, buffer-manipulation
---
Execute Python code directly within a Vim buffer, replacing the selected lines with the output or performing in-place transformations

```vim
python << EOL
import vim, StringIO,sys
def PyExecReplace(line1,line2):
  r = vim.current.buffer.range(int(line1),int(line2))
  redirected = StringIO.StringIO()
  sys.stdout = redirected
  exec('\n'.join(r) + '\n')
  sys.stdout = sys.__stdout__
  output = redirected.getvalue().split('\n')
  r[:] = output[:-1]
  redirected.close()
EOL
command -range Pyer python PyExecReplace(<f-line1>,<f-line2>)
```
```lua
local function py_exec_replace(line1, line2)
  local buffer = vim.api.nvim_get_current_buf()
  local lines = vim.api.nvim_buf_get_lines(buffer, line1-1, line2, false)
  local code = table.concat(lines, '\n')
  
  local output = vim.fn.system('python3 -c "' .. code .. '"')
  
  vim.api.nvim_buf_set_lines(buffer, line1-1, line2, false, vim.split(output, '\n'))
end

vim.api.nvim_create_user_command('Pyer', function(opts)
  py_exec_replace(opts.line1, opts.line2)
end, { range = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Execute_Python_from_within_current_file)
***
# Title: Preserve Search Register When Running Commands
# Category: clever_tricks
# Tags: search, command-preservation, register-management
---
Create a function that executes commands without modifying the search register, which is useful for preserving search history during operations

```vim
function! SafeSearchCommand(line1, line2, theCommand)
  let search = @/
  execute a:line1 . "," . a:line2 . a:theCommand
  let @/ = search
endfunction

com! -range -nargs=+ SS call SafeSearchCommand(<line1>, <line2>, <q-args>)
com! -range -nargs=* S call SafeSearchCommand(<line1>, <line2>, 's' . <q-args>)
```
```lua
function _G.safe_search_command(line1, line2, command)
  local search = vim.fn.getreg('/')
  vim.cmd(string.format('%d,%d%s', line1, line2, command))
  vim.fn.setreg('/', search)
end

vim.api.nvim_create_user_command('SS', function(opts)
  _G.safe_search_command(opts.line1, opts.line2, opts.args)
end, { range = true, nargs = '+' })

vim.api.nvim_create_user_command('S', function(opts)
  _G.safe_search_command(opts.line1, opts.line2, 's' .. opts.args)
end, { range = true, nargs = '*' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Execute_commands_without_changing_the_search_register)
***
# Title: Extract Phone Number Under Cursor
# Category: clever_tricks
# Tags: text-extraction, function, cursor-position
---
Create a function to extract and clean phone numbers from text, with optional error handling

```vim
function! CPhone(check)
  let s = '[-+./()0-9 ]*'
  let nr = matchstr(getline('.'), '\s*\zs'.s.'\%'.col('.').'c'.s)
  let nr = substitute(nr, '\s\+$', '', '')
  if a:check && empty(nr)
    throw 'No phone number under cursor.'
  endif
  return nr
endfunction
```
```lua
function CPhone(check)
  local s = '[-+./()0-9 ]*'
  local line = vim.fn.getline('.')
  local col = vim.fn.col('.')
  local nr = vim.fn.matchstr(line, '\s*\zs'..s..'\%'..col..'c'..s)
  nr = nr:gsub('%s+$', '')
  
  if check and nr == '' then
    error('No phone number under cursor')
  end
  
  return nr
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Finding_phone_numbers)
***
# Title: Group Lines with Matching Column Pattern
# Category: clever_tricks
# Tags: line-manipulation, search, text-processing
---
Insert blank lines between groups of lines that match a specific pattern at a given column position. Useful for organizing and visually separating similar data groups.

```vim
function! GroupMatchingLines()
  let pattern = strpart(getline('.'), col('.') - 1, strlen(@@))
  if !empty(pattern)
    let pattern = escape(pattern, '\.*$^~[')
    let col_cursor = col('.')
    let pattern = '\%'.col_cursor.'c'.'\('.pattern.'\)\@!'
    let [rowm,colm] = searchpos(pattern,'W')
    if rowm > 0
      '.-1put ='''
      exe 'normal! j'.col_cursor.'|'
      return
    endif
  endif
  echo 'String not found'
endfunction

nnoremap <F9> :call GroupMatchingLines()<CR>
```
```lua
function _G.group_matching_lines()
  local pattern = vim.fn.strpart(vim.fn.getline('.'), vim.fn.col('.') - 1, #vim.fn.getreg('"'))
  if pattern ~= '' then
    pattern = vim.fn.escape(pattern, '\.*$^~[')
    local col_cursor = vim.fn.col('.')
    local search_pattern = string.format('\%%dc\(\%s\)\@!', pattern)
    local result = vim.fn.searchpos(search_pattern, 'W')
    
    if result[1] > 0 then
      vim.cmd('.-1put =""')
      vim.cmd(string.format('normal! j%d|', col_cursor))
      return
    end
  end
  print('String not found')
end

vim.keymap.set('n', '<F9>', _G.group_matching_lines, { desc = 'Group matching lines' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Group_matching_lines)
***
# Title: Quick Hex and Decimal Number Conversion
# Category: clever_tricks
# Tags: number-conversion, command-line, conversion
---
Easily convert between hex and decimal numbers using built-in Vim functions and commands

```vim
" Convert decimal to hex
:echo printf('%x', 74565)

" Convert hex to decimal
:echo 0x12345

" In insert mode, convert numbers
" Ctrl-R = 0x09ab Enter (inserts 2475)
" Ctrl-R = printf('0x%04x',2475) Enter (inserts 0x09ab)
```
```lua
-- Convert decimal to hex
print(string.format('%x', 74565))

-- Convert hex to decimal
print(tonumber('0x12345'))

-- In Neovim, use vim.fn to mimic Vim's conversion
-- Example: printf equivalent
print(vim.fn.printf('%x', 74565))
print(vim.fn.printf('0x%04x', 2475))
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Hex_or_unhex_strings)
***
# Title: Quick Number Type Detection and Conversion
# Category: clever_tricks
# Tags: number-conversion, cursor-word, utility
---
Function to detect and convert numbers under cursor between decimal and hexadecimal, handling various input formats

```vim
function! DecAndHex(number)
  if a:number =~? '^\d\+$'
    let dec = a:number
    echo dec . printf('  ->  0x%X, -(0x%X)', dec, -dec)
  elseif a:number =~? '^0x\x\+$'
    let hex = substitute(a:number, '^0x', '', '')
    echo '0x' . hex . printf('  ->  %d', eval('0x'.hex))
  endif
endfunction
```
```lua
function _G.dec_and_hex(number)
  local dec = tonumber(number)
  local hex = tonumber(number, 16)
  
  if dec then
    print(string.format('%d  ->  0x%X, -(0x%X)', dec, dec, -dec))
  elseif hex then
    print(string.format('0x%X  ->  %d', hex, hex))
  else
    print('Not a valid number')
  end
end

-- Bind to a key
vim.keymap.set('n', 'gn', function()
  local word = vim.fn.expand('<cword>')
  _G.dec_and_hex(word)
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Hex_or_unhex_strings)
***
# Title: Highlight Current Word for Easy Cursor Tracking
# Category: clever_tricks
# Tags: cursor-tracking, highlight, navigation
---
Toggle highlighting of the word under the cursor to help track cursor position in large files

```vim
nnoremap <C-K> :call HighlightNearCursor()<CR>
function HighlightNearCursor()
  if !exists("s:highlightcursor")
    match Todo /\k*\%#\k*/
    let s:highlightcursor=1
  else
    match None
    unlet s:highlightcursor
  endif
endfunction
```
```lua
vim.keymap.set('n', '<C-K>', function()
  if not vim.g.highlightcursor then
    vim.cmd('match Todo /\\k*\\%#\\k*/')
    vim.g.highlightcursor = true
  else
    vim.cmd('match None')
    vim.g.highlightcursor = nil
  end
end, { desc = 'Toggle cursor word highlight' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Highlight_current_word_to_find_cursor)
***
# Title: Quickly Obscure Text with Rot13 Encoding
# Category: clever_tricks
# Tags: text-manipulation, key-mapping, security
---
Instantly encode text using rot13 to quickly obscure screen contents when someone approaches

```vim
map <F3> ggg?G
```
```lua
vim.keymap.set('n', '<F3>', 'ggg?G', { desc = 'Obscure text with rot13 encoding' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/How_to_obscure_text_instantaneously)
***
# Title: Rot13 Encoding for Visible Screen Only
# Category: clever_tricks
# Tags: text-manipulation, cursor-position, key-mapping
---
Encode only the visible screen with rot13, preserving cursor position

```vim
map <F3> mzHVLg?`z
```
```lua
vim.keymap.set('n', '<F3>', 'mzHVLg?`z', { desc = 'Rot13 encode visible screen' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/How_to_obscure_text_instantaneously)
***
# Title: Identify Syntax Highlighting Group Under Cursor
# Category: clever_tricks
# Tags: syntax, debugging, highlight
---
Create a mapping to reveal the syntax highlighting groups at the current cursor position, which is useful for understanding and customizing syntax highlighting

```vim
nnoremap <F10> :echo "hi<" . synIDattr(synID(line("."),col("."),1),"name") . '> trans<'
\ . synIDattr(synID(line("."),col("."),0),"name") . "> lo<"
\ . synIDattr(synIDtrans(synID(line("."),col("."),1)),"name") . ">"<CR>
```
```lua
vim.keymap.set('n', '<F10>', function()
  local line = vim.fn.line('.')
  local col = vim.fn.col('.')
  local synID = vim.fn.synID(line, col, 1)
  local transID = vim.fn.synID(line, col, 0)
  local loID = vim.fn.synIDtrans(synID)
  
  print(string.format(
    "hi<%s> trans<%s> lo<%s>", 
    vim.fn.synIDattr(synID, 'name'),
    vim.fn.synIDattr(transID, 'name'),
    vim.fn.synIDattr(loID, 'name')
  ))
end, { desc = 'Show syntax highlighting groups' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Identify_the_syntax_highlighting_group_used_at_the_cursor)
***
# Title: Insert Current Directory Name Quickly
# Category: clever_tricks
# Tags: command-line, insert-mode, productivity
---
Multiple ways to quickly insert the current working directory name in your buffer

```vim
" Method 1: Using external command
!!pwd

" Method 2: Using getcwd() function
:inoremap \fp <C-R>=getcwd()<CR>
```
```lua
-- Method 1: Using external command in normal mode
vim.cmd('!!pwd')

-- Method 2: Create a key mapping to insert current directory
vim.keymap.set('i', '<leader>fp', function()
  local cwd = vim.fn.getcwd()
  vim.api.nvim_put({cwd}, '', true, true)
end, { desc = 'Insert current directory path' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Insert_current_directory_name)
***
# Title: Quickly Insert Image Size in HTML Tags
# Category: clever_tricks
# Tags: html, perl, automation, text-manipulation
---
Automatically insert image width and height into HTML img tags using Perl's Image::Size module

```vim
function! PerlImageSize()
  g/src
  normal $
  normal N
  normal 2w
  perl << EOF
  use Image::Size;
  $jo = VIM::Eval("expand('<cfile>');");
  $size = Image::Size::html_imgsize("$jo");
  VIM::Eval("setreg('a', '$size')");
EOF
  normal $
  normal "ap
endfunction
nnoremap <F4> :call PerlImageSize()<CR>
```
```lua
function _G.perl_image_size()
  -- Note: This requires Perl and Image::Size module
  vim.cmd('g/src')
  vim.cmd('normal! $')
  vim.cmd('normal! N')
  vim.cmd('normal! 2w')
  
  -- Perl functionality would need to be replicated differently in Lua
  -- Potential alternative: Use Lua image libraries or external commands
end

vim.keymap.set('n', '<F4>', _G.perl_image_size, { desc = 'Insert image size in HTML tag' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Insert_image_size_into_html_tag)
***
# Title: Rotate Email Signatures Dynamically
# Category: clever_tricks
# Tags: email, mapping, text-manipulation
---
A clever way to rotate through multiple email signatures from a text file, automatically moving the current signature to the end after use

```vim
map <Leader>ms :e c:\sign.txt<CR>ggV/^--  $<CR>k"*xG$a<C-R><C-O>*<Esc>:w<CR>:bd<CR>G$a<C-M><Esc>"*P
```
```lua
vim.keymap.set('n', '<leader>ms', function()
  -- Open signatures file
  vim.cmd.edit('~/sign.txt')
  
  -- Extract first signature
  -- Note: This would require more complex Lua manipulation
  -- Recommend reimplementing with more robust file handling
  vim.cmd('normal! ggV/^--  $
k"*xG$a<C-R><C-O>*')
  vim.cmd.write()
  vim.cmd.bdelete()
  vim.cmd('normal! G$a
')
end, { desc = 'Rotate Email Signature' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Insert_mail_signatures_from_a_rotating_file)
***
# Title: Obscure Vim Command Obfuscation Trick
# Category: clever_tricks
# Tags: vim-tricks, command-manipulation, text-transformation
---
Showcase of complex text manipulation and transformation using Vim's powerful command chaining and substitution capabilities

```vim
vim -c ":%s%s*%Cyrnfr)fcbafbe[Oenz(Zbbyranne%|:%s)[[()])-)Ig|norm Vg?"
```
```lua
-- Lua equivalent demonstrates text transformation
-- Actual implementation would depend on specific transformation intent
vim.cmd([[%s%s*%Cyrnfr)fcbafbe[Oenz(Zbbyranne%]])
vim.cmd([[%s)[[()])-)Ig]])
vim.cmd('norm Vg?')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/JAVH_-_Just_another_Vim_Hacker)
***
# Title: Create Personal Memo File with Vim Help-Style Links
# Category: clever_tricks
# Tags: documentation, note-taking, custom-markup
---
Create a personal memo file using Vim help-style markup, enabling easy navigation and organization of notes with internal links and tags

```vim
" Memo file example with Vim help-style markup
*memo.txt* My Personal Memo

*subjects* *toc*
|cmd| Command Tips |dev| Developments

*cmd* Commands Section
*General* General Commands

" Vim settings for help-like file
vim:tw=78:fo=tcq2:isk=!-~,^*,^\|,^":ts=8:ft=help:norl:
```
```lua
-- Lua approach for creating a memo file
-- Use vim.o and vim.opt to set file-specific settings
vim.o.filetype = 'help'
vim.opt.iskeyword:append({'!-~', '^*', '^\|', '^"'})

-- Example of creating a memo buffer
vim.api.nvim_create_buf(true, false)
vim.api.nvim_buf_set_lines(0, 0, -1, false, {
  '*memo.txt* My Personal Memo',
  '',
  '*subjects* *toc*',
  '|cmd| Command Tips |dev| Developments',
  '',
  '*cmd* Commands Section',
  '*General* General Commands'
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Keep_a_to-do_memo_file_with_links_as_in_Vim_help)
***
# Title: Dynamic ZIP Code Lookup in Vim
# Category: clever_tricks
# Tags: web-lookup, external-command, utility
---
Lookup US ZIP code city and state directly from Vim using TCL and web scraping

```vim
function ZIPLookup (word)
  tcl puts [ZipLookup [::vim::expr a:word]]
endfunction

menu &Utilities.&ZipLookup :call ZIPLookup(expand("<cword>")) <CR>
```
```lua
-- Lua equivalent requires external plugin or custom function
-- Could be implemented using vim.fn.system() and a web request library
function _G.zip_lookup()
  local zipcode = vim.fn.expand('<cword>')
  -- Implement web request and parsing in Lua
  -- Example pseudo-code, actual implementation would require more robust handling
  local result = vim.fn.system('curl -s https://zip4.usps.com/zip4/zip_responseA.jsp?zipcode=' .. zipcode)
  vim.notify(result, vim.log.levels.INFO)
end

-- Set up keymap
vim.keymap.set('n', '<leader>zl', _G.zip_lookup, { desc = 'Lookup ZIP code' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Lookup_the_city_and_state_of_a_given_US_Zip_code_using_TCL)
***
# Title: C/C++ Macro Expansion in Vim
# Category: clever_tricks
# Tags: macro-expansion, c-cpp, development
---
Expand C/C++ macros using gcc in a preview window, helping developers understand macro preprocessing

```vim
function! ExpandCMacro()
  let l:macro_file_name = "__macroexpand__" . tabpagenr()
  let l:file_row = line(".")
  let l:file_name = expand("%")
  let l:file_window = winnr()
  
  execute "normal! Oint " . l:macro_file_name . ";"
  execute "w"
  
  if bufwinnr(l:macro_file_name) != -1
    execute bufwinnr(l:macro_file_name) . "wincmd w"
    setlocal modifiable
    execute "normal! ggdG"
  else
    execute "bot 10split " . l:macro_file_name
    execute "setlocal filetype=cpp"
    execute "setlocal buftype=nofile"
    nnoremap <buffer> q :q!<CR>
  endif
  
  silent! execute "r!gcc -E " . l:file_name
  execute "normal! ggV/int " . l:macro_file_name . ";$\<CR>d"
  execute "normal! jdG"
  execute "%!indent -st -kr"
  execute "normal! gg=G"
  
  execute "normal! G"
  let l:macro_end_row = line(".")
  execute "resize " . l:macro_end_row
  execute "normal! gg"
  
  setlocal nomodifiable
  execute l:file_window . "wincmd w"
  execute l:file_row
  execute "normal!u"
  execute "w"
  
  let @/ = getline('.')
endfunction
```
```lua
function _G.expand_c_macro()
  local macro_file_name = string.format("__macroexpand__%d", vim.fn.tabpagenr())
  local file_row = vim.fn.line(".")
  local file_name = vim.fn.expand("%")
  local file_window = vim.fn.winnr()

  vim.cmd(string.format("normal! Oint %s;", macro_file_name))
  vim.cmd("w")

  if vim.fn.bufwinnr(macro_file_name) ~= -1 then
    vim.cmd(string.format("%dwincmd w", vim.fn.bufwinnr(macro_file_name)))
    vim.api.nvim_win_set_option(0, 'modifiable', true)
    vim.cmd("normal! ggdG")
  else
    vim.cmd(string.format("bot 10split %s", macro_file_name))
    vim.api.nvim_buf_set_option(0, 'filetype', 'cpp')
    vim.api.nvim_buf_set_option(0, 'buftype', 'nofile')
    vim.api.nvim_buf_set_keymap(0, 'n', 'q', ':q!<CR>', {noremap = true, silent = true})
  end

  vim.cmd(string.format("r!gcc -E %s", file_name))
  vim.cmd(string.format("normal! ggV/int %s;$\<CR>d", macro_file_name))
  vim.cmd("normal! jdG")
  vim.cmd("%!indent -st -kr")
  vim.cmd("normal! gg=G")

  vim.cmd("normal! G")
  local macro_end_row = vim.fn.line(".")
  vim.cmd(string.format("resize %d", macro_end_row))
  vim.cmd("normal! gg")

  vim.api.nvim_win_set_option(0, 'modifiable', false)
  vim.cmd(string.format("%dwincmd w", file_window))
  vim.cmd(tostring(file_row))
  vim.cmd("normal!u")
  vim.cmd("w")

  vim.fn.setreg('/', vim.fn.getline('.'))
end

-- Mapping
vim.api.nvim_create_autocmd('FileType', {
  pattern = 'cpp',
  callback = function()
    vim.keymap.set('n', '<leader>m', _G.expand_c_macro, { desc = 'Expand C/C++ Macro' })
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Macro_expansion_C/C%2B%2B)
***
# Title: Persistent Echo Messages in Vim
# Category: clever_tricks
# Tags: scripting, messages, autocmd
---
Ensure echo messages are visible and don't disappear quickly, especially useful for script debugging and user notifications

```vim
func! PersistentEcho(msg)
  echo a:msg
  let g:PersistentEcho=a:msg
endfun
let g:PersistentEcho=''
if &ut>200|let &ut=200|endif
au CursorHold * if PersistentEcho!=''|echo PersistentEcho|let PersistentEcho=''|endif
```
```lua
local function persistent_echo(msg)
  vim.api.nvim_echo({{msg, 'Normal'}}, false, {})
  vim.g.persistent_echo = msg
end

vim.o.updatetime = math.min(vim.o.updatetime, 200)

vim.api.nvim_create_autocmd('CursorHold', {
  callback = function()
    if vim.g.persistent_echo and vim.g.persistent_echo ~= '' then
      vim.api.nvim_echo({{vim.g.persistent_echo, 'Normal'}}, false, {})
      vim.g.persistent_echo = ''
    end
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Make_echo_seen_when_it_would_otherwise_disappear_and_go_unseen)
***
# Title: Insert Numbered Lists Easily
# Category: clever_tricks
# Tags: list-generation, range, formatting
---
Generate numbered lists or sequences with built-in Vim range and map functions

```vim
:put =range(11,15)

" Format numbers with leading zeros
:put =map(range(1,150), 'printf(''%04d'', v:val)')
```
```lua
-- Insert numbered list
vim.cmd.put(vim.fn.range(11, 15))

-- Format numbers with leading zeros
vim.cmd.put(vim.fn.map(vim.fn.range(1, 150), function(_, val)
  return string.format('%04d', val)
end))
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Making_a_list_of_numbers)
***
# Title: Vim-Like Browser Navigation Extensions
# Category: clever_tricks
# Tags: browser, productivity, navigation
---
Multiple browser extensions provide Vim-style keyboard navigation, allowing users to browse without a mouse using familiar Vim keybindings

```lua
-- Recommended extensions for Vim-like browser navigation:
-- Chrome/Firefox: Vimium, Tridactyl, Surfingkeys
-- Dedicated Vim browsers: Qutebrowser, Vieb, Vimb
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mozilla_Vim_Keybindings)
***
# Title: Make Echo Persistent in Vim Scripts
# Category: clever_tricks
# Tags: scripting, messages, autocmd
---
Ensures echo messages remain visible by using CursorHold autocmd to prevent disappearing messages in Vim scripts

```vim
func! PersistentEcho(msg)
  echo a:msg
  let g:PersistentEcho=a:msg
endfun

let g:PersistentEcho=''
if &ut>200|let &ut=200|endif
au CursorHold * if PersistentEcho!=''|echo PersistentEcho|let PersistentEcho=''|endif
```
```lua
local function persistent_echo(msg)
  vim.api.nvim_echo({{msg, 'Normal'}}, false, {})
  vim.g.persistent_echo = msg
end

vim.g.persistent_echo = ''

-- Set up autocmd to display persistent message
vim.api.nvim_create_autocmd('CursorHold', {
  callback = function()
    if vim.g.persistent_echo ~= '' then
      vim.api.nvim_echo({{vim.g.persistent_echo, 'Normal'}}, false, {})
      vim.g.persistent_echo = ''
    end
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/OPENBRACKET_for_script_writers_CLOSEBRACKET_make_echo_seen_when_it_would_otherwise_disappear_and_go_unseen)
***
# Title: Open URLs from Current Line in Browser
# Category: clever_tricks
# Tags: url-handling, external-command, productivity
---
Extract and open URLs from the current line in a web browser using a custom function

```vim
function! Browser()
  let line = matchstr(getline("."), '[a-z]*://[^ >,;:]*')
  if line != ""
    exec "!xdg-open " . line
  endif
endfunction
map <Leader>w :call Browser()<CR>
```
```lua
function _G.open_url_from_line()
  local line = vim.fn.matchstr(vim.fn.getline('.'), '[a-z]*://[^ >,;:]*')
  if line ~= "" then
    vim.fn.system({'xdg-open', line})
  end
end

vim.keymap.set('n', '<Leader>w', _G.open_url_from_line, { desc = 'Open URL from current line' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_a_web-browser_with_the_URL_in_the_current_line)
***
# Title: Platform-Specific URL Opening
# Category: clever_tricks
# Tags: cross-platform, url-handling, external-command
---
Platform-specific methods to open URLs using system commands

```vim
" Mac OS X
function! HandleURI()
  let s:uri = matchstr(getline("."), '[a-z]*://[^ >,;:]*')
  if s:uri != ""
    exec "!open " . s:uri
  endif
endfunction

" Linux
nnoremap <leader>w :silent !xdg-open <C-R>=escape("<C-R><C-F>", "#?&;|%")<CR><CR>
```
```lua
-- Mac OS X
function _G.mac_open_uri()
  local uri = vim.fn.matchstr(vim.fn.getline('.'), '[a-z]*://[^ >,;:]*')
  if uri ~= "" then
    vim.fn.system({'open', uri})
  end
end

-- Linux
vim.keymap.set('n', '<Leader>w', function()
  local url = vim.fn.expand('<cfile>')
  vim.fn.system({'xdg-open', url})
end, { desc = 'Open URL under cursor' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_a_web-browser_with_the_URL_in_the_current_line)
***
# Title: Dynamic Page Count for Hardcopy Printing
# Category: clever_tricks
# Tags: printing, formatting, hardcopy
---
Automatically calculate total pages when printing, accounting for varying lines per page

```vim
function! PH_Multiple()
  let lpp = "73" " lpp - lines per page
  let modulo = line('$') % lpp
  if modulo != 0
    return ( line('$') / lpp ) + 1
  else
    return line('$') / lpp
  endif
endfunction
set printheader=%<%f%h%m%=Page\ %N\ of\ %{PH_Multiple()}
```
```lua
function PrintPageCount()
  local lpp = 73 -- lines per page
  local total_lines = vim.fn.line('$')
  local pages = math.floor(total_lines / lpp)
  
  if total_lines % lpp ~= 0 then
    pages = pages + 1
  end
  
  return pages
end

vim.opt.printheader = '%<%f%h%m%=Page %N of ' .. vim.fn.eval('PrintPageCount()')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Page_1_of_123_in_header_of_hardcopy)
***
# Title: Confirm Before Quitting in Insert Mode
# Category: clever_tricks
# Tags: key-mapping, insert-mode, workflow
---
Adds a confirmation dialog when accidentally typing 'wq' in insert mode, preventing unintended file saves and quits

```vim
function WQHelper()
  let x = confirm("Current Mode == Insert-Mode!\n Would you like ':wq'?", " &Yes \n &No", 1, 1)
  if x == 1
    silent! :wq
  else
    "???
  endif
endfunction

iab wq <BS><Esc>:call WQHelper()<CR>
```
```lua
function _G.wq_helper()
  local choice = vim.fn.confirm(
    "Current Mode == Insert-Mode!\nWould you like ':wq'?", 
    "&Yes\n&No", 
    1
  )
  if choice == 1 then
    vim.cmd('wq')
  end
end

vim.keymap.set('i', 'wq', '<BS><Esc>:lua _G.wq_helper()<CR>')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Prompted_quit_in_insert-mode)
***
# Title: Create Comment Boxes with External Utility
# Category: clever_tricks
# Tags: text-formatting, external-tools, comments
---
Use the 'boxes' utility to automatically create formatted comment boxes around text in code

```vim
" Map F2 to create comment boxes for selected text
vmap <F2> !boxes -s 80 <CR>
```
```lua
-- Lua equivalent for creating comment boxes
vim.keymap.set('v', '<F2>', '!boxes -s 80<CR>', { desc = 'Create comment box' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Put_boxes_around_comments_in_code)
***
# Title: Recursive Macros for Automated Text Manipulation
# Category: clever_tricks
# Tags: macros, text-processing, automation
---
Use recursive macros to perform complex text transformations across an entire file by recording a macro that calls itself, allowing for dynamic and flexible editing

```vim
" Record a recursive macro
qqq  " Clear register q
qq   " Start recording
f2   " Find '2' character
D    " Delete rest of line
Fr   " Find last 'r'
p    " Paste deleted text
j    " Move to next line
@q   " Execute macro recursively
q    " Stop recording
```
```lua
-- Lua equivalent of recursive macro recording
-- Note: Macros are typically still recorded in normal mode
-- Can be executed in Lua using vim.fn.execute('@q')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Record_a_recursive_macro)
***
# Title: Fix Syntax Highlighting with F12 Mapping
# Category: clever_tricks
# Tags: syntax-highlighting, key-mapping, performance
---
Create a quick mapping to resync syntax highlighting when it breaks, improving editor responsiveness

```vim
noremap <F12> <Esc>:syntax sync fromstart<CR>
inoremap <F12> <C-o>:syntax sync fromstart<CR>
```
```lua
vim.keymap.set({'n', 'i'}, '<F12>', ':syntax sync fromstart<CR>', { desc = 'Resync syntax highlighting' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Refresh_out-of-sync_syntax_highlighting)
***
# Title: Preserve Cursor Position During Script Undo
# Category: clever_tricks
# Tags: cursor-position, undo, scripting
---
Ensure cursor returns to original position after undoing script-made changes by creating a 'fake' text modification

```vim
" In a function before making changes
execute "normal! i "
execute "normal! a\<BS>"
```
```lua
-- Lua equivalent for preserving cursor position
local function preserve_cursor_on_undo()
  vim.cmd('normal! i ')
  vim.cmd('normal! a\<BS>')
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Restore_the_cursor_position_after_undoing_text_change_made_by_a_script)
***
# Title: Reverse Block Order Using Macros
# Category: clever_tricks
# Tags: macros, text-manipulation, recording
---
Efficiently reorder blocks of text by recording a macro to move blocks to the beginning of the file

```vim
ma
qa
jV/<\/div><CR>
:m0<CR>
'a
q
@a@@@@@@
```
```lua
-- Note: Translated macro approach
-- 1. Set mark at first block end
-- 2. Record macro to move subsequent blocks
-- 3. Replay macro multiple times

-- Example implementation
local function reverse_blocks()
  -- Start at first block end
  -- Record macro to move next block to top
  -- Replay macro until blocks reordered
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Reversing_order_of_blocks_of_text)
***
# Title: Dynamic Mail Signature Rotation in Vim
# Category: clever_tricks
# Tags: email, scripting, key-mapping
---
Automatically rotate mail signatures by replacing the existing signature with a new one from a quotes file

```vim
function! RotateSig()
  normal! mQG
  execute '?^-- $'
  execute ':nohl'
  normal! o<Esc>
  normal! dG
  normal! <CR>
  execute 'r !~/bin/autosig ~/.quotes \%'
  normal! `Q
endfunction

" Mapping
nnoremap ,r :call RotateSig()<CR>
```
```lua
function _G.rotate_signature()
  -- Mark current position
  vim.api.nvim_command('normal! mQ')
  
  -- Go to signature marker
  vim.api.nvim_command('?^-- $')
  vim.api.nvim_command('nohlsearch')
  
  -- Add new line and delete existing signature
  vim.api.nvim_command('normal! o')
  vim.api.nvim_command('normal! dG')
  
  -- Insert new signature from external command
  vim.api.nvim_command('read !~/bin/autosig ~/.quotes %')
  
  -- Return to original position
  vim.api.nvim_command('normal! `Q')
end

-- Key mapping
vim.keymap.set('n', ',r', _G.rotate_signature, { desc = 'Rotate email signature' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Rotating_mail_signatures)
***
# Title: Inspect Character Class in Vim
# Category: clever_tricks
# Tags: character-classes, text-inspection, regex
---
Display all characters matching a specific character class, showing their character and ASCII value

```vim
fun! s:Show()
  norm! viwy
  echo 'class [:' . @" . ':]' . "\n"
  let pat = '[[:' . @" . ':]]'
  let i = 0
  while i < 256
    let ch = nr2char(i)
    if ch =~ pat | echon ch . '(' . i . ')' . "\t" | endif
    let i = i + 1
  endwhile
endfun
nn cc :call <SID>Show()<Cr>
```
```lua
function _G.show_character_class()
  vim.cmd('normal! viwy')
  local class = vim.fn.getreg('"')
  print('class [:' .. class .. ':]\')
  
  local pattern = '[[:' .. class .. ':]]'
  
  for i = 0, 255 do
    local ch = vim.fn.nr2char(i)
    if ch:match(pattern) then
      io.write(ch .. '(' .. i .. ')\t')
    end
  end
end

vim.keymap.set('n', 'cc', _G.show_character_class, { desc = 'Show character class details' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip502)
***
# Title: Use Vim as a Bookmark Manager
# Category: clever_tricks
# Tags: url-management, browser-integration, productivity
---
Create a centralized URL bookmark file that can be easily opened in a web browser directly from Vim

```vim
autocmd BufRead ~/url map <F8> :call BrowserURL()<CR>
let g:web_browser = "konqueror"
function! BrowserURL()
  if getline('.') !~ '^\s*\#'
    if g:web_browser == "konqueror"
      exe ":!dcop `dcopfind -a 'konqueror*'` konqueror-mainwindow\#1 newTab ".getline('.')
    elseif g:web_browser == "mozilla"
      exe ":!mozilla -remote \"openurl(".getline('.').", new-tab)\""
    endif
  endif
endfunction
```
```lua
vim.api.nvim_create_autocmd('BufRead', {
  pattern = '~/url',
  callback = function()
    vim.keymap.set('n', '<F8>', function()
      local line = vim.fn.getline('.')
      if not line:match('^%s*#') then
        vim.fn.system('xdg-open ' .. line)
      end
    end)
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip555)
***
# Title: Generate Unicode Character Table
# Category: clever_tricks
# Tags: unicode, character-display, text-manipulation
---
Create a comprehensive table of Unicode characters within a specified range, useful for exploring character sets and font support

```vim
function! GenerateUnicode(first, last)
  let i = a:first
  while i <= a:last
    if (i%256 == 0)
      $put ='----------------------------------------------------'
      $put ='     0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F '
      $put ='----------------------------------------------------'
    endif
    let c = printf('%04X ', i)
    for j in range(16)
      let c = c . nr2char(i) . ' '
      let i += 1
    endfor
    $put =c
  endwhile
endfunction
```
```lua
function _G.generate_unicode(first, last)
  local buffer = vim.api.nvim_create_buf(true, true)
  vim.api.nvim_set_current_buf(buffer)

  local i = first
  while i <= last do
    if (i % 256 == 0) then
      vim.api.nvim_buf_set_lines(buffer, -1, -1, false, {
        '----------------------------------------------------',
        '     0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F ',
        '----------------------------------------------------'
      })
    end

    local line = string.format('%04X ', i)
    for j = 1, 16 do
      line = line .. string.char(i) .. ' '
      i = i + 1
    end

    vim.api.nvim_buf_set_lines(buffer, -1, -1, false, {line})
  end
end

-- Usage: :lua generate_unicode(0x9900, 0x9fff)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip576)
***
# Title: Create Postfix Abbreviations for Code Snippets
# Category: clever_tricks
# Tags: abbreviations, code-generation, productivity
---
Use Vim abbreviations to quickly generate code snippets by typing a word followed by an abbreviation trigger

```vim
:ab ff <Esc>^d$ifor(int i=0;i<<Esc>pi.length;i++){<CR><CR>}//end for loop over array <Esc>pi[i]<Esc>==k==k==ji<Tab>
```
```lua
-- Note: In Neovim, you can use vim.cmd to set abbreviations
vim.cmd('ab ff <Esc>^d$ifor(int i=0;i<<Esc>pi.length;i++){<CR><CR>}//end for loop over array <Esc>pi[i]<Esc>==k==k==ji<Tab>')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip593)
***
# Title: Create Text Abbreviations for Frequent Typos
# Category: clever_tricks
# Tags: abbreviations, typing, autocorrect
---
Automatically correct common typos or expand shorthand text while typing in insert mode

```vim
iabbrev teh the
iabbrev seperate separate
iabbrev #i #include
iabbrev #d #define
```
```lua
vim.cmd('iabbrev teh the')
vim.cmd('iabbrev seperate separate')
vim.cmd('iabbrev #i #include')
vim.cmd('iabbrev #d #define')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip610)
***
# Title: Efficient Debug Print Statements in C++
# Category: clever_tricks
# Tags: debugging, key-mapping, language-specific
---
Streamline creating print statements by remapping keys to reduce keystrokes and shift key usage when debugging C++ code

```vim
function! CppSetupCout()
  inoremap , <Space><<
  inoremap < ,
  inoremap ' "
  inoremap " '
  imap ; <Esc>:call CppResetCout()<CR>a;
endfunction
```
```lua
function _G.cpp_setup_cout()
  vim.keymap.set('i', ',', '<Space><<', { buffer = true })
  vim.keymap.set('i', '<', ',', { buffer = true })
  vim.keymap.set('i', "'", '"', { buffer = true })
  vim.keymap.set('i', '"', "'", { buffer = true })
end

vim.api.nvim_create_autocmd('FileType', {
  pattern = 'cpp',
  callback = _G.cpp_setup_cout
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip625)
***
# Title: Execute Accidentally Inserted Normal Mode Commands
# Category: clever_tricks
# Tags: insert-mode, mapping, undo
---
Allows executing normal mode commands accidentally typed in insert mode by quickly undoing and executing the text as a command

```vim
inoremap <somekey> <Esc>u@.

autocmd CursorHoldI * call feedkeys("\<C-G>u", 'tn')
```
```lua
-- Lua equivalent
vim.keymap.set('i', '<somekey>', '<Esc>u@.', { desc = 'Undo and execute as command' })

vim.api.nvim_create_autocmd('CursorHoldI', {
  callback = function()
    vim.fn.feedkeys('\<C-G>u', 'tn')
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip637)
***
# Title: Transfer Text Between Vim Instances
# Category: clever_tricks
# Tags: file-transfer, cross-session, text-exchange
---
Easily copy and paste text between different Vim/Neovim sessions using a temporary file

```vim
" Copy and paste between different Vim sessions
nmap _Y :!echo "" > ~/.vi_tmp<CR><CR>:w! ~/.vi_tmp<CR>
vmap _Y :w! ~/.vi_tmp<CR>
nmap _P :r ~/.vi_tmp<CR>
```
```lua
-- Function to copy text to a temp file
function CopyToTempFile()
  vim.fn.writefile(vim.fn.getline(1, '$'), vim.fn.expand('~/.vi_tmp'))
end

-- Function to paste from temp file
function PasteFromTempFile()
  vim.cmd('r ~/.vi_tmp')
end

-- Set up keymappings
vim.keymap.set({'n', 'v'}, '_Y', CopyToTempFile, { desc = 'Copy to temp file' })
vim.keymap.set('n', '_P', PasteFromTempFile, { desc = 'Paste from temp file' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip66)
***
# Title: Launch Multiple Vim Instances in Windows
# Category: clever_tricks
# Tags: windows, multi-instance, launcher
---
Use Rundll32.exe to launch multiple Vim instances reliably in Windows, bypassing single-instance limitations

```vim
C:\WINDOWS\system32\rundll32.exe Shell32.dll,ShellExec_RunDLL "C:\Program Files\Vim\vim72\gvim.exe"
```
```lua
-- For Neovim, use vim.fn.system() to launch
vim.fn.system('rundll32.exe Shell32.dll,ShellExec_RunDLL "nvim"')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip676)
***
# Title: Quick Word Count in Vim
# Category: clever_tricks
# Tags: text-editing, statistics, productivity
---
Multiple methods to count words in a document, including partial selections and live word count

```vim
" Count words in current buffer
g Ctrl-g

" Count words in selected block
V5j
g Ctrl-g

" Get word count using external command
:w !wc
```
```lua
-- Note: Word count functionality is built-in
-- Use g Ctrl-g in normal or visual mode

-- Custom word count function for status line
function WordCount()
  local words = vim.fn.wordcount()
  return words.words .. ' words'
end

-- Add to status line
vim.opt.statusline:append('%{v:lua.WordCount()}')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip689)
***
# Title: Quick Word Count in Vim/Neovim
# Category: clever_tricks
# Tags: word-count, buffer-management, text-editing
---
Multiple ways to count words in a buffer or selected text, including built-in and external methods

```vim
" Count words in current buffer
g Ctrl-g

" Count words in selected block
V5j
g Ctrl-g

" Count words using external wc command
:w !wc
```
```lua
-- For current buffer word count
-- Use g Ctrl-g in normal mode

-- For external word count
vim.api.nvim_command('w !wc')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Word_count)
***
