# Title: Custom statusline
# Category: UI
# Tags: statusline, custom, display
---
Use `vim.opt.statusline` to set a custom statusline format.

```vim
:lua vim.opt.statusline = "%f %y %m %= %l:%c"
```

**Source:** ** Community contributed
***
# Title: Check highlight groups
# Category: UI
# Tags: highlight, groups, colors
---
Use `:hi` to view all highlight groups and their current settings.

```vim
:hi  " show all highlight groups
```

**Source:** ** Community contributed
***
# Title: Highlight groups
# Category: UI
# Tags: highlight, groups, fun
---
Use the following code to create command `HLList`. 
When run, the command creates a scratch buffer with one line per highlight group, with each line styled with its own group.

```vim
command! HLList lua local b=vim.api.nvim_create_buf(false,true) vim.api.nvim_set_current_buf(b) local g=vim.fn.getcompletion("","highlight") vim.api.nvim_buf_set_lines(b,0,-1,false,g) for i,n in ipairs(g) do pcall(vim.api.nvim_buf_add_highlight,b,-1,n,i-1,0,-1) end
```

**Source:** ** Community contributed
***
# Title: Change highlight group on the fly
# Category: UI
# Tags: highlight, groups, fun
---
You can change the highlight group on the fly. For example, the next command changes all comments to red italic:

```vim
:hi Comment guifg=#ffaa00 gui=italic
```

**Source:** ** Community contributed
***
# Title: Flash yanked text
# Category: UI
# Tags: highlight, group, yank, flash
---
Use the following command to flash yanked text using the `IncSearch` highlight for `200` milliseconds.

```vim
:au TextYankPost * lua=vim.highlight.on_yank{higroup='IncSearch',timeout=200}
```

**Source:** ** Community contributed
***
# Title: Print treesitter highlight group info
# Category: UI
# Tags: highlight, group, treesitter
---
Use the following command to check the highlight info for the text under the cursor:

```vim
:lua print(vim.treesitter.get_captures_at_cursor()[1] or "NONE")
```

**Source:** ** Community contributed
***
# Title: Beautiful transparent theme with background image
# Category: UI
# Tags: theme, transparency, background, aesthetic, kitty, tokyonight
---
Create a beautiful working environment by combining a transparent Neovim theme with a tinted background image in your terminal emulator.
**Neovim configuration (Tokyonight with transparency):**
**Kitty terminal configuration (~/.config/kitty/kitty.conf):**
This creates a beautiful aesthetic where your code appears over a subtly tinted background image, combining terminal customization with Neovim's transparent theme support.

```lua
{
  "folke/tokyonight.nvim",
  lazy = false,
  priority = 2000,
  opts = { transparent = true }  -- Enable transparency
}
```

**Source:** ** Community contributed
***
# Title: Quick Window Maximization Shortcut
# Category: ui
# Tags: keyboard-shortcut, fullscreen
---
Use F11 or custom KDE shortcut to toggle window maximization

```lua
-- Configure a custom mapping if needed
vim.keymap.set('n', '<F11>', ':set invfullscreen<CR>', { desc = 'Toggle Fullscreen' })
```

**Source:** ** https://vim.fandom.com/wiki/Automatically_maximizing_gvim_in_KDE
***
# Title: Change Cursor Color and Shape in Different Modes
# Category: ui
# Tags: cursor, terminal-config, mode-specific
---
Customize cursor color and shape to visually distinguish between Vim modes, improving user awareness

```vim
if &term =~ "xterm\|rxvt"
  " use an orange cursor in insert mode
  let &t_SI = "\<Esc>]12;orange\x7"
  " use a red cursor otherwise
  let &t_EI = "\<Esc>]12;red\x7"
endif

" Cursor shape changes
if &term =~ '^xterm\|rxvt'
  let &t_SI .= "\<Esc>[4 q"  " solid underscore in insert mode
  let &t_EI .= "\<Esc>[2 q"  " solid block in normal mode
endif
```
```lua
local function set_cursor_style()
  if vim.env.TERM:match("xterm") or vim.env.TERM:match("rxvt") then
    -- Cursor color changes
    vim.cmd('let &t_SI = "\\<Esc>]12;orange\\x7"')
    vim.cmd('let &t_EI = "\\<Esc>]12;red\\x7"')
    
    -- Cursor shape changes
    vim.cmd('let &t_SI .= "\\<Esc>[4 q"')  -- Underscore in insert mode
    vim.cmd('let &t_EI .= "\\<Esc>[2 q"')  -- Block in normal mode
  end
end

vim.api.nvim_create_autocmd('VimEnter', {
  callback = set_cursor_style
})
```

**Source:** ** https://vim.fandom.com/wiki/Change_cursor_color_in_different_modes
***
# Title: Disable Cursor Blinking in Vim/Neovim
# Category: ui
# Tags: cursor, display-config
---
Disable cursor blinking to reduce visual distraction and improve focus

```vim
" Disable all blinking:
:set guicursor+=a:blinkon0

" Restore default:
:set guicursor&
```
```lua
-- Disable cursor blinking
vim.opt.guicursor:append('a:blinkon0')

-- Alternatively, to restore default
vim.opt.guicursor = vim.o.guicursor
```

**Source:** ** https://vim.fandom.com/wiki/Change_cursor_color_in_different_modes
***
# Title: Dynamic Cursor Shape in Different Modes
# Category: ui
# Tags: terminal-integration, cursor-customization, mode-indicator
---
Change cursor shape dynamically based on Vim mode, providing visual feedback for insert, replace, and normal modes

```vim
" Cursor shape settings
let &t_SI = "\<Esc>[6 q"  " Insert mode: vertical bar
let &t_SR = "\<Esc>[4 q"  " Replace mode: underline
let &t_EI = "\<Esc>[2 q"  " Normal mode: block
```
```lua
-- Cursor shape configuration
vim.cmd([[let &t_SI = "\<Esc>[6 q"  " Insert mode: vertical bar
let &t_SR = "\<Esc>[4 q"  " Replace mode: underline
let &t_EI = "\<Esc>[2 q"  " Normal mode: block]])
```

**Source:** ** https://vim.fandom.com/wiki/Change_cursor_shape_in_different_modes
***
# Title: Quickly Adjust Font Size in Neovim GUI
# Category: ui
# Tags: font-size, gui, mapping
---
Provides a flexible, cross-platform method to dynamically adjust GUI font size using key mappings or mouse wheel

```vim
function! AdjustFontSize(amount)
    if !has("gui_running")
        return
    endif

    let l:min_font_size = 5
    let l:max_font_size = 64

    let l:font_info = GetFontInfo()
    let l:font_name = l:font_info.name
    let l:font_size = l:font_info.size

    if a:amount == '-'
        let l:font_size = l:font_size - 1
    elseif a:amount == '+'
        let l:font_size = l:font_size + 1
    endif

    let l:font_size = max([l:min_font_size, min([l:max_font_size, l:font_size])])
    let &guifont = substitute(&guifont, l:font_size_pattern, l:font_size, '')
endfunction
```
```lua
function _G.adjust_font_size(amount)
    if not vim.g.gui_running then
        return
    end

    local min_font_size = 5
    local max_font_size = 64

    local font_info = get_font_info()
    local font_name = font_info.name
    local font_size = tonumber(font_info.size)

    if amount == '-' then
        font_size = font_size - 1
    elseif amount == '+' then
        font_size = font_size + 1
    end

    font_size = math.max(min_font_size, math.min(max_font_size, font_size))
    vim.o.guifont = vim.fn.substitute(vim.o.guifont, '\d+', tostring(font_size), '')
end

-- Example mappings
vim.keymap.set('n', '<F11>', function() _G.adjust_font_size('-') end)
vim.keymap.set('n', '<F12>', function() _G.adjust_font_size('+') end)
vim.keymap.set('n', '<C-ScrollWheelDown>', function() _G.adjust_font_size('-') end)
vim.keymap.set('n', '<C-ScrollWheelUp>', function() _G.adjust_font_size('+') end)
```

**Source:** ** https://vim.fandom.com/wiki/Change_font_size_quickly
***
# Title: Identify Active Vim Instance by Color
# Category: ui
# Tags: focus, colorscheme, multi-instance
---
Change color scheme when Vim gains or loses focus to visually distinguish active window

```vim
" Change color scheme on window focus
:autocmd FocusLost * :colorscheme desert
:autocmd FocusGained * :colorscheme default
```
```lua
vim.api.nvim_create_augroup('VimFocusColorScheme', { clear = true })

vim.api.nvim_create_autocmd('FocusLost', {
  group = 'VimFocusColorScheme',
  callback = function()
    vim.cmd('colorscheme desert')
  end
})

vim.api.nvim_create_autocmd('FocusGained', {
  group = 'VimFocusColorScheme',
  callback = function()
    vim.cmd('colorscheme default')
  end
})
```

**Source:** ** https://vim.fandom.com/wiki/Change_gvim_colorscheme_when_focus_changes
***
# Title: Statusline Color Indicator for Vim Modes
# Category: ui
# Tags: statusline, mode-indicator, autocmd
---
Dynamically change statusline color to visually indicate current Vim mode (normal/insert/replace)

```vim
" Enable statusline always
set laststatus=2

" Change statusline color based on mode
function! InsertStatuslineColor(mode)
  if a:mode == 'i'
    hi statusline guibg=magenta
  elseif a:mode == 'r'
    hi statusline guibg=blue
  else
    hi statusline guibg=red
  endif
endfunction

au InsertEnter * call InsertStatuslineColor(v:insertmode)
au InsertChange * call InsertStatuslineColor(v:insertmode)
au InsertLeave * hi statusline guibg=green

" Default statusline to green on Vim entry
hi statusline guibg=green
```
```lua
-- Change statusline color based on mode
function InsertStatuslineColor(mode)
  if mode == 'i' then
    vim.cmd('hi statusline guibg=magenta')
  elseif mode == 'r' then
    vim.cmd('hi statusline guibg=blue')
  else
    vim.cmd('hi statusline guibg=red')
  end
end

-- Create autocmds for mode color changes
vim.api.nvim_create_augroup('ModeStatusline', { clear = true })
vim.api.nvim_create_autocmd('InsertEnter', {
  group = 'ModeStatusline',
  callback = function()
    InsertStatuslineColor(vim.v.insertmode)
  end
})
vim.api.nvim_create_autocmd('InsertChange', {
  group = 'ModeStatusline',
  callback = function()
    InsertStatuslineColor(vim.v.insertmode)
  end
})
vim.api.nvim_create_autocmd('InsertLeave', {
  group = 'ModeStatusline',
  callback = function()
    vim.cmd('hi statusline guibg=green')
  end
})

-- Default statusline to green on Vim entry
vim.cmd('hi statusline guibg=green')
```

**Source:** ** https://vim.fandom.com/wiki/Change_statusline_color_to_show_insert_or_normal_mode
***
# Title: Dynamic Color Scheme for Context Awareness
# Category: ui
# Tags: color-scheme, autocmd, context-switching
---
Automatically change color schemes to visually distinguish different files, directories, or Vim instances, reducing accidental edits

```vim
au BufEnter * if (exists("b:colors_name")) | let b:current_colors=colors_name
  \ | execute "colorscheme " . b:colors_name | endif
au BufLeave * if (exists("b:current_colors")) | execute "colorscheme " . b:current_colors | endif
```
```lua
vim.api.nvim_create_autocmd('BufEnter', {
  callback = function()
    if vim.b.colors_name then
      vim.g.current_colors = vim.g.colors_name
      vim.cmd('colorscheme ' .. vim.b.colors_name)
    end
  end
})

vim.api.nvim_create_autocmd('BufLeave', {
  callback = function()
    if vim.g.current_colors then
      vim.cmd('colorscheme ' .. vim.g.current_colors)
    end
  end
})
```

**Source:** ** https://vim.fandom.com/wiki/Change_the_color_scheme_to_show_where_you_are
***
# Title: Color Scheme for Different Directories
# Category: ui
# Tags: color-scheme, autocmd, file-context
---
Change color scheme based on the current file's directory to quickly identify which project or directory you're working in

```vim
autocmd BufEnter * if match(@%,'/otherdir/')>=0 | colorscheme oceanblack | else | colorscheme inkpot | end
```
```lua
vim.api.nvim_create_autocmd('BufEnter', {
  callback = function()
    local current_file = vim.fn.expand('%:p')
    if current_file:match('/otherdir/') then
      vim.cmd('colorscheme oceanblack')
    else
      vim.cmd('colorscheme inkpot')
    end
  end
})
```

**Source:** ** https://vim.fandom.com/wiki/Change_the_color_scheme_to_show_where_you_are
***
# Title: Customize Mouse Cursor Shape in Vim
# Category: ui
# Tags: mouse, cursor, customization
---
Change the mouse cursor shape in different Vim modes for improved visual feedback

```vim
:set mouseshape=n:pencil

" For different modes, you can use various shapes
" Check :help 'mouseshape' for more options
```
```lua
-- Note: This is X11/Linux specific
-- Neovim doesn't have direct mouseshape setting
-- May require external configuration or GUI settings
```

**Source:** ** https://vim.fandom.com/wiki/Change_the_gvim_mouse_arrow_cursor
***
# Title: Customize Omni-Completion Popup Menu Colors
# Category: ui
# Tags: completion, color-scheme, customization
---
Improve readability of the completion popup menu by customizing its background and style

```vim
" GUI mode color customization
highlight Pmenu guibg=brown gui=bold

" Console Vim color customization
highlight Pmenu ctermbg=238 gui=bold
```
```lua
-- Customize completion menu colors
vim.cmd.highlight('Pmenu guibg=brown gui=bold')
vim.cmd.highlight('Pmenu ctermbg=238 gui=bold')
```

**Source:** ** https://vim.fandom.com/wiki/Change_the_pink_omnicomplete_popup_to_a_readable_color
***
# Title: Console-Like Fonts for Neovim on Windows
# Category: ui
# Tags: fonts, display, windows
---
Recommended console-style fonts for improving Neovim's visual appearance on Windows

```lua
-- Recommended fonts in Neovim configuration
-- Add to init.lua or init.vim
vim.opt.guifont = 'FixedSys Excelsior:h10'  -- Unicode-friendly console font
-- Or
vim.opt.guifont = 'ProFont:h10'  -- Another recommended console-style font
```

**Source:** ** https://vim.fandom.com/wiki/Console-like_fonts_for_Windows_GVim
***
# Title: Mouse and UI Enhancements
# Category: ui
# Tags: interface, mouse-support, display
---
Enable mouse support and improve user interface with minimal configuration

```vim
" UI and mouse settings
if has('mouse')
  set mouse=a
endif
set number
set ruler
set laststatus=2
set cmdheight=2
```
```lua
-- Neovim UI and mouse configuration
if vim.fn.has('mouse') == 1 then
  vim.opt.mouse = 'a'
end
vim.opt.number = true
vim.opt.ruler = true
vim.opt.laststatus = 2
vim.opt.cmdheight = 2
```

**Source:** ** https://vim.fandom.com/wiki/Example_Vimrc
***
# Title: Toggle Line Numbers Easily
# Category: ui
# Tags: toggle, display, line-numbers
---
Quickly toggle line numbers on and off with a simple command

```vim
set nu!
:set nu!
```
```lua
vim.opt.number = not vim.opt.number:get()
```

**Source:** ** https://vim.fandom.com/wiki/From_Vim_Help/2008
***
# Title: Full Mouse Support in Console Vim
# Category: ui
# Tags: mouse, terminal, interaction
---
Enable full mouse support in console Vim, including scrolling and clicking, making terminal Vim more interactive

```vim
set mouse=a
```
```lua
vim.opt.mouse = 'a'
```

**Source:** ** https://vim.fandom.com/wiki/Great_wildmode/wildmenu_and_console_mouse
***
# Title: Toggle GUI Elements Dynamically
# Category: ui
# Tags: gui, interface, customization
---
Easily toggle visibility of menu bar, toolbar, and scrollbars in Neovim GUI

```vim
" Toggle menu bar
nnoremap <C-F1> :if &go=~#'m'<Bar>set go-=m<Bar>else<Bar>set go+=m<Bar>endif<CR>

" Toggle toolbar
nnoremap <C-F2> :if &go=~#'T'<Bar>set go-=T<Bar>else<Bar>set go+=T<Bar>endif<CR>

" Toggle right scrollbar
nnoremap <C-F3> :if &go=~#'r'<Bar>set go-=r<Bar>else<Bar>set go+=r<Bar>endif<CR>
```
```lua
-- Toggle menu bar
vim.keymap.set('n', '<C-F1>', function()
  local current_opts = vim.o.guioptions
  vim.o.guioptions = current_opts:find('m') and current_opts:gsub('m', '') or current_opts .. 'm'
end, { desc = 'Toggle menu bar' })

-- Toggle toolbar
vim.keymap.set('n', '<C-F2>', function()
  local current_opts = vim.o.guioptions
  vim.o.guioptions = current_opts:find('T') and current_opts:gsub('T', '') or current_opts .. 'T'
end, { desc = 'Toggle toolbar' })

-- Toggle right scrollbar
vim.keymap.set('n', '<C-F3>', function()
  local current_opts = vim.o.guioptions
  vim.o.guioptions = current_opts:find('r') and current_opts:gsub('r', '') or current_opts .. 'r'
end, { desc = 'Toggle right scrollbar' })
```

**Source:** ** https://vim.fandom.com/wiki/Hide_specific_ToolBar_buttons
***
# Title: Remove Specific Toolbar Buttons
# Category: ui
# Tags: customization, toolbar, interface
---
Remove specific buttons from the GUI toolbar to simplify interface

```vim
" Remove specific toolbar buttons
aunmenu ToolBar.FindNext
aunmenu ToolBar.FindPrev
```
```lua
-- Remove specific toolbar buttons
-- Note: This might require a plugin or custom implementation in Neovim
-- Consult your specific GUI configuration for exact method
```

**Source:** ** https://vim.fandom.com/wiki/Hide_specific_ToolBar_buttons
***
# Title: Toggle GUI Elements Dynamically
# Category: ui
# Tags: gui, configuration, key-mapping
---
Add key mappings to dynamically toggle menu bar, toolbar, and scrollbars in Neovim GUI

```vim
nnoremap <C-F1> :if &go=~#'m'<Bar>set go-=m<Bar>else<Bar>set go+=m<Bar>endif<CR>
nnoremap <C-F2> :if &go=~#'T'<Bar>set go-=T<Bar>else<Bar>set go+=T<Bar>endif<CR>
nnoremap <C-F3> :if &go=~#'r'<Bar>set go-=r<Bar>else<Bar>set go+=r<Bar>endif<CR>
```
```lua
vim.keymap.set('n', '<C-F1>', function()
  local go = vim.o.guioptions
  vim.o.guioptions = go:match('m') and go:gsub('m', '') or go .. 'm'
end, { desc = 'Toggle menu bar' })

vim.keymap.set('n', '<C-F2>', function()
  local go = vim.o.guioptions
  vim.o.guioptions = go:match('T') and go:gsub('T', '') or go .. 'T'
end, { desc = 'Toggle toolbar' })

vim.keymap.set('n', '<C-F3>', function()
  local go = vim.o.guioptions
  vim.o.guioptions = go:match('r') and go:gsub('r', '') or go .. 'r'
end, { desc = 'Toggle right scrollbar' })
```

**Source:** ** https://vim.fandom.com/wiki/Hide_toolbar
***
# Title: Highlight Inserted Text in Insert Mode
# Category: ui
# Tags: highlight, insert-mode, visual-feedback
---
Dynamically highlight text as you type in insert mode, providing visual feedback and helping track text insertion

```vim
highlight Inserted ctermfg=red guifg=red
function! s:AddHighlight() abort
  let [_, lnum, col; rest] = getpos('.')
  let w:insert_hl = matchadd('Inserted', '\%'.col.'c\%'.lnum.'l\_.*\%#')
endfunction

function! s:DeleteHighlight() abort
  if exists('w:insert_hl')
      call matchdelete(w:insert_hl)
  endif
endfunction

augroup InsertHL
  autocmd!
  autocmd InsertEnter * call s:AddHighlight()
  autocmd InsertLeave * call s:DeleteHighlight()
augroup END
```
```lua
vim.api.nvim_create_augroup('InsertHL', { clear = true })

vim.api.nvim_create_autocmd('InsertEnter', {
  group = 'InsertHL',
  callback = function()
    local col = vim.fn.col('.')
    local row = vim.fn.line('.')
    vim.api.nvim_buf_add_highlight(0, -1, 'Inserted', row-1, col-1, -1)
  end
})

vim.api.nvim_create_autocmd('InsertLeave', {
  group = 'InsertHL',
  callback = function()
    vim.api.nvim_buf_clear_namespace(0, -1, 0, -1)
  end
})

vim.cmd('highlight Inserted ctermfg=red guifg=red')
```

**Source:** ** https://vim.fandom.com/wiki/Highlight_inserted_text_in_insert_mode
***
# Title: Use Tearoff Menus with Keyboard Shortcuts
# Category: ui
# Tags: gui, menu-navigation, keyboard-shortcut
---
Activate tearoff menus using Alt+Menu Hotletter to open menus in a separate window, enabling faster keyboard-driven menu interaction

```vim
" Enable tearoff menus
set guioptions+=t
```
```lua
-- Enable tearoff menus in Neovim
vim.opt.guioptions:append('t')
```

**Source:** ** https://vim.fandom.com/wiki/Make_great_use_of_those_homemade_menus
***
# Title: Prevent Mouse Drag from Entering Visual Mode
# Category: ui
# Tags: mouse, visual-mode, configuration
---
Disable automatic visual mode selection when mouse dragging in Vim, preventing unintended text selection

```vim
noremap <LeftDrag> <LeftMouse>
noremap! <LeftDrag> <LeftMouse>
```
```lua
vim.keymap.set({'n', '!'}, '<LeftDrag>', '<LeftMouse>', { noremap = true })
```

**Source:** ** https://vim.fandom.com/wiki/Make_mouse_drag_not_select_text_or_go_into_visual_mode
***
# Title: Disable Mouse Interaction in Vim
# Category: ui
# Tags: mouse, configuration
---
Completely disable mouse interaction in Vim to prevent unintended mode switches or selections

```vim
set mouse=
```
```lua
vim.opt.mouse = ''
```

**Source:** ** https://vim.fandom.com/wiki/Make_mouse_drag_not_select_text_or_go_into_visual_mode
***
# Title: Highlight Matching Braces Instantly
# Category: ui
# Tags: highlight, editing
---
Configure instant brace matching with configurable display time

```vim
set showmatch
set matchtime=3  " Highlight for 300ms
```
```lua
vim.opt.showmatch = true
vim.opt.matchtime = 3
```

**Source:** ** https://vim.fandom.com/wiki/Match_It_Plugin
***
# Title: Show Matching Braces Briefly
# Category: ui
# Tags: syntax-highlighting, editing-experience
---
Configure showmatch to briefly highlight matching braces when typing closing brackets

```vim
set showmatch
set matchtime=3
```
```lua
vim.opt.showmatch = true
vim.opt.matchtime = 3
```

**Source:** ** https://vim.fandom.com/wiki/Moving_to_matching_braces
***
# Title: Non-Blinking Block Cursor in Linux Console
# Category: ui
# Tags: terminal, cursor, console
---
Disable cursor blinking in Linux console for a cleaner visual experience

```vim
if &term == "linux"
  set t_ve+=^[[?81;0;112c
endif
```
```lua
if vim.o.term == "linux" then
  vim.o.t_ve = vim.o.t_ve .. "\x1b[?81;0;112c"
end
```

**Source:** ** https://vim.fandom.com/wiki/Non-blinking_block_cursor_in_a_Linux_console
***
# Title: Show Non-Native File Format in Statusline
# Category: ui
# Tags: statusline, file-format, customization
---
Display a visual indicator when a file's format differs from the native system format, helping identify potential cross-platform issues

```vim
function ShowFileFormatFlag(var)
  if ( a:var == 'dos' )
    return '[dos]'
  elseif ( a:var == 'mac' )
    return '[mac]'
  else
    return ''
  endif
endfunction

hi User1 term=bold cterm=bold ctermfg=red ctermbg=darkblue

set statusline+=%1*%{ShowFileFormatFlag(&fileformat)}%*
```
```lua
vim.cmd('hi User1 term=bold cterm=bold ctermfg=red ctermbg=darkblue')

local function show_file_format_flag()
  local ff = vim.bo.fileformat
  if ff == 'dos' then
    return '[dos]'
  elseif ff == 'mac' then
    return '[mac]'
  else
    return ''
  end
end

vim.opt.statusline:append('%1*%{v:lua.show_file_format_flag()}%*')
```

**Source:** ** https://vim.fandom.com/wiki/Non-native_fileformat_for_your_statusline
***
# Title: Dynamic Color Scheme Switcher
# Category: ui
# Tags: color-scheme, theme, key-mapping
---
Easily cycle through Vim color schemes using function keys, with support for random and time-based color scheme selection

```vim
" Vim color scheme switching script
nnoremap <F8> :call NextColor(1)<CR>
nnoremap <S-F8> :call NextColor(-1)<CR>
nnoremap <A-F8> :call NextColor(0)<CR>
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
```

**Source:** ** https://vim.fandom.com/wiki/Rotate_color_themes
***
# Title: Time-Based Color Scheme Selection
# Category: ui
# Tags: color-scheme, time-based, theme
---
Automatically change color scheme based on time of day, providing visual variety throughout the day

```vim
function! s:HourColor()
  let hr = str2nr(strftime('%H'))
  if hr <= 3
    let i = 0
  elseif hr <= 7
    let i = 1
  elseif hr <= 14
    let i = 2
  elseif hr <= 18
    let i = 3
  else
    let i = 4
  endif
  let nowcolors = 'elflord morning desert evening pablo'
  execute 'colorscheme '.split(nowcolors)[i]
endfunction
```
```lua
local function hour_color()
  local hour = tonumber(os.date('%H'))
  local color_index = 0
  
  if hour <= 3 then color_index = 0
  elseif hour <= 7 then color_index = 1
  elseif hour <= 14 then color_index = 2
  elseif hour <= 18 then color_index = 3
  else color_index = 4 end
  
  local nowcolors = {'elflord', 'morning', 'desert', 'evening', 'pablo'}
  vim.cmd('colorscheme ' .. nowcolors[color_index + 1])
end

-- Usage: call hour_color() at startup or create a command
vim.api.nvim_create_user_command('TimeColorScheme', hour_color, {})
```

**Source:** ** https://vim.fandom.com/wiki/Rotate_color_themes
***
# Title: Quick Font Selector Keymapping
# Category: ui
# Tags: key-mapping, font, interactive
---
Provides a quick keyboard shortcut to open the font selection dialog in GUI Vim

```vim
map <F3> <Esc>:set guifont=*<CR>
```
```lua
vim.keymap.set('n', '<F3>', ':set guifont=*<CR>', { desc = 'Open Font Selector' })
```

**Source:** ** https://vim.fandom.com/wiki/VimTip632
***
# Title: Hide/Toggle GUI Elements in Neovim
# Category: ui
# Tags: gui, interface, customization
---
Easily hide or toggle menu bar, toolbar, and scrollbars to maximize screen space and simplify the interface

```vim
" Remove GUI elements
set guioptions-=m  " remove menu bar
set guioptions-=T  " remove toolbar
set guioptions-=r  " remove right-hand scroll bar
set guioptions-=L  " remove left-hand scroll bar

" Toggle menu bar with Ctrl-F1
nnoremap <C-F1> :if &go=~#'m'<Bar>set go-=m<Bar>else<Bar>set go+=m<Bar>endif<CR>
```
```lua
-- Remove GUI elements
vim.o.guioptions = vim.o.guioptions:gsub('m', '')  -- remove menu bar
vim.o.guioptions = vim.o.guioptions:gsub('T', '')  -- remove toolbar
vim.o.guioptions = vim.o.guioptions:gsub('r', '')  -- remove right scrollbar
vim.o.guioptions = vim.o.guioptions:gsub('L', '')  -- remove left scrollbar

-- Toggle menu bar with Ctrl-F1
vim.keymap.set('n', '<C-F1>', function()
  local go = vim.o.guioptions
  vim.o.guioptions = go:find('m') and go:gsub('m', '') or go .. 'm'
end, { desc = 'Toggle menu bar' })
```

**Source:** ** https://vim.fandom.com/wiki/VimTip665
***
# Title: Dynamically Switch Vim Color Schemes
# Category: ui
# Tags: color-scheme, key-mapping, customization
---
Easily cycle through available color schemes with keyboard shortcuts, including random selection and time-based color scheme switching

```vim
" Key mappings for color scheme switching
nnoremap <F8> :call NextColor(1)<CR>
nnoremap <S-F8> :call NextColor(-1)<CR>
nnoremap <A-F8> :call NextColor(0)<CR>
```
```lua
-- Color scheme switching in Neovim
vim.keymap.set('n', '<F8>', function() 
  vim.fn.NextColor(1)
end, { desc = 'Next color scheme' })

vim.keymap.set('n', '<S-F8>', function()
  vim.fn.NextColor(-1)
end, { desc = 'Previous color scheme' })

vim.keymap.set('n', '<A-F8>', function()
  vim.fn.NextColor(0)
end, { desc = 'Random color scheme' })
```

**Source:** ** https://vim.fandom.com/wiki/VimTip693
***
# Title: Customize Toolbar for Quick Launching
# Category: ui
# Tags: toolbar, customization, windows
---
Replace existing toolbar icon to launch explorer with selected URL/path

```vim
vnoremenu 1.140 ToolBar.New "wy:!start explorer <C-R>w<CR>
```
```lua
vim.cmd('vnoremenu 1.140 ToolBar.New "wy:!start explorer <C-R>w<CR>')
```

**Source:** ** https://vim.fandom.com/wiki/VimTip732
***
# Title: Display Non-Native File Format in Statusline
# Category: ui
# Tags: statusline, file-format, customization
---
Add a custom function to highlight non-native file formats in the statusline, making it easy to identify files with different line endings

```vim
function ShowFileFormatFlag(var)
  if ( a:var == 'dos' )
    return '[dos]'
  elseif ( a:var == 'mac' )
    return '[mac]'
  else
    return ''
  endif
endfunction

hi User1 term=bold cterm=bold ctermfg=red ctermbg=darkblue

set statusline+=%1*%{ShowFileFormatFlag(&fileformat)}%*
```
```lua
vim.api.nvim_create_user_command('ShowFileFormatFlag', function()
  local fileformat = vim.o.fileformat
  if fileformat == 'dos' then
    return '[dos]'
  elseif fileformat == 'mac' then
    return '[mac]'
  else
    return ''
  end
end, {})

vim.cmd.highlight('User1 term=bold cterm=bold ctermfg=red ctermbg=darkblue')

vim.o.statusline = vim.o.statusline .. '%1*%{v:lua.ShowFileFormatFlag()}%*'
```

**Source:** ** https://vim.fandom.com/wiki/VimTip736
***
# Title: Customize Vim Statusline with Dynamic Information
# Category: ui
# Tags: statusline, customization, ui-enhancement
---
Create a comprehensive statusline that displays file details, cursor position, and timestamp dynamically

```vim
set statusline=%F%m%r%h%w\ [FORMAT=%{&ff}]\ [TYPE=%Y]\ [POS=%l,%v][%p%%]\ %{strftime("%d/%m/%y\ -\ %H:%M")}
```
```lua
vim.opt.statusline = table.concat({
  '%F%m%r%h%w',
  ' [FORMAT=%{&ff}]',
  ' [TYPE=%Y]',
  ' [POS=%l,%v][%p%%]',
  ' %{strftime("%d/%m/%y - %H:%M")}'
}, '')
```

**Source:** ** https://vim.fandom.com/wiki/VimTip739
***
# Title: Always Show Statusline in Single Window
# Category: ui
# Tags: statusline, ui-configuration
---
Ensure the statusline is always visible, even in single window mode

```vim
set laststatus=2
```
```lua
vim.opt.laststatus = 2
```

**Source:** ** https://vim.fandom.com/wiki/VimTip739
***
# Title: Dynamically Adjust Font Size in GUI
# Category: ui
# Tags: font-size, gui, configuration
---
Provides a flexible function to incrementally adjust font size in GUI Vim/Neovim with min and max size constraints

```vim
function! AdjustFontSize(amount)
  if has("gui_gtk2") && has("gui_running")
    let fontname = substitute(&guifont, s:pattern, '\1', '')
    let cursize = substitute(&guifont, s:pattern, '\2', '')
    let newsize = cursize + a:amount
    if (newsize >= s:minfontsize) && (newsize <= s:maxfontsize)
      let newfont = fontname . newsize
      let &guifont = newfont
    endif
  endif
endfunction
```
```lua
function _G.adjust_font_size(amount)
  if vim.fn.has('gui_running') == 1 then
    local guifont = vim.o.guifont
    local font_name = guifont:match('^(.*):h')
    local current_size = tonumber(guifont:match(':h(%d+)'))
    local new_size = current_size + amount
    
    if new_size >= 6 and new_size <= 16 then
      vim.o.guifont = string.format('%s:h%d', font_name, new_size)
    end
  end
end

-- Optional mappings
vim.keymap.set('n', '<C-Up>', function() _G.adjust_font_size(1) end)
vim.keymap.set('n', '<C-Down>', function() _G.adjust_font_size(-1) end)
```

**Source:** ** https://vim.fandom.com/wiki/VimTip760
***
# Title: Cross-Platform Font Size Management
# Category: ui
# Tags: cross-platform, font-size, gui
---
Robust multiplatform implementation for font size adjustment supporting Linux, Windows, and macOS

```vim
function! GetFontInfo()
  let l:font_name_pattern = '\v(^.{-1,})( \d+$)@='
  let l:font_size_pattern = '\v(\d+$)'
  let l:font_name = matchstr(&guifont, l:font_name_pattern)
  let l:font_size = matchstr(&guifont, l:font_size_pattern)
  return { 'name': l:font_name, 'size': l:font_size }
endfunction
```
```lua
local function get_font_info()
  local guifont = vim.o.guifont
  local font_name = guifont:match('^(.+)%s*%d+$')
  local font_size = guifont:match('(%d+)$')
  
  return {
    name = font_name or '',
    size = font_size or ''
  }
end

-- Optional mouse wheel zoom
vim.keymap.set('n', '<C-ScrollWheelUp>', function()
  local font_info = get_font_info()
  -- Implement font size increase logic
end)

vim.keymap.set('n', '<C-ScrollWheelDown>', function()
  local font_info = get_font_info()
  -- Implement font size decrease logic
end)
```

**Source:** ** https://vim.fandom.com/wiki/VimTip760
***
