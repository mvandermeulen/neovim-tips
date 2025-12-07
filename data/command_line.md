# Title: Command line editing
# Category: Command Line
# Tags: command, edit, navigation
---
Use `Ctrl+b` to go to beginning of line, `Ctrl+e` to end, `Ctrl+h` to delete character, `Ctrl+w` to delete word.

```vim
:Ctrl+b  " go to beginning of command line
:Ctrl+e  " go to end of command line
:Ctrl+h  " delete character backward
:Ctrl+w  " delete word backward
```

**Source:** ** Community contributed
***
# Title: Command-line cursor movement
# Category: Command Line
# Tags: command, cursor, movement, navigation
---
Use arrow keys or `Ctrl+b`/`Ctrl+e` for movement, `Shift+Left`/`Shift+Right` or `Ctrl+Left`/`Ctrl+Right` for word movement.

```vim
" In command mode:
<Left>/<Right>     " move cursor by character
Ctrl+b/Ctrl+e      " move to beginning/end of line
Shift+Left/Right   " move by word
Ctrl+Left/Right    " move by word (alternative)
```

**Source:** ** Community contributed
***
# Title: Command-line deletion operations
# Category: Command Line
# Tags: command, delete, backspace, clear
---
Use `Backspace` or `Ctrl+h` to delete character, `Del` to delete forward, `Ctrl+w` to delete word, `Ctrl+u` to clear line.

```vim
" In command mode:
<BS>/Ctrl+h  " delete character backward
<Del>        " delete character forward
Ctrl+w       " delete word backward
Ctrl+u       " clear from cursor to beginning
```

**Source:** ** Community contributed
***
# Title: Command-line history with filtering
# Category: Command Line
# Tags: command, history, filter, search
---
Use `Shift+Up`/`Shift+Down` or `PageUp`/`PageDown` to recall commands that start with current text.

```vim
" Type partial command, then:
:se<Shift+Up>    " find previous commands starting with 'se'
:ed<PageDown>    " find next commands starting with 'ed'
```

**Source:** ** Community contributed
***
# Title: Command-line completion modes
# Category: Command Line
# Tags: command, completion, tab, modes
---
Use `Tab` for next completion, `Shift+Tab` for previous, `Ctrl+d` to list all, `Ctrl+a` to insert all matches, `Ctrl+l` for longest common part.

```vim
" In command mode:
:e <Tab>        " complete filename
:e <Shift+Tab>  " previous completion
:set <Ctrl+d>   " list all completions
:b <Ctrl+a>     " insert all buffer matches
:help <Ctrl+l>  " complete to longest common part
```

**Source:** ** Community contributed
***
# Title: Command-line register insertion
# Category: Command Line
# Tags: command, register, insert, content
---
Use `Ctrl+r` followed by register name to insert register contents into command line.

```vim
" In command mode:
:Ctrl+r "     " insert default register
:Ctrl+r a     " insert register 'a'
:Ctrl+r %     " insert current filename
:Ctrl+r :     " insert last command
:Ctrl+r /     " insert last search pattern
```

**Source:** ** Community contributed
***
# Title: Command-line literal insertion
# Category: Command Line
# Tags: command, literal, insert, special
---
Use `Ctrl+v` or `Ctrl+q` to insert the next character literally (useful for special characters).

```vim
" In command mode:
:echo "Ctrl+v<Tab>"   " insert literal tab character
:s/Ctrl+v<Esc>/x/g    " search for literal Esc character
```

**Source:** ** Community contributed
***
# Title: Command-line mode switching
# Category: Command Line
# Tags: command, mode, switch, abandon
---
Use `Ctrl+c` or `Esc` to abandon command, `Ctrl+\ Ctrl+n` or `Ctrl+\ Ctrl+g` to go to normal mode.

```vim
" In command mode:
Ctrl+c           " abandon command without executing
<Esc>            " abandon command (alternative)
Ctrl+\ Ctrl+n    " go to normal mode
Ctrl+\ Ctrl+g    " go to normal mode (alternative)
```

**Source:** ** Community contributed
***
# Title: Command-line window access
# Category: Command Line
# Tags: command, window, edit, history
---
Use `Ctrl+f` to open command-line window for full editing, `Ctrl+o` to execute one normal mode command.

```vim
" In command mode:
Ctrl+f  " open command-line window for editing
Ctrl+o  " execute one normal mode command and return
```

**Source:** ** Community contributed
***
# Title: Command-line word manipulation
# Category: Command Line
# Tags: command, word, delete, kill, clear
---
Use `Ctrl+w` to delete word before cursor, `Ctrl+u` to delete from cursor to beginning of line.

```vim
" In command mode:
Ctrl+w  " delete word before cursor
Ctrl+u  " delete from cursor to beginning
Ctrl+k  " delete from cursor to end of line
```

**Source:** ** Community contributed
***
# Title: Perl Syntax Checking in Vim
# Category: command_line
# Tags: perl, syntax-checking, error-handling
---
Configures Vim to run Perl syntax checks and parse errors, allowing quick navigation to error locations

```vim
" Compiler configuration for Perl
setlocal errorformat=%f:%l:\ %m
setlocal makeprg=perl\ -MVimCompile\ -c\ %
```
```lua
-- Lua equivalent for Perl syntax checking
vim.opt.errorformat = '%f:%l: %m'
vim.opt.makeprg = 'perl -MVimCompile -c %'
```

**Source:** ** https://vim.fandom.com/wiki/%22compiler%22_for_perl
***
# Title: Capture External Command Output Flexibly
# Category: command_line
# Tags: shell-integration, system-command, text-manipulation
---
Provides multiple methods to capture and insert output from shell commands into Vim buffers, with flexibility for different use cases

```vim
" Append shell command output to current line
function! GetDate(format)
  let format = empty(a:format) ? '+%A %Y-%m-%d %H:%M UTC' : a:format
  let cmd = '/bin/date -u ' . shellescape(format)
  let result = substitute(system(cmd), '[\]
|[[:cntrl:]]', '', 'g')
  call setline(line('.'), getline('.') . ' ' . result)
endfunction

" Custom command to open new buffer with command output
:command! -nargs=* -complete=shellcmd R new | setlocal buftype=nofile bufhidden=hide noswapfile | r !<args>
```
```lua
-- Lua equivalent for appending command output
function _G.get_date(format)
  format = format == '' and '+%A %Y-%m-%d %H:%M UTC' or format
  local cmd = string.format('/bin/date -u %s', vim.fn.shellescape(format))
  local result = vim.fn.system(cmd):gsub('[\n\r\t]', '')
  local current_line = vim.api.nvim_get_current_line()
  vim.api.nvim_set_current_line(current_line .. ' ' .. result)
end

-- Create custom command for shell output
vim.api.nvim_create_user_command('R', function(opts)
  vim.cmd('new')
  vim.bo.buftype = 'nofile'
  vim.bo.bufhidden = 'hide'
  vim.bo.swapfile = false
  vim.cmd('read !' .. opts.args)
end, { nargs = '*', complete = 'shellcmd' })
```

**Source:** ** https://vim.fandom.com/wiki/Append_output_of_an_external_command
***
# Title: Execute Commands Across Line Ranges
# Category: command_line
# Tags: range-command, global-command, advanced-editing
---
Apply any command to a specific line range using global command with empty pattern

```vim
:n1,n2 g/^/ command
```
```lua
-- Lua equivalent would typically be a function or use vim.cmd
-- Example: Execute command on lines 5-10
vim.cmd('5,10g/^/ echo "Processing line"')
```

**Source:** ** https://vim.fandom.com/wiki/Apply_range_to_any_command_that_does_not_accept_ranges
***
# Title: Custom Make Command with Quickfix
# Category: command_line
# Tags: custom-command, build, workflow
---
Create a custom :Make command that runs make and automatically opens quickfix window if errors exist

```vim
:command -nargs=* Make make <args> | cwindow 3
```
```lua
vim.api.nvim_create_user_command('Make', function(opts)
  vim.cmd('make ' .. opts.args)
  vim.cmd('cwindow 3')
end, { nargs = '*' })
```

**Source:** ** https://vim.fandom.com/wiki/Automatically_open_the_quickfix_window_on_:make
***
# Title: Quick Firefox URL Navigation from Vim
# Category: command_line
# Tags: web-development, browser-integration, productivity
---
Add custom commands to quickly open URLs in Firefox directly from Vim

```vim
command! -nargs=1 Repl silent !echo \
      "repl.home();
      content.location.href = '<args>';
      repl.enter(content);
      repl.quit();" |
      nc localhost 4242

nmap <leader>mh :Repl http://
nmap <silent> <leader>ml :Repl file:///%:p<CR>
nmap <silent> <leader>md :Repl http://localhost/
```
```lua
vim.api.nvim_create_user_command('Repl', function(opts)
  vim.fn.system(string.format(
    'echo "repl.home(); content.location.href = \'%s\'; ' ..
    'repl.enter(content); repl.quit();" | nc localhost 4242',
    opts.args
  ))
end, { nargs = 1 })

vim.keymap.set('n', '<leader>mh', ':Repl http://', { desc = 'Open URL in Firefox' })
vim.keymap.set('n', '<leader>ml', ':Repl file://' .. vim.fn.expand('%:p') .. '<CR>', { desc = 'Open current file in Firefox' })
vim.keymap.set('n', '<leader>md', ':Repl http://localhost/<CR>', { desc = 'Open localhost in Firefox' })
```

**Source:** ** https://vim.fandom.com/wiki/Automatically_refresh_display_of_html_on_saving_file
***
# Title: Silent External Command Execution
# Category: command_line
# Tags: external-commands, workflow, productivity
---
Execute external commands silently without interrupting workflow

```vim
command! -nargs=1 Silent
    execute 'silent !' . <q-args>
    | execute 'redraw!'
```
```lua
-- Create a silent command executor
vim.api.nvim_create_user_command('Silent', function(ctx)
    vim.fn.system(ctx.args)
    vim.cmd.redraw()
end, { nargs = 1 })
```

**Source:** ** https://vim.fandom.com/wiki/Avoid_hit_enter
***
# Title: Silent External Command Execution
# Category: command_line
# Tags: shell, external-commands, ui
---
Run external commands silently without interrupting the Vim interface

```vim
command! -nargs=1 Silent
    \ execute 'silent !' . <q-args>
    \ | execute 'redraw!'
```
```lua
vim.api.nvim_create_user_command('Silent', function(opts)
    vim.cmd('silent !' .. opts.args)
    vim.cmd('redraw!')
end, { nargs = 1 })
```

**Source:** ** https://vim.fandom.com/wiki/Avoiding_the_%22Hit_ENTER_to_continue%22_prompts
***
# Title: Powerful Global Command for Line Matching
# Category: command_line
# Tags: search, pattern-matching, editing
---
Use :g command to apply actions to lines matching a pattern

```vim
:g/pattern/d  " Delete all lines matching pattern
```
```lua
-- Can be used directly in command mode
-- For programmatic approach:
vim.cmd('g/pattern/d')
```

**Source:** ** https://vim.fandom.com/wiki/Best_Tips
***
# Title: Perl-Based Command Evaluation in Vim
# Category: command_line
# Tags: perl, evaluation, command-extension
---
Add a custom command to evaluate Perl expressions directly in Vim, allowing quick calculations and code execution

```vim
:command! -nargs=+ Evaluate :perl VIM::Msg(eval{<args>})
```
```lua
-- Lua equivalent would require a different approach
-- In Neovim, you might use vim.fn.system() or a Lua-based implementation
-- Note: Direct Perl integration may require additional plugin or configuration
```

**Source:** ** https://vim.fandom.com/wiki/Calculator_and_code_evaluation_using_Perl
***
# Title: Escape Shell Command Special Characters
# Category: command_line
# Tags: shell, command-escaping, external-commands
---
Properly escape shell command special characters to prevent errors when running external commands

```vim
" Use shellescape() for commands with special characters
let escaped_cmd = shellescape(original_cmd)
```
```lua
-- Use vim.fn.shellescape() to escape special characters
local escaped_cmd = vim.fn.shellescape(original_cmd)
```

**Source:** ** https://vim.fandom.com/wiki/Cannot_create_temporary_file
***
# Title: Escape Shell Commands Properly
# Category: command_line
# Tags: shell-commands, escaping, security
---
Properly escape shell commands with special characters to prevent errors, especially in Vim 7.3.845+

```vim
let escaped_command = shellescape(original_command)
```
```lua
local escaped_command = vim.fn.shellescape(original_command)
```

**Source:** ** https://vim.fandom.com/wiki/Cannot_open_temporary_file
***
# Title: Capture Ex Command Output in New Tab
# Category: command_line
# Tags: ex-commands, output-capture, productivity
---
Easily capture and view output of Vim commands in a new tab for clean, temporary viewing

```vim
function! TabMessage(cmd)
  redir => message
  silent execute a:cmd
  redir END
  if empty(message)
    echoerr "no output"
  else
    tabnew
    setlocal buftype=nofile bufhidden=wipe noswapfile nobuflisted nomodified
    silent put=message
  endif
endfunction
command! -nargs=+ -complete=command TabMessage call TabMessage(<q-args>)
```
```lua
function _G.tab_message(cmd)
  local output = vim.api.nvim_exec(cmd, true)
  if output == "" then
    vim.notify("No output", vim.log.levels.WARN)
    return
  end
  vim.cmd('tabnew')
  vim.api.nvim_buf_set_option(0, 'buftype', 'nofile')
  vim.api.nvim_buf_set_option(0, 'bufhidden', 'wipe')
  vim.api.nvim_buf_set_option(0, 'swapfile', false)
  vim.api.nvim_buf_set_lines(0, 0, -1, false, vim.split(output, "\n"))
end

vim.api.nvim_create_user_command('TabMessage', function(opts)
  _G.tab_message(opts.args)
end, { nargs = '+', complete = 'command' })
```

**Source:** ** https://vim.fandom.com/wiki/Capture_ex_command_output
***
# Title: Remote Vim Session Control via Client-Server
# Category: command_line
# Tags: remote-editing, client-server, vim-management
---
Remotely save and close Vim sessions using the client-server protocol, useful for managing Vim instances across different machines

```vim
vim --servername GVIM --remote-send '<Esc>:wqa<CR>'
```
```lua
-- Lua equivalent for remote Vim interaction
-- Requires setting up Vim's client-server functionality
-- Example command to be run in terminal
-- vim.fn.remote_send('GVIM', '<Esc>:wqa<CR>')
```

**Source:** ** https://vim.fandom.com/wiki/Close_vim_you_left_open_remotely
***
# Title: Check Remote Vim Session Mode and Context
# Category: command_line
# Tags: remote-debugging, vim-modes, session-info
---
Remotely query the current Vim session's mode and working directory using client-server expressions

```vim
vim --servername GVIM --remote-expr 'mode()'
```
```lua
-- Lua approach to query Vim session state
-- vim.fn.remote_expr('GVIM', 'mode()')
-- vim.fn.remote_expr('GVIM', 'getcwd()')
```

**Source:** ** https://vim.fandom.com/wiki/Close_vim_you_left_open_remotely
***
# Title: Combine Multiple Code Checking Tools in Quickfix
# Category: command_line
# Tags: quickfix, code-checking, error-handling
---
Run multiple code checking tools and combine their results in a single quickfix list, useful for comprehensive code analysis

```vim
function! DoMake(...)
  update
  let savemp = &makeprg
  let qflist = []
  for prg in a:000
    let &makeprg = prg . ' %'
    silent make!
    let qflist += getqflist()
  endfor
  if empty(qflist)
    cclose
  else
    call setqflist(qflist)
    copen
    cfirst
  endif
  let &makeprg = savemp
endfunction

command! Pycheck call DoMake('pyflakes', 'pep8')
```
```lua
function _G.do_make(...)
  vim.cmd('update')
  local save_makeprg = vim.o.makeprg
  local qflist = {}
  
  for _, prg in ipairs({...}) do
    vim.o.makeprg = prg .. ' %'
    vim.cmd('silent make!')
    vim.list_extend(qflist, vim.fn.getqflist())
  end
  
  if #qflist == 0 then
    vim.cmd('cclose')
  else
    vim.fn.setqflist(qflist)
    vim.cmd('copen')
    vim.cmd('cfirst')
  end
  
  vim.o.makeprg = save_makeprg
end

vim.api.nvim_create_user_command('Pycheck', function()
  _G.do_make('pyflakes', 'pep8')
end, {})
```

**Source:** ** https://vim.fandom.com/wiki/Combine_quickfix_steps
***
# Title: Master Command-Line History Navigation
# Category: command_line
# Tags: history, productivity, navigation
---
Efficiently navigate and edit previous commands using the command-line window, which allows full Vim editing capabilities for command recall

```vim
" Open command-line window for commands
nnoremap : q:i

" Open command-line window for searches
nnoremap / q/i

" Open command-line window for reverse searches
nnoremap ? q?i
```
```lua
-- Open command-line windows with enhanced navigation
vim.keymap.set('n', ':', function()
  vim.cmd('q:i')
end, { desc = 'Open command history window' })

vim.keymap.set('n', '/', function()
  vim.cmd('q/i')
end, { desc = 'Open search history window' })

vim.keymap.set('n', '?', function()
  vim.cmd('q?i')
end, { desc = 'Open reverse search history window' })
```

**Source:** ** https://vim.fandom.com/wiki/Command-line_window
***
# Title: Keep Command Window Open After Execution
# Category: command_line
# Tags: workflow, automation, productivity
---
Automatically reopen command window at the same line after executing a command, useful for repeating a series of commands

```vim
" Autocmd to keep command window open and track current line
autocmd CmdwinEnter * nnoremap <buffer> <F5> :let g:CmdWindowLineMark=line(".")<CR><CR>q::execute "normal ".g:CmdWindowLineMark."G"<CR>
```
```lua
vim.api.nvim_create_autocmd('CmdwinEnter', {
  callback = function()
    vim.keymap.set('n', '<F5>', function()
      -- Store current line number
      vim.g.CmdWindowLineMark = vim.fn.line('.')
      -- Execute current line
      vim.cmd('normal! \<CR>')
      -- Reopen command window and go to stored line
      vim.cmd('q:')
      vim.cmd(string.format('normal! %dG', vim.g.CmdWindowLineMark))
    end, { buffer = true })
  end
})
```

**Source:** ** https://vim.fandom.com/wiki/Command-line_window
***
# Title: Remove Last Path Component in Command Line
# Category: command_line
# Tags: command-line, file-navigation, productivity
---
Easily remove the last path component when navigating directories in command line, making file path editing more efficient

```vim
cnoremap <C-t> <C-\>e(<SID>RemoveLastPathComponent())<CR>
function! s:RemoveLastPathComponent()
  return substitute(getcmdline(), '\%(\ \|[\/]\@!\f\)\+[\/]\=$\|.$', '', '')
endfunction
```
```lua
vim.keymap.set('c', '<C-t>', function()
  local cmdline = vim.fn.getcmdline()
  local modified_cmdline = cmdline:gsub('[^/\\]+[/\\]?$', '')
  return modified_cmdline
end, { expr = true, replace_keycodes = true })
```

**Source:** ** https://vim.fandom.com/wiki/Command_line_filename_autocompletion_%22undo%22:_remove_last_path_component
***
# Title: Source Vim Script Directly from Command Line
# Category: command_line
# Tags: cli, script-sourcing, startup
---
Use -S flag to source a Vim script when launching Vim, which is more concise than using -c option

```vim
vim -S foobar.vim
```
```lua
vim.cmd('source foobar.vim')
```

**Source:** ** https://vim.fandom.com/wiki/Command_line_switch_to_source_a_script
***
# Title: Quick File Opening with Shell Command Shortcuts
# Category: command_line
# Tags: shell-integration, file-navigation, productivity
---
Quickly open the most recently modified file or files matching specific criteria using shell aliases and functions

```vim
# Open most recent file
alias vew='vi `ls -t * | head -1`

# Open files containing a specific substring
function v() {
  vim *${1}*
}
```
```lua
-- Lua equivalents typically done via external shell functions
-- In Neovim, you can use telescope.nvim for similar functionality
-- Example telescope mapping
vim.keymap.set('n', '<leader>fr', require('telescope.builtin').oldfiles, { desc = 'Recent files' })
```

**Source:** ** https://vim.fandom.com/wiki/Command_line_tricks
***
# Title: Advanced Vim/GVim Command Line Options
# Category: command_line
# Tags: cli-options, file-editing, startup
---
Powerful command-line options for opening files with specific behaviors

```vim
# Command line option examples
gvim -u local_vimrc        # Use specific vimrc
gvim --noplugin           # Disable plugins
gvim -R important.txt     # Open read-only
gvim +10 file.txt         # Open and jump to line 10
gvim -c "/search" file.c  # Open and jump to search match
```
```lua
-- While these are CLI options, in Neovim you can replicate some behaviors
-- Open read-only
vim.g.started_with_read_only = true

-- Jump to specific line on open
vim.api.nvim_win_set_cursor(0, {10, 0})
```

**Source:** ** https://vim.fandom.com/wiki/Command_line_tricks
***
# Title: Mass File Editing with Arguments
# Category: command_line
# Tags: bulk-edit, search-replace, productivity
---
Perform find and replace operations across multiple files efficiently

```vim
vim -c "argdo %s/ABC/DEF/g | w" *.txt
vim -c "argdo %s/FOO/BAR/g | update" `grep -l FOO *`
```
```lua
-- Lua equivalent using nvim-spectre or manual approach
-- Requires external grep and argument manipulation
local files = vim.fn.systemlist('grep -l FOO *')
for _, file in ipairs(files) do
  vim.cmd('edit ' .. file)
  vim.cmd(':%s/FOO/BAR/g')
  vim.cmd('write')
end
```

**Source:** ** https://vim.fandom.com/wiki/Command_line_tricks
***
# Title: Powerful Command-Line History Navigation
# Category: command_line
# Tags: command-history, search-history, productivity
---
Use command-line window to easily edit and repeat previous commands or searches with full Vim editing capabilities

```vim
" Map : and / to open command window directly
nnoremap : q:i
nnoremap / q/i
nnoremap ? q?i
```
```lua
-- Open command window directly in Neovim
vim.keymap.set('n', ':', function() vim.cmd('q:i') end, { desc = 'Open command window' })
vim.keymap.set('n', '/', function() vim.cmd('q/i') end, { desc = 'Open search command window' })
vim.keymap.set('n', '?', function() vim.cmd('q?i') end, { desc = 'Open reverse search command window' })
```

**Source:** ** https://vim.fandom.com/wiki/Command_window
***
# Title: Keep Command Window Open After Execution
# Category: command_line
# Tags: automation, workflow, command-window
---
Create a mapping to execute a command and automatically reopen the command window, maintaining context

```vim
" Reopen command window after executing a command
autocmd CmdwinEnter * nnoremap <buffer> <F5> :let g:CmdWindowLineMark=line('.')<CR><CR>q::execute 'normal '.g:CmdWindowLineMark.'G'<CR>
```
```lua
-- Lua equivalent for keeping command window open
vim.api.nvim_create_autocmd('CmdwinEnter', {
  callback = function()
    vim.keymap.set('n', '<F5>', function()
      -- Store current line
      vim.g.CmdWindowLineMark = vim.fn.line('.')
      -- Execute current line
      vim.cmd('normal! \<CR>')
      -- Reopen command window and go to previous line
      vim.cmd('q:')
      vim.cmd('normal! ' .. vim.g.CmdWindowLineMark .. 'G')
    end, { buffer = true })
  end
})
```

**Source:** ** https://vim.fandom.com/wiki/Command_window
***
# Title: Run Java Class from Current File
# Category: command_line
# Tags: java, execution, file-path
---
Quickly run the compiled Java class from the current file's directory

```vim
map <F6> :!java -cp %:p:h %:t:r<CR>
```
```lua
vim.keymap.set('n', '<F6>', function()
  local classpath = vim.fn.expand('%:p:h')
  local classname = vim.fn.expand('%:t:r')
  vim.cmd('!java -cp ' .. classpath .. ' ' .. classname)
end, { desc = 'Run Java class' })
```

**Source:** ** https://vim.fandom.com/wiki/Compile_Java_with_Jikes
***
# Title: Quick Compile Current File with GCC
# Category: command_line
# Tags: compilation, gcc, build-tools
---
Configure Vim to compile the current file quickly using gcc with a single command

```vim
set makeprg=gcc\ -o\ %<\ %
```
```lua
vim.opt.makeprg = 'gcc -o %< %'
```

**Source:** ** https://vim.fandom.com/wiki/Compiling_the_actual_file_with_gcc
***
# Title: Quick Number Conversion with User Commands
# Category: command_line
# Tags: number-conversion, utility-commands
---
Define user commands to convert numbers between decimal and hexadecimal in visual or normal mode

```vim
command! -nargs=? -range Dec2hex call s:Dec2hex(<line1>, <line2>, '<args>')
command! -nargs=? -range Hex2dec call s:Hex2dec(<line1>, <line2>, '<args>')
```
```lua
vim.api.nvim_create_user_command('Dec2hex', function(opts)
  local start_line = opts.line1
  local end_line = opts.line2
  local arg = opts.args
  -- Implement conversion logic
end, { nargs = '?', range = true })

vim.api.nvim_create_user_command('Hex2dec', function(opts)
  local start_line = opts.line1
  local end_line = opts.line2
  local arg = opts.args
  -- Implement conversion logic
end, { nargs = '?', range = true })
```

**Source:** ** https://vim.fandom.com/wiki/Convert_decimal_to_hex
***
# Title: Create Custom Count Command
# Category: command_line
# Tags: custom-command, search, productivity
---
Add a custom command to easily count pattern occurrences

```vim
command -nargs=1 Count :%s/<args>//gn
```
```lua
vim.api.nvim_create_user_command('Count', ':%s/<args>//gn', {})
```

**Source:** ** https://vim.fandom.com/wiki/Count_number_of_matches_of_a_pattern
***
# Title: Verbose Command Execution Debugging
# Category: command_line
# Tags: debugging, verbosity, troubleshooting
---
Set verbose levels to get more detailed information about command execution

```vim
:9verbose edit somefile.txt.gz
```
```lua
-- Neovim equivalent for verbose command execution
-- Use :9verbose before commands to get detailed debug information
```

**Source:** ** https://vim.fandom.com/wiki/Debugging_window_autocommands
***
# Title: Selective Line Deletion with Exceptions
# Category: command_line
# Tags: global-command, filtering, text-manipulation
---
Delete lines matching a pattern while preserving specific exceptions using global command

```vim
:global:^./help/:if (match(getline(line('.')), '^./help/de/') == -1) | delete | endif

" Alternative method:
:g#\(^\./help/\)\(de/\)\@!#d
```
```lua
-- Lua equivalent using vim.api and global command
vim.cmd('g#\(^\./help/\)\(de/\)\@!#d')

-- More explicit Lua approach
for i = vim.fn.line('$'), 1, -1 do
  local line = vim.fn.getline(i)
  if line:match('^./help/') and not line:match('^./help/de/') then
    vim.cmd(i .. 'delete')
  end
end
```

**Source:** ** https://vim.fandom.com/wiki/Delete_some_lines_with_some_exceptions
***
# Title: Quickly Describe SQL Table from Vim
# Category: command_line
# Tags: sql, external-command, productivity
---
Use a custom bash script to retrieve and insert table description directly into Vim buffer

```vim
:r !describe <tableName>
```
```lua
-- Equivalent Lua command
vim.api.nvim_command('r !describe ' .. table_name)
```

**Source:** ** https://vim.fandom.com/wiki/Describe_a_SQL_table_from_Vim
***
# Title: Repeat Ex Commands with Single Keystroke
# Category: command_line
# Tags: command-repeat, ex-mode, productivity
---
Quickly repeat the last Ex (colon) command using @: and repeat again with @@

```vim
" Press @: to repeat last Ex command
" Press @@ to repeat again
```
```lua
-- No direct Lua equivalent, but can be mapped similarly
vim.keymap.set('n', '<leader>@', '@:', { desc = 'Repeat last Ex command' })
```

**Source:** ** https://vim.fandom.com/wiki/Did_you_know
***
# Title: Disable Command-Line Abbreviations Temporarily
# Category: command_line
# Tags: abbreviations, command-mode, workaround
---
Two methods to temporarily prevent command abbreviations from expanding: using paste mode or literal character insertion

```vim
" Method 1: Toggle paste mode
set invpaste

" Method 2: Literal character insertion
" Press <C-V> before the expansion character
```
```lua
-- Method 1: Toggle paste mode
vim.opt.paste = not vim.opt.paste:get()

-- Method 2: Use Vim's built-in literal insertion
-- Press <C-V> before the expansion character
```

**Source:** ** https://vim.fandom.com/wiki/Disabling_cabbrev
***
# Title: Quickly Inspect Vim Environment
# Category: command_line
# Tags: inspection, diagnostics, environment
---
Comprehensive set of commands to display various Vim environment details, useful for troubleshooting and understanding current configuration

```vim
" Example commands for environment inspection
:set all      " Show all options
:map          " Show all mappings
:scriptnames  " List sourced scripts
```
```lua
-- Lua equivalents for environment inspection
vim.cmd('set all')      -- Show all options
vim.cmd('map')          -- Show all mappings
vim.cmd('scriptnames')  -- List sourced scripts

-- More Neovim-specific approach
print(vim.inspect(vim.opt))  -- Inspect options
print(vim.inspect(vim.keymap.list()))
```

**Source:** ** https://vim.fandom.com/wiki/Displaying_the_current_Vim_environment
***
# Title: Quickly Open Files with Whereis Command
# Category: command_line
# Tags: shell-function, file-navigation, command-line-tools
---
Create a shell function to quickly open files found by the whereis command in Vim/Neovim

```vim
function vvim() { vim `whereis $1|cut -d: -f2` }
function ggvim() { gvim `whereis $1|cut -d: -f2` }
```
```lua
-- Bash function to be added to .bashrc or .bash_profile
-- function vvim() {
--   nvim `whereis "$1" | cut -d: -f2`
-- }

-- In Neovim, you could create a similar command
vim.api.nvim_create_user_command('VVim', function(opts)
  local file = vim.fn.system('whereis ' .. opts.args .. ' | cut -d: -f2'):gsub('%s+', '')
  vim.cmd('edit ' .. file)
end, { nargs = 1 })
```

**Source:** ** https://vim.fandom.com/wiki/Edit_file_found_by_whereis
***
# Title: Enhanced Command Window Navigation
# Category: command_line
# Tags: command-line, navigation, productivity
---
Improve command window functionality with custom mappings for easier navigation and command recall

```vim
" Enter command window with single keystroke
nmap <Esc> q:<C-W>_
nmap q/ q/<C-W>_
nmap q? q?<C-W>_

" Custom autocommands for command window
augroup ECW_au
  au!
  au CmdwinEnter * nmap <Esc> :q<CR>
  au CmdwinLeave * nmap <Esc> q:<C-W>_
augroup END
```
```lua
vim.keymap.set('n', '<Esc>', 'q:<C-W>_', { desc = 'Open command window' })
vim.keymap.set('n', 'q/', 'q/<C-W>_', { desc = 'Open search command window' })
vim.keymap.set('n', 'q?', 'q?<C-W>_', { desc = 'Open reverse search command window' })

-- Create augroup for command window behavior
local augroup = vim.api.nvim_create_augroup('ECW_au', { clear = true })

vim.api.nvim_create_autocmd('CmdwinEnter', {
  group = augroup,
  callback = function()
    vim.keymap.set('n', '<Esc>', ':q<CR>', { buffer = true })
  end
})

vim.api.nvim_create_autocmd('CmdwinLeave', {
  group = augroup,
  callback = function()
    vim.keymap.set('n', '<Esc>', 'q:<C-W>_', { buffer = true })
  end
})
```

**Source:** ** https://vim.fandom.com/wiki/Enhanced_command_window
***
# Title: Command Window Enhanced Completion
# Category: command_line
# Tags: command-line, completion, search
---
Add advanced navigation and completion features to the command window, similar to command-line behavior

```vim
" Arrow key navigation in command window
augroup ECW_au
  au CmdwinEnter : imap <UP> <C-O>y0<C-O>:let@/='^'.@0<CR><C-O>?<Esc><Esc>
  au CmdwinLeave : iunmap <UP>
  au CmdwinEnter : imap <DOWN> <C-O>y0<C-O>:let@/='^'.@0<CR><C-O>/<Esc><Esc>
  au CmdwinLeave : iunmap <DOWN>
  au CmdwinLeave : :let @/=""
augroup END
```
```lua
-- Enhanced command window navigation
local augroup = vim.api.nvim_create_augroup('ECW_au', { clear = true })

vim.api.nvim_create_autocmd('CmdwinEnter', {
  group = augroup,
  pattern = ':',
  callback = function()
    vim.keymap.set('i', '<Up>', function()
      vim.cmd('normal! y0')
      vim.fn.setreg('/', '^' .. vim.fn.getreg('"'))
      vim.cmd('normal! ?')
    end, { buffer = true })
    
    vim.keymap.set('i', '<Down>', function()
      vim.cmd('normal! y0')
      vim.fn.setreg('/', '^' .. vim.fn.getreg('"'))
      vim.cmd('normal! /')
    end, { buffer = true })
  end
})

vim.api.nvim_create_autocmd('CmdwinLeave', {
  group = augroup,
  callback = function()
    vim.fn.setreg('/', '')
  end
})
```

**Source:** ** https://vim.fandom.com/wiki/Enhanced_command_window
***
# Title: Manipulate Environment Variables in Vim
# Category: command_line
# Tags: environment, variables, shell-interaction
---
Easily read, modify, and insert environment variables directly within Vim

```vim
" Display PATH variable
:echo $PATH

" Assign PATH to a Vim variable
:let myvar = $PATH

" Modify PATH for current session
:let $PATH = '/foo:/bar'

" Append to PATH
:let $PATH .= ':/foo:/bar'
```
```lua
-- Display PATH variable
print(vim.env.PATH)

-- Assign PATH to a variable
local myvar = vim.env.PATH

-- Modify PATH for current session
vim.env.PATH = '/foo:/bar'

-- Append to PATH
vim.env.PATH = vim.env.PATH .. ':/foo:/bar'
```

**Source:** ** https://vim.fandom.com/wiki/Environment_variables
***
# Title: Asynchronously Run External Commands in Windows
# Category: command_line
# Tags: windows, external-commands, async-execution
---
Run external console programs without blocking Vim, with optional pause to view output

```vim
" Run compiled program corresponding to current source file
nnoremap <silent> <F5> :!start cmd /c "%:p:r:s,$,.exe," & pause<CR>
```
```lua
-- Lua equivalent for running external programs
vim.keymap.set('n', '<F5>', function()
  vim.cmd('!start cmd /c "' .. vim.fn.expand('%:p:r') .. '.exe" & pause')
end, { silent = true })
```

**Source:** ** https://vim.fandom.com/wiki/Execute_external_programs_asynchronously_under_Windows
***
# Title: Quick Vim Help in Full Window
# Category: command_line
# Tags: help, command-line, documentation
---
Quickly open Vim help for a specific topic in a full window from the command line

```vim
#!/bin/bash
vim -c "help $1" -c only
```
```lua
-- Lua equivalent (shell script)
local function open_help(topic)
  vim.cmd(string.format('help %s', topic))
  vim.cmd('only')
end
```

**Source:** ** https://vim.fandom.com/wiki/Fast_help_in_full_window
***
# Title: Command-Line Help Search Functions
# Category: command_line
# Tags: help, search, documentation
---
Bash functions to quickly search and open Vim help or helpgrep results

```vim
vimhelp() {
  view -c "help $1" -c on -c "au! VimEnter *"
}

vimhelpgrep() {
  vim -c "helpgrep $1" -c on -c copen -c "au! VimEnter *"
}
```
```lua
-- Lua functions for Neovim help search
local function vim_help(topic)
  vim.cmd(string.format('help %s', topic))
  vim.cmd('only')
end

local function vim_help_grep(topic)
  vim.cmd(string.format('helpgrep %s', topic))
  vim.cmd('copen')
end
```

**Source:** ** https://vim.fandom.com/wiki/Fast_help_in_full_window
***
# Title: Quickly Navigate Directories from Command Line
# Category: command_line
# Tags: navigation, productivity, file-operations
---
Custom mappings to quickly access current file's directory and navigate parent directories from command line, useful for large projects

```vim
func! CurrentFileDir()
  return "e " . expand("%:p:h") . "/"
endfunc

func! DeleteTillSlash()
  let cmd = getcmdline()
  let cmd_edited = substitute(cmd, "\\(.*/\\).*", "\\1", "")
  if cmd == cmd_edited
    let cmd_edited = substitute(cmd, "\\(.*/\\).*/", "\\1", "")
  endif
  return cmd_edited
endfunc

cno $c e <C-\>eCurrentFileDir()<CR>
cmap <C-q> <C-\>eDeleteTillSlash()<CR>
```
```lua
local function current_file_dir()
  return 'e ' .. vim.fn.expand('%:p:h') .. '/'
end

local function delete_till_slash()
  local cmd = vim.fn.getcmdline()
  local cmd_edited = cmd:gsub('(.*/)[^/]*$', '%1')
  if cmd == cmd_edited then
    cmd_edited = cmd:gsub('(.*/).*/', '%1')
  end
  return cmd_edited
end

vim.api.nvim_create_user_command('CurrentFileDir', current_file_dir, {})
vim.keymap.set('c', '$c', function()
  vim.cmd('e ' .. vim.fn.expand('%:p:h') .. '/')
end)

vim.keymap.set('c', '<C-q>', function()
  local cmd = vim.fn.getcmdline()
  local new_cmd = cmd:gsub('(.*/)[^/]*$', '%1')
  vim.fn.setcmdline(new_cmd)
end)
```

**Source:** ** https://vim.fandom.com/wiki/Faster_directory_browsing_from_command_line
***
# Title: Fuzzy File Name Completion
# Category: command_line
# Tags: completion, file-search, navigation
---
Use tab and Ctrl-D for dynamic file name completion and listing

```vim
:e <space>Ctrl-D  # List all files
:e get<Tab>      # Complete files starting with 'get'
```
```lua
-- These are built-in Vim/Neovim command line completion features
-- Use in command mode with Ctrl-D or Tab
```

**Source:** ** https://vim.fandom.com/wiki/File_explorer
***
# Title: Get VIMRUNTIME Path in Bash Scripts
# Category: command_line
# Tags: shell-scripting, vim-environment
---
Retrieve the VIMRUNTIME directory path using Vim in a bash script, which can be useful for scripting and plugin development

```vim
vim --cmd 'echo $VIMRUNTIME' --cmd 'quit' 2> /tmp/VIMRUNTIME.txt
VIMRUNTIME=`perl -pe 's/
//g' /tmp/VIMRUNTIME.txt`
rm -f /tmp/VIMRUNTIME.txt
```
```lua
-- Lua equivalent for getting VIMRUNTIME
local handle = io.popen('vim --cmd "echo $VIMRUNTIME" --cmd "quit"')
local vimruntime = handle:read('*a'):gsub('[\r\n]', '')
handle:close()
```

**Source:** ** https://vim.fandom.com/wiki/Find_VIMRUNTIME_in_a_bash_script
***
# Title: Escape Shell Commands Properly
# Category: command_line
# Tags: shell-commands, escaping
---
Use shellescape() to properly escape special characters in external shell commands to prevent errors

```vim
" Example: Escape command with special characters
let escaped_cmd = shellescape(original_cmd)
```
```lua
-- Use vim.fn.shellescape() to escape shell commands
local escaped_cmd = vim.fn.shellescape(original_cmd)
```

**Source:** ** https://vim.fandom.com/wiki/Fix_errors_that_relate_to_reading_or_creating_files_in_the_temp_or_tmp_environment_on_an_MS_Windows_PC
***
# Title: Get Shell Command for Current Directory
# Category: command_line
# Tags: directory, shell-integration, clipboard
---
Generate a shell 'cd' command for the current Vim working directory, which can be easily pasted into a terminal

```vim
com Scd let @+="cd \"" . escape(getcwd(), "\"") . """
```
```lua
vim.api.nvim_create_user_command('Scd', function()
  local cwd = vim.fn.getcwd()
  vim.fn.setreg('+', 'cd "' .. cwd:gsub('"', '\"%') .. '"')
end, {})
```

**Source:** ** https://vim.fandom.com/wiki/Get_a_shell_command_for_changing_to_the_current_directory
***
# Title: Command Line Completion List Extraction
# Category: command_line
# Tags: command-completion, vim-function, utility
---
Extracts a list of possible command line completions using Vim's built-in completion mechanism

```vim
function! GetCmdCompletion(cmd_prefix)
  let [cwh,ls,v] = [&cwh, &ls, @v]
  set cwh=1 ls=0
  execute 'nn <buffer> z&u :' . a:cmd_prefix . '<c-a><c-f>"vyyo<cr>'
  normal z&u
  let res = split(@v)
  let [&cwh,&ls,@v] = [cwh,ls,v]
  return res
endfunction
```
```lua
function _G.get_cmd_completion(cmd_prefix)
  local cwh = vim.o.cmdheight
  local ls = vim.o.laststatus
  local original_reg = vim.fn.getreg('v')

  vim.o.cmdheight = 1
  vim.o.laststatus = 0

  vim.cmd('nn <buffer> z&u :' .. cmd_prefix .. '<c-a><c-f>"vyyo<cr>')
  vim.cmd('normal z&u')

  local res = vim.fn.split(vim.fn.getreg('v'))

  vim.o.cmdheight = cwh
  vim.o.laststatus = ls
  vim.fn.setreg('v', original_reg)

  return res
end
```

**Source:** ** https://vim.fandom.com/wiki/Get_ex_command_line_completion_as_a_list
***
# Title: Enhanced Command-Line Completion
# Category: command_line
# Tags: completion, command-line, usability
---
Improve command-line completion with a menu and enhanced tab behavior, showing all possible completions and automatically completing to the longest common string

```vim
set wildmenu
set wildmode=list:longest,full
```
```lua
vim.opt.wildmenu = true
vim.opt.wildmode = 'list:longest,full'
```

**Source:** ** https://vim.fandom.com/wiki/Great_wildmode/wildmenu_and_console_mouse
***
# Title: Fix Common Command-Line Typos
# Category: command_line
# Tags: typo-correction, command-line, productivity
---
Automatically correct common command-line typos like accidentally holding Shift or mistyping quit/write commands

```vim
" Correct common command typos
cabbrev Q quit
cabbrev W write
cabbrev q!@ q!
cabbrev wq!@ wq!
```
```lua
-- Correct common command typos in Neovim
vim.cmd('cabbrev Q quit')
vim.cmd('cabbrev W write')
vim.cmd('cabbrev q!@ q!')
vim.cmd('cabbrev wq!@ wq!')
```

**Source:** ** https://vim.fandom.com/wiki/Handle_common_command_typos
***
# Title: Insert Buffer Contents into Command Line
# Category: command_line
# Tags: command-line, text-insertion, productivity
---
Quickly insert text from the current buffer into command line using different methods

```vim
" Method 1: Use Shift-Insert
" Method 2: Use Ctrl-R Ctrl-W to insert current word
```
```lua
-- Insert current word in command line
vim.keymap.set('c', '<C-r><C-w>', function()
  local word = vim.fn.expand('<cword>')
  vim.api.nvim_feedkeys(word, 'n', true)
end)
```

**Source:** ** https://vim.fandom.com/wiki/How_to_insert_the_contents_of_a_buffer_into_the_command_line
***
# Title: Find Perl Path Dynamically
# Category: command_line
# Tags: system-command, path-discovery
---
Quickly insert the path to perl executable using which command

```vim
:r !which perl
```
```lua
vim.cmd('r !which perl')
```

**Source:** ** https://vim.fandom.com/wiki/Insert_a_file
***
# Title: Complex Vim Command-Line Chaining
# Category: command_line
# Tags: command-line, vim-tricks, advanced-usage
---
Demonstrates how to chain multiple Vim commands using -c flag, useful for quick one-liner operations or automated tasks

```vim
vim -c "cmd1|cmd2|cmd3"
# Example: Print paste contents to default printer
gvim -c 's/^/\=@*/|hardcopy!|q!'
```
```lua
-- Lua equivalent using vim.cmd
-- Note: Direct command-line usage remains similar
vim.cmd('s/^/\=@*')
vim.cmd('hardcopy!')
vim.cmd('q!')
```

**Source:** ** https://vim.fandom.com/wiki/JAVH_-_Just_another_Vim_Hacker
***
# Title: List and Filter Loaded Vim Scripts
# Category: command_line
# Tags: scripting, debugging, configuration
---
Easily list and filter loaded Vim scripts, allowing quick inspection of loaded plugins and scripts

```vim
function! s:Filter_lines(cmd, filter)
  let save_more = &more
  set nomore
  redir => lines
  silent execute a:cmd
  redir END
  let &more = save_more
  new
  setlocal buftype=nofile bufhidden=hide noswapfile
  put =lines
  g/^\s*$/d
  %s/^\s*\d\+:\s*//e
  if !empty(a:filter)
    execute 'v/' . a:filter . '/d'
  endif
  0
endfunction
command! -nargs=? Scriptnames call s:Filter_lines('scriptnames', <q-args>)
```
```lua
function _G.filter_scripts(cmd, filter)
  local lines = vim.fn.execute(cmd)
  local filtered_lines = {}
  
  for _, line in ipairs(vim.split(lines, '\n')) do
    if filter == '' or line:find(filter) then
      table.insert(filtered_lines, line:gsub('^%s*%d+:%s*', ''))
    end
  end
  
  local buf = vim.api.nvim_create_buf(false, true)
  vim.api.nvim_buf_set_lines(buf, 0, -1, false, filtered_lines)
  vim.api.nvim_buf_set_option(buf, 'buftype', 'nofile')
  vim.api.nvim_buf_set_option(buf, 'bufhidden', 'hide')
  vim.api.nvim_buf_set_option(buf, 'swapfile', false)
  
  vim.api.nvim_command('buffer ' .. buf)
end

vim.api.nvim_create_user_command('Scriptnames', function(opts)
  _G.filter_scripts('scriptnames', opts.args or '')
end, { nargs = '?' })
```

**Source:** ** https://vim.fandom.com/wiki/List_loaded_scripts
***
# Title: Compile Current Buffer with Flexible Make Command
# Category: command_line
# Tags: compilation, build, make, quickfix
---
Easily compile the current file and populate quickfix list with compiler errors

```vim
" Set make program to compile current file
set makeprg=gcc\ -o\ %<\ %

" Compile current file
:make %:r
```
```lua
-- Set make program for compiling current file
vim.o.makeprg = 'gcc -o %< %'

-- Compile current file and open quickfix
vim.cmd('make %:r')
```

**Source:** ** https://vim.fandom.com/wiki/Make-compile_current_buffer
***
# Title: Custom Make Command with Quickfix
# Category: command_line
# Tags: make, custom-commands, build-tools
---
Create a custom Make command that automatically opens quickfix window with a specified height

```vim
command! -nargs=* Make make <args> | cwindow 3
```
```lua
vim.api.nvim_create_user_command('Make', function(opts)
  vim.cmd('make ' .. opts.args)
  vim.cmd('cwindow 3')
end, { nargs = '*' })
```

**Source:** ** https://vim.fandom.com/wiki/Make_make_more_helpful
***
# Title: Compile Current File with Quickfix Support
# Category: command_line
# Tags: compilation, quickfix, make
---
Set up a quick way to compile the current file and open compilation errors in the quickfix window

```vim
" Configure make program for gcc compilation
set makeprg=gcc\ -o\ %<\ %

" Mapping to compile current file
nnoremap <F7> :update<CR>:make<CR>
```
```lua
-- Configure make program for gcc compilation
vim.o.makeprg = 'gcc -o %< %'

-- Mapping to compile current file
vim.keymap.set('n', '<F7>', function()
  vim.cmd.write()
  vim.cmd.make()
end, { desc = 'Compile current file' })
```

**Source:** ** https://vim.fandom.com/wiki/Map_function_keys_to_compile_and_run_your_code
***
# Title: Quickly Repeat Previous Command
# Category: command_line
# Tags: productivity, key-mapping, command-repeat
---
Easily re-run the last command using a leader key mapping

```vim
nmap <Leader>. :<C-P><CR>
```
```lua
vim.keymap.set('n', '<Leader>.', function()
  vim.cmd(':<C-P><CR>')
end, { desc = 'Repeat previous command' })
```

**Source:** ** https://vim.fandom.com/wiki/Mapping_to_enter_colon_commands
***
# Title: Chain Multiple Vim Commands with Pipe
# Category: command_line
# Tags: command-chaining, productivity, text-manipulation
---
Execute multiple Vim commands sequentially, with each command running only if the previous command succeeds

```vim
%s/htm/html/c | %s/JPEG/jpg/c | %s/GIF/gif/c
```
```lua
-- For Lua, use vim.cmd to execute multiple commands
vim.cmd('s/htm/html/c | s/JPEG/jpg/c | s/GIF/gif/c')
```

**Source:** ** https://vim.fandom.com/wiki/Multiple_commands_at_once
***
# Title: Create Convenient Shell Aliases
# Category: command_line
# Tags: shell-alias, workflow, productivity
---
Set up shell aliases to quickly open files in existing Vim instances with custom server names

```vim
alias gvir="gvim --remote"
alias gvdev="gvim --servername dev --remote"
alias gvlib="gvim --servername lib --remote"
```
```lua
-- These are shell aliases, not Lua code
-- Add to your .bashrc or .zshrc
-- alias gvir='nvim --remote'
-- alias gvdev='nvim --servername dev --remote'
-- alias gvlib='nvim --servername lib --remote'
```

**Source:** ** https://vim.fandom.com/wiki/Open_file_in_already_running_vim_from_elsewhere
***
# Title: Quick Word/WORD Paste in Command Line
# Category: command_line
# Tags: text-objects, command-line, navigation
---
Easily paste word or WORD under cursor into command line using keyboard shortcuts

```vim
" <C-r><C-w> - Paste word under cursor
" <C-r><C-a> - Paste WORD under cursor
```
```lua
-- Functionality is built-in, no specific Lua implementation needed
-- Can be used directly in command and search modes
```

**Source:** ** https://vim.fandom.com/wiki/Paste_registers_in_search_or_colon_commands_instead_of_using_the_clipboard
***
# Title: Quick Postgres Query Execution in Vim
# Category: command_line
# Tags: database, external-command, productivity
---
Execute PostgreSQL queries directly from Vim by mapping a key to run the current file as a database query

```vim
map <F9> :!psql -d yourdb < % <BAR> less
```
```lua
vim.keymap.set('n', '<F9>', function()
  vim.cmd('!psql -d yourdb < % | less')
end, { desc = 'Run current file as Postgres query' })
```

**Source:** ** https://vim.fandom.com/wiki/Quick_and_dirty_Postgres_query
***
# Title: Quick Launch Browser from Vim
# Category: command_line
# Tags: windows, external-commands, productivity
---
Quickly open a URL in the default browser directly from Vim using the :!start explorer command

```vim
:!start explorer http://www.vim.org/
```
```lua
vim.fn.system('start explorer http://www.vim.org/')
```

**Source:** ** https://vim.fandom.com/wiki/Quick_launch_html_and_other_Windows_documents
***
# Title: Quick File Peek Without Opening Buffer
# Category: command_line
# Tags: file-preview, quick-view, vim-tricks
---
View file contents directly in Vim's command line without opening a new buffer, useful for quick file inspection

```vim
:echo join(readfile('foo.bat'), "\n")
```
```lua
vim.api.nvim_command(string.format('echo join(readfile("%s"), "\n")', 'foo.bat'))
```

**Source:** ** https://vim.fandom.com/wiki/Quick_peek_at_files
***
# Title: Quick Buffer and Global Commands
# Category: command_line
# Tags: buffer-management, global-commands, text-manipulation
---
Apply commands across all buffers or matching lines efficiently

```vim
:bufdo %s/pattern/substitution/g  # Replace in all buffers
:g/pattern/d  # Delete all lines matching pattern
```
```lua
-- For buffer-wide substitution
vim.cmd('bufdo %s/pattern/substitution/g')

-- For deleting lines matching pattern
vim.cmd('g/pattern/d')
```

**Source:** ** https://vim.fandom.com/wiki/Quick_tips
***
# Title: Configure Quickfix for Visual Studio Build Errors
# Category: command_line
# Tags: build-integration, error-handling, compiler
---
Set up a custom make program and mapping to parse Visual Studio compiler errors in Vim, enabling quick navigation through compilation errors

```vim
set makeprg=/bin/dovcmake
map <F7> :make <C-R>%<CR>
```
```lua
vim.o.makeprg = '/bin/dovcmake'
vim.keymap.set('n', '<F7>', function()
  vim.cmd('make ' .. vim.fn.expand('%'))
end, { desc = 'Run makefile for current file' })
```

**Source:** ** https://vim.fandom.com/wiki/Quickfix_and_Visual_Studio_and_cygwin
***
# Title: Use Quickfix with Doxygen for Error Navigation
# Category: command_line
# Tags: quickfix, documentation, error-handling
---
Configure Vim's quickfix to navigate through Doxygen documentation generation errors, similar to compiler errors

```vim
:set makeprg=doxygen
:make Doxyfile
```
```lua
vim.opt.makeprg = 'doxygen'
vim.cmd('make Doxyfile')
```

**Source:** ** https://vim.fandom.com/wiki/Quickfix_and_doxygen
***
# Title: Powerful Range-Based Text Editing
# Category: command_line
# Tags: editing, ranges, search-replace
---
Use flexible range specifiers for precise text manipulation across lines

```vim
:%s/old/new/g                 " Replace in all lines
:21,25s/old/new/g         " Replace in specific line range
:.,$s/old/new/g           " Replace from current line to end
:/pattern/,/endpattern/ s/old/new/g  " Replace between patterns
```
```lua
-- Lua equivalent uses Vim command mode
vim.cmd(':%s/old/new/g')               -- Replace in all lines
vim.cmd(':21,25s/old/new/g')           -- Replace in specific line range
vim.cmd(':.,$s/old/new/g')             -- Replace from current line to end
vim.cmd(':/pattern/,/endpattern/ s/old/new/g')  -- Replace between patterns
```

**Source:** ** https://vim.fandom.com/wiki/Range
***
# Title: Flexible Line Range Operations in Vim
# Category: command_line
# Tags: range, text-manipulation, search-replace
---
Use flexible range specifiers for powerful text editing across multiple lines, including marks, line numbers, and search patterns

```vim
" Examples of range operations
:21,25s/old/new/g     " Substitute in lines 21-25
:%s/old/new/g         " Substitute in all lines
:'a,'bd               " Delete lines from mark a to b
:/apples/,/peaches/s/^/# /g  " Comment lines between patterns
```
```lua
-- Lua equivalents use ex commands
vim.cmd('21,25s/old/new/g')      -- Substitute in lines 21-25
vim.cmd('%s/old/new/g')          -- Substitute in all lines
vim.cmd("'a,'bd")                 -- Delete lines from mark a to b
vim.cmd('/apples/,/peaches/s/^/# /g')  -- Comment lines between patterns
```

**Source:** ** https://vim.fandom.com/wiki/Ranges
***
# Title: Read and Modify Environment Variables in Vim
# Category: command_line
# Tags: environment, variables, shell-interaction
---
Easily read, display, and modify environment variables directly within Vim, allowing for dynamic shell configuration

```vim
" Display PATH variable
:echo $PATH

" Assign PATH to a Vim variable
:let myvar = $PATH

" Modify PATH for current session
:let $PATH = '/foo:/bar'

" Append to PATH
:let $PATH .= ':/foo:/bar'
```
```lua
-- Display PATH variable
print(vim.env.PATH)

-- Assign PATH to a variable
local myvar = vim.env.PATH

-- Modify PATH for current session
vim.env.PATH = '/foo:/bar'

-- Append to PATH
vim.env.PATH = vim.env.PATH .. ':/foo:/bar'
```

**Source:** ** https://vim.fandom.com/wiki/Read_Write_System_Enviroment_Variables
***
# Title: Base64 Decoding in Vim Using System Commands
# Category: command_line
# Tags: encoding, text-processing, system-commands
---
Decode base64 encoded strings directly within Vim using Ruby or Perl embedded interpreters

```vim
" Ruby base64 decoding
:ruby require "base64"
:.rubydo $_=Base64.decode64 $_

" Perl base64 decoding
:perl require MIME::Base64
:.perldo $_=MIME::Base64::decode($_)
```
```lua
-- Lua base64 decoding (requires 'base64' luarocks package)
local base64 = require('base64')
vim.api.nvim_command(string.format(':lua vim.api.nvim_set_current_line(base64.decode(vim.api.nvim_get_current_line()))'))
```

**Source:** ** https://vim.fandom.com/wiki/Read_base64_raw_string/email_in_Vim
***
# Title: Advanced Command Line Recall
# Category: command_line
# Tags: command-history, navigation
---
Use q: to open command-line window for easier command history navigation and editing without leaving home row

```vim
" Open command-line window
q:
```
```lua
-- Open command-line window
vim.cmd('q:')
```

**Source:** ** https://vim.fandom.com/wiki/Repeat_last
***
# Title: Repeat Last Ex Command Efficiently
# Category: command_line
# Tags: ex-commands, productivity, repeat
---
Use @: to repeat the last colon command, and @@ to repeat subsequent times. Useful for batch operations across files.

```vim
" Repeat last colon command
@:
" Repeat again
@@
" Repeat multiple times
10@@
```
```lua
-- Repeat last command in Ex mode
vim.cmd('normal! @:')
-- Repeat again
vim.cmd('normal! @@')
-- Repeat multiple times
vim.cmd('normal! 10@@')
```

**Source:** ** https://vim.fandom.com/wiki/Repeat_last_colon_command
***
# Title: Repeat Ex Command on Multiple Blocks
# Category: command_line
# Tags: global-command, text-manipulation, bulk-editing
---
Use the global command to apply an Ex command (like sort) to multiple blocks of text separated by blank lines

```vim
:g/^\s*$/;//-1sort
```
```lua
-- Sort each block of text in a file
vim.cmd('g/^\s*$/;//-1sort')
```

**Source:** ** https://vim.fandom.com/wiki/Repeating_an_ex_command_on_multiple_blocks
***
# Title: Replace Built-in Commands with Command Abbreviations
# Category: command_line
# Tags: command-abbreviation, customization, typo-correction
---
Create command abbreviations to replace or modify built-in Vim commands, useful for correcting typos or customizing command behavior

```vim
" Function to create command abbreviations
function! CommandCabbr(abbreviation, expansion)
  execute 'cabbr ' . a:abbreviation . ' <c-r>=getcmdpos() == 1 && getcmdtype() == ":" ? "' . a:expansion . '" : "' . a:abbreviation . '"<CR>'
endfunction
command! -nargs=+ CommandCabbr call CommandCabbr(<f-args>)

" Example: Replace 'w1' with 'w!' to force write
cabbrev w1 <c-r>=(getcmdtype()==':' && getcmdpos()==1 ? 'w!' : 'w1')<CR>
```
```lua
-- Function to create command abbreviations
local function command_cabbr(abbreviation, expansion)
  vim.api.nvim_create_user_command('CommandCabbr', function(opts)
    local cmd = string.format('cabbr %s <c-r>=(getcmdpos() == 1 && getcmdtype() == ":" ? "%s" : "%s")<CR>', 
      opts.args[1], opts.args[2], opts.args[1])
    vim.cmd(cmd)
  end, { nargs = '+' })
end

-- Example: Replace 'w1' with 'w!' to force write
vim.cmd('cabbrev w1 <c-r>=(getcmdtype()==":" && getcmdpos()==1 ? "w!" : "w1")<CR>')
```

**Source:** ** https://vim.fandom.com/wiki/Replace_a_built-in_command_using_cabbrev
***
# Title: Quickly Find Full Command Path in Scripts
# Category: command_line
# Tags: shell-integration, command-lookup, productivity
---
Replace a command with its full system path using 'which' directly in Vim, useful for scripting and ensuring absolute command references

```vim
!which $(cat)
```
```lua
-- Lua equivalent for finding command full path
local function get_command_path(cmd)
  local handle = io.popen('which ' .. cmd)
  local result = handle:read('*a'):gsub('%s+', '')
  handle:close()
  return result
end

-- Usage example
-- vim.fn.setline('.', get_command_path('cat'))
```

**Source:** ** https://vim.fandom.com/wiki/Replace_selected_shell_command_with_full_path_when_editing_scripts
***
# Title: Run Commands Within Current Function
# Category: command_line
# Tags: text-editing, function-scope, search-replace
---
Create a mapping to restrict commands like substitution to the current function body in C/C++/Java files

```vim
:cmap ;tf ?^{??(?,/^}/
```
```lua
-- Lua equivalent requires more complex setup
vim.keymap.set('c', ';tf', '?^{??(?,/^}/', { desc = 'Select current function scope' })
```

**Source:** ** https://vim.fandom.com/wiki/Run_Vim_command_on_current_C/C%2B%2B/Java_function
***
# Title: Master Command-Line History Navigation
# Category: command_line
# Tags: history, navigation, productivity
---
Efficiently navigate and reuse command and search history using command-line window and history keys

```vim
" Open command-line window for commands
nnoremap : q:i

" Open command-line window for searches
nnoremap / q/i

" Open command-line window for reverse searches
nnoremap ? q?i
```
```lua
-- Open command-line window for commands
vim.keymap.set('n', ':', function() vim.cmd('q:') end, { desc = 'Open command history window' })

-- Open command-line window for searches
vim.keymap.set('n', '/', function() vim.cmd('q/') end, { desc = 'Open search history window' })

-- Open command-line window for reverse searches
vim.keymap.set('n', '?', function() vim.cmd('q?') end, { desc = 'Open reverse search history window' })
```

**Source:** ** https://vim.fandom.com/wiki/VimTip45
***
# Title: Use Quickfix Window for Compile Errors
# Category: command_line
# Tags: compilation, error-handling, productivity
---
Use :cw to open a quickfix window that lists compilation errors and allows quick navigation between error locations

```vim
set makeprg=javac
set makeef=c:\dev\src\errors.txt
set errorformat=%A%f:%l:\ %m,%C%m
noremap <M-1> :w<CR>:set ch=5<CR>:make -d C:\dev\classes %:p<CR>
noremap <M-2> :cp<CR>
noremap <M-3> :cn<CR>
noremap <M-4> :cl<CR>
```
```lua
vim.o.makeprg = 'javac'
vim.o.makeef = 'c:\\dev\\src\\errors.txt'
vim.o.errorformat = '%A%f:%l: %m,%C%m'

vim.keymap.set('n', '<M-1>', ':w<CR>:set ch=5<CR>:make -d C:\\dev\\classes %:p<CR>', { desc = 'Compile current file' })
vim.keymap.set('n', '<M-2>', ':cp<CR>', { desc = 'Previous error' })
vim.keymap.set('n', '<M-3>', ':cn<CR>', { desc = 'Next error' })
vim.keymap.set('n', '<M-4>', ':cl<CR>', { desc = 'List errors' })
```

**Source:** ** https://vim.fandom.com/wiki/VimTip458
***
# Title: Easily Capture Shell Command Output in Buffer
# Category: command_line
# Tags: shell-commands, external-tools, scripting
---
Provides multiple methods to insert shell command output into Vim/Neovim buffers, with flexible insertion techniques

```vim
" Command to create a new scratch buffer with command output
:command! -nargs=* -complete=shellcmd R new | setlocal buftype=nofile bufhidden=hide noswapfile | r !<args>
```
```lua
-- Lua equivalent for creating a command to capture shell output
vim.api.nvim_create_user_command('R', function(ctx)
  vim.cmd('new')
  vim.bo.buftype = 'nofile'
  vim.bo.bufhidden = 'hide'
  vim.bo.swapfile = false
  vim.cmd('r !' .. ctx.args)
end, { nargs = '*', complete = 'shellcmd' })
```

**Source:** ** https://vim.fandom.com/wiki/VimTip467
***
# Title: Quick XML Wellformedness Check
# Category: command_line
# Tags: xml, validation, external-tool
---
Validate XML file's wellformedness directly from Vim using xmllint

```vim
!xmllint --noout %
```
```lua
vim.cmd('!xmllint --noout %')
```

**Source:** ** https://vim.fandom.com/wiki/VimTip583
***
# Title: Create Custom Vim Commands with Autocompletion
# Category: command_line
# Tags: custom-commands, autocompletion, plugin-development
---
Demonstrates creating a user-defined command with range support, parameter passing, and autocompletion

```vim
" Create a custom command with autocompletion
command! -range=% -nargs=1 -complete=file MyCommand <line1>,<line2>call s:MyCommandFunction(<f-args>)

function! s:MyCommandFunction(...) range
  split
  execute "norm! " . a:firstline . "GV"
  execute "norm! " . a:lastline . 'G"ay'
  enew
  norm! "ap
  exe "sav! " . a:1
  q
endfunction
```
```lua
-- Lua equivalent for creating a custom command
vim.api.nvim_create_user_command('MyCommand', function(opts)
  local start_line = opts.line1
  local end_line = opts.line2
  local filename = opts.args
  
  -- Create a new buffer and copy selected lines
  local bufnr = vim.api.nvim_create_buf(true, true)
  vim.api.nvim_set_current_buf(bufnr)
  
  -- Get the lines from the original buffer
  local lines = vim.api.nvim_buf_get_lines(0, start_line - 1, end_line, false)
  vim.api.nvim_buf_set_lines(bufnr, 0, -1, false, lines)
  
  -- Save the buffer to the specified filename
  vim.cmd('write! ' .. filename)
  vim.cmd('bdelete')
end, {
  nargs = 1,
  range = true,
  complete = 'file'
})
```

**Source:** ** https://vim.fandom.com/wiki/VimTip591
***
# Title: Quick Python Code Execution in Vim
# Category: command_line
# Tags: python, execution, mapping
---
Simple mappings to quickly run Python code or the current file

```vim
" Save and run current Python file
noremap <F5> <ESC>:w<CR>:silent execute "!python %"<CR><CR>
```
```lua
vim.keymap.set('n', '<F5>', function()
  vim.cmd('write')  -- Save current file
  vim.cmd('!python %')  -- Execute current file
end, { desc = 'Run current Python file' })
```

**Source:** ** https://vim.fandom.com/wiki/VimTip609
***
# Title: Command Window Ctrl-D Completion
# Category: command_line
# Tags: completion, command-window, auto-completion
---
Add advanced completion functionality to command window using Ctrl-D

```vim
function! s:ECWCtrlD()
  if (match(@", '^ *[a-z]\?map\s\s*\(\S\S*\)\?\s*$') >=0 )
    let s:foo = @"
    let save_more=&more
    set nomore
    execute ':redir @" |'.s:foo.'|redir END'
    let &more = save_more
    put=@"
    return
  endif
  let s:foo = substitute(@", '\(.*\)\(\S\S*\s*\)$', '\2', '')
  let s:foo = substitute(s:foo, '\s*$', '*', '')
  let @"=glob(s:foo)
  if(@" == "") | let @"='no match' | endif
  put=@"
endfunction

command -nargs=0 ECWCtrlD call s:ECWCtrlD()
```
```lua
local function ecw_ctrl_d()
  local line = vim.fn.getline('.')
  local cursor_pos = vim.fn.col('.')
  local text_before_cursor = line:sub(1, cursor_pos)
  
  local completion = vim.fn.glob(text_before_cursor .. '*')
  
  if completion == '' then
    completion = 'no match'
  end
  
  vim.fn.append('.', completion)
end

vim.api.nvim_create_user_command('ECWCtrlD', ecw_ctrl_d, {})
```

**Source:** ** https://vim.fandom.com/wiki/VimTip681
***
# Title: Quick Copy and Paste with pbcopy/pbpaste
# Category: command_line
# Tags: macos, clipboard, file-operations
---
Use macOS pbcopy and pbpaste commands directly from Vim for system clipboard operations

```vim
" Copy current line to clipboard
:.!pbcopy

" Copy specific lines to clipboard
:4,8!pbcopy

" Copy current filename to clipboard
:!echo "%:p" | pbcopy

" Paste clipboard content to current line
:r !pbpaste
```
```lua
-- These can typically be used directly in Neovim's command mode as well
```

**Source:** ** https://vim.fandom.com/wiki/VimTip687
***
# Title: Dynamically Replace Grep with Custom Search Program
# Category: command_line
# Tags: search, custom-commands, quickfix
---
Create flexible custom commands that temporarily replace grep with alternative search tools like cscope or lid, allowing quick exploration of code without permanent configuration changes

```vim
fu! Mycscope(func)
  let tmp1=&grepprg
  let tmp2=&grepformat
  set grepformat=%f\ %*[a-zA-Z_0-9]\ %l\ %m
  set grepprg=cscope\ -R\ -L\ -3
  exe "grep ".a:func
  let &grepprg=tmp1
  let &grepformat=tmp2
endf
command -nargs=* CScope :silent call Mycscope("<args>")
```
```lua
function _G.mycscope(func)
  local tmp1 = vim.o.grepprg
  local tmp2 = vim.o.grepformat
  vim.o.grepformat = '%f %*[a-zA-Z_0-9] %l %m'
  vim.o.grepprg = 'cscope -R -L -3'
  vim.cmd('grep ' .. func)
  vim.o.grepprg = tmp1
  vim.o.grepformat = tmp2
end

vim.api.nvim_create_user_command('CScope', function(opts)
  _G.mycscope(opts.args)
end, { nargs = '*' })
```

**Source:** ** https://vim.fandom.com/wiki/VimTip688
***
# Title: Quick PHP Syntax Checking in Vim/Neovim
# Category: command_line
# Tags: php, syntax-checking, linting
---
Quickly check PHP syntax directly from the editor without leaving the buffer

```vim
map <C-B> :!php -l %<CR>
```
```lua
vim.keymap.set('n', '<C-b>', ':!php -l %<CR>', { desc = 'Check PHP syntax' })
```

**Source:** ** https://vim.fandom.com/wiki/VimTip692
***
# Title: Execute Shell Command in Explorer Directory
# Category: command_line
# Tags: shell-command, file-explorer, custom-function
---
Execute a shell command in the directory currently shown in the file explorer without changing the current working directory

```vim
function! MyFileHandler(filename)
  let oldpath = getcwd()
  let currentdirectory = ""
  if(isdirectory(a:filename))
    let currentdirectory = strpart(a:filename, 0, strlen(a:filename) - 1)
  else
    let currentdirectory = a:filename
  endif
  let lastslash = strridx(currentdirectory, "/")
  let currentdirectory = strpart(currentdirectory, 0, lastslash)
  let usercommand = input(currentdirectory . "# ")
  if(strlen(usercommand) > 0)
    execute "cd " . currentdirectory
    execute "!" . usercommand
    execute "cd " . oldpath
  endif
endfunction

let g:explFileHandler = "MyFileHandler"
```
```lua
function _G.my_file_handler(filename)
  local oldpath = vim.fn.getcwd()
  local currentdirectory = ""
  
  if vim.fn.isdirectory(filename) == 1 then
    currentdirectory = filename:sub(1, -2)
  else
    currentdirectory = filename
  end
  
  local lastslash = currentdirectory:match(".*()/.+$") or 0
  currentdirectory = currentdirectory:sub(1, lastslash)
  
  local usercommand = vim.fn.input(currentdirectory .. "# ")
  
  if #usercommand > 0 then
    vim.cmd('cd ' .. currentdirectory)
    vim.cmd('!' .. usercommand)
    vim.cmd('cd ' .. oldpath)
  end
end

-- Assuming you're using explorer.vim or similar plugin
vim.g.explFileHandler = 'my_file_handler'
```

**Source:** ** https://vim.fandom.com/wiki/VimTip717
***
# Title: Quick XML Validation with xmllint
# Category: command_line
# Tags: xml, validation, shell-command
---
Quickly check XML document well-formedness directly from Vim using xmllint

```vim
!xmllint --noout %
```
```lua
vim.cmd('!xmllint --noout %')
```

**Source:** ** https://vim.fandom.com/wiki/Vim_as_XML_Editor
***
