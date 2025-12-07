# Title: Toggle invisible characters
# Category: Display
# Tags: invisible, characters, toggle
---
Use `:set list!` to toggle display of invisible characters (tabs, spaces, etc.).

```vim
" Vimscript:
:set list!  " toggle invisible characters
```
```lua
-- Lua:
vim.opt.list = not vim.opt.list:get()  -- toggle invisible characters
```

**Source:** Community contributed
***
# Title: Ex commands - folding display
# Category: Display
# Tags: ex, fold, display, column, text
---
Use `:set foldcolumn` to show fold column, `:set foldtext` for custom fold text, `:set fillchars` for fill characters.

```vim
" Vimscript:
:set foldcolumn=4     " show fold indicators in 4-char column
:set fillchars=fold:.,vert:|  " customize fill characters
:set foldtext=MyFoldText()    " custom fold text function
```
```lua
-- Lua:
vim.opt.foldcolumn = '4'  -- show fold indicators in 4-char column
vim.opt.fillchars = { fold = '.', vert = '|' }  -- customize fill characters
vim.opt.foldtext = 'v:lua.MyFoldText()'  -- custom fold text function
```

**Source:** Community contributed
***
# Title: Ex commands - status line and tabs
# Category: Display
# Tags: ex, status, line, tab, label
---
Use `:set laststatus` for status line, `:set showtabline` for tab line, `:set statusline` for custom status.

```vim
" Vimscript:
:set laststatus=2     " always show status line
:set showtabline=2    " always show tab line
:set statusline=%f\ %m%r%h%w\ [%Y]\ [%{&ff}]\ %=%l,%c\ %p%%
```
```lua
-- Lua:
vim.opt.laststatus = 2  -- always show status line
vim.opt.showtabline = 2  -- always show tab line
vim.opt.statusline = '%f %m%r%h%w [%Y] [%{&ff}] %=%l,%c %p%%'
```

**Source:** Community contributed
***
# Title: Conceal text with syntax highlighting
# Category: Display
# Tags: conceal, hide, text, syntax, conceallevel
---
Use `:set conceallevel=2` to hide concealed text and `:syntax match` with `conceal` to define what to hide.

```vim
" Vimscript:
:set conceallevel=2       " hide concealed text completely
:set conceallevel=0       " show all text normally
:syntax match htmlTag '<[^>]*>' conceal  " hide HTML tags
" Toggle conceal on/off
nnoremap <leader>c :let &conceallevel = (&conceallevel == 2) ? 0 : 2<CR>
```
```lua
-- Lua:
vim.opt.conceallevel = 2  -- hide concealed text completely
vim.opt.conceallevel = 0  -- show all text normally
vim.cmd('syntax match htmlTag \'<[^>]*>\' conceal')  -- hide HTML tags

-- Toggle conceal on/off
vim.keymap.set('n', '<leader>c', function()
  vim.opt.conceallevel = vim.opt.conceallevel:get() == 2 and 0 or 2
end, { desc = 'Toggle conceal' })
```

**Source:** Community contributed
***
# Title: Toggle Diff Highlighting in Merge Conflicts
# Category: display
# Tags: syntax-highlighting, diff-mode, ui
---
Add mappings to quickly disable diff syntax highlighting in one window, which can help reduce visual noise during three-way merges

```vim
" Example mapping to toggle diff highlighting
nnoremap <leader>dh :set nodiff<CR>
```
```lua
-- Lua equivalent for toggling diff highlighting
vim.keymap.set('n', '<leader>dh', function()
  vim.wo.diff = not vim.wo.diff
end, { desc = 'Toggle diff highlighting' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/A_better_Vimdiff_Git_mergetool)
***
# Title: Show ASCII/Unicode Value of Character
# Category: display
# Tags: character-info, unicode, status-line
---
Display the ASCII or Unicode value of the character under the cursor in decimal, hex, and octal formats

```vim
" Add to statusline to show character values
:set statusline=%<%f%h%m%r%=%b\ 0x%B\ \ %l,%c%V\ %P
:set laststatus=2
```
```lua
-- Configure status line to show character values
vim.opt.statusline = '%<%f%h%m%r%=%b 0x%B  %l,%c%V %P'
vim.opt.laststatus = 2
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Ascii_Value)
***
# Title: Get Character Value in Command Mode
# Category: display
# Tags: character-info, command-mode
---
Quickly view ASCII/Unicode value of the current character using built-in commands

```vim
" Use ga in normal mode
" Or :ascii/:as in command mode
```
```lua
-- These commands work the same in Neovim
-- Press 'ga' in normal mode
-- Or use :ascii or :as in command mode
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Ascii_Value)
***
# Title: Soft Line Wrapping
# Category: display
# Tags: text-display, ui, navigation
---
Enable soft line wrapping that displays long lines across multiple screen lines without changing the actual text

```vim
set wrap
set linebreak
```
```lua
vim.opt.wrap = true
vim.opt.linebreak = true

-- Use gj and gk to move by screen lines instead of real lines
vim.keymap.set('n', 'j', 'gj', { noremap = true })
vim.keymap.set('n', 'k', 'gk', { noremap = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Automatic_word_wrapping)
***
# Title: Dynamic Font Size Adjustment in GUI
# Category: display
# Tags: gui, font-size, key-mapping
---
Quickly change font size in GVim using function and key mappings for better readability

```vim
function! ScaleFontUp()
  let gf_size_whole = matchstr(&guifont, '\(\:h\)\@<=\d\+')
  let gf_size_frac = matchstr(&guifont, '\(\:h\d\+\.\)\@<=\d\=')
  let font_size = gf_size_whole * 10 + gf_size_frac
  let font_size = font_size + 5
  let gf_size_whole = font_size / 10
  let gf_size_frac = font_size - gf_size_whole * 10
  let new_font_size = ':h'.gf_size_whole.'.'.gf_size_frac.':'
  let &guifont = substitute(&guifont, '\:h.\{-}\:', new_font_size, '')
endfunction

function! ScaleFontDown()
  let gf_size_whole = matchstr(&guifont, '\(\:h\)\@<=\d\+')
  let gf_size_frac = matchstr(&guifont, '\(\:h\d\+\.\)\@<=\d\=')
  let font_size = gf_size_whole * 10 + gf_size_frac
  let font_size = font_size - 5
  let gf_size_whole = font_size / 10
  let gf_size_frac = font_size - gf_size_whole * 10
  let new_font_size = ':h'.gf_size_whole.'.'.gf_size_frac.':'
  let &guifont = substitute(&guifont, '\:h.\{-}\:', new_font_size, '')
endfunction

nmap <C-S-F11> :call ScaleFontDown()<CR>
nmap <C-S-F12> :call ScaleFontUp()<CR>
```
```lua
local function scale_font_up()
  local guifont = vim.o.guifont
  local current_size = tonumber(guifont:match(':h([%d.]+)'))
  local new_size = current_size and (current_size + 0.5) or 10
  vim.o.guifont = guifont:gsub(':h[%d.]+', ':h' .. string.format('%.1f', new_size))
end

local function scale_font_down()
  local guifont = vim.o.guifont
  local current_size = tonumber(guifont:match(':h([%d.]+)'))
  local new_size = current_size and (current_size - 0.5) or 10
  vim.o.guifont = guifont:gsub(':h[%d.]+', ':h' .. string.format('%.1f', new_size))
end

vim.keymap.set('n', '<C-S-F11>', scale_font_down, { desc = 'Decrease font size' })
vim.keymap.set('n', '<C-S-F12>', scale_font_up, { desc = 'Increase font size' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Change_guifont_to_see_more_of_your_file)
***
# Title: Toggle Cursor Line and Column Highlighting
# Category: display
# Tags: ui, cursor-highlight, visual-enhancement
---
Easily toggle highlighting of the current line and column to improve cursor visibility

```vim
" Highlight current line and column
:hi CursorLine   cterm=NONE ctermbg=darkred ctermfg=white guibg=darkred guifg=white
:hi CursorColumn cterm=NONE ctermbg=darkred ctermfg=white guibg=darkred guifg=white
:nnoremap <Leader>c :set cursorline! cursorcolumn!<CR>
```
```lua
-- Highlight current line and column
vim.cmd('hi CursorLine cterm=NONE ctermbg=darkred ctermfg=white guibg=darkred guifg=white')
vim.cmd('hi CursorColumn cterm=NONE ctermbg=darkred ctermfg=white guibg=darkred guifg=white')
vim.keymap.set('n', '<Leader>c', function()
  vim.o.cursorline = not vim.o.cursorline
  vim.o.cursorcolumn = not vim.o.cursorcolumn
end, { desc = 'Toggle cursor line and column highlight' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Color_active_line)
***
# Title: Customize PuTTY Colors for Vim Desert Scheme
# Category: display
# Tags: color-scheme, terminal, customization
---
Detailed guide for configuring PuTTY color palette to match Vim's desert color scheme, improving terminal syntax highlighting and readability

```vim
:colorscheme desert
```
```lua
vim.cmd('colorscheme desert')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Desert_color_scheme_with_Vim_in_PuTTY)
***
# Title: Smart Line Number and Column Display
# Category: display
# Tags: ui, line-numbers, configuration
---
Customize line number display width and behavior

```vim
set number
set numberwidth=4
```
```lua
vim.opt.number = true
vim.opt.numberwidth = 4
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Did_you_know)
***
# Title: Display Date and Time in Status Line
# Category: display
# Tags: status-line, time-display, configuration
---
Customize the status line to show current date and time, updating when you interact with the editor

```vim
set ruler
set rulerformat=%55(%{strftime('%a\ %b\ %e\ %I:%M\ %p')}\ %5l,%-6(%c%V%)\ %P%)
```
```lua
vim.opt.ruler = true
vim.opt.rulerformat = '%55(%{strftime("%a %b %e %I:%M %p")} %5l,%-6(%c%V%) %P%)'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Display_date-and-time_on_status_line)
***
# Title: Automatic Status Line Update with Timer
# Category: display
# Tags: status-line, timer, auto-update
---
Use Vim 8+ timers to automatically refresh the status line at regular intervals

```vim
let timer = timer_start(4000, 'UpdateStatusBar', {'repeat':-1})
function! UpdateStatusBar(timer)
  execute 'let &ro = &ro'
endfunction
```
```lua
local timer = vim.fn.timer_start(4000, function()
  vim.o.readonly = vim.o.readonly
end, {repeat = -1})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Display_date-and-time_on_status_line)
***
# Title: Relative Line Numbers for Easy Navigation
# Category: display
# Tags: navigation, ui, editing
---
Show relative line numbers to make movement and editing commands more intuitive

```vim
set relativenumber
set number
```
```lua
vim.opt.relativenumber = true
vim.opt.number = true
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Display_line_numbers)
***
# Title: Customize Line Number Appearance
# Category: display
# Tags: ui, configuration, theming
---
Customize the appearance of line numbers in the gutter

```vim
set numberwidth=3
highlight LineNr term=bold cterm=NONE ctermfg=DarkGrey ctermbg=NONE gui=NONE guifg=DarkGrey guibg=NONE
```
```lua
vim.opt.numberwidth = 3
vim.api.nvim_set_hl(0, 'LineNr', {
  fg = 'DarkGrey',
  bold = true
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Display_line_numbers)
***
# Title: Toggle Between Light and Dark Color Schemes
# Category: display
# Tags: color-scheme, key-mapping, theme-switching
---
Create a function to easily switch between two color scheme styles with a single keypress

```vim
function! s:SwitchPSCStyle()
  if exists('g:psc_style')
    if g:psc_style == 'cool'
      let g:psc_style = 'warm'
    elseif g:psc_style == 'warm'
      let g:psc_style = 'cool'
    endif
  else
    let g:psc_style = 'warm'
  endif
  colorscheme ps_color
endfunction
map <silent> <F6> :call <SID>SwitchPSCStyle()<CR>
```
```lua
local function switch_color_style()
  local style = vim.g.psc_style
  
  if style == nil then
    vim.g.psc_style = 'warm'
  elseif style == 'cool' then
    vim.g.psc_style = 'warm'
  elseif style == 'warm' then
    vim.g.psc_style = 'cool'
  end
  
  vim.cmd('colorscheme ps_color')
end

vim.keymap.set('n', '<F6>', switch_color_style, { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Easily_switch_between_two_styles_of_color_scheme)
***
# Title: Quickly Customize Syntax Highlighting Colors
# Category: display
# Tags: syntax-highlighting, color-scheme, customization
---
Easily modify specific syntax highlighting colors directly in your configuration without editing full color scheme files

```vim
highlight comment ctermfg=lightblue
highlight constant ctermfg=red
```
```lua
vim.cmd('highlight comment ctermfg=lightblue')
vim.cmd('highlight constant ctermfg=red')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Fine_tuning_syntax_colors)
***
# Title: Ignore Whitespace in Diff Mode
# Category: display
# Tags: diff, whitespace, comparison
---
Ignore whitespace changes when performing diff operations, reducing noise in comparisons

```vim
set diffopt+=iwhite
```
```lua
vim.opt.diffopt:append('iwhite')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Fix_error_E97_Cannot_create_diffs_under_Windows)
***
# Title: Truncate Long Echoed Messages
# Category: display
# Tags: messages, truncation, ui
---
Automatically shorten long messages in the command line to fit within the screen width

```vim
set shortmess+=T

" Function to safely echo truncated messages
function! ShortEcho(msg)
  let saved=&shortmess
  set shortmess+=T
  exe "norm :echomsg " . a:msg . "\n"
  let &shortmess=saved
endfunction
```
```lua
-- Enable message truncation
vim.opt.shortmess:append('T')

-- Function to safely echo truncated messages
function _G.short_echo(msg)
  local saved_shortmess = vim.o.shortmess
  vim.o.shortmess = vim.o.shortmess .. 'T'
  vim.cmd.norm({ args = {':echomsg ' .. msg .. '\n'} })
  vim.o.shortmess = saved_shortmess
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Get_shortened_messages_from_using_echomsg)
***
# Title: Screen Drawing and Color Output in Vim Scripts
# Category: display
# Tags: scripting, ui, colors
---
Techniques for creating colorful screen output and animations in Vim scripts using echo commands and highlighting

```vim
set nomore
let &ch=&lines-1

" Colored text output
echohl None
echon "xxxx"
echohl Visual
echon "yyyy"

while drawing
  redraw!
  " echo some lines
endwhile
let &ch=1
```
```lua
-- Disable 'more' prompts
vim.o.nomore = true

-- Set command height for drawing
vim.o.cmdheight = vim.o.lines - 1

-- Colored text output example
vim.cmd('echohl None')
vim.cmd('echon "xxxx"')
vim.cmd('echohl Visual')
vim.cmd('echon "yyyy"')

-- Screen drawing technique
for _ in ipairs(drawing_frames) do
  vim.cmd('redraw!')
  -- Draw frame
end

-- Reset command height
vim.o.cmdheight = 1
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Graphics_and_Drawing_in_vimscript)
***
# Title: Highlight Current Line and Column
# Category: display
# Tags: ui, cursor-highlight, navigation
---
Dynamically highlight the current line and column to improve cursor visibility and spatial awareness in large files

```vim
" Highlight current line and column
:hi CursorLine   cterm=NONE ctermbg=darkred ctermfg=white guibg=darkred guifg=white
:hi CursorColumn cterm=NONE ctermbg=darkred ctermfg=white guibg=darkred guifg=white
:nnoremap <Leader>c :set cursorline! cursorcolumn!<CR>
```
```lua
-- Highlight current line and column
vim.api.nvim_set_hl(0, 'CursorLine', { bg = 'darkred', fg = 'white' })
vim.api.nvim_set_hl(0, 'CursorColumn', { bg = 'darkred', fg = 'white' })
vim.keymap.set('n', '<Leader>c', function()
  vim.wo.cursorline = not vim.wo.cursorline
  vim.wo.cursorcolumn = not vim.wo.cursorcolumn
end, { desc = 'Toggle cursor line and column highlight' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Highlight_current_line)
***
# Title: Dynamic Cursor Line Highlighting After Jumps
# Category: display
# Tags: cursor-highlight, autocmd, navigation
---
Automatically highlight the cursor line after significant cursor jumps, making it easier to track cursor position in large files

```vim
function s:Cursor_Moved()
  let cur_pos = winline()
  if g:last_pos == 0
    set cul
    let g:last_pos = cur_pos
    return
  endif
  let diff = g:last_pos - cur_pos
  if diff > 1 || diff < -1
    set cul
  else
    set nocul
  endif
  let g:last_pos = cur_pos
endfunction
autocmd CursorMoved,CursorMovedI * call s:Cursor_Moved()
let g:last_pos = 0
```
```lua
local function cursor_moved()
  local cur_pos = vim.fn.winline()
  if vim.g.last_pos == 0 then
    vim.opt.cursorline = true
    vim.g.last_pos = cur_pos
    return
  end
  
  local diff = vim.g.last_pos - cur_pos
  if math.abs(diff) > 1 then
    vim.opt.cursorline = true
  else
    vim.opt.cursorline = false
  end
  
  vim.g.last_pos = cur_pos
end

vim.api.nvim_create_autocmd({'CursorMoved', 'CursorMovedI'}, {
  callback = cursor_moved
})

vim.g.last_pos = 0
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Highlight_cursor_line_after_cursor_jump)
***
# Title: Highlight Debug Blocks in C/C++ Code
# Category: display
# Tags: syntax-highlighting, debugging, code-visualization
---
Create custom syntax highlighting for debug blocks to easily distinguish and visually skip debug-related code sections

```vim
syn region MySkip contained start="^\s*#\s*\(if\>\|ifdef\>\|ifndef\>\)" skip="\\$" end="^\s*#\s*endif\>" contains=MySkip

let g:CommentDefines = ""

hi link MyCommentOut2 MyCommentOut
hi link MySkip MyCommentOut
hi link MyCommentOut Comment

map <silent> ,a :call AddCommentDefine()<CR>
map <silent> ,x :call ClearCommentDefine()<CR>

function! AddCommentDefine()
  let g:CommentDefines = "\\(" . expand("<cword>") . "\\)"
  syn clear MyCommentOut
  syn clear MyCommentOut2
  exe 'syn region MyCommentOut start="^\s*#\s*ifdef\s\+' . g:CommentDefines . '\>" end=".\|$" contains=MyCommentOut2'
  exe 'syn region MyCommentOut2 contained start="' . g:CommentDefines . '" end="^\s*#\s*\(endif\>\|else\>\|elif\>\)" contains=MySkip'
endfunction

function! ClearCommentDefine()
  let g:ClearCommentDefine = ""
  syn clear MyCommentOut
  syn clear MyCommentOut2
endfunction
```
```lua
vim.cmd[[
  augroup DebugHighlight
    autocmd!
    autocmd Syntax * syn region MySkip contained start="^\s*#\s*\(if\>\|ifdef\>\|ifndef\>\)" skip="\\$" end="^\s*#\s*endif\>" contains=MySkip
  augroup END

  hi link MyCommentOut2 MyCommentOut
  hi link MySkip MyCommentOut
  hi link MyCommentOut Comment
]]

-- Function to add comment define
function _G.add_comment_define()
  local word = vim.fn.expand('<cword>')
  vim.cmd('syn clear MyCommentOut')
  vim.cmd('syn clear MyCommentOut2')
  vim.cmd(string.format('syn region MyCommentOut start="^\s*#\s*ifdef\s\+%s\>" end=".\|$" contains=MyCommentOut2', word))
  vim.cmd(string.format('syn region MyCommentOut2 contained start="%s" end="^\s*#\s*\(endif\>\|else\>\|elif\>\)" contains=MySkip', word))
end

-- Function to clear comment define
function _G.clear_comment_define()
  vim.cmd('syn clear MyCommentOut')
  vim.cmd('syn clear MyCommentOut2')
end

-- Key mappings
vim.keymap.set('n', ',a', _G.add_comment_define, { desc = 'Add comment define' })
vim.keymap.set('n', ',x', _G.clear_comment_define, { desc = 'Clear comment define' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Highlight_debug_blocks_in_programs)
***
# Title: Highlight Lines Exceeding Length Limit
# Category: display
# Tags: highlighting, text-width, code-style
---
Automatically highlight lines that exceed a specified character width, helping maintain code readability and consistent formatting

```vim
:let w:m1=matchadd('Search', '\%<81v.\%>77v', -1)
:let w:m2=matchadd('ErrorMsg', '\%>80v.\+', -1)

" Automatically apply on buffer enter
:au BufWinEnter * let w:m1=matchadd('Search', '\%<81v.\%>77v', -1)
:au BufWinEnter * let w:m2=matchadd('ErrorMsg', '\%>80v.\+', -1)
```
```lua
-- Highlight lines exceeding 80 characters
vim.api.nvim_create_autocmd('BufWinEnter', {
  callback = function()
    vim.fn.matchadd('Search', '\%<81v.\%>77v', -1)
    vim.fn.matchadd('ErrorMsg', '\%>80v.\+', -1)
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Highlight_long_lines)
***
# Title: Highlight Multiple Words with Different Colors
# Category: display
# Tags: highlighting, search, visual-enhancement
---
Easily highlight multiple words in different colors across a document, with advanced search and management capabilities for word highlights

```vim
" Enable multiple word highlighting
" Toggle highlight mode
map <leader>m :call ToggleHighlight()<CR>

" Highlight current word
nnoremap <silent> <k1> :call HighlightWord(1)<CR>
```
```lua
-- Lua equivalent for multiple word highlighting
vim.keymap.set('n', '<leader>m', function()
  -- Toggle highlight mode
end, { desc = 'Toggle multiple word highlighting' })

vim.keymap.set('n', '<k1>', function()
  -- Highlight current word in first highlight group
end, { desc = 'Highlight current word' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Highlight_multiple_words)
***
# Title: Highlight Problematic Whitespace
# Category: display
# Tags: whitespace, syntax-highlighting, code-quality
---
Dynamically highlight various whitespace issues like trailing spaces, mixed indentation, and misplaced tabs to improve code cleanliness

```vim
function! ShowWhitespace(flags)
  let bad = ''
  let pat = []
  for c in split(a:flags, '\zs')
    if c == 'e'
      call add(pat, '\s\+$')
    elseif c == 'i'
      call add(pat, '^\t*\zs \+')
    elseif c == 's'
      call add(pat, ' \+\ze\t')
    elseif c == 't'
      call add(pat, '[^\t]\zs\t\+')
    else
      let bad .= c
    endif
  endfor
  if len(pat) > 0
    let s = join(pat, '\|')
    exec 'syntax match ExtraWhitespace "'.s.'" containedin=ALL'
  else
    syntax clear ExtraWhitespace
  endif
endfunction

nnoremap <Leader>ws :call ToggleShowWhitespace()<CR>
highlight ExtraWhitespace ctermbg=darkgreen guibg=darkgreen
```
```lua
local function show_whitespace(flags)
  local pat = {}
  local bad = ''
  
  for c in flags:gmatch('.') do
    if c == 'e' then
      table.insert(pat, '\s\+$')
    elseif c == 'i' then
      table.insert(pat, '^\t*\zs \+')
    elseif c == 's' then
      table.insert(pat, ' \+\ze\t')
    elseif c == 't' then
      table.insert(pat, '[^\t]\zs\t\+')
    else
      bad = bad .. c
    end
  end
  
  if #pat > 0 then
    local s = table.concat(pat, '\|')
    vim.cmd('syntax match ExtraWhitespace "' .. s .. '" containedin=ALL')
  else
    vim.cmd('syntax clear ExtraWhitespace')
  end
  
  if #bad > 0 then
    print('ShowWhitespace ignored: ' .. bad)
  end
end

vim.keymap.set('n', '<Leader>ws', function()
  vim.cmd('highlight ExtraWhitespace ctermbg=darkgreen guibg=darkgreen')
  show_whitespace('est')
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Highlight_some_whitespace_characters)
***
# Title: Highlight Unwanted Whitespace
# Category: display
# Tags: whitespace, highlighting, code-cleanup
---
Automatically highlight trailing spaces, spaces before tabs, and other problematic whitespace to maintain clean code

```vim
" Highlight trailing whitespace and spaces before tabs
autocmd ColorScheme * highlight ExtraWhitespace ctermbg=red guibg=red
match ExtraWhitespace /\s\+$\| \+\ze\t/

" Prevent highlighting during insert mode
autocmd InsertEnter * match ExtraWhitespace /\s\+\%#\@<!$/
autocmd InsertLeave * match ExtraWhitespace /\s\+$/
```
```lua
-- Highlight unwanted whitespace in Neovim
vim.api.nvim_create_augroup('WhitespaceHighlight', { clear = true })

vim.api.nvim_create_autocmd('ColorScheme', {
  group = 'WhitespaceHighlight',
  callback = function()
    vim.api.nvim_set_hl(0, 'ExtraWhitespace', { bg = 'red' })
  end
})

-- Match and highlight trailing whitespace
vim.api.nvim_create_autocmd({'InsertEnter', 'InsertLeave'}, {
  group = 'WhitespaceHighlight',
  pattern = '*',
  callback = function(ev)
    local hl_pattern = ev.event == 'InsertEnter' 
      and '\s\+\%#\@<!$' 
      or '\s\+$'
    vim.fn.matchadd('ExtraWhitespace', hl_pattern)
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Highlight_unwanted_spaces)
***
# Title: Show Whitespace with List Chars
# Category: display
# Tags: whitespace, visualization
---
Customize display of whitespace characters to make invisible characters visible

```vim
" Toggle list view and customize list characters
:set list listchars=tab:»·,trail:·,extends:>,precedes:<
```
```lua
-- Configure list characters in Neovim
vim.opt.list = true
vim.opt.listchars:append({
  tab = '»·',
  trail = '·',
  extends = '>',
  precedes = '<'
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Highlight_unwanted_spaces)
***
# Title: Highlight Long Lines
# Category: display
# Tags: syntax-highlighting, code-style, visual-guide
---
Visually highlight lines that exceed a specified length, helping maintain code readability and adherence to line length standards

```vim
highlight NearColLimit term=italic,bold cterm=italic ctermbg=yellow ctermfg=darkblue gui=bold,italic guibg=yellow guifg=darkblue
highlight OverColLimit term=inverse,bold cterm=bold ctermbg=red ctermfg=white gui=bold guibg=red guifg=white
syntax match NearColLimit /\%<81v.\%>77v/
syntax match OverColLimit /\%>80v.\+/
```
```lua
vim.cmd('highlight NearColLimit term=italic,bold cterm=italic ctermbg=yellow ctermfg=darkblue gui=bold,italic guibg=yellow guifg=darkblue')
vim.cmd('highlight OverColLimit term=inverse,bold cterm=bold ctermbg=red ctermfg=white gui=bold guibg=red guifg=white')
vim.cmd('syntax match NearColLimit /\%<81v.\%>77v/')
vim.cmd('syntax match OverColLimit /\%>80v.\+/')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Highlighting)
***
# Title: Quickly Highlight Current Line
# Category: display
# Tags: cursor-highlight, ui-enhancement, visual-guide
---
Add a simple mapping to highlight the current line, making it easier to track cursor position

```vim
highlight LineTooLong cterm=bold ctermbg=red guibg=LightYellow
match LineTooLong /\%>80v.\+/
```
```lua
vim.cmd('highlight LineTooLong cterm=bold ctermbg=red guibg=LightYellow')
vim.cmd('match LineTooLong /\%>80v.\+/')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Highlighting)
***
# Title: Highlight and Manage Unwanted Whitespace
# Category: display
# Tags: whitespace, highlighting, formatting
---
Easily identify and manage trailing whitespace, tabs, and inconsistent indentation across files

```vim
" Highlight trailing whitespace
autocmd ColorScheme * highlight ExtraWhitespace ctermbg=red guibg=red
match ExtraWhitespace /\s\+$/

" Prevent whitespace highlighting during insert mode
autocmd InsertEnter * match ExtraWhitespace /\s\+\%#\@<!$/
autocmd InsertLeave * match ExtraWhitespace /\s\+$/
```
```lua
local function setup_whitespace_highlight()
  vim.api.nvim_create_augroup('WhitespaceHighlight', { clear = true })
  
  vim.api.nvim_create_autocmd('ColorScheme', {
    group = 'WhitespaceHighlight',
    callback = function()
      vim.api.nvim_set_hl(0, 'ExtraWhitespace', { bg = 'red' })
    end
  })

  vim.api.nvim_create_autocmd('InsertEnter', {
    group = 'WhitespaceHighlight',
    pattern = '*',
    command = 'match ExtraWhitespace /\s\+\%#\@<!$/'
  })

  vim.api.nvim_create_autocmd('InsertLeave', {
    group = 'WhitespaceHighlight',
    pattern = '*',
    command = 'match ExtraWhitespace /\s\+$/'
  })
end

setup_whitespace_highlight()
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Highlighting_whitespaces_at_end_of_line)
***
# Title: Print with Line Numbers
# Category: display
# Tags: printing, configuration
---
Enable line numbers when printing without modifying the actual file

```vim
:set printoptions=number:y
```
```lua
vim.opt.printoptions = 'number:y'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Insert_line_numbers_2)
***
# Title: Center Cursor Vertically in Window
# Category: display
# Tags: scrolling, window-management, navigation
---
Dynamically keep the cursor centered vertically by setting scrolloff to half the window height, with a toggle function

```vim
" Toggle centered cursor
nnoremap <Leader>zz :let &scrolloff=999-&scrolloff<CR>

" Automatic centering autocmd
augroup VCenterCursor
  au!
  au BufEnter,WinEnter,WinNew,VimResized *,*.*
        \ let &scrolloff=winheight(win_getid())/2
augroup END
```
```lua
-- Toggle centered cursor
vim.keymap.set('n', '<Leader>zz', function()
  vim.o.scrolloff = 999 - vim.o.scrolloff
end, { desc = 'Toggle cursor centering' })

-- Automatic centering
vim.api.nvim_create_augroup('VCenterCursor', { clear = true })
vim.api.nvim_create_autocmd({'BufEnter', 'WinEnter', 'WinNew', 'VimResized'}, {
  group = 'VCenterCursor',
  pattern = {'*', '*.*'},
  callback = function()
    vim.o.scrolloff = math.floor(vim.api.nvim_win_get_height(0) / 2)
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Keep_your_cursor_centered_vertically_on_the_screen)
***
# Title: Force Redraw to Prevent Message Disappearance
# Category: display
# Tags: messages, redraw
---
Use :redraw to ensure messages are displayed and not overwritten by postponed redraws

```vim
:new | redraw | echo "there is a new window"
```
```lua
vim.cmd('new')
vim.cmd('redraw')
vim.api.nvim_echo({{'there is a new window', 'Normal'}}, false, {})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Make_echo_seen_when_it_would_otherwise_disappear_and_go_unseen)
***
# Title: Configure Scrolloff for Context
# Category: display
# Tags: scrolling, view-management, configuration
---
Set a minimum number of lines visible above and below the cursor to maintain context during navigation

```vim
" Ensure at least 5 lines of context around cursor
set scrolloff=5

" Keep cursor always centered
set scrolloff=999
```
```lua
-- Set minimum context lines around cursor
vim.opt.scrolloff = 5  -- 5 lines of context

-- Alternatively, keep cursor always centered
vim.opt.scrolloff = 999
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Make_search_results_appear_in_the_middle_of_the_screen)
***
# Title: Highlight Valid IP Addresses
# Category: display
# Tags: syntax-highlighting, regex, pattern-matching
---
Automatically highlight valid IP addresses in a file using a sophisticated regex pattern

```vim
syn match ipaddr /\(\(25\_[0-5]\|2\_[0-4]\_[0-9]\|\_[01]\?\_[0-9]\_[0-9]\?\)\.\)\{3\}\(25\_[0-5]\|2\_[0-4]\_[0-9]\|\_[01]\?\_[0-9]\_[0-9]\?\)/
hi link ipaddr Identifier
```
```lua
vim.cmd([[syn match ipaddr /\(\(25\[0-5]\|2\[0-4]\[0-9]\|\[01]?\[0-9]\[0-9]?\)\.\)\{3\}\(25\[0-5]\|2\[0-4]\[0-9]\|\[01]?\[0-9]\[0-9]?\)/]])
vim.cmd('hi link ipaddr Identifier')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Match_valid_IP_address)
***
# Title: Highlight Matching Braces
# Category: display
# Tags: ui, editing, visual-cues
---
Briefly highlight matching braces when typing to improve code readability and navigation

```vim
set showmatch
set matchtime=3  " Highlight for 300ms"
```
```lua
vim.opt.showmatch = true
vim.opt.matchtime = 3
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Matchit)
***
# Title: Highlight Cursor Line in Insert Mode
# Category: display
# Tags: mode-feedback, visual-cue, autocmd
---
Provides a visual indicator of insert mode by changing the cursor line background color

```vim
augroup InsertModeHighlight
    autocmd InsertEnter * highlight CursorLine ctermbg=17
    autocmd InsertLeave * highlight CursorLine ctermbg=none
augroup END
```
```lua
vim.api.nvim_create_augroup('InsertModeHighlight', { clear = true })

vim.api.nvim_create_autocmd('InsertEnter', {
    group = 'InsertModeHighlight',
    callback = function()
        vim.cmd('highlight CursorLine guibg=#000055')
    end
})

vim.api.nvim_create_autocmd('InsertLeave', {
    group = 'InsertModeHighlight',
    callback = function()
        vim.cmd('highlight CursorLine guibg=NONE')
    end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/More_visible_mode_feedback)
***
# Title: Improve Wrapped Line Handling
# Category: display
# Tags: text-display, line-wrapping, editor-config
---
Configure settings to improve text wrapping and display behavior for better readability

```vim
setlocal linebreak
setlocal nolist
setlocal display+=lastline
```
```lua
vim.opt.linebreak = true
vim.opt.list = false
vim.opt.display:append('lastline')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Move_through_wrapped_lines)
***
# Title: Highlight Multiple Words in Different Colors
# Category: display
# Tags: search, highlighting, visual-enhancement
---
Easily highlight multiple words with different colors in a single buffer, allowing for quick visual pattern recognition and search navigation

```vim
" Toggle highlight mapping
map <leader>m :call ToggleHighlightMapping()<CR>

" Highlight word under cursor
" Use numeric keypad 1-9 to highlight with different colors
```
```lua
-- Example implementation in Lua
-- Note: Full conversion would require custom function
vim.keymap.set('n', '<leader>m', function()
  -- Toggle highlight mapping logic
end, { desc = 'Toggle multiple word highlighting' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Multiple_Hilighted_Search)
***
# Title: Dynamic Color Scheme Switcher
# Category: display
# Tags: color-schemes, ui, customization
---
Easily cycle through color schemes using keyboard shortcuts, with options to select specific color schemes or use all installed schemes

```vim
" Color scheme switching script
nnoremap <F8> :call NextColor(1)<CR>
nnoremap <S-F8> :call NextColor(-1)<CR>
nnoremap <A-F8> :call NextColor(0)<CR>

" Set color schemes dynamically
:SetColors all     " Use all installed color schemes
:SetColors my      " Use predefined color schemes
:SetColors blue slate ron  " Use specific color schemes
```
```lua
-- Lua equivalent for color scheme switching
vim.keymap.set('n', '<F8>', function()
  vim.cmd('call NextColor(1)')
end, { desc = 'Next color scheme' })

vim.keymap.set('n', '<S-F8>', function()
  vim.cmd('call NextColor(-1)')
end, { desc = 'Previous color scheme' })

vim.keymap.set('n', '<A-F8>', function()
  vim.cmd('call NextColor(0)')
end, { desc = 'Random color scheme' })

-- Use :SetColors command as in Vimscript
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/One_page_summary_of_color_schemes)
***
# Title: Print Syntax Highlighted Buffer in Black and White
# Category: display
# Tags: printing, syntax-highlighting, color-scheme
---
Create a mapping to print syntax-highlighted code in black and white, preserving original syntax highlighting while printing

```vim
map <C-p> :color print_bw<CR>:hardcopy<CR>:color sean<CR>:syn on<CR>
```
```lua
vim.keymap.set('n', '<C-p>', function()
  vim.cmd('color print_bw')
  vim.cmd('hardcopy')
  vim.cmd('color sean')  -- Replace with your color scheme
  vim.cmd('syn on')
end, { desc = 'Print buffer in black and white' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Print_syntax_highlighted_buffer_in_one_color)
***
# Title: Custom Syntax Highlighting for Printing
# Category: display
# Tags: printing, syntax-highlighting, customization
---
Create a separate color scheme for printing that differs from screen display, allowing unique formatting for printed documents

```vim
command! -nargs=* Hardcopy call DoMyPrint('<args>')

function DoMyPrint(args)
  let colorsave=g:colors_name
  color print
  exec 'hardcopy '.a:args
  exec 'color '.colorsave
endfunction
```
```lua
vim.api.nvim_create_user_command('Hardcopy', function(opts)
  local current_colorscheme = vim.g.colors_name
  vim.cmd('colorscheme print')
  vim.cmd('hardcopy ' .. (opts.args or ''))
  vim.cmd('colorscheme ' .. current_colorscheme)
end, { nargs = '*' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Printing_with_syntax_highlighting_independent_of_your_normal_highlighting)
***
# Title: Visually Highlight Unwanted Whitespace
# Category: display
# Tags: whitespace, visual-cues, formatting
---
Configure Vim to display whitespace characters, making trailing or problematic spaces visible

```vim
set list listchars=tab:»·,trail:·
" Alternative style
set list lcs=tab:·⁖,trail:¶
```
```lua
vim.opt.list = true
vim.opt.listchars:append({
  tab = '»·',
  trail = '·'
})

-- Alternative style
vim.opt.listchars:append({
  tab = '·⁖',
  trail = '¶'
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Remove_trailing_spaces)
***
# Title: Visualize Tab Characters in Vim
# Category: display
# Tags: whitespace, formatting, visual-guide
---
Show tab characters as vertical lines or symbols to help understand indentation and whitespace

```vim
" Show tabs as vertical lines
set list
set listchars=tab:\|\ 

" Alternative for newer Vim versions
set listchars=tab:>-
```
```lua
-- Show tabs as vertical lines
vim.opt.list = true
vim.opt.listchars:append({ tab = '| ' })

-- Alternative style
vim.opt.listchars:append({ tab = '>-' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip460)
***
# Title: Toggle Tab Visualization Function
# Category: display
# Tags: toggle, visualization, whitespace
---
Create a toggle function to switch between showing and hiding tab characters with custom highlighting

```vim
function! SeeTab()
  if !exists("g:SeeTabEnabled")
    let g:SeeTabEnabled = 1
    set list
    set listchars=tab:\|
    highlight SpecialKey guifg=black guibg=magenta
  else
    set nolist
    unlet g:SeeTabEnabled
  endif
endfunction
command! SeeTab call SeeTab()
```
```lua
local function see_tab()
  if not vim.g.see_tab_enabled then
    vim.g.see_tab_enabled = true
    vim.opt.list = true
    vim.opt.listchars:append({ tab = '| ' })
    vim.cmd('highlight SpecialKey guifg=black guibg=magenta')
  else
    vim.opt.list = false
    vim.g.see_tab_enabled = nil
  end
end

vim.api.nvim_create_user_command('SeeTab', see_tab, {})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip460)
***
# Title: Customize GVim Colors to Match Console Vim
# Category: display
# Tags: color-scheme, gui-colors, theme
---
Customize GVim colors to match console Vim's color palette, providing a consistent visual experience across different Vim interfaces

```vim
set background=dark
hi SpecialKey guifg=Blue
hi Normal guifg=Gray guibg=Black
hi Comment guifg=Cyan
hi Constant guifg=Magenta
hi Statement guifg=Yellow
```
```lua
vim.o.background = 'dark'

-- Custom highlight groups
vim.api.nvim_set_hl(0, 'SpecialKey', { fg = 'Blue' })
vim.api.nvim_set_hl(0, 'Normal', { fg = 'Gray', bg = 'Black' })
vim.api.nvim_set_hl(0, 'Comment', { fg = 'Cyan' })
vim.api.nvim_set_hl(0, 'Constant', { fg = 'Magenta' })
vim.api.nvim_set_hl(0, 'Statement', { fg = 'Yellow' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip527)
***
# Title: Quick Background Color Toggle
# Category: display
# Tags: color-scheme, ui-customization, theme
---
Easily switch between light and dark backgrounds with a single keymap

```vim
map <F11> :let &background = ( &background == "dark"? "light" : "dark" )<CR>
```
```lua
vim.keymap.set('n', '<F11>', function()
  vim.o.background = vim.o.background == 'dark' and 'light' or 'dark'
end, { desc = 'Toggle background color' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip53)
***
# Title: Custom Syntax Highlighting Colors
# Category: display
# Tags: syntax-highlighting, color-customization
---
Modify specific syntax highlighting colors for comments, search results, and error messages

```vim
hi Comment ctermfg=DarkGrey guifg=DarkGrey
hi Search guibg=LightBlue
highlight ErrorMsg guibg=White guifg=Red
```
```lua
vim.cmd('hi Comment ctermfg=DarkGrey guifg=DarkGrey')
vim.cmd('hi Search guibg=LightBlue')
vim.cmd('highlight ErrorMsg guibg=White guifg=Red')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip53)
***
# Title: View and Test Available Colors in Vim/Neovim
# Category: display
# Tags: colors, colorscheme, testing
---
Script to generate a comprehensive view of available colors, helping users explore and select color schemes interactively

```vim
" Script to display all named colors in rgb.txt
new
setlocal buftype=nofile bufhidden=hide noswapfile
0read $VIMRUNTIME/rgb.txt
" Filter and process color names
silent execute 'v/'.find_color.'/d'
silent g/grey/d
```
```lua
-- Lua equivalent for color exploration
local function show_colors()
  local colors = vim.fn.readfile(vim.fn.expand('$VIMRUNTIME/rgb.txt'))
  local filtered_colors = vim.tbl_filter(function(color)
    return color:match('^%s*%d+%s*%d+%s*%d+%s*%w+$') and not color:match('grey')
  end, colors)
  
  local buf = vim.api.nvim_create_buf(true, true)
  vim.api.nvim_buf_set_lines(buf, 0, -1, false, filtered_colors)
  vim.api.nvim_set_current_buf(buf)
end

-- Call with :lua ShowColors()
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip634)
***
# Title: Dynamic Color Testing Across Terminal and GUI
# Category: display
# Tags: colors, testing, terminal
---
Generate color test scripts for both console and GUI Vim, allowing comprehensive color visualization

```vim
function! VimColorTest(outfile, fgend, bgend)
  let result = []
  for fg in range(a:fgend)
    for bg in range(a:bgend)
      let kw = printf('%-7s', printf('c_%d_%d', fg, bg))
      let h = printf('hi %s ctermfg=%d ctermbg=%d', kw, fg, bg)
      let s = printf('syn keyword %s %s', kw, kw)
      call add(result, printf('%-32s | %s', h, s))
    endfor
  endfor
  call writefile(result, a:outfile)
  execute 'edit '.a:outfile
  source %
endfunction
```
```lua
function _G.color_test(outfile, fgend, bgend)
  local result = {}
  for fg = 0, fgend - 1 do
    for bg = 0, bgend - 1 do
      local kw = string.format('c_%d_%d', fg, bg)
      local h = string.format('hi %s ctermfg=%d ctermbg=%d', kw, fg, bg)
      local s = string.format('syn keyword %s %s', kw, kw)
      table.insert(result, string.format('%-32s | %s', h, s))
    end
  end
  
  vim.fn.writefile(result, outfile)
  vim.cmd('edit ' .. outfile)
  vim.cmd('source %')
end

-- Usage: :lua color_test('colortest.txt', 16, 16)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip634)
***
# Title: Display Character ASCII/Unicode Value
# Category: display
# Tags: character-info, unicode, status-line
---
Show the ASCII or Unicode value of the current character in the status line, which helps with encoding and character analysis

```vim
set statusline=%<%f%h%m%r%=%b\ 0x%B\ \ %l,%c%V\ %P
set laststatus=2
```
```lua
vim.opt.statusline = '%<%f%h%m%r%=%b 0x%B  %l,%c%V %P'
vim.opt.laststatus = 2
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip67)
***
# Title: Get Character Information Quickly
# Category: display
# Tags: character-info, unicode, command-mode
---
Use built-in commands to quickly retrieve ASCII/Unicode values of the current character in decimal, hex, and octal formats

```vim
" In command mode, press ga
" Or use :ascii command
```
```lua
-- In command mode, press ga
-- Or use :ascii command
-- Neovim inherits these Vim commands directly
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip67)
***
# Title: Conditionally Set Command Height
# Category: display
# Tags: ui, startup-configuration
---
Automatically increase command height to prevent 'Hit-Enter' prompts

```vim
if &cmdheight == 1
  set cmdheight=2
endif
```
```lua
if vim.o.cmdheight == 1 then
  vim.o.cmdheight = 2
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip680)
***
# Title: Quick Syntax Color Customization
# Category: display
# Tags: syntax-highlighting, color-scheme, customization
---
Easily modify specific syntax highlight colors directly in your vimrc without editing full color scheme files

```vim
highlight comment ctermfg=lightblue
highlight constant ctermfg=red
```
```lua
vim.cmd('highlight comment ctermfg=lightblue')
vim.cmd('highlight constant ctermfg=red')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip737)
***
# Title: Highlight Code Between Matching Curly Braces
# Category: display
# Tags: syntax-highlighting, code-navigation
---
Automatically highlight the code section between matching curly braces to help identify code blocks and prevent errors

```vim
highlight ShowMatches guibg=darkgrey guifg=white
au! Cursorhold * exe 'match ShowMatches /\v%(%#\{%(%(\....))/'
set ut=30
```
```lua
-- Lua equivalent for highlighting matching braces
vim.api.nvim_create_autocmd('CursorHold', {
  callback = function()
    vim.fn.matchadd('ShowMatches', '\v%(%#\{%(%(\....))/)
  end
})

vim.api.nvim_set_hl(0, 'ShowMatches', { bg = 'darkgrey', fg = 'white' })
vim.o.updatetime = 30
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip754)
***
# Title: Improve Long Line Readability
# Category: display
# Tags: wrapping, line-display, readability
---
Configure Vim/Neovim to handle long lines more gracefully with improved wrapping and display settings

```vim
" Settings for better long line handling
set wrap
set linebreak
set display+=lastline
set scrolloff=99999
```
```lua
-- Settings for better long line handling
vim.opt.wrap = true
vim.opt.linebreak = true
vim.opt.display:append('lastline')
vim.opt.scrolloff = 99999
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Working_with_long_lines)
***
