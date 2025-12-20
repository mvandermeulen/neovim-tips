# Title: Window navigation basics
# Category: Window Management
# Tags: window, navigation, movement
---
Use `Ctrl+w h/j/k/l` to move to left/down/up/right windows, `Ctrl+w w` to cycle through windows, `Ctrl+w p` for previous window.

```vim
Ctrl+w h  " move to left window
Ctrl+w j  " move to window below
Ctrl+w k  " move to window above
Ctrl+w l  " move to right window
Ctrl+w w  " cycle to next window
Ctrl+w p  " go to previous window
```

**Source:** Community contributed
***
# Title: Window closing
# Category: Window Management
# Tags: window, close, quit
---
Use `Ctrl+w c` to close current window, `Ctrl+w o` to close all windows except current, `Ctrl+w q` to quit current window.

```vim
Ctrl+w c  " close current window
Ctrl+w o  " close all other windows
Ctrl+w q  " quit current window
```

**Source:** Community contributed
***
# Title: Window position navigation
# Category: Window Management
# Tags: window, position, navigation
---
Use `Ctrl+w t` to go to top window and `Ctrl+w b` to go to bottom window.

```vim
Ctrl+w t  " go to top window
Ctrl+w b  " go to bottom window
```

**Source:** Community contributed
***
# Title: Special window commands
# Category: Window Management
# Tags: window, special, file, tag
---
Use `Ctrl+w T` to move current window to a new tab page.

```vim
Ctrl+w T  " move current window to new tab
```

**Source:** Community contributed
***
# Title: Move windows
# Category: Window Management
# Tags: window, move, position
---
Use `Ctrl+w H/J/K/L` to move current window to far left/bottom/top/right.

```vim
Ctrl+w H  " move window to far left
Ctrl+w J  " move window to bottom
Ctrl+w K  " move window to top  
Ctrl+w L  " move window to far right
```

**Source:** Community contributed
***
# Title: Better gm command
# Category: Window Management
# Tags: cursor, middle, navigation, movement
---
Improved gm command that moves cursor to the middle of the physical line, ignoring whitespace.

```vim
" Vimscript:
function! s:Gm()
  execute 'normal! ^'
  let first_col = virtcol('.')
  execute 'normal! g_'
  let last_col  = virtcol('.')
  execute 'normal! ' . (first_col + last_col) / 2 . '|'
endfunction
nnoremap <silent> gm :call <SID>Gm()<CR>
onoremap <silent> gm :call <SID>Gm()<CR>
```

```lua
-- Lua:
local function better_gm()
  vim.cmd('normal! ^')
  local first_col = vim.fn.virtcol('.')
  vim.cmd('normal! g_')
  local last_col = vim.fn.virtcol('.')
  vim.cmd('normal! ' .. math.floor((first_col + last_col) / 2) .. '|')
end

vim.keymap.set('n', 'gm', better_gm, { silent = true, desc = 'Go to middle of line' })
vim.keymap.set('o', 'gm', better_gm, { silent = true, desc = 'Go to middle of line' })
```

**Source:** Community contributed
***
# Title: Keep cursor centered
# Category: Window Management
# Tags: cursor, center, scroll, display
---
Keep cursor centered vertically on screen for better visibility while editing.

```vim
" Vimscript:
" Keep cursor centered when scrolling
nnoremap <C-d> <C-d>zz
nnoremap <C-u> <C-u>zz
nnoremap n nzz
nnoremap N Nzz

" Or automatic centering
set scrolloff=999
```

```lua
-- Lua:
-- Keep cursor centered when scrolling
vim.keymap.set('n', '<C-d>', '<C-d>zz', { desc = 'Scroll down and center' })
vim.keymap.set('n', '<C-u>', '<C-u>zz', { desc = 'Scroll up and center' })
vim.keymap.set('n', 'n', 'nzz', { desc = 'Next search result and center' })
vim.keymap.set('n', 'N', 'Nzz', { desc = 'Previous search result and center' })

-- Or automatic centering
vim.opt.scrolloff = 999
```

**Source:** Community contributed
***
# Title: Change cursor shape in modes
# Category: Window Management
# Tags: cursor, shape, mode, visual
---
Configure different cursor shapes for different modes to provide visual feedback.

```vim
" Vimscript:
set guicursor=n-v-c:block,i-ci-ve:ver25,r-cr:hor20,o:hor50
" Block in normal, vertical bar in insert, horizontal in replace
```

```lua
-- Lua:
vim.opt.guicursor = 'n-v-c:block,i-ci-ve:ver25,r-cr:hor20,o:hor50'
-- Block in normal, vertical bar in insert, horizontal in replace
```

**Source:** Community contributed
***
# Title: Keep window when closing buffer
# Category: Window Management
# Tags: buffer, close, window, preserve
---
Use tabs as workspaces to organize different projects or contexts.

```vim
:tabnew         " create new tab
:tabclose       " close current tab
:tabonly        " close all other tabs
:tabn           " next tab
:tabp           " previous tab
gt              " next tab (normal mode)
gT              " previous tab (normal mode)
:tab split      " open current buffer in new tab
```

**Source:** Community contributed
***
# Title: Focus mode for writing
# Category: Window Management
# Tags: focus, writing, distraction, zen
---
Create a distraction-free environment for writing and focused editing.

```vim
" Simple focus mode
:set laststatus=0     " hide statusline
:set nonumber         " hide line numbers
:set norelativenumber " hide relative numbers
:set signcolumn=no    " hide sign column

" Toggle function
function! ToggleFocusMode()
  if &laststatus == 2
    set laststatus=0 nonumber norelativenumber signcolumn=no
  else
    set laststatus=2 number relativenumber signcolumn=yes
  endif
endfunction
nnoremap <F12> :call ToggleFocusMode()<CR>
```

**Source:** Community contributed
***
# Title: Quick file explorer
# Category: Window Management
# Tags: explorer, netrw, files, browse
---
Use `:only` or `:on` to close all windows except the current one, making it take up the full screen.

```vim
:only   " close all other windows (keep current)
:on     " short form of :only
Ctrl+w o " normal mode shortcut for :only
```

**Source:** Community contributed
***
# Title: Window commands from Ex mode
# Category: Window Management
# Tags: wincmd, window, command, ex, mode
---
Use `:wincmd {key}` to execute window commands from Ex mode, useful in scripts and mappings.

```vim
:wincmd j     " same as Ctrl+w j (move to window below)
:wincmd =     " same as Ctrl+w = (equalize windows)
:wincmd o     " same as Ctrl+w o (close other windows)
:wincmd v     " same as Ctrl+w v (vertical split)
:wincmd s     " same as Ctrl+w s (horizontal split)
```

**Source:** Community contributed
***
# Title: Smart window navigation keymaps
# Category: Window Management
# Tags: navigation, keymap, window, split, lua
---
Create intuitive window navigation keymaps using Ctrl+hjkl for seamless movement between splits.

```lua
-- Simple window navigation with Ctrl+hjkl:
vim.keymap.set('n', '<C-h>', '<C-w>h', { desc = 'Move to left window' })
vim.keymap.set('n', '<C-j>', '<C-w>j', { desc = 'Move to window below' })
vim.keymap.set('n', '<C-k>', '<C-w>k', { desc = 'Move to window above' })
vim.keymap.set('n', '<C-l>', '<C-w>l', { desc = 'Move to right window' })

-- Window resizing with arrow keys:
vim.keymap.set('n', '<C-Up>', ':resize +2<CR>', { desc = 'Increase window height' })
vim.keymap.set('n', '<C-Down>', ':resize -2<CR>', { desc = 'Decrease window height' })
vim.keymap.set('n', '<C-Left>', ':vertical resize -2<CR>', { desc = 'Decrease window width' })
vim.keymap.set('n', '<C-Right>', ':vertical resize +2<CR>', { desc = 'Increase window width' })

-- Quick window management:
vim.keymap.set('n', '<leader>wv', '<C-w>v', { desc = 'Split window vertically' })
vim.keymap.set('n', '<leader>ws', '<C-w>s', { desc = 'Split window horizontally' })
vim.keymap.set('n', '<leader>wq', '<C-w>q', { desc = 'Close current window' })
vim.keymap.set('n', '<leader>wo', '<C-w>o', { desc = 'Close other windows' })
```

**Source:** Community contributed
***
# Title: Keep Quickfix Window at Fixed Height
# Category: window_management
# Tags: autocmd, quickfix, window-resize
---
Automatically maintain a consistent quickfix window height across window switches, useful for debugging and error navigation

```vim
function MaximizeAndResizeQuickfix(quickfixHeight)
  set lazyredraw
  set ei=WinEnter
  wincmd _
  if (getbufvar(winbufnr(winnr()), "&buftype") == "quickfix")
    wincmd p
    resize
    wincmd p
    exe "resize " . a:quickfixHeight
  endif
  set ei-=WinEnter
  set nolazyredraw
endfunction

au WinEnter * call MaximizeAndResizeQuickfix(8)
```

```lua
local function maximize_and_resize_quickfix(quickfix_height)
  vim.o.lazyredraw = true
  vim.o.eventignore = 'WinEnter'
  vim.cmd('wincmd _')
  
  if vim.bo.buftype == 'quickfix' then
    vim.cmd('wincmd p')
    vim.cmd('resize')
    vim.cmd('wincmd p')
    vim.cmd('resize ' .. quickfix_height)
  end
  
  vim.o.eventignore = ''
  vim.o.lazyredraw = false
end

vim.api.nvim_create_autocmd('WinEnter', {
  callback = function() maximize_and_resize_quickfix(8) end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Always_keep_quickfix_window_at_specified_height)
***
# Title: Dynamically Resize Quickfix Window Height
# Category: window_management
# Tags: quickfix, window-resize, autocmd
---
Automatically adjust quickfix window height to fit contents, with min and max limits

```vim
au FileType qf call AdjustWindowHeight(3, 10)
function! AdjustWindowHeight(minheight, maxheight)
  exe max([min([line("$"), a:maxheight]), a:minheight]) . "wincmd _"
endfunction
```

```lua
vim.api.nvim_create_autocmd('FileType', {
  pattern = 'qf',
  callback = function()
    local last_line = vim.fn.line('$')
    local height = math.max(math.min(last_line, 10), 3)
    vim.cmd(height .. 'wincmd _')
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Automatically_fitting_a_quickfix_window_height)
***
# Title: Maximize Vim Window Size in KDE
# Category: window_management
# Tags: window-size, kde, gui
---
Set exact window lines and columns to achieve maximization in KDE using .gvimrc

```vim
set lines=999 columns=999
```

```lua
vim.opt.lines = 999
vim.opt.columns = 999
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Automatically_maximizing_gvim_in_KDE)
***
# Title: Buffer Split Management
# Category: window_management
# Tags: splits, buffers, window-navigation
---
Create and navigate buffer splits with flexible positioning

```vim
:split
:vsplit
:vertical sb 3
Ctrl-W hjkl
```

```lua
-- Create splits
vim.cmd('split')  -- Horizontal split
vim.cmd('vsplit')  -- Vertical split

-- Navigate splits
vim.keymap.set('n', '<C-w>h', '<C-w>h', { desc = 'Move to left split' })
vim.keymap.set('n', '<C-w>j', '<C-w>j', { desc = 'Move to bottom split' })
vim.keymap.set('n', '<C-w>k', '<C-w>k', { desc = 'Move to top split' })
vim.keymap.set('n', '<C-w>l', '<C-w>l', { desc = 'Move to right split' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Buffer)
***
# Title: Customize GVim Popup Menu for Window Management
# Category: window_management
# Tags: mouse, popup-menu, window-control
---
Add custom menu options to close windows directly from the right-click popup menu in GVim

```vim
:set mousemodel=popup
:amenu PopUp.Close.Window :confirm close<CR>
:amenu PopUp.Close.Other :confirm only<CR>
```

```lua
-- Set mouse model for popup menu
vim.opt.mousemodel = 'popup'

-- Add menu items for closing windows
vim.cmd('amenu PopUp.Close.Window :confirm close<CR>')
vim.cmd('amenu PopUp.Close.Other :confirm only<CR>')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Close_windows_from_gvim_popup_menu)
***
# Title: Control New Window Split Position
# Category: window_management
# Tags: splits, window-layout, configuration
---
Quickly resize vertical windows by moving focus and expanding width with custom keymaps

```vim
" Resize vertical windows with Ctrl-h and Ctrl-l
nmap <c-h> <c-w>h<c-w>_<c-w>><c-w>>
nmap <c-l> <c-w>l<c-w>_<c-w>><c-w>>
```

```lua
-- Resize vertical windows dynamically
vim.keymap.set('n', '<C-h>', '<C-w>h<C-w>_<C-w>><C-w>>', { desc = 'Resize window left' })
vim.keymap.set('n', '<C-l>', '<C-w>l<C-w>_<C-w>><C-w>>', { desc = 'Resize window right' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Custom_resizing_on_the_spot)
***
# Title: Use Window-Local Variables for Initialization
# Category: window_management
# Tags: variables, window-local, initialization
---
Demonstrates how to use window-local variables to track and manage window-specific settings

```vim
" Create an augroup for window initialization
augroup WindowInit
  au!
  autocmd VimEnter * let w:created=1
augroup END
```

```lua
-- Create an augroup for window initialization
local window_init_group = vim.api.nvim_create_augroup('WindowInit', { clear = true })
vim.api.nvim_create_autocmd('VimEnter', {
  group = window_init_group,
  callback = function()
    vim.w.created = true
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Detect_window_creation_with_WinEnter)
***
# Title: Easily Compare Two Files in Vim/Neovim
# Category: window_management
# Tags: diff-mode, file-comparison, window-split
---
Quick methods to compare two files side by side using built-in diff commands

```vim
" Method 1: Split and diff two files
:sp <filename>
:windo diffthis

" Method 2: Vertical split with diff
:vert diffsplit <filename>
```

```lua
-- Method 1: Split and diff two files
vim.cmd('sp ' .. filename)
vim.cmd('windo diffthis')

-- Method 2: Vertical split with diff
vim.cmd('vert diffsplit ' .. filename)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Diff_the_current_buffer_with_another_file)
***
# Title: Easily Turn Off Diff Mode
# Category: window_management
# Tags: diff-mode, window-management, buffer-reset
---
Quickly disable diff mode across all windows without closing buffers

```vim
" Switch off diff mode for all windows
command! DiffOff call DiffOff()
function! DiffOff()
  windo set nodiff
  windo set noscrollbind
  windo set foldmethod=manual
  windo set foldcolumn=0
  windo unlet! b:did_ftplugin | let &filetype = &filetype
endfunction
```

```lua
-- Switch off diff mode for all windows
vim.api.nvim_create_user_command('DiffOff', function()
  for _, win in ipairs(vim.api.nvim_list_wins()) do
    vim.api.nvim_win_call(win, function()
      vim.wo.diff = false
      vim.wo.scrollbind = false
      vim.wo.foldmethod = 'manual'
      vim.wo.foldcolumn = '0'
    end)
  end
end, {})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Diff_the_current_buffer_with_another_file)
***
# Title: Open Multiple Files in New Windows
# Category: window_management
# Tags: file-operations, custom-commands, window-splitting
---
Create custom commands to open multiple files in new windows, supporting glob patterns and flexible file selection

```vim
command! -nargs=* -complete=file New call Foreach( "new %% ", <f-args> )
command! -nargs=* -complete=file Vnew call Foreach( "vnew %% ", <f-args> )

function! Foreach( ... )
  let cmd = a:1
  let fnames = []
  for i in range( 1, a:0 - 1 )
    let l = split( glob( a:000[i] ), "\n" )
    if len( l ) < 1
      let l = [ a:000[i] ]
    endif
    call extend( fnames, l )
  endfor
  for fname in fnames
    let cmd1 = substitute( cmd, '%%', fname, 'g' )
    exe cmd1
  endfor
endfunction
```

```lua
local function foreach(cmd, ...)
  local fnames = {}
  for _, pattern in ipairs({...}) do
    local files = vim.fn.glob(pattern, false, true)
    if #files == 0 then
      table.insert(files, pattern)
    end
    vim.list_extend(fnames, files)
  end

  for _, fname in ipairs(fnames) do
    local exec_cmd = cmd:gsub('%%', fname)
    vim.cmd(exec_cmd)
  end
end

vim.api.nvim_create_user_command('New', function(opts)
  foreach('new ' .. opts.args, unpack(opts.fargs))
end, { nargs = '*', complete = 'file' })

vim.api.nvim_create_user_command('Vnew', function(opts)
  foreach('vnew ' .. opts.args, unpack(opts.fargs))
end, { nargs = '*', complete = 'file' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Execute_command_on_each_file_in_a_list)
***
# Title: Execute SQL Queries in Split Window
# Category: window_management
# Tags: sql, external-commands, productivity
---
Execute SQL queries from Vim and display results in a split window, allowing seamless database interaction without leaving the editor

```vim
au FileType sql map <F12> <C-W><C-O>:silent w !isql -SYourServerName -DYourDatabaseName -UYourUserName -PYourPassword > tmpsqlresult.txt<CR>:split tmpsqlresult.txt<CR>
```

```lua
vim.api.nvim_create_autocmd('FileType', {
  pattern = 'sql',
  callback = function()
    vim.keymap.set('n', '<F12>', function()
      vim.cmd('silent w !isql -SYourServerName -DYourDatabaseName -UYourUserName -PYourPassword > tmpsqlresult.txt')
      vim.cmd('split tmpsqlresult.txt')
    end, { buffer = true })
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Execute_sybase-sql_queries_and_see_the_result_in_a_split_window)
***
# Title: Quick Window Resizing with Keyboard Shortcuts
# Category: window_management
# Tags: key-mapping, window-resize, productivity
---
Adds intuitive keyboard shortcuts to quickly resize Vim/Neovim windows horizontally and vertically without complex chording

```vim
if bufwinnr(1)
  map <kPlus> <C-W>+
  map <kMinus> <C-W>-
  map <kDivide> <c-w><
  map <kMultiply> <c-w>>
endif
```

```lua
if vim.fn.bufwinnr(1) ~= -1 then
  vim.keymap.set('n', '<kPlus>', '<C-W>+', { noremap = true, silent = true })
  vim.keymap.set('n', '<kMinus>', '<C-W>-', { noremap = true, silent = true })
  vim.keymap.set('n', '<kDivide>', '<C-W><', { noremap = true, silent = true })
  vim.keymap.set('n', '<kMultiply>', '<C-W>>', { noremap = true, silent = true })
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Fast_window_resizing_with_plus/minus_keys)
***
# Title: Alt Key Window Management Shortcuts
# Category: window_management
# Tags: key-mapping, window-navigation, productivity
---
Efficient window resizing and navigation using Alt key combinations without moving hands from home row

```vim
map <silent> <A-h> <C-w><
map <silent> <A-j> <C-W>-
map <silent> <A-k> <C-W>+
map <silent> <A-l> <C-w>>

map <silent> <A-n> <C-w><C-w>
map <silent> <A-p> <C-w><S-w>
```

```lua
vim.keymap.set('n', '<A-h>', '<C-w><', { silent = true })
vim.keymap.set('n', '<A-j>', '<C-W>-', { silent = true })
vim.keymap.set('n', '<A-k>', '<C-W>+', { silent = true })
vim.keymap.set('n', '<A-l>', '<C-w>>', { silent = true })

vim.keymap.set('n', '<A-n>', '<C-w><C-w>', { silent = true })
vim.keymap.set('n', '<A-p>', '<C-w><S-w>', { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Fast_window_resizing_with_plus/minus_keys)
***
# Title: Open Tag in Split Window
# Category: window_management
# Tags: navigation, tags, window-split
---
Quickly open a tag definition in a new split window without losing the current context

```vim
:map <C-\> :sp<CR><C-]><C-w>_
```

```lua
vim.keymap.set('n', '<C-\>', function()
  vim.cmd('sp')
  vim.cmd('tag')
  vim.cmd('wincmd _')
end, { desc = 'Open tag in new split window' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Follow_tag_in_new_window)
***
# Title: Window Splitting and Sizing Control
# Category: window_management
# Tags: window-layout, ui-configuration
---
Control window sizing and option inheritance when splitting windows

```vim
set equalalways
set eadirection=both
" Local options are copied to new windows
```

```lua
vim.opt.equalalways = true
vim.opt.eadirection = 'both'
-- Neovim inherits local options when splitting windows
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/From_Vim_Help/2009)
***
# Title: Display Python Docs in Preview Window
# Category: window_management
# Tags: python, documentation, preview-window
---
Create a custom command to show Python documentation in a preview window, making it easy to view help without leaving the current buffer

```vim
command! -nargs=1 -bar Pyhelp :call ShowPydoc(<f-args>)
function! ShowPydoc(what)
  let path = $TEMP . '/' . a:what . '.pydoc'
  call system(s:pydoc_path . " " . a:what . (&shellredir))
  execute "pedit" fnameescape(path)
endfunction
```

```lua
vim.api.nvim_create_user_command('Pyhelp', function(opts)
  local what = opts.args
  local path = vim.fn.tempname() .. '/' .. what .. '.pydoc'
  vim.fn.system('pydoc ' .. what .. ' > ' .. path)
  vim.cmd('pedit ' .. path)
end, { nargs = 1 })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Get_help_on_Python_libraries)
***
# Title: Go to Nth-from-Last Window
# Category: window_management
# Tags: window-navigation, window-commands
---
Efficiently navigate to the nth window from the last window using winnr() function

```vim
:map <F12> :exe winnr('$') - 1 'wincmd w'<CR>
```

```lua
vim.keymap.set('n', '<F12>', function()
  vim.cmd.wincmd(tostring(vim.fn.winnr('$') - 1))
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Going_to_the_nth-from-last_window)
***
# Title: Close Tab and Focus Left Tab Automatically
# Category: window_management
# Tags: tab-navigation, key-mapping, workflow
---
Provides a custom mapping to close a tab and automatically focus on the left tab, improving tab navigation efficiency

```vim
noremap <silent><C-S-w> :if tabpagenr() != tabpagenr('$')<CR>:tabclose<CR>:if tabpagenr() > 1<CR>:tabprev<CR>:endif<CR>:else<CR>:tabclose<CR>:endif<CR>
```

```lua
vim.keymap.set('n', '<C-S-w>', function()
  local current_tab = vim.fn.tabpagenr()
  local total_tabs = vim.fn.tabpagenr('$')
  
  if current_tab ~= total_tabs then
    vim.cmd('tabclose')
    if vim.fn.tabpagenr() > 1 then
      vim.cmd('tabprev')
    end
  else
    vim.cmd('tabclose')
  end
end, { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Have_focus_on_left_tab_after_tabclose)
***
# Title: Enable Mouse Focus Across Splits
# Category: window_management
# Tags: mouse, split-windows, interaction
---
Enable mouse focus to easily interact with multiple window splits

```vim
set mousefocus
```

```lua
vim.opt.mousefocus = true
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/How_to_Have_a_Vim_Rave)
***
# Title: Prevent Cursor Movement When Switching Windows
# Category: window_management
# Tags: mouse-handling, focus, window-interaction
---
Temporarily disable mouse interactions when switching windows to prevent cursor repositioning

```vim
au!
  au FocusLost * let g:oldmouse=&mouse | set mouse=
  au FocusGained * if exists('g:oldmouse') | let &mouse=g:oldmouse | unlet g:oldmouse | endif
augroup END
```

```lua
local function setup_mouse_focus()
  local augroup = vim.api.nvim_create_augroup('MouseFocusPreserve', { clear = true })
  
  vim.api.nvim_create_autocmd('FocusLost', {
    group = augroup,
    callback = function()
      vim.g.oldmouse = vim.o.mouse
      vim.o.mouse = ''
    end
  })
  
  vim.api.nvim_create_autocmd('FocusGained', {
    group = augroup,
    callback = function()
      if vim.g.oldmouse then
        vim.o.mouse = vim.g.oldmouse
        vim.g.oldmouse = nil
      end
    end
  })
end

setup_mouse_focus()
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/How_to_not_move_cursor_when_selecting_window_with_mouse)
***
# Title: Open Source Navigator Files in Vim Tabs
# Category: window_management
# Tags: tab-management, external-tool, integration
---
Provides a quick way to maximize the current window without closing other windows or with full screen

```vim
" Maximize current window keeping other windows open
map <F5> <C-W>_<C-W><Bar>

" Close other windows and maximize current
:only
" or
CTRL-W o
```

```lua
-- Maximize current window while keeping others
vim.keymap.set('n', '<F5>', '<C-W>_<C-W>|', { desc = 'Maximize current window' })

-- Close other windows and maximize current
vim.keymap.set('n', '<leader>wo', ':only<CR>', { desc = 'Close other windows' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Maximize_current_window)
***
# Title: Toggle Window Maximize/Restore
# Category: window_management
# Tags: window, toggle, maximize
---
Creates a function to toggle between maximizing and restoring a window, useful for quickly changing window size

```vim
let w:windowmaximized = 0
function! MaxRestoreWindow()
  if w:windowmaximized == 1
    let w:windowmaximized = 0
    :simalt ~r
  else
    let w:windowmaximized = 1
    :simalt ~x
  endif
endfunction
map <F5> :call MaxRestoreWindow()<CR>
```

```lua
local windowMaximized = false

local function maxRestoreWindow()
  windowMaximized = not windowMaximized
  if windowMaximized then
    vim.cmd('simalt ~x')  -- Maximize
  else
    vim.cmd('simalt ~r')  -- Restore
  end
end

vim.keymap.set('n', '<F5>', maxRestoreWindow, { desc = 'Toggle window maximize' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Maximize_or_restore_window)
***
# Title: Maximize Vim Window on Windows
# Category: window_management
# Tags: windows, startup, configuration
---
Automatically maximize Vim window when launching on Windows systems

```vim
au GUIEnter * simalt ~x
```

```lua
vim.api.nvim_create_autocmd('UIEnter', {
  callback = function()
    if vim.fn.has('win32') == 1 then
      vim.cmd('simalt ~x')
    end
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Maximize_or_set_initial_window_size)
***
# Title: Toggle Window Maximization Without Losing Splits
# Category: window_management
# Tags: window-layout, toggle-maximize, session-preservation
---
Provides a function to maximize the current window and easily restore the previous split layout without losing window configuration

```vim
function! MaximizeToggle()
  if exists("s:maximize_session")
    exec "source " . s:maximize_session
    call delete(s:maximize_session)
    unlet s:maximize_session
    let &hidden=s:maximize_hidden_save
    unlet s:maximize_hidden_save
  else
    let s:maximize_hidden_save = &hidden
    let s:maximize_session = tempname()
    set hidden
    exec "mksession! " . s:maximize_session
    only
  endif
endfunction

nnoremap <C-W>O :call MaximizeToggle()<CR>
nnoremap <C-W>o :call MaximizeToggle()<CR>
nnoremap <C-W><C-O> :call MaximizeToggle()<CR>
```

```lua
local function maximize_toggle()
  if vim.g.maximize_session then
    vim.cmd('source ' .. vim.g.maximize_session)
    os.remove(vim.g.maximize_session)
    vim.g.maximize_session = nil
    vim.o.hidden = vim.g.maximize_hidden_save
  else
    vim.g.maximize_hidden_save = vim.o.hidden
    vim.g.maximize_session = vim.fn.tempname()
    vim.o.hidden = true
    vim.cmd('mksession! ' .. vim.g.maximize_session)
    vim.cmd('only')
  end
end

vim.keymap.set('n', '<C-W>O', maximize_toggle)
vim.keymap.set('n', '<C-W>o', maximize_toggle)
vim.keymap.set('n', '<C-W><C-O>', maximize_toggle)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Maximize_window_and_return_to_previous_split_structure)
***
# Title: Quick Tab Management for Editing Multiple Files
# Category: window_management
# Tags: tabs, file-navigation, buffer-management
---
Simple mappings to open current buffer in a new tab and quickly close it, improving multi-file editing workflow

```vim
nmap t% :tabedit %<CR>
nmap td :tabclose<CR>
```

```lua
vim.keymap.set('n', 't%', ':tabedit %<CR>', { desc = 'Open current buffer in new tab' })
vim.keymap.set('n', 'td', ':tabclose<CR>', { desc = 'Close current tab' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Maximize_window_and_return_to_previous_split_structure)
***
# Title: Minimize and Restore Vim Windows Quickly
# Category: window_management
# Tags: window-control, system-integration, productivity
---
Use Ctrl-Z to suspend/minimize Vim in the background, with an optional system-wide shortcut for quick restoration

```vim
" Built-in Vim suspend functionality
" Ctrl-Z suspends Vim in normal/visual mode
```

```lua
-- Neovim uses the same built-in suspend functionality
-- Use Ctrl-Z to suspend the current Vim instance
-- Restore using fg in terminal or system shortcut
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Minimize_and_restore_gvim_under_Windows_using_shortcut_keys)
***
# Title: Move Window Between Tabs Dynamically
# Category: window_management
# Tags: tabs, window-navigation, advanced-movement
---
Functions to move the current window between tabs, allowing dynamic rearrangement of buffers across tab pages

```vim
function MoveToNextTab()
  "there is only one window
  if tabpagenr('$') == 1 && winnr('$') == 1
    return
  endif
  "preparing new window
  let l:tab_nr = tabpagenr('$')
  let l:cur_buf = bufnr('%')
  if tabpagenr() < tab_nr
    close!
    if l:tab_nr == tabpagenr('$')
      tabnext
    endif
    sp
  else
    close!
    tabnew
  endif
  "opening current buffer in new window
  exe "b".l:cur_buf
endfunc
```

```lua
function _G.move_to_next_tab()
  local total_tabs = vim.fn.tabpagenr('$')
  local current_tab = vim.fn.tabpagenr()
  local current_buf = vim.fn.bufnr('%')
  
  if total_tabs == 1 and vim.fn.winnr('$') == 1 then
    return
  end
  
  if current_tab < total_tabs then
    vim.cmd('close!')
    vim.cmd('tabnext')
    vim.cmd('split')
  else
    vim.cmd('close!')
    vim.cmd('tabnew')
  end
  
  vim.cmd('buffer ' .. current_buf)
end

-- Add a keymap
vim.keymap.set('n', '<A-.>', '<cmd>lua move_to_next_tab()<CR>', { desc = 'Move window to next tab' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Move_current_window_between_tabs)
***
# Title: Dynamic Window Resizing with F1 Key
# Category: window_management
# Tags: key-mapping, window-resize, gui
---
Cycle through predefined window sizes and toggle line numbers using F1 key, useful for adjusting workspace layout

```vim
nmap <F1> :call ResizeWindow()<CR>
imap <F1> <Esc><F1>a

function! ResizeWindow()
  if (has("gui_running"))
    if s:selectedsize == 1
      let s:selectedsize = 2
      set number
      set columns=88
      set lines=35
    elseif s:selectedsize == 2
      set number
      let s:selectedsize = 3
      set columns=98
      set lines=45
    else
      let s:selectedsize = 1
      set nonumber
      set columns=80
      set lines=25
    endif
  endif
endfunction

let s:selectedsize=1
call ResizeWindow()
```

```lua
local selectedSize = 1

local function resizeWindow()
  if vim.g.neovide or vim.fn.has('gui_running') == 1 then
    if selectedSize == 1 then
      selectedSize = 2
      vim.o.number = true
      vim.o.columns = 88
      vim.o.lines = 35
    elseif selectedSize == 2 then
      selectedSize = 3
      vim.o.number = true
      vim.o.columns = 98
      vim.o.lines = 45
    else
      selectedSize = 1
      vim.o.number = false
      vim.o.columns = 80
      vim.o.lines = 25
    end
  end
end

vim.keymap.set({'n', 'i'}, '<F1>', resizeWindow)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Nice_window_resizing)
***
# Title: Resize Windows with Alt+Arrow Keys
# Category: window_management
# Tags: key-mapping, window-resize
---
Quickly resize windows vertically using Alt+Left/Right arrow keys

```vim
map <M-right> <Esc>:resize +2 <CR>
map <M-left> <Esc>:resize -2 <CR>
```

```lua
vim.keymap.set('n', '<M-Right>', ':resize +2<CR>', { silent = true })
vim.keymap.set('n', '<M-Left>', ':resize -2<CR>', { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Nice_window_resizing)
***
# Title: Open Neovim Matching Console Window Geometry
# Category: window_management
# Tags: window-geometry, terminal-integration, x11
---
Dynamically position Neovim window to match the current terminal's size and position using X11 window information

```vim
# Korn shell function to get current window geometry
function gv
{
  xwi=$(xwininfo -id $WINDOWID)
  # Extract window position and size
  x=${xyposn%+[0-9]*}
  y=${xyposn##*+}
  w=${wh%x*}
  h=${wh#*x}

  # Adjust for borders and menus
  h=h-4
  x=x-4
  y=y-18

  # Open gvim with matching geometry
  gvim -geometry "${w}x${h}+${x}+${y}" "$@"
}
```

```lua
-- Lua function to get window geometry and open Neovim
local function open_matching_window()
  -- Use vim.fn.system to run xwininfo and parse output
  local xwi = vim.fn.system('xwininfo -id ' .. os.getenv('WINDOWID'))
  
  -- Extract window dimensions (simplified example)
  local x, y, w, h = xwi:match('Corners: (%d+)%+(%d+).*geometry (%d+)x(%d+)')
  
  -- Adjust geometry
  h = tonumber(h) - 4
  x = tonumber(x) - 4
  y = tonumber(y) - 18
  
  -- Open Neovim with matching geometry
  vim.cmd('!nvim -c "set lines=' .. h .. ' columns=' .. w .. '"')
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Opening_gvim_atop_a_console_window)
***
# Title: Open New Buffers Below Current Window
# Category: window_management
# Tags: splits, buffer-management, configuration
---
Configure Vim/Neovim to open new split windows below the current window by default

```vim
set splitbelow
```

```lua
vim.opt.splitbelow = true
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Opening_new_buffer_below_the_current)
***
# Title: Open New Vertical Buffers to the Right
# Category: window_management
# Tags: splits, buffer-management, configuration
---
Configure Vim/Neovim to open new vertical split windows to the right of the current window

```vim
set splitright
```

```lua
vim.opt.splitright = true
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Opening_new_buffer_below_the_current)
***
# Title: Dynamic Tag Preview with Full-Height Vertical Window
# Category: window_management
# Tags: tags, preview, navigation
---
Flexible function to open tag previews in vertical or horizontal windows, with custom height and positioning

```vim
function PreviewTag(top)
  set previewheight=25
  exe "silent! pclose"
  if &previewwindow
    return
  endif
  let w = expand("<cword>")
  exe "ptjump " . w
  if a:top
    return
  endif
  exe "silent! wincmd P"
  if &previewwindow
    if has("folding")
      silent! .foldopen
    endif
    wincmd L
    wincmd p
    if !&previewwindow
      wincmd _
    endif
  endif
endfunction
```

```lua
function _G.preview_tag(top)
  vim.o.previewheight = 25
  vim.cmd('silent! pclose')
  
  if vim.wo.previewwindow then
    return
  end
  
  local word = vim.fn.expand('<cword>')
  vim.cmd('ptjump ' .. word)
  
  if top then
    return
  end
  
  vim.cmd('silent! wincmd P')
  if vim.wo.previewwindow then
    if vim.wo.foldenable then
      vim.cmd('silent! .foldopen')
    end
    vim.cmd('wincmd L')
    vim.cmd('wincmd p')
    
    if not vim.wo.previewwindow then
      vim.cmd('wincmd _')
    end
  end
end

-- Key mappings
vim.keymap.set('n', '<C-]>', function() _G.preview_tag(false) end)
vim.keymap.set('n', '<M-]>', function() _G.preview_tag(true) end)
vim.keymap.set('n', '<M-[>', ':pc<CR>')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Optionally_open_matching_or_selected_tag_in_full_height_vertical_window)
***
# Title: Quick Window Navigation with Spacebar
# Category: window_management
# Tags: key-mapping, window-navigation, productivity
---
Use spacebar to quickly switch between and maximize split windows, improving navigation efficiency

```vim
"Jump between windows
map <Space> <c-W>w
"Open window wide
map <Space><Space> :call OpenSplittedWindowWide()<CR>

function OpenSplittedWindowWide()
  normal ^W|
  normal ^W20+
endfunction
```

```lua
-- Jump between windows
vim.keymap.set('n', '<Space>', '<C-W>w', { desc = 'Switch to next window' })

-- Open window wide
vim.keymap.set('n', '<Space><Space>', function()
  vim.cmd('wincmd |')  -- Maximize width
  vim.cmd('wincmd +')  -- Maximize height
end, { desc = 'Maximize current window' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Press_space_to_jump_between_windows_and_to_expand_them)
***
# Title: Alternative Window Navigation Shortcuts
# Category: window_management
# Tags: key-mapping, window-navigation, productivity
---
Use Ctrl-J/K to move between horizontal splits and maximize them quickly

```vim
map <C-J> <C-W>j<C-W>_
map <C-K> <C-W>k<C-W>_
```

```lua
vim.keymap.set('n', '<C-J>', '<C-W>j<C-W>_', { desc = 'Move down and maximize window' })
vim.keymap.set('n', '<C-K>', '<C-W>k<C-W>_', { desc = 'Move up and maximize window' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Press_space_to_jump_between_windows_and_to_expand_them)
***
# Title: Multiple Views of Same Buffer in Different Tabs
# Category: window_management
# Tags: tabs, buffer-management, workflow
---
Easily resize Vim/Neovim windows using function keys with different modifier behaviors

```vim
" Resize windows using F8 and F9
:map <F8> :set columns+=10<CR>
:map <S-F8> :set columns-=10<CR>
:map <C-F8> :set columns=132<CR>
:map <M-F8> :set columns=80<CR>

:map <F9> :set lines+=5<CR>
:map <S-F9> :set lines-=5<CR>
:map <C-F9> :set lines=60<CR>
:map <M-F9> :set lines=30<CR>
```

```lua
-- Resize windows using function keys
vim.keymap.set('n', '<F8>', ':set columns+=10<CR>', { desc = 'Increase window width' })
vim.keymap.set('n', '<S-F8>', ':set columns-=10<CR>', { desc = 'Decrease window width' })
vim.keymap.set('n', '<C-F8>', ':set columns=132<CR>', { desc = 'Set standard wide width' })
vim.keymap.set('n', '<M-F8>', ':set columns=80<CR>', { desc = 'Set standard narrow width' })

vim.keymap.set('n', '<F9>', ':set lines+=5<CR>', { desc = 'Increase window height' })
vim.keymap.set('n', '<S-F9>', ':set lines-=5<CR>', { desc = 'Decrease window height' })
vim.keymap.set('n', '<C-F9>', ':set lines=60<CR>', { desc = 'Set standard tall height' })
vim.keymap.set('n', '<M-F9>', ':set lines=30<CR>', { desc = 'Set standard short height' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Quick_window_resizing)
***
# Title: Resize Windows with Ctrl + Cursor Keys
# Category: window_management
# Tags: window-resize, key-mapping
---
Resize split windows relative to neighboring windows using Ctrl and cursor keys

```vim
" Resize split windows
nmap <C-Left> <C-W>-<C-W>-
nmap <C-Right> <C-W>+<C-W>+
nmap <C-Up> <C-W>><C-W>>
nmap <C-Down> <C-W><<C-W><
```

```lua
-- Resize split windows
vim.keymap.set('n', '<C-Left>', '<C-W>-<C-W>-', { desc = 'Decrease horizontal split size' })
vim.keymap.set('n', '<C-Right>', '<C-W>+<C-W>+', { desc = 'Increase horizontal split size' })
vim.keymap.set('n', '<C-Up>', '<C-W>><C-W>>', { desc = 'Increase vertical split size' })
vim.keymap.set('n', '<C-Down>', '<C-W><<C-W><', { desc = 'Decrease vertical split size' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Quick_window_resizing)
***
# Title: Quickly Resize Windows in Neovim
# Category: window_management
# Tags: window-resize, split-management, key-mapping
---
Provides multiple methods to resize split windows quickly, with keyboard shortcuts and command-line commands

```vim
" Resize window vertically
Ctrl-w +  " Increase height by 1 line
Ctrl-w -  " Decrease height by 1 line
Ctrl-w >  " Increase width by 1 column
Ctrl-w <  " Decrease width by 1 column

" Max out window height/width
Ctrl-w _   " Maximize window height
Ctrl-w |   " Maximize window width

" Proportional resizing
nnoremap <Leader>+ :exe "resize " . (winheight(0) * 3/2)<CR>
nnoremap <Leader>- :exe "resize " . (winheight(0) * 2/3)<CR>
```

```lua
-- Resize window functions
vim.keymap.set('n', '<C-w>+', '<C-w>+', { desc = 'Increase window height' })
vim.keymap.set('n', '<C-w>-', '<C-w>-', { desc = 'Decrease window height' })
vim.keymap.set('n', '<C-w>>', '<C-w>>', { desc = 'Increase window width' })
vim.keymap.set('n', '<C-w><', '<C-w><', { desc = 'Decrease window width' })

-- Proportional resizing
vim.keymap.set('n', '<Leader>+', function()
  local current_height = vim.api.nvim_win_get_height(0)
  vim.api.nvim_win_set_height(0, math.floor(current_height * 1.5))
end, { desc = 'Increase window height by 1.5x' })

vim.keymap.set('n', '<Leader>-', function()
  local current_height = vim.api.nvim_win_get_height(0)
  vim.api.nvim_win_set_height(0, math.floor(current_height * 2/3))
end, { desc = 'Decrease window height by 0.67x' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Resize_splits_more_quickly)
***
# Title: Dynamic Window Resizing for Line Numbers
# Category: window_management
# Tags: window-resize, line-numbers, toggle
---
Automatically adjust window columns when toggling line numbers to maintain layout

```vim
function! Toggle_num()
  if !exists("g:grow")
    let g:grow = &numberwidth
  endif
  set number!
  if &number
    exec "set columns+=" . g:grow
  else
    exec "set columns-=" . g:grow
  endif
endfunction
map <M-n> :call Toggle_num()<CR>
```

```lua
local function toggle_num()
  local grow = vim.o.numberwidth
  vim.wo.number = not vim.wo.number
  if vim.wo.number then
    vim.o.columns = vim.o.columns + grow
  else
    vim.o.columns = vim.o.columns - grow
  end
end

vim.keymap.set('n', '<M-n>', toggle_num, { desc = 'Toggle line numbers and adjust window' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Resize_window_when_showing/hiding_line_numbers)
***
# Title: Resize Terminal for Diff View
# Category: window_management
# Tags: terminal, xterm, window-resize
---
Automatically resize terminal window when running vimdiff to provide more horizontal space for comparing files

```vim
if &diff
  set columns=140
endif
```

```lua
if vim.o.diff then
  vim.o.columns = 140
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Resize_xterm_when_running_vimdiff)
***
# Title: Window Zooming Toggle
# Category: window_management
# Tags: window-manipulation, productivity, toggle
---
Easily maximize the current window while minimizing others, with a toggle functionality

```vim
function! ToggleMaxWins()
  if exists('g:windowMax')
    au! maxCurrWin
    wincmd =
    unlet g:windowMax
  else
    augroup maxCurrWin
        au! WinEnter * wincmd _
    augroup END
    do maxCurrWin WinEnter
    let g:windowMax=1
  endif
endfunction
nnoremap <Leader>max :call ToggleMaxWins()<CR>
```

```lua
local function toggle_max_wins()
  if vim.g.window_max then
    vim.cmd('wincmd =')
    vim.g.window_max = nil
  else
    vim.api.nvim_create_augroup('max_curr_win', { clear = true })
    vim.api.nvim_create_autocmd('WinEnter', {
      group = 'max_curr_win',
      callback = function()
        vim.cmd('wincmd _')
      end
    })
    vim.g.window_max = true
  end
end

vim.keymap.set('n', '<Leader>max', toggle_max_wins, { desc = 'Toggle window maximization' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Rolodex_Vim)
***
# Title: Rolodex Window Mode
# Category: window_management
# Tags: window-layout, productivity, display
---
Create a dynamic window layout where the current window is full height and others are minimized

```vim
set noequalalways winminheight=0 winheight=9999 helpheight=9999
```

```lua
vim.opt.equalalways = false
vim.opt.winminheight = 0
vim.opt.winheight = 9999
vim.opt.helpheight = 9999
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Rolodex_Vim)
***
# Title: Restore Current Window/Buffer After Global Command
# Category: window_management
# Tags: buffer-navigation, window-management, automation
---
Create custom commands that perform actions across windows/buffers while preserving the original window or buffer context

```vim
function! BufDo(command)
  let currBuff=bufnr("%")
  execute 'bufdo ' . a:command
  execute 'buffer ' . currBuff
endfunction
com! -nargs=+ -complete=command Bufdo call BufDo(<q-args>)
```

```lua
function _G.buf_do(command)
  local current_buf = vim.api.nvim_get_current_buf()
  for _, buf in ipairs(vim.api.nvim_list_bufs()) do
    vim.api.nvim_set_current_buf(buf)
    vim.cmd(command)
  end
  vim.api.nvim_set_current_buf(current_buf)
end
vim.api.nvim_create_user_command('BufDo', function(opts)
  _G.buf_do(opts.args)
end, { nargs = '+' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Run_a_command_in_multiple_files)
***
# Title: Auto-Resize Window for Diff Mode
# Category: window_management
# Tags: diff, window-resize, gui-settings
---
Automatically expand window width when in diff mode for better side-by-side comparison

```vim
" Window settings for diff mode
if &diff
  let &columns = ((&columns*2 > 172)? 172: &columns*2)
endif
```

```lua
-- Lua equivalent for diff mode window resizing
if vim.o.diff then
  local columns = vim.o.columns
  vim.o.columns = math.min(columns * 2, 172)
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip488)
***
# Title: Synchronous Scrolling in Multiple Windows
# Category: window_management
# Tags: split-windows, scrolling, window-navigation
---
Enable synchronized scrolling across multiple Vim/Neovim windows, allowing simultaneous vertical scrolling

```vim
:set scrollbind
:set scb! (to toggle)
```

```lua
-- Set scrollbind for current window
vim.wo.scrollbind = true

-- Toggle scrollbind
vim.cmd('set scb!')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip52)
***
# Title: Prevent Accidental Window Closure
# Category: window_management
# Tags: key-mapping, window-navigation, safety
---
Disable the default <C-W>o command that closes all other windows to prevent accidentally destroying your window layout

```vim
nnoremap <C-W>O :echo "sucker"<CR>
nnoremap <C-W>o :echo "sucker"<CR>
nnoremap <C-W><C-O> :echo "sucker"<CR>
```

```lua
vim.keymap.set('n', '<C-W>o', function() vim.notify('Window closure prevented', vim.log.levels.WARN) end)
vim.keymap.set('n', '<C-W>O', function() vim.notify('Window closure prevented', vim.log.levels.WARN) end)
vim.keymap.set('n', '<C-W><C-O>', function() vim.notify('Window closure prevented', vim.log.levels.WARN) end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip58)
***
# Title: Open GVim Matching Console Window Position
# Category: window_management
# Tags: window-positioning, shell-integration, x11
---
Dynamically position GVim window to match the current console window's geometry using X11 window information

```vim
function gv
  xwi=$(xwininfo -id $WINDOWID)
  # Extract window geometry details
  # Position and resize gvim to match console window
  gvim -geometry "${w}x${h}+${x}+${y}" "$@"
endfunction
```

```lua
function _G.open_gvim_matching_console()
  local windowid = vim.env.WINDOWID
  if not windowid then return end
  
  -- Use vim.fn.system() to get xwininfo details
  -- Implement geometry extraction and gvim positioning
  vim.cmd('!gvim -geometry "'..geometry..'"')
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip607)
***
# Title: Toggle Line Numbers Across All Windows
# Category: window_management
# Tags: key-mapping, toggle, multi-window
---
Toggle line numbers simultaneously in all open windows, maintaining current window focus

```vim
func! s:NumToggle()
  let s:current_winnr = winnr()
  windo set invnumber
  exec s:current_winnr."winc w"
endfunc
map <F12> :call <SID>NumToggle()<CR>
```

```lua
local function num_toggle()
  local current_win = vim.api.nvim_get_current_win()
  vim.cmd('windo set invnumber')
  vim.api.nvim_set_current_win(current_win)
end

vim.keymap.set('n', '<F12>', num_toggle, { desc = 'Toggle line numbers in all windows' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip757)
***
