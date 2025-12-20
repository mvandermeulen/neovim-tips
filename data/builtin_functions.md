# Title: Get file type and encoding
# Category: Functions
# Tags: getftype, getfperm, file, info
---
Use `getftype()` to determine file type and `getfperm()` to get file permissions for the current or specified file.
Or:

```vim
:echo getftype(expand('%'))     " file type (file, dir, link, etc.)
:echo getfperm(expand('%'))     " file permissions (rwxrwxrwx)
:echo getfsize(expand('%'))     " file size in bytes
```

```lua
print(vim.fn.getftype(vim.fn.expand('%')))
print(vim.fn.getfperm(vim.fn.expand('%')))
print(vim.fn.getfsize(vim.fn.expand('%')))
```

**Source:** Community contributed
***
# Title: String manipulation functions
# Category: Functions
# Tags: substitute, matchstr, split, string
---
Use `substitute()`, `matchstr()`, and `split()` functions for powerful string manipulation without changing buffers.
Or:

```vim
:echo substitute("hello world", "world", "vim", "g")  " hello vim
:echo matchstr("file.txt", '\\.\\w\\+$')             " .txt
:echo split("a,b,c", ",")                            " ['a', 'b', 'c']
```

```lua
print(vim.fn.substitute("hello world", "world", "vim", "g"))
print(vim.fn.matchstr("file.txt", '\\.\\w\\+$'))
print(vim.fn.split("a,b,c", ","))
```

**Source:** Community contributed
***
# Title: Buffer and window information
# Category: Functions
# Tags: bufnr, winnr, tabpagenr, info
---
Use `bufnr()`, `winnr()`, `tabpagenr()` to get current buffer, window, and tab numbers for scripting.
Or:

```vim
:echo bufnr('%')        " current buffer number
:echo winnr()           " current window number
:echo tabpagenr()       " current tab number
:echo winnr('$')        " total number of windows
```

```lua
print(vim.fn.bufnr('%'))
print(vim.fn.winnr('%'))
print(vim.fn.tabpagenr('%'))
print(vim.fn.winnr('%'))
```

**Source:** Community contributed
***
# Title: Path manipulation functions
# Category: Functions
# Tags: fnamemodify, resolve, simplify, path
---
Use `fnamemodify()` to manipulate file paths and `resolve()` to resolve symbolic links and shortcuts.
Or:

```vim
:echo fnamemodify(expand('%'), ':p:h')     " full directory path
:echo fnamemodify(expand('%'), ':t:r')     " filename without extension
:echo resolve(expand('%'))                 " resolve symlinks
:echo simplify('../path/./file')           " normalize path
```

```lua
print(vim.fn.fnamemodify(vim.fn.expand('%'), ':p:h'))
print(vim.fn.fnamemodify(vim.fn.expand('%'), ':t:r'))
print(vim.fn.resolve(vim.fn.expand('%')))
print(vim.fn.simplify('../path/./file'))
```

**Source:** Community contributed
***
# Title: Search and match functions
# Category: Functions
# Tags: search, searchpos, match, pattern
---
Use `search()`, `searchpos()`, and `match()` functions for programmatic searching without moving cursor.
Or:

```vim
:echo search('pattern')                    " find pattern, return line number
:echo searchpos('pattern')                 " return [line, column]
:echo match('hello world', 'wor')          " find position in string (6)
:echo matchend('hello world', 'wor')       " end position (9)
```

```lua
print(vim.fn.search('pattern'))
print(vim.fn.searchpos('pattern'))
print(vim.fn.match('hello world', 'wor'))
print(vim.fn.matchend('hello world', 'wor'))
```

**Source:** Community contributed
***
# Title: Line and column functions
# Category: Functions
# Tags: line, col, getline, setline
---
Use `line()`, `col()`, `getline()`, `setline()` for precise cursor positioning and line manipulation.
Or:

```vim
:echo line('.')         " current line number
:echo col('.')          " current column number
:echo getline('.')      " current line text
:call setline('.', 'new text')  " replace current line
```

```lua
print(vim.fn.line('.'))
print(vim.fn.col('.'))
print(vim.fn.getline('.'))
vim.fn.setline('.', 'new text')
```

**Source:** Community contributed
***
# Title: Date and time functions
# Category: Functions
# Tags: strftime, localtime, getftime, date
---
Use `strftime()` and `localtime()` for date/time manipulation, and `getftime()` for file timestamps.
Or:

```vim
:echo strftime('%Y-%m-%d %H:%M:%S')       " current date/time
:echo strftime('%Y-%m-%d', localtime())   " current date
:echo getftime(expand('%'))               " file modification time
:put =strftime('%Y-%m-%d')                " insert current date
```

```lua
print(vim.fn.strftime('%Y-%m-%d %H:%M:%S'))
print(vim.fn.strftime('%Y-%m-%d', vim.fn.localtime()))
print(vim.fn.getftime('%Y-%m-%d', vim.fn.expand('%')))
vim.api.nvim_put({os.date('%Y-%m-%d')}, 'c', true, true)
```

**Source:** Community contributed
***
# Title: System and environment functions
# Category: Functions
# Tags: system, systemlist, environ, getenv
---
Use `system()` and `systemlist()` to execute shell commands and `getenv()` to access environment variables.
Or:

```vim
:echo system('date')                      " execute shell command
:echo systemlist('ls -la')               " return as list
:echo getenv('HOME')                      " get environment variable
:echo exists('$EDITOR')                  " check if env var exists
```

```lua
print(vim.fn.system('date'))
print(vim.fn.systemlist('ls -la'))
print(vim.fn.geten('HOME'))
print(vim.fn.exists('$EDITOR'))
```

**Source:** Community contributed
***
# Title: List and dictionary functions
# Category: Functions
# Tags: len, empty, has_key, keys, values
---
Use `len()`, `empty()`, `has_key()`, `keys()`, `values()` for working with lists and dictionaries.
Or:

```vim
:let mylist = [1, 2, 3]
:echo len(mylist)                         " length: 3
:echo empty(mylist)                       " false (0)
:let mydict = {'a': 1, 'b': 2}
:echo has_key(mydict, 'a')               " true (1)
:echo keys(mydict)                        " ['a', 'b']
```

```lua
local mylist = {1, 2, 3}
print(#mylist)
print(vim.tbl_isempty(mylist))
local mydict = {a = 1, b = 2}
print(mydict.a ~= nil)
print(vim.inspect(vim.tbl_keys(mydict)))
```

**Source:** Community contributed
***
# Title: Type checking functions
# Category: Functions
# Tags: type, islocked, exists, function
---
Use `type()`, `islocked()`, and `exists()` functions to check variable types and existence.
Or:

```vim
:echo type(42)                   " 0 (Number)
:echo type("string")             " 1 (String)  
:echo type([])                   " 3 (List)
:echo type({})                   " 4 (Dictionary)
:echo exists('g:my_var')         " check if variable exists
```

```lua
print(vim.fn.type(42))
print(vim.fn.type("string"))
print(vim.fn.type([]))
print(vim.fn.type({}))
print(vim.fn.exists('g:my_var'))
```

**Source:** Community contributed
***
# Title: Mathematical functions
# Category: Functions
# Tags: abs, pow, sqrt, sin, cos, math
---
Use built-in math functions like `abs()`, `pow()`, `sqrt()`, `sin()`, `cos()` for calculations in vim script.
Or:

```vim
:echo abs(-5)                    " absolute value: 5
:echo pow(2, 3)                  " 2 to power of 3: 8
:echo sqrt(16)                   " square root: 4.0
:echo sin(3.14159/2)             " sine: ~1.0
:echo round(3.7)                 " round: 4
```

```lua
print(vim.fn.abs(-5))
print(vim.fn.pow(2, 3))
print(vim.fn.sqrt(16))
print(vim.fn.sin(3.14159/2))
print(vim.fn.round(3.7))
```

**Source:** Community contributed
***
# Title: Buffer content functions
# Category: Functions
# Tags: getbufline, setbufline, append, delete
---
Use `getbufline()` and `setbufline()` to read and modify buffer content without switching to the buffer.
Or:

```vim
:echo getbufline(1, 1, 10)              " get lines 1-10 from buffer 1
:call setbufline(2, 1, 'new first line') " set line 1 in buffer 2
:call append(line('.'), 'new line')      " append after current line
:call delete(line('.'))                  " delete current line
```

```lua
print(vim.fn.getbufline(1, 1, 10))
vim.fn.setbufline(2, 1, 'new first line')
vim.fn.append(vim.fn.line('.'), 'new line')
vim.fn.delete(vim.fn.line('.'))
```

**Source:** Community contributed
***
# Title: Input and interaction functions
# Category: Functions
# Tags: input, inputsave, inputlist, confirm
---
Use `input()`, `inputlist()`, `confirm()` functions to create interactive vim scripts with user prompts.
Or:

```vim
:let name = input('Enter name: ')         " prompt for input
:let choice = inputlist(['1. Red', '2. Blue', '3. Green'])
:let result = confirm('Save changes?', "&Yes\n&No\n&Cancel")
:echo "You chose: " . choice
```

```lua
local name = vim.fn.input('Enter name: ')
local choice = vim.fn.inputlist(['1.Red', '2. Blue', '3. Green'])
local result = vim.fn.confirm('Save changes?', '&Yes\n&No\n&Cancel')
print("You chose: " .. choice)
```

**Source:** Community contributed
***
# Title: Window and tab functions
# Category: Functions
# Tags: winheight, winwidth, tabpagebuflist, winsaveview
---
Use window dimension and state functions to manage window layouts programmatically.
Or:

```vim
:echo winheight(0)               " current window height
:echo winwidth(0)                " current window width  
:let view = winsaveview()        " save cursor position and view
:call winrestview(view)          " restore saved view
:echo tabpagebuflist()           " list buffers in current tab
```

```lua
print(vim.fn.winheight(0))
print(vim.fn.winwidth(0))
local view = vim.fn.winsaveview()
vim.fn.winrestview(view)
print(vim.fn.tabpaebuflist())
```

**Source:** Community contributed
***
# Title: Highlighting and syntax functions
# Category: Functions
# Tags: synID, synIDattr, hlID, syntax
---
Use syntax highlighting functions to query and manipulate syntax highlighting programmatically.
Or:

```vim
:echo synID(line('.'), col('.'), 1)      " syntax ID under cursor
:echo synIDattr(synID(line('.'), col('.'), 1), 'name')  " syntax name
:echo hlID('Comment')                    " highlight group ID
:echo synIDattr(hlID('Comment'), 'fg')   " foreground color
```

```lua
print(vim.fn.synID(vim.fn.line('.'), vim.fn.col('.'), 1))
print(vim.fn.synIDattr(vim.fn.synId(vim.fn.line('.'), vim.fn.col('.'), 1), 'name'))
print(vim.fn.hlID('Comment'))
print(vim.fn.synIDattr(vim.fn.hlID('Comment'), 'fg'))
```

**Source:** Community contributed
***
# Title: Regular expression functions
# Category: Functions
# Tags: matchadd, matchdelete, matchlist, regex
---
Use `matchadd()`, `matchdelete()`, `matchlist()` for advanced pattern matching and highlighting.
Or:

```vim
:let m = matchadd('Search', 'TODO')      " highlight all TODO
:call matchdelete(m)                     " remove highlighting
:echo matchlist('file.txt', '\\(.*\\)\\.\\(.*\\)')  " capture groups
:echo matchstr('hello123world', '\\d\\+') " extract digits: 123
```

```lua
local m = vim.fn.matchadd('Search', 'TODO')
vim.fn.matchdelete(m)
print(vim.fn.matchlist('file.txt', '\\(.*\\)\\.\\(.*\\)'))
print(vim.fn.matchstr('hello123world', '\\d\\+'))
```

**Source:** Community contributed
***
# Title: Fold information functions
# Category: Functions
# Tags: foldclosed, foldtext, foldlevel, folding
---
Use folding functions to query and manipulate code folds programmatically.
Or:

```vim
:echo foldclosed(line('.'))      " check if current line is folded
:echo foldlevel(line('.'))       " fold level of current line
:echo foldtext()                 " default fold text
:set foldtext=MyCustomFoldText() " custom fold text function
```

```lua
print(vim.fn.foldclosed(vim.fn.line('.')))
print(vim.fn.foldlevel(vim.fn.line('.')))
print(vim.fn.foldnext())
vim.opt.foldtext = MyCustomFoldText()
```

**Source:** Community contributed
***
# Title: File and directory functions
# Category: Functions
# Tags: glob, globpath, isdirectory, readable
---
Use `glob()`, `globpath()`, `isdirectory()` for file system operations and path expansion.
Or:

```vim
:echo glob('*.txt')              " find all .txt files
:echo globpath(&rtp, 'plugin/*.vim')  " find plugins in runtimepath
:echo isdirectory(expand('%:h')) " check if directory exists
:echo readable(expand('%'))      " check if file is readable
```

```lua
print(vim.fn.glob('*.txt'))
print(vim.fn.globpath(&rtp, 'plugin/*.vim'))
print(vim.fn.isdirectory(vim.fn.expand('%:h')))
print(vim.fn.readable(vim.fn.expand('%')))
```

**Source:** Community contributed
***
# Title: Register manipulation functions
# Category: Functions
# Tags: getreg, setreg, getregtype, registers
---
Use `getreg()`, `setreg()`, `getregtype()` to programmatically work with vim registers.
Or:

```vim
:echo getreg('"')                " get default register content
:call setreg('a', 'hello world') " set register 'a'
:echo getregtype('a')            " get register type (v, V, or Ctrl-V)
:call setreg('+', "@")            " copy default register to clipboard
```

```lua
print(vim.fn.getreg('"'))
vim.fn.setreg('a', 'hello world')
print(vim.fn.getregtype('a'))
vim.fn.setreg('+', "@")
```

**Source:** Community contributed
***
# Title: Cursor and mark functions
# Category: Functions
# Tags: cursor, getpos, setpos, marks
---
Use `cursor()`, `getpos()`, `setpos()` for precise cursor and mark manipulation.
Or:

```vim
:call cursor(10, 5)              " move cursor to line 10, column 5
:let pos = getpos('.')           " get current cursor position
:call setpos('.', pos)           " restore cursor position
:echo getpos("'a")               " get position of mark 'a'
```

```lua
vim.fn.cursor(10, 5)
local pos = vim.fn.getpos('.')
vim.fn.setpos('.', pos)
print(vim.fn.getpos("'a"))
```

**Source:** Community contributed
***
# Title: Create Custom Help Tags Programmatically
# Category: builtin_functions
# Tags: help, custom-tags, automation
---
Programmatically add custom help tags to make personal notes easily searchable

```vim
function! AddMyHelpTags()
  exe 'echo -e "sfsed\t ~/Documents/mynotesfile.mytext\t/\*sfsed\*" >> ~/.vim/doc/tags'
  exe 'sort ~/.vim/doc/tags > /tmp/foo.vim.tags'
  exe 'mv -f /tmp/foo.vim.tags ~/.vim/doc/tags'
endfunction
```

```lua
local function add_help_tags()
  local tags_path = vim.fn.expand('~/.vim/doc/tags')
  local new_tag = 'sfsed\t ~/Documents/mynotesfile.mytext\t/*sfsed*\n'
  
  -- Append tag and sort
  vim.fn.writefile(
    vim.fn.sort(vim.fn.readfile(tags_path) + {new_tag}),
    tags_path
  )
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Add_your_note_files_to_Vim_help)
***
# Title: Detect Comments Across Filetypes
# Category: builtin_functions
# Tags: syntax, scripting, highlight
---
Use syntax highlighting to check if cursor is in a comment, string, or preprocessor statement, independent of filetype

```vim
" Check if cursor is in a comment
let is_comment = synIDattr(synIDtrans(synID(line('.'), col('.'), 0)), 'name') == 'Comment'

" Check if cursor is in comment, string, or preprocessor
let is_special = synIDattr(synIDtrans(synID(line('.'), col('.'), 0)), 'name') =~ 'Comment\|Constant\|PreProc'
```

```lua
-- Check if cursor is in a comment
local function is_comment()
  return vim.fn.synIDattr(vim.fn.synIDtrans(vim.fn.synID(vim.fn.line('.'), vim.fn.col('.'), 0)), 'name') == 'Comment'
end

-- Check if cursor is in comment, string, or preprocessor
local function is_special()
  local syn_name = vim.fn.synIDattr(vim.fn.synIDtrans(vim.fn.synID(vim.fn.line('.'), vim.fn.col('.'), 0)), 'name')
  return syn_name:match('Comment') or syn_name:match('Constant') or syn_name:match('PreProc')
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Check_for_comments_independent_of_filetype)
***
# Title: Get Cursor Position as Byte Percentage
# Category: builtin_functions
# Tags: status-line, cursor-position, file-metadata
---
Calculate and display cursor position as byte percentage instead of default line percentage, which is more accurate for files with varying line lengths

```vim
function! Percent()
  let byte = line2byte(line(".")) + col(".") - 1
  let size = (line2byte(line("$") + 1) - 1)
  return (byte * 100) / size
endfunction
```

```lua
function _G.byte_percentage()
  local byte = vim.fn.line2byte(vim.fn.line('.')) + vim.fn.col('.') - 1
  local size = vim.fn.line2byte(vim.fn.line('$') + 1) - 1
  return math.floor((byte * 100) / size)
end

-- Add to statusline
vim.opt.statusline:append('%{v:lua.byte_percentage()}%')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Get_cursor_position_as_byte_percentage_instead_of_line_percentage)
***
# Title: Print Full-Width Messages Without 'Press Enter'
# Category: builtin_functions
# Tags: scripting, message-display, vim-functions
---
A utility function to print messages across full screen width without triggering 'Press Enter' prompt by temporarily modifying ruler and showcmd settings

```vim
function! WideMsg(msg)
  let x=&ruler | let y=&showcmd
  set noruler noshowcmd
  redraw
  echo a:msg
  let &ruler=x | let &showcmd=y
endfun
```

```lua
function _G.WideMsg(msg)
  local ruler = vim.o.ruler
  local showcmd = vim.o.showcmd
  vim.o.ruler = false
  vim.o.showcmd = false
  vim.cmd.redraw()
  vim.api.nvim_echo({{msg}}, false, {})
  vim.o.ruler = ruler
  vim.o.showcmd = showcmd
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/How_to_print_full_screen_width_messages)
***
# Title: Insert Current Date/Time with Strftime()
# Category: builtin_functions
# Tags: date, timestamp, abbreviations
---
Easily insert current date and time using Vim's built-in strftime() function with various formatting options

```vim
" Insert current date/time on F5
:nnoremap <F5> "=strftime("%c")<CR>P
:inoremap <F5> <C-R>=strftime("%c")<CR>

" Abbreviation for quick timestamp
:iab <expr> dts strftime("%c")
```

```lua
-- Insert current date/time on F5
vim.keymap.set('n', '<F5>', function()
  vim.api.nvim_put({os.date("%c")}, '', true, true)
end)

vim.keymap.set('i', '<F5>', function()
  return os.date("%c")
end, { expr = true })

-- Create abbreviation for quick timestamp
vim.cmd.iabbrev('dts', os.date("%c"))
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Insert_current_date_or_time)
***
# Title: Save and Restore Cursor Position Precisely
# Category: builtin_functions
# Tags: cursor-position, screen-position, utility-function
---
Create a function to precisely save and restore cursor and screen positions, which is useful when performing operations that might disrupt cursor placement

```vim
function CurPos(action)
  if a:action == "save"
    let b:saveve = &virtualedit
    let b:savesiso = &sidescrolloff
    set virtualedit=all
    set sidescrolloff=0
    let b:curline = line(".")
    let b:curvcol = virtcol(".")
    let b:curwcol = wincol()
  elseif a:action == "restore"
    execute "normal! ".b:midline."Gzz".b:curline."G0"
    execute "normal! ".b:curvcol."|")
  endif
endfunction
```

```lua
function _G.CurPos(action)
  if action == "save" then
    vim.b.saveve = vim.o.virtualedit
    vim.b.savesiso = vim.o.sidescrolloff
    vim.o.virtualedit = "all"
    vim.o.sidescrolloff = 0
    vim.b.curline = vim.fn.line(".")
    vim.b.curvcol = vim.fn.virtcol(".")
    vim.b.curwcol = vim.fn.wincol()
  elseif action == "restore" then
    vim.cmd(string.format("normal! %dGzz%dG0", vim.b.midline, vim.b.curline))
    vim.cmd(string.format("normal! %d|", vim.b.curvcol))
  end
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Maintain_cursor_and_screen_position)
***
# Title: Measure Command Execution Time
# Category: builtin_functions
# Tags: performance, benchmarking, timing
---
Function to measure the execution time of Vim commands across multiple iterations, useful for performance testing and optimization

```vim
function! Time(com, ...)
  let time = 0.0
  let numberOfTimes = a:0 ? a:1 : 50000
  for i in range(numberOfTimes + 1)
    let t = reltime()
    execute a:com
    let time += reltime(t)[1]
    echo i.' / '.numberOfTimes
    redraw
  endfor
  echo 'Average time: '.string(numberOfTimes / i)
endfunction
```

```lua
function Time(com, numberOfTimes)
  numberOfTimes = numberOfTimes or 50000
  local totalTime = 0
  for i = 1, numberOfTimes do
    local startTime = vim.fn.reltime()
    vim.cmd(com)
    local elapsedTime = vim.fn.reltime(startTime)
    totalTime = totalTime + elapsedTime[1]
    print(string.format('%d / %d', i, numberOfTimes))
    vim.cmd('redraw')
  end
  print(string.format('Average time: %.6f', totalTime / numberOfTimes))
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Measure_time_taken_to_execute_a_command)
***
# Title: Recreate Vim Temporary File Directory
# Category: builtin_functions
# Tags: file-operations, temp-files, system-interaction
---
Programmatically recreate Vim's temporary file directory if it has been deleted, which can happen on long-running systems

```vim
:call mkdir(fnamemodify(tempname(),':h'),'p',0700)
```

```lua
vim.fn.mkdir(vim.fn.fnamemodify(vim.fn.tempname(), ':h'), 'p', 700)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Recreate_Tempfile_Directory)
***
# Title: Alternative Command Path Lookup in Vim
# Category: builtin_functions
# Tags: command-lookup, path-search
---
Search for command in system PATH using Vim's globpath function, works across different shell environments

```vim
:echo globpath(substitute($PATH, ':', ',', 'g'), 'cat')
```

```lua
-- Lua implementation of PATH search
local function find_in_path(cmd)
  local path = vim.env.PATH:gsub(':', ',')
  return vim.fn.globpath(path, cmd)
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Replace_selected_shell_command_with_full_path_when_editing_scripts)
***
# Title: Convert Numbers Between Hex and Decimal
# Category: builtin_functions
# Tags: conversion, number-manipulation, utility
---
Easily convert numbers between hexadecimal and decimal formats using built-in Vim/Neovim functions with flexible conversion methods

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
function _G.dec2hex(arg)
  return string.format('%x', tonumber(arg))
end

-- Convert hex to decimal
function _G.hex2dec(arg)
  arg = arg:lower():match('^0x') and arg or '0x' .. arg
  return tonumber(arg)
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip448)
***
# Title: Flexible External Command Processing with system()
# Category: builtin_functions
# Tags: shell-integration, scripting, text-manipulation
---
Demonstrates using system() function to capture and process command output safely in scripts, with proper argument escaping

```vim
function! GetDate(format)
  let format = empty(a:format) ? '+%A %Y-%m-%d %H:%M UTC' : a:format
  let cmd = '/bin/date -u ' . shellescape(format)
  let result = substitute(system(cmd), '[\]\'[[:cntrl:]]', '', 'g')
  call setline(line('.'), getline('.') . ' ' . result)
endfunction
```

```lua
function GetDate(format)
  local fmt = format == '' and '+%A %Y-%m-%d %H:%M UTC' or format
  local cmd = '/bin/date -u ' .. vim.fn.shellescape(fmt)
  local result = vim.fn.substitute(vim.fn.system(cmd), '[\]\'[[:cntrl:]]', '', 'g')
  vim.fn.setline('.', vim.fn.getline('.') .. ' ' .. result)
end

-- Optional mapping
vim.keymap.set('n', '<F8>', function() GetDate('') end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip467)
***
# Title: Generate a Customizable Calendar in Vim
# Category: builtin_functions
# Tags: calendar, date-management, custom-function
---
Create a flexible calendar generation function that outputs days, weeks, and months to a new buffer with customizable parameters

```vim
function! Calendar(year, month, day, weekday, week, daycount)
  new
  set buftype=nofile bufhidden=hide noswapfile
  " Function implementation to generate calendar days
  " Supports generating calendar for multiple days
endfunction

" Map to generate calendar for 1000 days
map <S-F7> :call Calendar(2002, 12, 30, 1, 1, 1000)<CR><CR>
```

```lua
function _G.generate_calendar(year, month, day, weekday, week, daycount)
  vim.cmd('new')
  vim.bo.buftype = 'nofile'
  vim.bo.bufhidden = 'hide'
  vim.bo.swapfile = false
  
  -- Lua implementation of calendar generation logic
  -- Similar structure to Vimscript version
end

-- Map to generate calendar
vim.keymap.set('n', '<S-F7>', function()
  _G.generate_calendar(2002, 12, 30, 1, 1, 1000)
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip560)
***
