# Title: Send commands to terminal
# Category: Terminal
# Tags: terminal, command, send
---
Use `vim.api.nvim_chan_send()` to send commands to terminal buffer from Lua.

```vim
:lua vim.api.nvim_chan_send(terminal_job_id, "ls\n")
```

**Source:** Community contributed
***
# Title: Terminal mode - exit to normal mode
# Category: Terminal
# Tags: terminal, mode, exit, normal
---
Use `Ctrl+\ Ctrl+n` to exit terminal mode and go to normal mode.

```vim
" In terminal mode:
Ctrl+\ Ctrl+n  " exit to normal mode
```

**Source:** Community contributed
***
# Title: Terminal mode - execute one command
# Category: Terminal
# Tags: terminal, mode, execute, command
---
Use `Ctrl+\ Ctrl+o` to execute one normal mode command and return to terminal mode.

```vim
" In terminal mode:
Ctrl+\ Ctrl+o  " execute one normal mode command
```

**Source:** Community contributed
***
# Title: Terminal mode - key forwarding
# Category: Terminal
# Tags: terminal, keys, forwarding, passthrough
---
All keys except `Ctrl+\` are forwarded directly to the terminal job. Use `Ctrl+\` as escape prefix for Neovim commands.

```vim
" In terminal mode:
ls<Enter>           " sent to terminal
Ctrl+c              " sent to terminal (interrupt)
Ctrl+\ Ctrl+n       " Neovim command (exit to normal)
```

**Source:** Community contributed
***
# Title: Open terminal in current window
# Category: Terminal
# Tags: terminal, open, current, window
---
Use `:terminal` or `:term` to open terminal in current window.

```vim
:terminal     " open terminal in current window
:term         " shorthand for :terminal
:term bash    " open specific shell
```

**Source:** Community contributed
***
# Title: Open terminal in new window
# Category: Terminal
# Tags: terminal, window, split, tab
---
Use `:sp | terminal` for horizontal split, `:vsp | terminal` for vertical split, `:tabe | terminal` for new tab.

```vim
:sp | terminal   " horizontal split terminal
:vsp | terminal  " vertical split terminal  
:tabe | terminal " terminal in new tab
```

**Source:** Community contributed
***
# Title: Terminal scrollback buffer
# Category: Terminal
# Tags: terminal, scrollback, buffer, history
---
In normal mode, you can navigate terminal scrollback buffer like any other buffer using standard movement commands.

```vim
" In terminal normal mode (after Ctrl+\ Ctrl+n):
gg    " go to top of scrollback
G     " go to bottom  
/text " search in terminal output
```

**Source:** Community contributed
***
# Title: Terminal insert mode
# Category: Terminal
# Tags: terminal, insert, mode, interaction
---
Use `i`, `a`, or `A` to return to terminal mode from normal mode for terminal interaction.

```vim
" From terminal normal mode:
i   " enter terminal mode at cursor
a   " enter terminal mode after cursor  
A   " enter terminal mode at end of line
```

**Source:** Community contributed
***
# Title: Create Custom Terminal Vim Wrapper Script
# Category: terminal
# Tags: external-editor, terminal-integration, shell-script
---
Create a wrapper script to open Vim in a terminal with support for command-line arguments

```vim
#!/bin/sh
ARGS="$@"
gnome-terminal "vim $ARGS"
```
```lua
-- Lua equivalent would typically be a shell script or can be implemented using vim.fn.system()
-- Example Lua wrapper function:
function OpenVimInTerminal(args)
  vim.fn.system(string.format('gnome-terminal "vim %s"', args))
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Alternative_to_gvim_as_external_pop-up_editor:_vim_%2B_gnome-terminal)
***
# Title: Keep Terminal Open After Vim Exit
# Category: terminal
# Tags: terminal-integration, workflow
---
Modify terminal wrapper to keep the terminal window open after exiting Vim

```vim
#!/bin/sh
ARGS="$@"
gnome-terminal "vim $ARGS; $SHELL"
```
```lua
-- Lua equivalent for shell script behavior
function OpenVimWithShell(args)
  vim.fn.system(string.format('gnome-terminal "vim %s; $SHELL"', args))
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Alternative_to_gvim_as_external_pop-up_editor:_vim_%2B_gnome-terminal)
***
# Title: Run External Commands Asynchronously in Windows
# Category: terminal
# Tags: external-commands, async, windows
---
Run console or GUI applications asynchronously without blocking Vim, with options to pause or keep the window open

```vim
" Run compiled program for current source file
nnoremap <silent> <F5> :!start cmd /c "%:p:r:s,$,.exe," & pause<CR>
```
```lua
-- Run compiled program asynchronously
vim.keymap.set('n', '<F5>', function()
  vim.cmd('!start cmd /c "' .. vim.fn.expand('%:p:r') .. '.exe" & pause')
end, { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Async_command)
***
# Title: Capture SQL Query Output in Vim
# Category: terminal
# Tags: sql, command-line, external-tools
---
Pipe SQL query results directly into Vim for easy viewing and manipulation of database query outputs

```vim
" MySQL CLI: Use pager to send query results to Vim
:pager vim -
```
```lua
-- Equivalent approach would be to use vim.fn.system() or terminal buffer
-- Example with MySQL CLI
-- In terminal: mysql -u user -p database
-- Then: pager vim -
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Capture_SQL_query_output)
***
# Title: tmux-Compatible Cursor Configuration
# Category: terminal
# Tags: tmux, cursor, terminal-config
---
Special configuration for cursor appearance and color in tmux environment

```vim
if exists('$TMUX')
  " set insert mode to cyan vertical line
  let &t_SI .= "\<esc>Ptmux;\<esc>\<esc>[6 q\<esc>\\"
  let &t_SI .= "\<esc>Ptmux;\<esc>\<esc>]12;cyan\x7\<esc>\\"
  
  " set normal mode to green block
  let &t_EI .= "\<esc>Ptmux;\<esc>\<esc>[2 q\<esc>\\"
  let &t_EI .= "\<esc>Ptmux;\<esc>\<esc>]12;green\x7\<esc>\\"
endif
```
```lua
if vim.env.TMUX then
  local function tmux_cursor_style()
    -- Insert mode: cyan vertical line
    vim.cmd('let &t_SI .= "\\<esc>Ptmux;\\<esc>\\<esc>[6 q\\<esc>\\\\"')
    vim.cmd('let &t_SI .= "\\<esc>Ptmux;\\<esc>\\<esc>]12;cyan\\x7\\<esc>\\\\"')
    
    -- Normal mode: green block
    vim.cmd('let &t_EI .= "\\<esc>Ptmux;\\<esc>\\<esc>[2 q\\<esc>\\\\"')
    vim.cmd('let &t_EI .= "\\<esc>Ptmux;\\<esc>\\<esc>]12;green\\x7\\<esc>\\\\"')
  end
  
  tmux_cursor_style()
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Change_cursor_color_in_different_modes)
***
# Title: Run Shell Commands in Vim Scratch Buffer
# Category: terminal
# Tags: shell-command, command-line, buffer-management
---
Create a custom command to run shell commands in a new scratch buffer, allowing easy command execution and output viewing within Vim

```vim
command! -complete=shellcmd -nargs=+ Shell call s:RunShellCommand(<q-args>)

function! s:RunShellCommand(cmdline)
  botright new
  setlocal buftype=nofile bufhidden=wipe nobuflisted noswapfile nowrap
  call setline(1, 'You entered:    ' . a:cmdline)
  execute '$read !'. a:cmdline
  setlocal nomodifiable
  1
endfunction
```
```lua
vim.api.nvim_create_user_command('Shell', function(opts)
  local cmdline = opts.args
  local bufnr = vim.api.nvim_create_buf(false, true)
  vim.api.nvim_command('botright split')
  vim.api.nvim_win_set_buf(0, bufnr)
  
  vim.api.nvim_buf_set_option(bufnr, 'buftype', 'nofile')
  vim.api.nvim_buf_set_option(bufnr, 'bufhidden', 'wipe')
  vim.api.nvim_buf_set_option(bufnr, 'swapfile', false)
  
  vim.api.nvim_buf_set_lines(bufnr, 0, -1, false, {'You entered: ' .. cmdline})
  
  local output = vim.fn.systemlist(cmdline)
  vim.api.nvim_buf_set_lines(bufnr, 1, -1, false, output)
  vim.api.nvim_buf_set_option(bufnr, 'modifiable', false)
  vim.api.nvim_win_set_cursor(0, {1, 0})
end, {nargs = '+', complete = 'shellcmd'})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Display_output_of_shell_commands_in_new_window)
***
# Title: Quick Version Control Commands in Vim
# Category: terminal
# Tags: git, version-control, command-line
---
Create shortcut commands for running version control operations directly from Vim

```vim
command! -complete=file -nargs=* Git call s:RunShellCommand('git '.<q-args>)
command! -complete=file -nargs=* Svn call s:RunShellCommand('svn '.<q-args>)
command! -complete=file -nargs=* Hg call s:RunShellCommand('hg '.<q-args>)
```
```lua
local function run_vcs_command(vcs, args)
  vim.api.nvim_create_user_command(vcs:upper(), function(opts)
    local full_cmd = string.format('%s %s', vcs, opts.args)
    vim.fn.system(full_cmd)
    print(full_cmd .. ' executed')
  end, { nargs = '*', complete = 'file' })
end

run_vcs_command('git')
run_vcs_command('svn')
run_vcs_command('hg')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Display_shell_commands%27_output_on_Vim_window)
***
# Title: Interactive Database Querying with Perl in Vim
# Category: terminal
# Tags: database, perl, external-integration
---
Use Vim's embedded Perl interpreter to connect to databases and manipulate data directly within the editor

```vim
" connect to perl's dbi module:
:perl use dbi;
" connect to the database:
:perl $dbh = dbi->connect( "DBI:mysql:$DBNAME:$HOST",$USER,$PASSWORD,
 { raiseerror => 1});
" perform a simple query:
:perl $result = $dbh->selectall_arrayref("show tables;");
" insert the list of tables into the current buffer's top:
:perl $curbuf->Append(0, map($_->[0], @{$result}));
```
```lua
-- Note: Requires Vim to be compiled with Perl support
-- Use :terminal and external psql/mysql commands in Neovim
vim.api.nvim_command('!psql -d my_database -c "show tables;"')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Editing_databases_with_Vim/Perl/DBI)
***
# Title: Quick SQL Query Execution in Vim
# Category: terminal
# Tags: sql, database, external-command
---
Filter selected SQL through an external database command and replace text with query results

```vim
:!psql -d my_database -f %
```
```lua
-- Execute SQL file through psql
vim.api.nvim_command('!psql -d my_database -f ' .. vim.fn.expand('%:p'))
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Editing_databases_with_Vim/Perl/DBI)
***
# Title: Enable Vim Server in Terminal
# Category: terminal
# Tags: client-server, remote-editing, vim-interaction
---
Add servername capability to Vim in terminal, allowing remote file editing and server interactions

```vim
vim --servername vim
```
```lua
-- Check if server is running
vim.fn.serverlist()

-- Start a named server
vim.fn.servername('myserver')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Enable_servername_capability_in_vim/xterm)
***
# Title: Smart Vim Server Function for Shell
# Category: terminal
# Tags: shell-function, client-server, workflow
---
Intelligent shell function to always use a single Vim server, creating one if none exists

```vim
function! VimServerWrapper()
  if serverlist() == ''
    call server2client('vim --servername VIM')
  endif
endfunction
```
```lua
function _G.smart_vim_server()
  local servers = vim.fn.serverlist()
  if servers == '' then
    vim.cmd('vim --servername VIM')
  end
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Enable_servername_capability_in_vim/xterm)
***
# Title: Quick Python Code Execution in Vim
# Category: terminal
# Tags: python, execution, quick-run
---
Simple mappings to quickly run Python scripts or selected code directly from Vim

```vim
" Save and run current file
noremap <F5> <ESC>:w<CR>:silent execute "!python %"<CR><CR>

" Run selected lines in Python
vnoremap <f5> :!python<CR>
```
```lua
vim.keymap.set('n', '<F5>', function()
  vim.cmd.write()
  vim.cmd.silent('!python %')
end, { desc = 'Run current Python file' })

vim.keymap.set('v', '<F5>', ':!python<CR>', { desc = 'Run selected Python code' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Execute_Python_from_within_current_file)
***
# Title: Quick IPython Integration with Vim
# Category: terminal
# Tags: python, integration, terminal-commands
---
Send commands from Vim to an IPython session using screen or terminal control

```vim
" Save and run current buffer in IPython session
nnoremap ' :wa<CR>:!screen -x ipython_vim -X stuff $'%run "%:p"
'<CR><CR>

" Open a new terminal with IPython in screen
com OpenIPython :!konsole -e screen -S ipython_vim ipython
```
```lua
-- Lua equivalent for IPython integration
vim.keymap.set('n', "'", function()
  vim.cmd('wa')  -- Save all buffers
  vim.fn.system('screen -x ipython_vim -X stuff "\%run ' .. vim.fn.expand('%:p') .. '\n"')
end, { desc = 'Run current file in IPython' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/IPython_integration)
***
# Title: Integrate PyUnit Testing in Vim/Neovim
# Category: terminal
# Tags: python, testing, quickfix, integration
---
Configure Vim/Neovim to run Python unit tests and navigate test results using quickfix mode

```vim
" Set PyUnit as compiler
:compiler pyunit

" Set test runner script
:setlocal makeprg=./alltests.py
```
```lua
-- Set PyUnit compiler for Python files
vim.api.nvim_create_autocmd('FileType', {
  pattern = 'python',
  callback = function()
    vim.cmd('compiler pyunit')
    vim.opt_local.makeprg = './alltests.py'
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Integration_with_PyUnit_testing_framework)
***
# Title: Dynamically Rename Konsole Tab in Vim
# Category: terminal
# Tags: terminal-integration, session-management, kde
---
Automatically rename Konsole tab to current file name or working directory, providing context in terminal sessions

```vim
" KDE3 Rename to current file
autocmd BufReadPost * :silent !dcop $KONSOLE_DCOP_SESSION renameSession %

" Rename to working directory when leaving Vim
autocmd VimLeavePre * :silent !dcop $KONSOLE_DCOP_SESSION renameSession $PWD
```
```lua
-- KDE4/5 Konsole tab renaming
vim.api.nvim_create_autocmd('BufReadPost', {
  callback = function()
    vim.fn.system('update_konsole_tab set "vim: ' .. vim.fn.expand('%:t') .. '"')
  end
})

vim.api.nvim_create_autocmd('VimLeavePre', {
  callback = function()
    vim.fn.system('update_konsole_tab clean')
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/KDE_Konsole_renameSession_to_edited_file_name)
***
# Title: Quick Terminal Window Maximize/Restore
# Category: terminal
# Tags: terminal, window-management
---
Simple terminal control sequences to maximize and restore window size

```vim
" Maximize window
echo -ne '\e[9;1t'

" Restore window
echo -ne '\e[9;0t'
```
```lua
-- Maximize window
vim.fn.system('echo -ne "\e[9;1t"')

-- Restore window
vim.fn.system('echo -ne "\e[9;0t"')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Resize_xterm_when_running_vimdiff)
***
# Title: Run MATLAB Scripts from Vim
# Category: terminal
# Tags: matlab, python-integration, external-execution
---
Execute MATLAB scripts directly from Vim using Python and Win32 COM interface

```vim
if has("win32")
  :py from win32com.client import Dispatch
  :py import vim
  :py h=Dispatch('matlab.application')
  map <buffer> ,r :w<CR>:py print h.Execute(vim.eval('expand("%:t:r")'))<CR>
endif
```
```lua
if vim.fn.has('win32') == 1 then
  local dispatch = require('pythonx.win32com.client').Dispatch
  local h = dispatch('matlab.application')
  vim.keymap.set('n', ',r', function()
    vim.cmd('write')
    local script_name = vim.fn.expand('%:t:r')
    print(h:Execute(script_name))
  end, { buffer = true })
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Run_Matlab_script_under_Windows)
***
# Title: Quick Shell Command Switching with Ctrl-Z
# Category: terminal
# Tags: shell-interaction, command-line, workflow
---
Use Ctrl-Z to suspend Vim and return to shell, then 'fg' to resume editing. Useful for quickly running shell commands without opening multiple terminal windows.

```vim
# Shell feature, not Vimscript specific
# Ctrl-Z to suspend
# fg to return to Vim
```
```lua
-- Lua can't directly implement shell suspend, but demonstrates shell interaction
-- Use :terminal or external shell commands
vim.keymap.set('n', '<leader>sh', ':terminal<CR>', { desc = 'Open terminal' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip535)
***
# Title: Screen Session Vim Integration
# Category: terminal
# Tags: screen, multi-terminal, workflow
---
Open Vim inside a screen session with a small delay to prevent file deletion issues

```vim
" Bash script for screen vim integration
screen -X screen /usr/bin/vim $@
sleep .2 # Prevent file deletion
```
```lua
-- Lua equivalent using vim.fn and os.execute
local function open_vim_in_screen(file)
  os.execute('screen -X screen /usr/bin/vim ' .. file)
  vim.fn.system('sleep 0.2')  -- Small delay
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip581)
***
# Title: Check Existing Vim Server Instances
# Category: terminal
# Tags: server, cli, remote-editing
---
List active Vim server instances to check if a server is already running

```vim
vim --serverlist
```
```lua
-- Check server list
-- Note: May require external command execution
vim.fn.system('vim --serverlist')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip699)
***
