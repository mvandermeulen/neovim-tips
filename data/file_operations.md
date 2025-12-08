# Title: Save file
# Category: File Operations
# Tags: file, save, write
---
Use `:w` to save current file, `:w {file}` to save as new file, or `:wall` to save all files.

```vim
:w             " save current file
:w newfile.txt " save as new file
:wall          " save all files
```

**Source:** Community contributed
***
# Title: Save as
# Category: File
# Tags: save, file
---
Use `:sav[eas] filepath` to save file under a different name

```vim
:sav ~/tmp/work.txt
```

**Source:** Community contributed
***
# Title: Insert current date
# Category: File Operations
# Tags: date, insert, command
---
Use `:r !date` to insert current date at cursor position.

```vim
:r !date  " insert current date
```

**Source:** Community contributed
***
# Title: Reload file from disk
# Category: File Operations
# Tags: reload, file, refresh
---
Use `:e!` to reload current file from disk, discarding unsaved changes.

```vim
:e!  " reload file from disk
```

**Source:** Community contributed
***
# Title: Ex commands - read and write operations
# Category: File Operations
# Tags: ex, read, write, append, output
---
Use `:read` or `:r` to read file into buffer, `:write` range to write part of buffer, `:.,$w` for current to end.

```vim
:r file.txt     " read file into current buffer
:read !date     " read output of command
:1,10w part.txt " write lines 1-10 to file
:.,$w end.txt   " write from current line to end
```

**Source:** Community contributed
***
# Title: Ex commands - file permissions and attributes
# Category: File Operations
# Tags: ex, file, permission, readonly, modifiable
---
Use `:set readonly` to make read-only, `:set nomodifiable` to prevent changes, `:set fileformat` for line endings.

```vim
" Vimscript:
:set readonly      " make buffer read-only
:set nomodifiable  " prevent any modifications
:set fileformat=unix  " set Unix line endings
:set fileformat=dos   " set DOS line endings
```
```lua
-- Lua:
vim.opt.readonly = true  -- make buffer read-only
vim.opt.modifiable = false  -- prevent any modifications
vim.opt.fileformat = 'unix'  -- set Unix line endings
vim.opt.fileformat = 'dos'   -- set DOS line endings
```

**Source:** Community contributed
***
# Title: Save multiple files at once
# Category: File Operations
# Tags: file, save, multiple, wall, xa
---
Use `:wa` to save all modified files, `:xa` to save all and exit, `:wqa` to save all and quit.

```vim
:wa      " write (save) all modified files
:xa      " write all modified files and exit
:wqa     " write all and quit all windows
:qa!     " quit all without saving
```

**Source:** Community contributed
***
# Title: Path separator conversion
# Category: File Operations
# Tags: path, separator, backslash, forward, slash
---
Use `:s` commands to easily convert between backslash and forward slash in file paths.

```vim
" Convert backslashes to forward slashes:
:%s/\\/\//g

" Convert forward slashes to backslashes:
:%s/\//\\/g

" Or use built-in function:
:echo substitute(@%, '\\', '/', 'g')
```

**Source:** Community contributed
***
# Title: Update file only if changed
# Category: File Operations
# Tags: file, update, save, changed, conditional
---
Use `:update` to save file only if it has been modified, more efficient than `:write`.

```vim
:update           " save only if file is modified
:map <F2> :update<CR>  " map F2 to conditional save
```

**Source:** Community contributed
***
# Title: Check file existence in scripts
# Category: File Operations
# Tags: file, exist, check, script, function
---
Use `filereadable()` to check if file exists and is readable, `readfile()` to read all lines.

```vim
" In Vim script:
if filereadable('config.vim')
  source config.vim
endif

" Read file into list:
let lines = readfile('data.txt')
```

**Source:** Community contributed
***
# Title: Browse for files with dialog
# Category: File Operations
# Tags: browse, dialog, gui, file, open
---
Use `:browse {command}` to open file browser dialog for commands that take filenames (GUI only).

```vim
:browse edit      " open file browser to edit file
:browse saveas    " open save-as dialog
:browse read      " browse to read file into buffer
:browse source    " browse to source a script file
```

**Source:** Community contributed
***
# Title: Write file and create all directories form the full file path
# Category: File Operations
# Tags: file, save, write
---
Use this command to write file if the full path contains non-existent directories. All directories that do not exist will be created before the save:

```vim
:write ++p
```

**Source:** Community contributed
***
# Title: Convert File Line Endings Easily
# Category: file_operations
# Tags: file-format, line-endings, conversion
---
Quickly convert file line endings between unix, dos, and mac formats with simple Vim commands

```vim
:e ++ff=dos
:setlocal ff=unix
:w
```
```lua
-- Convert current file to unix line endings
vim.cmd('e ++ff=dos')
vim.cmd('setlocal ff=unix')
vim.cmd('w')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/%5EM)
***
# Title: Batch Convert Line Endings Across Files
# Category: file_operations
# Tags: file-format, batch-processing, line-endings
---
Convert line endings for multiple files in a single operation using argdo or bufdo

```vim
:args *.c *.h
:argdo set ff=unix|update
```
```lua
-- Convert all .c and .h files to unix line endings
vim.cmd('args *.c *.h')
vim.cmd('argdo set ff=unix|update')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/%5EM)
***
# Title: Quick File Extension Manipulation
# Category: file_operations
# Tags: file-management, command-line
---
Easily add or change file extensions using custom commands that leverage Vim's expand() function

```vim
command! -nargs=1 AddExt execute "saveas ".expand("%:p").<q-args>
command! -nargs=1 ChgExt execute "saveas ".expand("%:p:r").<q-args>
```
```lua
vim.api.nvim_create_user_command('AddExt', function(opts)
  vim.cmd('saveas ' .. vim.fn.expand('%:p') .. opts.args)
end, { nargs = 1 })

vim.api.nvim_create_user_command('ChgExt', function(opts)
  vim.cmd('saveas ' .. vim.fn.expand('%:p:r') .. opts.args)
end, { nargs = 1 })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Add/change_file_extension_in_current_buffer)
***
# Title: Add Vim to Windows Send To Menu
# Category: file_operations
# Tags: windows, file-management, productivity
---
Easily add Vim to Windows Send To context menu for quick file opening with custom options

```vim
" Example shortcut creation in SendTo folder
" Use gvim.exe with various launch options
" e.g., gvim.exe -d (diff mode)
" e.g., gvim.exe -R (read-only mode)
```
```lua
-- In Neovim, this is more about file associations and keymaps
-- Lua equivalent would be configuring file handlers
vim.g.neovide_input_use_logo = true  -- Example of custom file handling
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Add_Vim_to_Windows_Send_To_menu)
***
# Title: Flexible Vim File Launch Options
# Category: file_operations
# Tags: windows, file-launch, custom-options
---
Create shortcuts to launch Vim with specific modes like diff or read-only

```vim
" Launch options for different file editing scenarios
" -d: Diff mode
" -R: Read-only mode
" -p: Open files in tabs
```
```lua
-- Lua approach to similar file launch configurations
-- Can be done via autocmds or file type associations
vim.api.nvim_create_autocmd('BufRead', {
  pattern = '*',
  callback = function()
    -- Custom file handling logic
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Add_Vim_to_Windows_Send_To_menu)
***
# Title: Open Files in Tabs Across Multiple Instances
# Category: file_operations
# Tags: file-handling, tabs, windows
---
Automatically open files in new tabs within the same Vim/Neovim instance using remote tab commands

```vim
gvim.exe --remote-tab-silent "%1"
```
```lua
-- For Neovim, this would typically be handled by terminal or file manager integration
-- Can be configured in init.lua with autocmds or external scripts
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Add_open-in-tabs_context_menu_for_Windows)
***
# Title: Quickly Switch Between Source and Header Files
# Category: file_operations
# Tags: file-navigation, c-development, productivity
---
Easily toggle between corresponding source and header files in C/C++ projects

```vim
" Map key combination to switch between .c/.cpp and .h files
map <F4> :e %:p:s,.h$,.X123X,:s,.cpp$,.h,:s,.X123X$,.cpp,<CR>
```
```lua
vim.keymap.set('n', '<F4>', function()
  local current_file = vim.fn.expand('%:p')
  local new_file = current_file:gsub('\.h$', '.X123X'):gsub('\.cpp$', '.h'):gsub('\.X123X$', '.cpp')
  vim.cmd.edit(new_file)
end, { desc = 'Switch between source and header' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/All_tips_for_C_family_programming)
***
# Title: Open All Files in Tabs by Default
# Category: file_operations
# Tags: tab-management, autocmd, workflow
---
Automatically open command-line arguments in separate tabs and create new tabs for each buffer

```vim
autocmd VimEnter * tab all
autocmd BufAdd * exe 'tablast | tabe "' . expand('<afile>') . '"'
```
```lua
vim.api.nvim_create_augroup('TabManagement', { clear = true })

vim.api.nvim_create_autocmd('VimEnter', {
  group = 'TabManagement',
  callback = function()
    vim.cmd('tab all')
  end
})

vim.api.nvim_create_autocmd('BufAdd', {
  group = 'TabManagement',
  callback = function()
    vim.cmd('tablast | tabe ' .. vim.fn.expand('<afile>'))
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Alternative_tab_navigation)
***
# Title: Associate Extensionless Files with Vim in Windows
# Category: file_operations
# Tags: windows, file-association, file-handling
---
Automatically open files without extensions in Vim using Windows command prompt or registry

```vim
assoc .=txtfile
```
```lua
-- For Neovim, this is more of a Windows system configuration
-- Typically handled through external system settings
-- Lua equivalent would involve using vim.fn to interact with system
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Associate_files_with_no_extension_to_Vim_under_Windows)
***
# Title: Launch Files with Default Application
# Category: file_operations
# Tags: windows, file-launch
---
Open the current file with its default system handler, similar to double-clicking in Windows Explorer

```vim
nmap <Leader>x :silent ! start "1" "%:p"<CR>
```
```lua
vim.keymap.set('n', '<Leader>x', function()
  vim.cmd('silent !start "1" "' .. vim.fn.expand('%:p') .. '"')
end, { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Async_command)
***
# Title: Set Working Directory to Current File
# Category: file_operations
# Tags: navigation, file-management, workflow
---
Automatically change Vim's working directory to the directory of the current file, making file operations more convenient

```vim
set autochdir

" Alternative manual mapping
nnoremap <leader>cd :cd %:p:h<CR>:pwd<CR>
```
```lua
-- Set working directory automatically
vim.opt.autochdir = true

-- Or create a manual mapping
vim.keymap.set('n', '<leader>cd', function()
  vim.cmd('cd %:p:h')
  print(vim.fn.getcwd())
end, { desc = 'Change to current file directory' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Authors)
***
# Title: Automatically Create Backup and Tmp Directories
# Category: file_operations
# Tags: backup, directory-management, cross-platform
---
Automatically creates backup and temporary directories across different operating systems, ensuring Vim has proper directories for storing backup and swap files

```vim
function! InitBackupDir()
  if has('win32') || has('win32unix') "windows/cygwin
    let l:separator = '_'
  else
    let l:separator = '.'
  endif
  let l:parent = $HOME . '/' . l:separator . 'vim/'
  let l:backup = l:parent . 'backup/'
  let l:tmp = l:parent . 'tmp/'
  if exists('*mkdir')
    if !isdirectory(l:parent)
      call mkdir(l:parent)
    endif
    if !isdirectory(l:backup)
      call mkdir(l:backup)
    endif
    if !isdirectory(l:tmp)
      call mkdir(l:tmp)
    endif
  endif
  let l:missing_dir = 0
  if isdirectory(l:tmp)
    execute 'set backupdir=' . escape(l:backup, ' ') . '/,.'
  else
    let l:missing_dir = 1
  endif
  if isdirectory(l:backup)
    execute 'set directory=' . escape(l:tmp, ' ') . '/,.'
  else
    let l:missing_dir = 1
  endif
  if l:missing_dir
    echo 'Warning: Unable to create backup directories:' l:backup 'and' l:tmp
    echo 'Try: mkdir -p' l:backup
    echo 'and: mkdir -p' l:tmp
    set backupdir=.
    set directory=.
  endif
endfunction
call InitBackupDir()
```
```lua
local function init_backup_dir()
  local separator = vim.fn.has('win32') == 1 and '_' or '.'
  local parent = vim.fn.expand('$HOME') .. '/' .. separator .. 'vim/'
  local backup = parent .. 'backup/'
  local tmp = parent .. 'tmp/'

  if vim.fn.exists('*mkdir') then
    if not vim.fn.isdirectory(parent) then
      vim.fn.mkdir(parent, 'p')
    end
    if not vim.fn.isdirectory(backup) then
      vim.fn.mkdir(backup, 'p')
    end
    if not vim.fn.isdirectory(tmp) then
      vim.fn.mkdir(tmp, 'p')
    end
  end

  local missing_dir = false
  if vim.fn.isdirectory(tmp) then
    vim.opt.backupdir = backup .. ',.'
  else
    missing_dir = true
  end

  if vim.fn.isdirectory(backup) then
    vim.opt.directory = tmp .. ',.'
  else
    missing_dir = true
  end

  if missing_dir then
    print('Warning: Unable to create backup directories: ' .. backup .. ' and ' .. tmp)
    print('Try: mkdir -p ' .. backup)
    print('and: mkdir -p ' .. tmp)
    vim.opt.backupdir = '.'
    vim.opt.directory = '.'
  end
end

init_backup_dir()
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Automatically_create_tmp_or_backup_directories)
***
# Title: Auto-Detect and Reload Mixed Line Endings
# Category: file_operations
# Tags: file-format, autocmd, line-endings
---
Automatically detect and reload files with mixed line endings, converting from Unix to DOS format when CR characters are detected at line ends

```vim
autocmd BufReadPost * nested
      \ if !exists('b:reload_dos') && !&binary && &ff=='unix' && (0 < search('\r$', 'nc')) |
      \   let b:reload_dos = 1 |
      \   e ++ff=dos |
      \ endif
```
```lua
vim.api.nvim_create_autocmd('BufReadPost', {
  nested = true,
  callback = function()
    local buf = vim.api.nvim_get_current_buf()
    if not vim.b[buf].reload_dos and
       not vim.o.binary and
       vim.o.fileformat == 'unix' and
       vim.fn.search('\r$', 'nc') > 0 then
      vim.b[buf].reload_dos = true
      vim.cmd('e ++ff=dos')
    end
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Automatically_reload_files_with_mixed_line-endings_in_DOS_fileformat)
***
# Title: Quick File Encoding Detection in Bash
# Category: file_operations
# Tags: bash, encoding, file-detection
---
Create a Bash alias to quickly detect file encoding using Vim without fully opening the file

```vim
alias vimenc='vim -c \'let $enc = &fileencoding | execute "!echo Encoding:  $enc" | q\''

# Usage: vimenc filename.xml
```
```lua
-- In your shell config (e.g., .bashrc or .zshrc)
-- Use the same alias as in Vimscript
-- Or create a Lua-based function
function _G.detect_file_encoding(filename)
  local encoding = vim.fn.readfile(filename, '', 1)
  print('Encoding: ' .. vim.o.fileencoding)
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Bash_file_encoding_alias)
***
# Title: Bulk Rename Files Using Vim
# Category: file_operations
# Tags: file-manipulation, shell-integration, bulk-rename
---
Efficiently rename multiple files by generating rename commands in Vim and executing them via shell

```vim
# List files
:ls | vim -

# Rename to lowercase
:%s/.*/mv -i '&' \L'&'/g

# Execute rename commands
:w !sh
```
```lua
-- Equivalent in Neovim can use vim.fn and vim.cmd
-- Open file list
vim.cmd('read !ls')

-- Create rename commands
vim.cmd(':%s/.*/mv -i "&" \L"&"/g')

-- Execute shell commands
vim.cmd(':w !sh')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Bulk_rename_files_with_Vim)
***
# Title: List Files in Current Directory Tree
# Category: file_operations
# Tags: file-listing, directory-navigation, custom-function
---
Create a function to recursively list all files in the current directory tree, displaying them in a new buffer for easy browsing and reference

```vim
function! ListTree(dir)
  new
  set buftype=nofile
  set bufhidden=hide
  set noswapfile
  normal i.
  while 1
    let file = getline(".")
    if (file == '')
      normal dd
    elseif (isdirectory(file))
      normal dd
      let @" = glob(file . "/*")
      normal O
      normal P
      let @" = glob(file . "/.[^.]*")
      if (@" != '')
        normal O
        normal P
      endif
    else
      if (line('.') == line('$'))
        return
      else
        normal j
      endif
    endif
  endwhile
endfunction

map <Leader>L :call ListTree('.')<CR>
```
```lua
function _G.list_tree(dir)
  vim.cmd('new')
  vim.bo.buftype = 'nofile'
  vim.bo.bufhidden = 'hide'
  vim.bo.swapfile = false

  vim.fn.append(0, '.')
  vim.cmd('normal! dd')

  local function process_file(file)
    if vim.fn.isdirectory(file) == 1 then
      local files = vim.fn.glob(file .. '/*')
      local hidden_files = vim.fn.glob(file .. '/.[^.]*')

      vim.fn.append('$', vim.split(files, '\n'))
      if hidden_files ~= '' then
        vim.fn.append('$', vim.split(hidden_files, '\n'))
      end
    end
  end

  local current_line = 1
  while current_line <= vim.fn.line('$') do
    local file = vim.fn.getline(current_line)
    if file ~= '' then
      process_file(file)
    end
    current_line = current_line + 1
  end
end

vim.keymap.set('n', '<Leader>L', _G.list_tree, { desc = 'List files in current directory tree' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Collect_filenames_of_current_subtree)
***
# Title: Customize Netrw Directory Listing Style
# Category: file_operations
# Tags: file-explorer, netrw, configuration
---
Set Netrw to display a tree-style directory listing, which provides a more comprehensive view of file structures

```vim
let g:netrw_liststyle=3
```
```lua
vim.g.netrw_liststyle = 3
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Collect_filenames_of_current_subtree)
***
# Title: Compress Vim Documentation Files
# Category: file_operations
# Tags: disk-space, documentation, compression
---
Compress Vim documentation files to save disk space while maintaining readability using gzip

```vim
# Compress all .txt files in doc directory
:!gzip *.txt

# Uncompress help.txt separately
:!gunzip help.txt
```
```lua
-- Compress files using Lua system command
vim.fn.system('gzip ' .. vim.o.runtimepath .. '/doc/*.txt')
vim.fn.system('gunzip ' .. vim.o.runtimepath .. '/doc/help.txt')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Compress_Vim_doc_files_to_save_space)
***
# Title: Quick File Copy Within Vim
# Category: file_operations
# Tags: file-management, command, productivity
---
Create a custom command to easily copy the current file to another location without leaving Vim

```vim
command Cpage silent !cp '%:p' "c:/Progra~1/Tomcat/webapps/console/pages/%"
```
```lua
vim.api.nvim_create_user_command('Cpage', function()
  local current_file = vim.fn.expand('%:p')
  local dest_path = 'c:/Progra~1/Tomcat/webapps/console/pages/'
  vim.fn.system('cp "' .. current_file .. '" "' .. dest_path .. '"')
end, {})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Copy_current_file_to_another_location_from_within_vim)
***
# Title: Create and Restore Vim Sessions Easily
# Category: file_operations
# Tags: session-management, workspace, productivity
---
Save and restore Vim editing sessions, including window layouts, open buffers, and project state with a single command

```vim
" Save session
:mksession projectname.vis

" Restore session
gvim -S projectname.vis
```
```lua
-- Save session
vim.cmd('mksession projectname.vis')

-- Restore session
-- Can be done via command-line or in Lua
require('nvim-session-manager').save_current_session()
require('nvim-session-manager').load_session()
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Create_Vim_sessions_that_you_can_open_with_double-click_in_Windows)
***
# Title: Create a Personal Knowledge Base in Vim
# Category: file_operations
# Tags: knowledge-management, file-navigation, organization
---
Efficiently manage a personal knowledge base using Vim's built-in file navigation and search capabilities

```vim
" Use gf to jump between files
" Create lowercase files for consistent naming
" Use directories for large topics
```
```lua
-- Use vim.cmd('gf') to jump between files
-- Recommended: Create a consistent file naming strategy
-- Use directories to organize large topics

-- Example of setting up a knowledge base directory
vim.g.kb_path = '~/knowledge_base'

-- Function to quickly open or create a knowledge base file
vim.keymap.set('n', '<leader>kn', function()
  local filename = vim.fn.input('Enter knowledge base file name: ')
  vim.cmd('edit ' .. vim.g.kb_path .. '/' .. filename:lower())
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Creating_and_maintaining_a_personal_Knowledge_Base_with_Vim)
***
# Title: Bulk Create Directories from Text List
# Category: file_operations
# Tags: mkdir, batch-operations, file-management
---
Create multiple directories from a list of names in a text file using a single Vim command

```vim
%g/\<\w\+\>/ y A | exe ' !mkdir '. shellescape(substitute(substitute(@a, '\n\+\s*', '', ''), '\s*\n\+', '', '')) | let @a = ""
```
```lua
-- Lua equivalent for creating directories from a list
local function create_dirs_from_list()
  local lines = vim.fn.getline(1, '$')
  for _, line in ipairs(lines) do
    local dir = line:match('%w+')
    if dir then
      vim.fn.mkdir(dir, 'p')
    end
  end
end

-- Usage: Call create_dirs_from_list() in Neovim
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Creating_directories_from_a_list)
***
# Title: Sync Disk After Every Write to Prevent Data Loss
# Category: file_operations
# Tags: data-protection, file-safety, crash-prevention
---
Automatically run sync command after each buffer write to reduce chances of file corruption during unexpected system crashes or power failures

```vim
" disk sync after every write
au BufWritePost * silent !sync
```
```lua
vim.api.nvim_create_autocmd('BufWritePost', {
  callback = function()
    vim.fn.system('sync')
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Decrease_chances_of_file_corruption_in_case_of_computer_crash)
***
# Title: Delete Files Directly from Vim
# Category: file_operations
# Tags: file-management, command-line
---
Create a custom command to delete files using Vim's delete() function, with filename completion and success/failure confirmation

```vim
command! -complete=file -nargs=1 Remove :echo 'Remove: '.'<f-args>'.' '.(delete(<f-args>) == 0 ? 'SUCCEEDED' : 'FAILED')
```
```lua
vim.api.nvim_create_user_command('Remove', function(opts)
  local filename = opts.args
  local result = vim.fn.delete(filename)
  print(string.format('Remove: %s %s', filename, result == 0 and 'SUCCEEDED' or 'FAILED'))
end, { nargs = 1, complete = 'file' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Delete_files_with_a_Vim_command)
***
# Title: Delete Current File and Close Buffer
# Category: file_operations
# Tags: buffer-management, file-delete
---
Quick command to delete the current file and close its buffer in one step

```vim
call delete(expand('%')) | bdelete!
```
```lua
vim.fn.delete(vim.fn.expand('%')) vim.cmd('bdelete!')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Delete_files_with_a_Vim_command)
***
# Title: Preserve Missing End-of-Line When Saving Files
# Category: file_operations
# Tags: file-formatting, eol, file-saving
---
Automatically preserve files without an end-of-line character, maintaining the original file format across different operating systems

```vim
" Preserve noeol (missing trailing eol) when saving file
augroup automatic_noeol
  au!
  au BufWritePre  * call <SID>TempSetBinaryForNoeol()
  au BufWritePost * call <SID>TempRestoreBinaryForNoeol()
augroup END

function! s:TempSetBinaryForNoeol()
  let s:save_binary = &binary
  if ! &eol && ! &binary
    let s:save_view = winsaveview()
    setlocal binary
    if &ff == "dos" || &ff == "mac"
      if line('$') > 1
        undojoin | exec "silent 1,$-1normal! A\<C-V>\<C-M>"
      endif
    endif
    if &ff == "mac"
      undojoin | %join!
    endif
  endif
endfunction

function! s:TempRestoreBinaryForNoeol()
  if ! &eol && ! s:save_binary
    if &ff == "dos"
      if line('$') > 1
        silent! undojoin | silent 1,$-1s/\r$//e
      endif
    elseif &ff == "mac"
      silent! undojoin | silent %s/\r/\r/ge
    endif
    setlocal nobinary
    call winrestview(s:save_view)
  endif
endfunction
```
```lua
local function temp_set_binary_for_noeol()
  local save_binary = vim.o.binary
  if not vim.o.eol and not vim.o.binary then
    local save_view = vim.fn.winsaveview()
    vim.o.binary = true
    local fileformat = vim.o.ff

    if fileformat == 'dos' or fileformat == 'mac' then
      if vim.fn.line('$') > 1 then
        vim.cmd('undojoin')
        vim.cmd('silent 1,$-1normal! A\<C-V>\<C-M>')
      end
    end

    if fileformat == 'mac' then
      vim.cmd('undojoin')
      vim.cmd('%join!')
    end

    return save_view, save_binary
  end
  return nil, save_binary
end

local function temp_restore_binary_for_noeol(save_view, save_binary)
  if save_view and not vim.o.eol and not save_binary then
    local fileformat = vim.o.ff

    if fileformat == 'dos' then
      if vim.fn.line('$') > 1 then
        vim.cmd('silent! undojoin')
        vim.cmd('silent 1,$-1s/\r$//e')
      end
    elseif fileformat == 'mac' then
      vim.cmd('silent! undojoin')
      vim.cmd('silent %s/\r/\r/ge')
    end

    vim.o.binary = false
    vim.fn.winrestview(save_view)
  end
end

-- Autocmd setup
vim.api.nvim_create_augroup('automatic_noeol', { clear = true })
vim.api.nvim_create_autocmd('BufWritePre', {
  group = 'automatic_noeol',
  callback = function()
    local save_view, save_binary = temp_set_binary_for_noeol()
    vim.b.noeol_save_view = save_view
    vim.b.noeol_save_binary = save_binary
  end
})

vim.api.nvim_create_autocmd('BufWritePost', {
  group = 'automatic_noeol',
  callback = function()
    temp_restore_binary_for_noeol(vim.b.noeol_save_view, vim.b.noeol_save_binary)
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Do_not_auto-add_a_newline_at_EOF)
***
# Title: Drag and Drop Files into Vim Command Line
# Category: file_operations
# Tags: file-navigation, command-line, drag-and-drop
---
Easily insert file paths into Vim command line by drag and dropping from file explorer or file manager

```lua
-- Drag and drop files works natively in Vim/Neovim
-- In command line, type :edit and then drag file
-- Or simply drag file directly into Vim window
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Drag_and_drop_file_names_into_the_Vim_command_line)
***
# Title: Modifier Keys for Drag and Drop in Vim
# Category: file_operations
# Tags: file-navigation, window-management, shortcuts
---
Use modifier keys to control how files are opened when drag and dropped

```lua
-- Drag and drop behaviors with modifier keys:
-- Ctrl: Open file in new split window
-- Shift: Change to file's directory
-- Default: Open file in current window
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Drag_and_drop_file_names_into_the_Vim_command_line)
***
# Title: Sync Vim Runtime Files with rsync
# Category: file_operations
# Tags: file-sync, runtime-files, system-management
---
Efficiently synchronize Vim runtime files from a remote FTP server using rsync, keeping your local runtime environment up to date

```vim
# Rsync command to sync Vim runtime files
rsync -avzcP --delete --exclude='/dos/' ftp.nluug.nl::Vim/runtime/ ./runtime/
```
```lua
-- While rsync is a shell command, you can trigger it in Lua using vim.fn.system()
vim.fn.system('rsync -avzcP --delete --exclude="/dos/" ftp.nluug.nl::Vim/runtime/ ./runtime/')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Easily_keep_runtime_files_up_to_date)
***
# Title: Quick Source/Header File Switching
# Category: file_operations
# Tags: navigation, file-switching, programming
---
Easily switch between source and header files in C/C++ projects with a flexible function that handles multiple file extensions

```vim
function! SwitchSourceHeader()
  if (expand("%:e") == "cpp")
    find %:t:r.h
  else
    find %:t:r.cpp
  endif
endfunction

nmap ,s :call SwitchSourceHeader()<CR>
```
```lua
function _G.switch_source_header()
  local ext = vim.fn.expand('%:e')
  if ext == 'cpp' then
    vim.cmd('find ' .. vim.fn.expand('%:t:r') .. '.h')
  else
    vim.cmd('find ' .. vim.fn.expand('%:t:r') .. '.cpp')
  end
end

vim.keymap.set('n', ',s', _G.switch_source_header, { desc = 'Switch between source and header' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Easily_switch_between_source_and_header_file)
***
# Title: Browse and Edit JAR Files Directly in Vim/Neovim
# Category: file_operations
# Tags: zip, java, file-browsing
---
Treat JAR files as zip archives, allowing direct browsing and editing of compressed file contents within Vim/Neovim

```vim
au BufRead,BufNewFile *.jar,*.war,*.ear,*.sar,*.rar set filetype=zip

" Alternative method
au BufReadCmd *.jar call zip#Browse(expand("<amatch>"))
```
```lua
vim.api.nvim_create_autocmd({"BufRead", "BufNewFile"}, {
  pattern = {"*.jar", "*.war", "*.ear", "*.sar", "*.rar"},
  callback = function()
    vim.bo.filetype = "zip"
  end
})

-- Alternative method for browsing
-- Requires zipPlugin to be installed
vim.api.nvim_create_autocmd("BufReadCmd", {
  pattern = "*.jar",
  callback = function()
    vim.fn['zip#Browse'](vim.fn.expand('<amatch>'))
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Edit_Java_jar_and_other_files)
***
# Title: Open or Jump to File in New Tab
# Category: file_operations
# Tags: file-handling, tabs, navigation
---
Use :drop to edit a file or jump to its existing tab/window, with option to open in new tab

```vim
" Open file in new tab or jump to existing
:tab drop filename.txt

" Custom command to simplify file opening
command! -nargs=1 -complete=file O tab drop <args>
```
```lua
-- Open file in new tab or jump to existing
vim.cmd('tab drop ' .. vim.fn.expand('%:p'))

-- Create custom command in Lua
vim.api.nvim_create_user_command('O', function(opts)
  vim.cmd('tab drop ' .. opts.args)
end, { nargs = 1, complete = 'file' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Edit_a_file_or_jump_to_it_if_already_open)
***
# Title: Create Timestamped Temporary File Copy
# Category: file_operations
# Tags: file-management, backup, mapping
---
Quickly create a timestamped copy of the current file in a temporary directory for safe editing

```vim
:map zs :exe "sav $TMP/" . expand("%:t") . strftime("-%Y-%m-%d_%H%M%S")<CR>
```
```lua
vim.keymap.set('n', 'zs', function()
  local filename = vim.fn.expand('%:t')
  local timestamp = os.date('%Y-%m-%d_%H%M%S')
  local tmp_dir = os.getenv('TMP') or '/tmp'
  local new_filename = string.format('%s/%s-%s', tmp_dir, filename, timestamp)
  vim.cmd('saveas ' .. new_filename)
end, { desc = 'Save file with timestamp in temp directory' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Edit_a_temporary_copy_of_the_current_file)
***
# Title: Edit Remote Files with SCP in Vim
# Category: file_operations
# Tags: remote-editing, ssh, networking
---
Easily edit configuration files across multiple remote servers using Vim's netrw plugin and SCP protocol without multiple logins

```vim
" Project file example for remote config editing
" Create a .project file with SCP paths
" Edit files across multiple servers transparently
```
```lua
-- Lua equivalent would use vim.fn.system() or a plugin like plenary.nvim for remote file handling
-- Example remote file opening
require('plenary.nvim').curl.get('scp://server1.domain.com///opt/myapp/etc/myapprc')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Edit_and_organize_several_remote_files_easily)
***
# Title: Secure GPG File Editing in Vim/Neovim
# Category: file_operations
# Tags: encryption, gpg, security
---
Automatically handle GPG encrypted files with secure buffer and write operations

```vim
augroup encrypted
  au!
  autocmd BufReadPre,FileReadPre *.gpg
    \ setlocal noswapfile bin
  autocmd BufReadPost,FileReadPost *.gpg
    \ execute "'[,']!gpg --decrypt --default-recipient-self" |
    \ setlocal nobin |
    \ execute "doautocmd BufReadPost " . expand("%:r")
  autocmd BufWritePre,FileWritePre *.gpg
    \ setlocal bin |
    \ '[,']!gpg --encrypt --default-recipient-self
  autocmd BufWritePost,FileWritePost *.gpg
    \ silent u |
    \ setlocal nobin
augroup END
```
```lua
vim.api.nvim_create_augroup('encrypted', { clear = true })

vim.api.nvim_create_autocmd({'BufReadPre', 'FileReadPre'}, {
  group = 'encrypted',
  pattern = '*.gpg',
  callback = function()
    vim.opt_local.swapfile = false
    vim.opt_local.binary = true
  end
})

vim.api.nvim_create_autocmd({'BufReadPost', 'FileReadPost'}, {
  group = 'encrypted',
  pattern = '*.gpg',
  callback = function()
    vim.cmd("'[,']!gpg --decrypt --default-recipient-self")
    vim.opt_local.binary = false
    vim.cmd("doautocmd BufReadPost " .. vim.fn.expand('%:r'))
  end
})

vim.api.nvim_create_autocmd({'BufWritePre', 'FileWritePre'}, {
  group = 'encrypted',
  pattern = '*.gpg',
  callback = function()
    vim.opt_local.binary = true
    vim.cmd("'[,']!gpg --encrypt --default-recipient-self")
  end
})

vim.api.nvim_create_autocmd({'BufWritePost', 'FileWritePost'}, {
  group = 'encrypted',
  pattern = '*.gpg',
  callback = function()
    vim.cmd('silent u')
    vim.opt_local.binary = false
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Edit_gpg_encrypted_files)
***
# Title: Batch Edit Multiple Files from File List
# Category: file_operations
# Tags: batch-editing, macro, command-line
---
Efficiently edit multiple files using a Vim macro and command-line file loading

```vim
vim -s scriptin `cat file-containing-files`

# In scriptin macro file:
qq/pattern^Mdd:wn^M^M@qq@q
```
```lua
-- Open multiple files from a list
-- Lua equivalent would typically use vim.fn.argv() or a plugin like telescope
-- For macro recording:
vim.fn.setreg('q', 'search_pattern_and_delete_macro')
-- Execute macro across files
vim.cmd('argdo norm! @q')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Edit_multiple_files_from_a_list_of_file_names)
***
# Title: Edit Remote Files via Network Protocols
# Category: file_operations
# Tags: remote-editing, network, scp, file-transfer
---
Directly edit remote files using built-in Vim network protocols without manual file transfers

```vim
vim scp://username@host//path/to/file
:Nread scp://username@host//path/to/file
:Nwrite scp://username@host//path/to/file
```
```lua
-- Open remote file
vim.cmd('edit scp://username@host//path/to/file')

-- Alternatively using Lua
vim.api.nvim_cmd({cmd = 'edit', args = {'scp://username@host//path/to/file'}}, {})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Edit_remote_files_locally_via_SCP/RCP/FTP)
***
# Title: Break Hard Links When Editing Files
# Category: file_operations
# Tags: hard-links, file-backup, unix
---
Automatically break hard links when editing a file, creating a separate copy instead of modifying all linked files

```vim
set backupcopy=auto,breakhardlink
```
```lua
vim.opt.backupcopy = "auto,breakhardlink"
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Editing_a_hard_link_to_a_file)
***
# Title: Edit Files on Non-Standard Port FTP Server
# Category: file_operations
# Tags: remote-editing, ftp, file-access
---
Edit remote files on an FTP server using a non-standard port by escaping the port number

```vim
:e ftp://ftp.server\#2121/path/to/file/filename
```
```lua
-- Neovim uses the same syntax as Vim for remote file editing
vim.cmd('e ftp://ftp.server\#2121/path/to/file/filename')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Editing_files_on_an_ftp_server_listening_on_a_non-standard_port)
***
# Title: Edit Remote Files via SCP
# Category: file_operations
# Tags: remote-editing, network, ssh
---
Open and edit remote files directly through SCP using Vim's netrw plugin, specifying remote user and absolute path

```vim
vim scp://remoteuser@server.tld//absolute/path/to/document

" Alternative methods:
:e scp://remoteuser@server.tld//absolute/path/to/document
:tabe scp://remoteuser@server.tld//absolute/path/to/document
```
```lua
-- Neovim supports the same SCP syntax
-- Open remote file in current window
vim.cmd('e scp://remoteuser@server.tld//absolute/path/to/document')

-- Open remote file in new tab
vim.cmd('tabe scp://remoteuser@server.tld//absolute/path/to/document')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Editing_remote_files_via_scp_in_vim)
***
# Title: Encrypt Files Securely in Vim
# Category: file_operations
# Tags: encryption, security, file-management
---
Use :X command to encrypt files and prevent unauthorized access, with additional settings to minimize trace evidence

```vim
" Encrypt file
:X

" Prevent leaving traces in viminfo
set viminfo='0,"/0,/0,:0,f0

" Disable swap and backup files
set noswapfile
set nobackup
set nowritebackup
```
```lua
-- Encryption is initiated interactively via :X command

-- Prevent trace evidence
vim.opt.viminfo = '0,"/0,/0,:0,f0'
vim.opt.swapfile = false
vim.opt.backup = false
vim.opt.writebackup = false
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Encrypt_a_file_without_leaving_traces)
***
# Title: Secure File Encryption in Vim
# Category: file_operations
# Tags: encryption, security, file-management
---
Encrypt files using built-in Vim encryption methods, with options for different encryption strengths

```vim
" Encrypt file with Blowfish2 (strongest method)
:X  " Prompt for encryption key
:setlocal cm=blowfish2  " Set strongest encryption method
```
```lua
-- Lua equivalent for encryption
vim.cmd('X')  -- Prompt for encryption key
vim.opt.cryptmethod = 'blowfish2'  -- Set strongest encryption method
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Encryption)
***
# Title: Quick Directory Exploration in Vim
# Category: file_operations
# Tags: navigation, file-explorer, directory
---
Easily explore directories and navigate file system directly from Vim using built-in commands

```vim
:Explore
:e /home/user
:e ..
:e <dir_path>
```
```lua
-- Open file explorer
vim.cmd('Explore')

-- Open specific directory
vim.cmd('e /home/user')

-- Go to parent directory
vim.cmd('e ..')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/File_explorer)
***
# Title: Batch Convert Line Endings in Multiple Files
# Category: file_operations
# Tags: file-format, batch-processing, line-endings
---
Convert line endings for multiple files matching a pattern in one command

```vim
:args *.c *.h
:argdo set ff=unix|update
```
```lua
-- Convert specified file types to unix line endings
vim.cmd('args *.c *.h')
vim.cmd('argdo set ff=unix|update')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/File_format)
***
# Title: Flexible File Find Function
# Category: file_operations
# Tags: file-search, custom-function, wildcard
---
Custom function to find files using partial name matches across directory tree

```vim
function! Find(name)
  let l:_name = substitute(a:name, "\s", "*", "g")
  let l:list=system("find . -iname '*".l:_name."*' -not -name \"*.class\" -and -not -name \"*.swp\" | perl -ne 'print "$.\t$_"'")
  " ... rest of original function ...
endfunction
command! -nargs=1 Find :call Find("<args>")
```
```lua
function _G.flexible_file_find(name)
  local escaped_name = name:gsub('%s', '*')
  local cmd = string.format("find . -iname '*%s*' -not -name '*.class' -and -not -name '*.swp'", escaped_name)
  local result = vim.fn.system(cmd)
  -- Implement selection logic similar to Vimscript version
end

vim.api.nvim_create_user_command('Find', function(opts)
  _G.flexible_file_find(opts.args)
end, { nargs = 1 })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/File_search_similar_to_cmd-t_in_TextMate)
***
# Title: Quickly Find and Edit Files Across Large Codebases
# Category: file_operations
# Tags: file-navigation, tags, search
---
Generate a tag file for quickly finding and opening files in large directory structures using ctags or custom find scripts

```vim
set tags=c:\files.tags

" Use :tj Foo<tab> to autocomplete and open files
```
```lua
-- Equivalent in Neovim
vim.opt.tags = 'c:\\files.tags'

-- Use built-in ctags functionality
-- Generate tags: ctags -R --file-tags=yes c:/
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Find_and_edit_any_file_in_a_directory_using_tag-like_pattern_matching)
***
# Title: Recursive File Finding in Vim
# Category: file_operations
# Tags: file-search, navigation, project-management
---
Create a custom function to find files recursively in subdirectories with interactive selection

```vim
function! Find(name)
  let l:list=system("find . -name '".a:name."' | perl -ne 'print \"$.\	$_"'")
  let l:num=strlen(substitute(l:list, "[^\n]", "", "g"))
  if l:num < 1
    echo "'".a:name."' not found"
    return
  endif
  if l:num != 1
    echo l:list
    let l:input=input("Which ? (CR=nothing)\n")
    if strlen(l:input)==0
      return
    endif
    let l:line=matchstr("\n".l:list, "\n".l:input."\	[^\n]*")
  else
    let l:line=l:list
  endif
  let l:line=substitute(l:line, "^[^\	]*\	./", "", "")
  execute ":e ".l:line
endfunction
command! -nargs=1 Find :call Find("<args>")
```
```lua
function _G.find_file(name)
  local list = vim.fn.system('find . -name "' .. name .. '" | perl -ne "print qq{$.\t$_}"')
  local num = #vim.split(list, '\n')

  if num < 1 then
    print("'" .. name .. "' not found")
    return
  end

  if num > 1 then
    print(list)
    local input = vim.fn.input('Which ? (CR=nothing)\n')

    if input == '' then
      return
    end

    local selected_line = vim.split(list, '\n')[tonumber(input)]
    vim.cmd('edit ' .. selected_line:gsub('^%d+\	%./', ''))
  else
    vim.cmd('edit ' .. list:gsub('^%d+\	%./', ''))
  end
end

vim.api.nvim_create_user_command('Find', function(opts)
  _G.find_file(opts.args)
end, { nargs = 1 })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Find_files_in_subdirectories)
***
# Title: Flexible Project File Search with Ignore Patterns
# Category: file_operations
# Tags: file-search, project-management, ignore-patterns
---
Create a file search function that allows configurable ignore patterns for files and directories

```vim
function! Find(...)
    if a:0==2
        let path=a:1
        let query=a:2
    else
        let path="./"
        let query=a:1
    endif

    if !exists("g:FindIgnore")
        let ignore = ""
    else
        let ignore = " | egrep -v '".join(g:FindIgnore, "|")."'"
    endif

    let l:list=system("find ".path." -type f -iname '*".query."*'".ignore)
    let l:num=strlen(substitute(l:list, "[^\n]", "", "g"))

    if l:num < 1
        echo "'".query."' not found"
        return
    endif

    if l:num == 1
        exe "open " . substitute(l:list, "\n", "", "g")
    else
        let tmpfile = tempname()
        exe "redir! > " . tmpfile
        silent echon l:list
        redir END
        let old_efm = &efm
        set efm=%f

        if exists(":cgetfile")
            execute "silent! cgetfile " . tmpfile
        else
            execute "silent! cfile " . tmpfile
        endif

        let &efm = old_efm
        botright copen
        call delete(tmpfile)
    endif
endfunction

command! -nargs=* Find :call Find(<f-args>)
```
```lua
function _G.flexible_file_search(...)
    local path = './'
    local query

    if select('#', ...) == 2 then
        path = select(1, ...)
        query = select(2, ...)
    else
        query = select(1, ...)
    end

    local ignore_patterns = vim.g.FindIgnore or {}
    local ignore_cmd = ignore_patterns and #ignore_patterns > 0
        and ' | egrep -v "' .. table.concat(ignore_patterns, '|') .. '"' or ''

    local find_cmd = string.format('find %s -type f -iname "*%s*"%s', path, query, ignore_cmd)
    local result = vim.fn.system(find_cmd)
    local num_results = select(2, result:gsub('\n', '\n'))

    if num_results == 0 then
        print("'" .. query .. "' not found")
        return
    end

    if num_results == 1 then
        vim.cmd('edit ' .. result:gsub('\n', ''))
    else
        local tmpfile = vim.fn.tempname()
        vim.fn.writefile(vim.split(result, '\n'), tmpfile)
        vim.cmd('cfile ' .. tmpfile)
        vim.cmd('botright copen')
        vim.fn.delete(tmpfile)
    end
end

vim.api.nvim_create_user_command('Find', function(opts)
    _G.flexible_file_search(unpack(opts.fargs))
end, { nargs = '*' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Find_files_in_subdirectories)
***
# Title: Open Current Visual Studio File in Vim
# Category: file_operations
# Tags: external-tools, workflow, integration
---
Configure Visual Studio to open the current file in Vim with cursor position preserved

```vim
Tools > External Tools > Add:
Title: &Vim
Command: C:\Vim\vim73\gvim.exe
Arguments: --servername gVimStudio --remote-silent +"execute 'normal! $(CurLine)G$(CurCol)|'" "$(ItemFileName)$(ItemExt)"
```
```lua
-- Lua equivalent would be to create a similar external tool configuration
-- This is mostly an IDE integration tip, so direct Lua translation isn't straightforward
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Have_Vim_open_a_file_in_Visual_Studio)
***
# Title: Hex Dump Binary Files
# Category: file_operations
# Tags: hex-editing, binary-files, file-inspection
---
Convert binary files to hex dump for inspection and editing using xxd utility

```vim
:r !xxd sample.bin
:%!xxd
:%!xxd -r
```
```lua
-- Read binary file as hex dump
vim.cmd('r !xxd sample.bin')

-- Convert buffer to hex mode
vim.cmd(':%!xxd')

-- Convert hex back to binary
vim.cmd(':%!xxd -r')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Hex_dump)
***
# Title: Generate C Source from Binary Files
# Category: file_operations
# Tags: binary-conversion, c-source, file-utility
---
Convert binary files into C-compatible byte arrays using xxd

```vim
:r !xxd -i sample.bin
```
```lua
-- Generate C source array from binary file
vim.cmd('r !xxd -i sample.bin')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Hex_dump)
***
# Title: Binary File Editing Mode
# Category: file_operations
# Tags: binary-files, hex-editing, file-modes
---
Open files in binary mode with hex display and line wrapping

```vim
vim -b myfile.bin
:setlocal display=uhex
:setlocal wrap
```
```lua
-- Open in binary mode
vim.o.binary = true
vim.o.display = 'uhex'
vim.o.wrap = true
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Hex_dump)
***
# Title: Hex Dump Binary Files with xxd
# Category: file_operations
# Tags: hex-editing, binary-files, utilities
---
Convert binary files to hex dump and back using Vim's built-in xxd utility, enabling hex editing of binary files

```vim
" Convert file to hex dump
:%!xxd

" Convert hex dump back to binary
:%!xxd -r
```
```lua
-- Convert file to hex dump
vim.cmd(':%!xxd')

-- Convert hex dump back to binary
vim.cmd(':%!xxd -r')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Hexdump2C)
***
# Title: Open Binary Files in Vim
# Category: file_operations
# Tags: binary-editing, file-modes
---
Open binary files with specific settings to prevent formatting issues

```vim
" Open in binary mode
vim -b myfile.bin

" Display non-printable characters in hex
:setlocal display=uhex
:setlocal wrap
```
```lua
-- Open in binary mode
-- Use command line argument or set buffer options
vim.opt.binary = true
vim.opt.display = 'uhex'
vim.opt.wrap = true
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Hexdump2C)
***
# Title: Create Vim Patches Easily
# Category: file_operations
# Tags: diff, patch-creation, development
---
Technique for creating patches from source file modifications using diff command

```vim
set patchmode=.orig
:!diff -u src/file.orig src/file > /tmp/file.diff
```
```lua
-- Set patch mode for automatic backups
vim.opt.patchmode = '.orig'

-- Example patch creation command (run in shell)
-- diff -u src/file.orig src/file > /tmp/file.diff
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/How_to_make_and_submit_a_patch)
***
# Title: Incremental Backups with Timestamped Files
# Category: file_operations
# Tags: backup, file-management, automation
---
Automatically create timestamped backup files in a central directory, preserving original file structure

```vim
" Incremental backup configuration
augroup backup
    autocmd!
    autocmd BufWritePre,FileWritePre * let &l:backupext = '~' . strftime('%F') . '~'
augroup END
```
```lua
vim.api.nvim_create_augroup('incremental_backup', { clear = true })
vim.api.nvim_create_autocmd({'BufWritePre', 'FileWritePre'}, {
  group = 'incremental_backup',
  callback = function()
    vim.o.backupext = '~' .. os.date('%Y-%m-%d') .. '~'
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Incremental_backup_in_central_backup_directory)
***
# Title: Central Backup Directory with Directory Creation
# Category: file_operations
# Tags: backup, file-management, directory-handling
---
Automatically create backup directories for files across different drives/paths

```vim
let g:root_backup_dir = 'f:\\vim_backups'
" Create backup directory if it doesn't exist
if !filewritable(g:root_backup_dir)
  silent execute '!mkdir ' . g:root_backup_dir
endif
set backupdir=g:root_backup_dir
```
```lua
local root_backup_dir = vim.fn.expand('f:/vim_backups')

-- Ensure backup directory exists
if vim.fn.filewritable(root_backup_dir) == 0 then
  vim.fn.mkdir(root_backup_dir, 'p')
end

vim.o.backupdir = root_backup_dir
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Incremental_backup_in_central_backup_directory)
***
# Title: Insert File or Command Output into Buffer
# Category: file_operations
# Tags: file-manipulation, command-execution
---
Quickly insert file contents or command output at cursor or specific buffer positions

```vim
:r foo.txt    " Insert file below cursor
:0r foo.txt   " Insert file before first line
:r !ls        " Insert directory listing
:$r !pwd      " Insert current working directory
```
```lua
-- Insert file
vim.cmd('r foo.txt')

-- Insert command output
vim.cmd('r !ls')
vim.cmd('$r !pwd')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Insert_a_file)
***
# Title: Insert Template Files into Buffer
# Category: file_operations
# Tags: file-templates, text-insertion, macros
---
Dynamically insert template files into the current buffer using a custom command that reads files specified by a special marker

```vim
command! -range=% Refile <line1>,<line2>g/^#refile=/exe ":r " . strpart(getline("."), 8) | normal! kdd
```
```lua
vim.api.nvim_create_user_command('Refile', function(opts)
  local current_line = vim.fn.line('.')
  local last_line = opts.line2

  for line = current_line, last_line do
    local line_text = vim.fn.getline(line)
    if line_text:match('^#refile=') then
      local file_path = line_text:sub(9)
      vim.cmd('read ' .. file_path)
      vim.cmd('normal! kdd')
    end
  end
end, { range = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Insert_template_files_into_buffer)
***
# Title: Quick File and Editing Commands
# Category: file_operations
# Tags: file-editing, command-line, save-quit
---
Efficient commands for editing, saving, and quitting files

```lua
-- File operations
vim.keymap.set('n', '<leader>q', ':q!<CR>', { desc = 'Quit without saving' })
vim.keymap.set('n', 'ZZ', ':wq<CR>', { desc = 'Save and quit' })
vim.keymap.set('n', ':e!', ':e!<CR>', { desc = 'Reload file' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Introduction_to_display_editing_using_vi)
***
# Title: Open File at Specific Line
# Category: file_operations
# Tags: cli-integration, file-opening
---
Launch Neovim and jump directly to a specific line number when opening a file

```vim
vim file.txt +123
```
```lua
-- Same CLI behavior works in Neovim
-- Launch with: nvim file.txt +123
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Jump_to_a_line_number)
***
# Title: Incremental File Backups with Unique Timestamps
# Category: file_operations
# Tags: backup, file-management, timestamps
---
Automatically create unique, timestamped backup files when editing documents, ensuring you never lose previous versions

```vim
set backupdir=c:\temp\vim_backup
let myvar = strftime("(%y%m%d)[%Hh%M]")
let myvar = "set backupext=_". myvar
execute myvar
```
```lua
vim.opt.backupdir = '/tmp/vim_backup'

-- Create backup with timestamp
local backup_ext = string.format("_(%s)[%s]",
  os.date("%y%m%d"),
  os.date("%Hh%M"))

vim.opt.backupext = backup_ext
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Keep_incremental_backups_of_edited_files)
***
# Title: Preserve Modified Flag After Writing to File
# Category: file_operations
# Tags: file-writing, buffer-management, autocmds
---
Prevents the modified flag from being reset when writing to a different file, maintaining the original buffer's modification state

```vim
function! BufWrite()
  let fileName = expand('<afile>')
  if fileName =~ 'ftp://\|rcp://\|scp://\|dav://\|rync://\|sftp://'
    return
  endif
  let _modified = &modified
  exec 'w'.(v:cmdbang?'!':'') v:cmdarg fileName
  if expand('%') !=# fileName
    let &modified = _modified
  endif
endfunction
```
```lua
local function buf_write()
  local file_name = vim.fn.expand('<afile>')
  local protocol_pattern = 'ftp://\|rcp://\|scp://\|dav://\|rync://\|sftp://'

  if file_name:match(protocol_pattern) then
    return
  end

  local was_modified = vim.o.modified
  vim.cmd('write' .. (vim.v.cmdbang and '!' or '') .. ' ' .. vim.v.cmdarg .. ' ' .. file_name)

  if vim.fn.expand('%') ~= file_name then
    vim.o.modified = was_modified
  end
end

-- Set up autocmd
vim.api.nvim_create_autocmd('BufWriteCmd', {
  callback = buf_write
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Keep_the_modified_flag_after_writing_to_a_file)
***
# Title: Open Files in New Tabs Across Desktops
# Category: file_operations
# Tags: desktop-integration, file-management, tab-handling
---
Automatically open files in new tabs in the current Vim instance, even across different desktops

```vim
gvim -p --remote-tab-silent %F
```
```lua
-- Lua equivalent for shell script
local function open_file_in_desktop_tab(file)
  local desktop = vim.fn.system('xprop -root -notype _NET_CURRENT_DESKTOP | perl -pe "s/.*?= (\d+)/$1/"'):gsub('\n', '')
  vim.cmd(string.format('edit ++tab +set\ servername=%s %s', desktop, file))
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Launch_files_in_new_tabs_under_Linux)
***
# Title: Open Files in New Tabs Across Desktop
# Category: file_operations
# Tags: file-handling, tabs, desktop-integration
---
Automatically open files in new tabs instead of new Vim instances, works with file managers and across desktops

```vim
vim -p --remote-tab-silent filename
```
```lua
-- Equivalent in Neovim can be achieved via shell script or vim.cmd
-- Example shell script approach:
-- vim.cmd('silent tabedit ' .. filename)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Launch_files_in_new_tabs_under_Unix)
***
# Title: Open Files in New Tabs Automatically
# Category: file_operations
# Tags: tabs, file-management, windows
---
Automatically open new files in tabs using an autocmd, which is useful for maintaining a clean workspace when opening multiple files

```vim
autocmd BufReadPost * tab ball

" Conditional version for diff mode
if (&diff==0)
    :autocmd BufReadPost * tab ball
endif
```
```lua
vim.api.nvim_create_autocmd('BufReadPost', {
  callback = function()
    if vim.o.diff == false then
      vim.cmd('tab ball')
    end
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Launch_files_in_new_tabs_under_Windows)
***
# Title: Open Files in New Tabs via Remote Command
# Category: file_operations
# Tags: windows, cli, file-management
---
Use remote tab silent command to open files in tabs from command line or file associations

```vim
"C:\Program Files\Vim\vim72\gvim.exe" --remote-tab-silent "%1"
```
```lua
-- Equivalent in Neovim terminal or external script
vim.fn.system({'nvim', '--remote-tab-silent', vim.fn.expand('%')})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Launch_files_in_new_tabs_under_Windows)
***
# Title: Capture Change Locations
# Category: file_operations
# Tags: change-tracking, file-export, logging
---
Redirect change list to a file for tracking editing history across sessions

```vim
" Export change list to file
:set nomore
:redir > changes.txt
:changes
:redir END
:set more
:e changes.txt
```
```lua
-- Export change list to file (Lua equivalent)
vim.o.more = false
vim.api.nvim_command('redir! > changes.txt')
vim.api.nvim_command('changes')
vim.api.nvim_command('redir END')
vim.o.more = true
vim.cmd('edit changes.txt')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/List_changes_to_the_current_file)
***
# Title: Bulk Open Files from Filename List
# Category: file_operations
# Tags: file-management, macro, bulk-editing
---
Efficiently open multiple files from a text file containing filenames using Vim's built-in macro and quickfix list functionality

```vim
" Method 1: Using macro
q0gf:rew<CR><DOWN-ARROW>q
@0

" Method 2: Using quickfix list
:setlocal efm=%f
:execute 'cfile '.expand('%')
```
```lua
-- Method 1: Using vim.cmd for macro
vim.cmd('q0gf:rew<CR><DOWN-ARROW>q')
vim.cmd('@0')

-- Method 2: Using quickfix list
vim.opt.errorformat = '%f'
vim.cmd('cfile ' .. vim.fn.expand('%'))

-- Additional Lua-friendly approach
local function open_files_from_list(filename)
  local files = {}
  for line in io.lines(filename) do
    table.insert(files, line)
  end
  for _, file in ipairs(files) do
    vim.cmd('edit ' .. file)
  end
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Load_files_from_list_of_filenames_in_a_text_file)
***
# Title: Track File Open Dialog to Current File's Directory
# Category: file_operations
# Tags: file-navigation, configuration
---
Automatically set the file open dialog to start in the current buffer's directory, making file navigation more convenient

```vim
set browsedir=buffer
```
```lua
vim.opt.browsedir = 'buffer'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Make_File-Open_track_directory_of_current_file)
***
# Title: Create Tar Archive of Open Buffers
# Category: file_operations
# Tags: buffer-management, file-archiving
---
Quickly create a tar archive of all files currently open in Vim buffers, preserving file paths

```vim
:silent bufdo !tar -rvf archive.tar %:p
```
```lua
vim.api.nvim_command('silent bufdo !tar -rvf archive.tar ' .. vim.fn.expand('%:p'))
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Make_tar_of_all_files_in_vim_buffer)
***
# Title: Zip Open Buffers Quickly
# Category: file_operations
# Tags: buffer-management, file-archiving
---
Create a zip archive of all files currently open in Vim buffers

```vim
:silent bufdo !zip proj.zip %
```
```lua
vim.api.nvim_command('silent bufdo !zip proj.zip ' .. vim.fn.expand('%'))
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Make_tar_of_all_files_in_vim_buffer)
***
# Title: Automatically Create Directories When Editing Files
# Category: file_operations
# Tags: directory-creation, autocommand, workflow-enhancement
---
Automatically create parent directories when opening a new file that doesn't exist, saving manual directory creation steps

```vim
au BufNewFile * :exe ': !mkdir -p ' . escape(fnamemodify(bufname('%'),':p:h'),'#% \')
```
```lua
vim.api.nvim_create_autocmd('BufNewFile', {
  callback = function()
    local dir = vim.fn.fnamemodify(vim.api.nvim_buf_get_name(0), ':p:h')
    vim.fn.mkdir(dir, 'p')
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mkdir_on_edit_if_needed)
***
# Title: Move Files Directly in Vim File Explorer
# Category: file_operations
# Tags: file-management, navigation, file-explorer
---
Use Vim's built-in file explorer to rename/move files without leaving the editor

```vim
:Explore
:Sex
:Sex!
Press 'R' to rename file
```
```lua
-- Open file explorer
vim.cmd.Explore()

-- Split window and open explorer
vim.cmd.Sex()

-- Vertically split explorer
vim.cmd.Sex({'bang': true})

-- Note: Use 'R' key to rename/move files in explorer
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Move_files_with_a_Vim_command)
***
# Title: Open Files in Tabs with Path Search
# Category: file_operations
# Tags: tabs, file-search, path
---
Configure Vim to search paths when opening files in new tabs, including subdirectories

```vim
" Configure path for file searching
set path=.,,**

" Use :tabfind to open files by searching path
:tabfind myfile.txt
```
```lua
-- Configure path for file searching
vim.opt.path = '.,,**'

-- Note: :tabfind is still a command, can be executed via vim.cmd
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Move_the_current_tabpage_forward_or_backward)
***
# Title: Convert OEM to ANSI Character Encoding
# Category: file_operations
# Tags: encoding, character-conversion, file-handling
---
Easily convert text files from OEM (DOS) to ANSI charset in Windows, ensuring proper character rendering

```vim
:set encoding=cp437
:set fileencoding=latin1
:wq
```
```lua
-- Convert OEM to ANSI encoding
vim.opt.encoding = 'cp437'
vim.opt.fileencoding = 'latin1'
vim.cmd.wq()
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/OEM_to_ANSI_conversion)
***
# Title: Quick Note Taking with Vim Alias
# Category: file_operations
# Tags: alias, note-taking, command-line
---
Create a shell alias to open a notes file, go to the last line, add a blank line, and start insert mode quickly

```vim
alias note="gvim -c $ +foldopen +put_ +startinsert ~/path-to-file/notes.md"
```
```lua
-- Lua equivalent for Neovim
-- In your shell configuration or init.lua
vim.api.nvim_create_user_command('Note', function()
  vim.cmd('edit ~/path-to-file/notes.md')
  vim.cmd('normal! G')
  vim.cmd('normal! o')
  vim.cmd('startinsert')
end, {})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_File,_Go_To_Last_Line,_Add_Blank_Line,_Change_To_Insert_Mode)
***
# Title: Convert PDF to Text in Vim
# Category: file_operations
# Tags: pdf, external-tools, text-conversion
---
Create a custom command to read PDF contents into Vim buffer using pdftotext utility

```vim
:command! -complete=file -nargs=1 Rpdf :r !pdftotext -nopgbrk <q-args> -
:command! -complete=file -nargs=1 Rpdf :r !pdftotext -nopgbrk <q-args> - |fmt -csw78
```
```lua
vim.api.nvim_create_user_command('Rpdf', function(opts)
  vim.cmd('read !pdftotext -nopgbrk ' .. opts.args .. ' -')
end, { nargs = 1, complete = 'file' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_PDF_files)
***
# Title: Open Windows Explorer from Current Buffer
# Category: file_operations
# Tags: file-navigation, windows, explorer
---
Quickly open Windows Explorer at the directory of the current buffer, optionally selecting the current file

```vim
" Open Explorer in current buffer's directory
nmap <F11> :!start explorer /e,,%:p:h<CR>
imap <F11> <Esc><F11>

" Open Explorer and select current file
nmap <F11> :!start explorer /select,%:p
```
```lua
-- Open Explorer in current buffer's directory
vim.keymap.set('n', '<F11>', function()
  vim.fn.system('start explorer /e,,' .. vim.fn.expand('%:p:h'))
end, { desc = 'Open Explorer in current directory' })

-- Open Explorer and select current file
vim.keymap.set('n', '<F11>', function()
  vim.fn.system('start explorer /select,' .. vim.fn.expand('%:p'))
end, { desc = 'Open Explorer and select current file' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_Windows_Explorer_showing_directory_of_current_buffer)
***
# Title: Open Finder for macOS Users
# Category: file_operations
# Tags: file-navigation, macos, finder
---
Quickly open Finder at the directory of the current buffer

```vim
nmap <Leader>f :!open %:p:h<CR>
```
```lua
vim.keymap.set('n', '<leader>f', function()
  vim.fn.system('open ' .. vim.fn.expand('%:p:h'))
end, { desc = 'Open Finder in current directory' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_Windows_Explorer_showing_directory_of_current_buffer)
***
# Title: Open Files in Tabs from Command Line
# Category: file_operations
# Tags: cli, tabs, file-opening
---
Use -p flag to open multiple files, each in its own tab when launching Vim

```vim
# Command line usage: gvim -p *.py
```
```lua
-- Use the same command-line flag when launching Neovim
-- nvim -p *.py
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_every_buffer_in_its_own_tabpage)
***
# Title: Open Files in Existing Vim Instance
# Category: file_operations
# Tags: remote-editing, multi-instance, cli-integration
---
Quickly open files in an already running Vim instance without launching multiple windows

```vim
gvim --remote first_file
gvim --remote +split first_file
```
```lua
-- Requires Vim with client-server enabled
-- Use shell command: nvim --remote first_file
-- Or create a function in init.lua
function open_in_existing_nvim(file)
  vim.fn.remote_send('<ESC>:e ' .. file .. '<CR>')
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_file_in_already_running_vim_from_elsewhere)
***
# Title: Handle Filenames with Spaces in Path
# Category: file_operations
# Tags: file-navigation, path-handling
---
Configure Vim to handle file paths with spaces by modifying isfname option

```vim
" Allow spaces in filenames
set isfname+=32
```
```lua
-- Allow spaces in filenames
vim.opt.isfname:append(32)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_filenames_containing_spaces_with_gf)
***
# Title: Open Multiple Files in Tabs Automatically
# Category: file_operations
# Tags: file-handling, tabs, windows
---
Automatically open files in new tabs when launched from Windows, using remote tab functionality

```vim
"C:\Program Files\Vim\vim72\gvim.exe" --remote-tab-silent "%1"
```
```lua
-- Neovim equivalent (typically configured via file associations)
-- Use :edit or :tabedit to open files in new tabs
vim.keymap.set('n', '<leader>nt', ':tabedit ', { desc = 'Open new tab' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_files_in_multiple_tabs_using_the_Windows_Context_Menu)
***
# Title: Open Multiple Files in Same Vim Instance on macOS
# Category: file_operations
# Tags: macos, applescript, file-management
---
Use AppleScript to open multiple files in the same Vim window on macOS, avoiding multiple Vim instances

```vim
on run argv
   tell application "Vim"
      repeat with n from 1 to (count of argv)
         set theUnixPath to item n of argv
         set theMacPath to (POSIX file theUnixPath) as string
         open file theMacPath
      end repeat
      activate
   end tell
end run
```
```lua
-- Lua equivalent would typically use Neovim's built-in commands
-- For macOS file opening, you might use vim.cmd or external script
vim.cmd('args ' .. table.concat(files, ' '))
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_files_in_same_window_under_Mac_OS_X)
***
# Title: Windows File Associations with Vim/Neovim
# Category: file_operations
# Tags: windows, file-associations, configuration
---
Configure Windows file associations to open specific file types in Vim/Neovim, with support for remote editing and custom actions

```vim
" Vim command to associate .php files with Vim
assoc .php=PHPFile
ftype PHPFile="C:\Program Files\Vim\vim82\gvim.exe" --remote-silent "%1"
```
```lua
-- Lua equivalent (conceptual, as this is a Windows registry operation)
-- Can use vim.fn.system() to run system commands if needed
-- Example of registering file type programmatically
vim.cmd('assoc .php=PHPFile')
vim.cmd('ftype PHPFile="C:\\Program Files\\Vim\\vim82\\gvim.exe" --remote-silent "%1"')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_files_with_existing_Gvim_window_in_Windows)
***
# Title: Open Current File's Directory in File Explorer
# Category: file_operations
# Tags: file-navigation, explorer, windows
---
Quickly open the directory of the current file in Windows file explorer from Vim/Neovim

```vim
map <C-e> :silent !explorer %:p:h:gs?/?\\\?<CR>
```
```lua
vim.keymap.set('n', '<C-e>', function()
  vim.fn.system('explorer ' .. vim.fn.expand('%:p:h'):gsub('/', '\\'))
end, { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_the_directory_for_the_current_file_in_Windows)
***
# Title: Cross-Platform File Directory Opener
# Category: file_operations
# Tags: cross-platform, file-navigation, multi-os
---
Flexible function to open current file's directory across different platforms and GUI environments

```vim
func! OpenCWD()
  if has("gui_running")
    if has("win32")
      !start explorer.exe %:p:h
    elseif has("mac") && has("unix")
      execute '!open ' . substitute(expand("%:p:h"), " ", "\\ ", "g")
    endif
  endif
endfunc
```
```lua
function _G.open_current_directory()
  local current_dir = vim.fn.expand('%:p:h')
  if vim.fn.has('win32') == 1 then
    vim.fn.system('start explorer.exe ' .. current_dir)
  elseif vim.fn.has('mac') == 1 then
    vim.fn.system('open ' .. current_dir:gsub(' ', '\\ '))
  end
end

vim.api.nvim_create_user_command('OpenCWD', _G.open_current_directory, {})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_the_directory_for_the_current_file_in_Windows)
***
# Title: Open File's Directory in Vim
# Category: file_operations
# Tags: file-navigation, directory-browsing
---
Quickly open the directory of the current file using Netrw built-in commands

```vim
" Netrw directory exploration commands
:Explore   " Open current file's directory
:Sexplore  " Split horizontally
:Vexplore  " Split vertically
```
```lua
-- Using Neovim's built-in commands
-- These are the same as Vim, but can be wrapped in Lua if needed
vim.cmd('Explore')    -- Open current file's directory
vim.cmd('Sexplore')   -- Split horizontally
vim.cmd('Vexplore')   -- Split vertically
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_the_folder_containing_the_currently_open_file)
***
# Title: Open Multiple Files from List File
# Category: file_operations
# Tags: file-management, command-line, bulk-editing
---
Efficiently open multiple files specified in a list file using Vim command-line arguments

```vim
gvim "+gl/^/exec 'badd '.getline('.')" +bdel +nohls +"cd %:h" LISTFILE
```
```lua
vim.cmd('args ' .. vim.fn.expand('mylist'))
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Opening_several_files_in_vim_via_ListFile)
***
# Title: Open Files with Wildcard Patterns
# Category: file_operations
# Tags: file-management, wildcard, globbing
---
Use wildcard patterns to open multiple files matching a specific pattern

```vim
gvim *\2*\xx.txt
```
```lua
vim.cmd('args *\2*\xx.txt')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Opening_several_files_in_vim_via_ListFile)
***
# Title: Open File with Clipboard Paste
# Category: file_operations
# Tags: clipboard, file-open, paste
---
Open a new file and immediately paste clipboard contents

```vim
gvim.exe -c 'normal ggdG"*p' file.txt
```
```lua
-- Equivalent approach in Neovim
-- Can be implemented via command-line or lua function
vim.cmd('enew')
vim.cmd('normal "*p')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Paste_from_the_clipboard_into_a_new_vim)
***
# Title: Quick HTML File Preview in Browser
# Category: file_operations
# Tags: html, preview, browser-integration
---
Easily preview HTML files in a browser directly from Vim/Neovim with cross-platform support

```vim
" Open current HTML file in default browser
nnoremap <F5> :update<Bar>silent !xdg-open %:p &<CR>

" Open URL under cursor in browser
nnoremap <F8> :silent !xdg-open <cfile> &<CR>
```
```lua
-- Open current file in default browser
vim.keymap.set('n', '<F5>', function()
  vim.cmd.update()
  vim.fn.system({'xdg-open', vim.fn.expand('%:p')} )
end, { desc = 'Preview current file in browser' })

-- Open URL under cursor in browser
vim.keymap.set('n', '<F8>', function()
  vim.fn.system({'xdg-open', vim.fn.expand('<cfile>')})
end, { desc = 'Open URL under cursor' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Preview_HTML_files_quickly)
***
# Title: Project File Search with Wildmenu
# Category: file_operations
# Tags: file-search, navigation, ui-enhancement
---
Enable wildmenu to display multiple file matches when using :find, allowing easy file selection

```vim
set wildmenu
set path=$PWD/**
```
```lua
vim.opt.wildmenu = true
vim.opt.path = vim.fn.getcwd() .. '/**'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Project_browsing_using_find)
***
# Title: Protect Reference Files from Accidental Changes
# Category: file_operations
# Tags: file-protection, read-only, safety
---
Prevent accidental modifications to reference or comparison files by setting them as non-modifiable and changing the color scheme for visual distinction

```vim
:set nomodifiable
:colorscheme peachpuff
```
```lua
vim.opt.modifiable = false
vim.cmd.colorscheme('peachpuff')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Protecting_a_file_from_accidental_changes)
***
# Title: Add Modeline to Permanently Protect File
# Category: file_operations
# Tags: file-protection, modeline, configuration
---
Use a modeline to make a file non-modifiable across editing sessions

```vim
// vim:noma
```
```lua
-- Add the following at the end of the file
-- vim:noma
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Protecting_a_file_from_accidental_changes)
***
# Title: Quick File Backup Mapping
# Category: file_operations
# Tags: backup, key-mapping, file-handling
---
Easily create a backup of the current file with a single keypress, temporarily enabling backup option

```vim
" Quick backup mapping
nnoremap <Leader>b :let x=&backup<Bar>set backup<Bar>write<Bar>let &backup=x<Bar>unlet x<Cr>
```
```lua
-- Lua equivalent for quick file backup
vim.keymap.set('n', '<Leader>b', function()
  local backup_orig = vim.o.backup
  vim.o.backup = true
  vim.cmd.write()
  vim.o.backup = backup_orig
end, { desc = 'Quick file backup' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Quick_mapping_for_backing_up_the_file)
***
# Title: Quick Backup of Current File with Timestamp
# Category: file_operations
# Tags: backup, file-management, timestamp
---
Quickly create a timestamped backup of the current file before making modifications, preserving the original file's view and extension

```vim
map ;s :up | saveas! %:p:r-<C-R>=strftime("%y%m%d-%H:%M")<CR>-bak.<C-R>=expand("%:e")<CR> | 3sleep | e #<CR>
```
```lua
vim.keymap.set('n', ';s', function()
  -- Update current file
  vim.cmd('update')

  -- Create timestamped backup with original extension
  local original_file = vim.fn.expand('%:p')
  local timestamp = os.date('%y%m%d-%H:%M')
  local backup_file = string.format('%s-%s-bak.%s',
    vim.fn.fnamemodify(original_file, ':r'),
    timestamp,
    vim.fn.expand('%:e'))

  -- Save backup and return to original file
  vim.cmd('saveas! ' .. backup_file)
  vim.cmd('sleep 3')
  vim.cmd('edit #')
end, { desc = 'Create timestamped backup' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Quick_save_to_a_temporary_file_before_more_edits)
***
# Title: Recover Overwritten File Using Swap File
# Category: file_operations
# Tags: file-recovery, swap-file, backup
---
Recover a file that was accidentally overwritten by using Vim's built-in recover command when a swap file exists

```vim
:recover
```
```lua
-- In Neovim, use the same command
vim.cmd('recover')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Recover_overwritten_file)
***
# Title: Recover Files After Crash or Power Failure
# Category: file_operations
# Tags: file-recovery, crash-recovery, backup
---
Easily recover unsaved files after system crashes using Vim's built-in recovery mode

```vim
vim -r <filename>  # Recover specific file
vim -r ""  # Recover unnamed file
vim -r  # List recoverable files
```
```lua
-- In terminal/command mode
-- Use same commands as Vimscript
-- Recommended to use :help recovery in Neovim for more details
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Recovering_files)
***
# Title: Easy File Encoding Switching
# Category: file_operations
# Tags: encoding, file-handling, utility
---
Create a function to quickly cycle through or select different file encodings when a file is loaded incorrectly

```vim
let g:enc_index = 0
function! ChangeFileencoding()
  let encodings = ['cp1251', 'koi8-u', 'cp866']
  execute 'e ++enc='.encodings[g:enc_index].' %:p'
  if g:enc_index >=2
	  let g:enc_index = 0
  else
	  let g:enc_index = g:enc_index + 1
  endif
endf
nmap <F8> :call ChangeFileencoding()<CR>
```
```lua
local M = {}
M.enc_index = 0

function M.change_file_encoding()
  local encodings = {'cp1251', 'koi8-u', 'cp866'}
  vim.cmd('e ++enc=' .. encodings[M.enc_index + 1] .. ' %:p')

  M.enc_index = (M.enc_index >= 2) and 0 or M.enc_index + 1
end

vim.keymap.set('n', '<F8>', M.change_file_encoding, { desc = 'Cycle file encodings' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Reload_the_same_file_in_different_encoding)
***
# Title: Reload File with Different Encoding
# Category: file_operations
# Tags: encoding, file-handling, charset
---
Quickly reload a file using a specific character encoding when Vim fails to detect the correct one

```vim
" Reload file with specific encoding
:e ++enc=utf-8

" Quick mapping to switch to UTF-8
nnoremap <F12> :e ++enc=utf-8<CR>
```
```lua
-- Reload file with specific encoding
vim.cmd('e ++enc=utf-8')

-- Quick mapping to switch to UTF-8
vim.keymap.set('n', '<F12>', ':e ++enc=utf-8<CR>', { desc = 'Reload file as UTF-8' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Reloading_a_file_using_a_different_encoding)
***
# Title: Batch Convert Line Endings for Multiple Files
# Category: file_operations
# Tags: batch-processing, file-format, line-endings
---
Convert line endings for multiple files in a single directory using argument list commands

```vim
:args *.c *.h
:argdo set ff=unix|update
```
```lua
-- Convert .c and .h files to Unix line endings
vim.cmd('args *.c *.h')
vim.cmd('argdo set ff=unix|update')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Removing_%5EM%27s_From_A_File)
***
# Title: Edit Files on FTP Server with Custom Port
# Category: file_operations
# Tags: remote-editing, ftp, file-access
---
Open files on an FTP server using a non-standard port by escaping the # character

```vim
:e ftp://ftp.server\#2121/path/to/file/filename
```
```lua
-- Use netrw to open FTP files with custom port
vim.cmd('e ftp://ftp.server\#2121/path/to/file/filename')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip480)
***
# Title: Decompile and View Java Class Files in Vim
# Category: file_operations
# Tags: java, decompiler, external-tools
---
Automatically decompile Java .class files when opening them in Vim using the JAD decompiler

```vim
augroup class
  au!
  au bufreadpost,filereadpost *.class %!jad.exe -noctor -ff -i -p %
  au bufreadpost,filereadpost *.class set readonly
  au bufreadpost,filereadpost *.class set ft=java
  au bufreadpost,filereadpost *.class normal gg=G
  au bufreadpost,filereadpost *.class set nomodified
augroup END
```
```lua
vim.api.nvim_create_augroup('JavaClassDecompile', { clear = true })

vim.api.nvim_create_autocmd({'BufReadPost', 'FileReadPost'}, {
  group = 'JavaClassDecompile',
  pattern = '*.class',
  callback = function()
    vim.cmd('%!jad -noctor -ff -i -p %')
    vim.opt_local.readonly = true
    vim.opt_local.filetype = 'java'
    vim.cmd('normal! gg=G')
    vim.opt_local.modified = false
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip54)
***
# Title: Edit Remote Files Seamlessly with Netrw
# Category: file_operations
# Tags: remote-editing, network, scp, file-transfer
---
Edit remote files locally using Vim's built-in network file transfer capabilities, supporting SCP, RCP, and FTP protocols without manual copying

```vim
" Open remote file via SCP
:e scp://user@hostname//path/to/file
```
```lua
-- Open remote file via SCP in Neovim
vim.cmd('edit scp://user@hostname//path/to/file')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip542)
***
# Title: Automatic Remote File Synchronization
# Category: file_operations
# Tags: remote-editing, file-sync, network
---
Automatically transfer and save remote files when editing, eliminating manual upload steps

```vim
" Write remote file back
:Nwrite scp://user@hostname//path/to/file
```
```lua
-- Write remote file back in Neovim
vim.cmd('Nwrite scp://user@hostname//path/to/file')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip542)
***
# Title: Optimize Large File Loading Performance
# Category: file_operations
# Tags: performance, file-handling, optimization
---
Automatically adjust Vim settings for large files to improve loading speed and reduce memory usage

```vim
" file is large from 10mb
let g:LargeFile = 1024 * 1024 * 10
augroup LargeFile
  au!
  autocmd BufReadPre * let f=getfsize(expand("<afile>")) | if f > g:LargeFile || f == -2 | call LargeFile() | endif
augroup END

function! LargeFile()
 set eventignore+=FileType
 setlocal bufhidden=unload
 setlocal buftype=nowrite
 setlocal undolevels=-1
 autocmd VimEnter * echo "The file is larger than " . (g:LargeFile / 1024 / 1024) . " MB, so some options are changed"
endfunction
```
```lua
vim.g.LargeFile = 1024 * 1024 * 10

vim.api.nvim_create_augroup('LargeFile', { clear = true })

vim.api.nvim_create_autocmd('BufReadPre', {
  group = 'LargeFile',
  callback = function()
    local file_size = vim.fn.getfsize(vim.fn.expand('<afile>'))
    if file_size > vim.g.LargeFile or file_size == -2 then
      vim.opt.eventignore:append('FileType')
      vim.bo.bufhidden = 'unload'
      vim.bo.buftype = 'nowrite'
      vim.bo.undolevels = -1

      vim.notify(string.format('The file is larger than %d MB, so some options are changed', vim.g.LargeFile / 1024 / 1024))
    end
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip611)
***
# Title: Restore Last Edited File and Cursor Position
# Category: file_operations
# Tags: session-management, cursor-restoration, startup
---
Automatically open the last edited file and restore cursor position when launching Vim/Neovim without arguments

```vim
" Go to last file if invoked without arguments
autocmd VimEnter * nested if
  \ argc() == 0 &&
  \ bufname("%") == "" &&
  \ bufname(2) != "" |
  \   exe "normal! `0" |
  \ endif

" Restore cursor position
autocmd BufReadPost *
  \ if line("'\"") > 1 && line("'\"") <= line("$") |
  \   exe "normal! g`\"" |
  \ endif
```
```lua
-- Restore last edited file and cursor position
vim.api.nvim_create_autocmd('VimEnter', {
  nested = true,
  callback = function()
    if vim.fn.argc() == 0 and vim.fn.bufname('%') == '' and vim.fn.bufname(2) ~= '' then
      vim.cmd('normal! `0')
    end
  end
})

-- Restore cursor position
vim.api.nvim_create_autocmd('BufReadPost', {
  callback = function()
    local last_pos = vim.fn.line('\'"')
    if last_pos > 1 and last_pos <= vim.fn.line('$') then
      vim.cmd('normal! g`"')
    end
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip613)
***
# Title: Save and Restore Session Automatically
# Category: file_operations
# Tags: session-management, persistence
---
Automatically save and restore Vim/Neovim sessions when launching without arguments

```vim
" Save session on exit
autocmd VimLeave * nested if (!isdirectory($HOME . "/.vim")) |
    \ call mkdir($HOME . "/.vim") |
    \ endif |
    \ execute "mksession! " . $HOME . "/.vim/Session.vim"

" Restore session on startup
autocmd VimEnter * nested if argc() == 0 && filereadable($HOME . "/.vim/Session.vim") |
    \ execute "source " . $HOME . "/.vim/Session.vim"
```
```lua
-- Save session on exit
vim.api.nvim_create_autocmd('VimLeave', {
  nested = true,
  callback = function()
    local vim_dir = vim.fn.expand('$HOME') .. '/.vim'
    if vim.fn.isdirectory(vim_dir) == 0 then
      vim.fn.mkdir(vim_dir, 'p')
    end
    vim.cmd('mksession! ' .. vim_dir .. '/Session.vim')
  end
})

-- Restore session on startup
vim.api.nvim_create_autocmd('VimEnter', {
  nested = true,
  callback = function()
    local session_file = vim.fn.expand('$HOME') .. '/.vim/Session.vim'
    if vim.fn.argc() == 0 and vim.fn.filereadable(session_file) == 1 then
      vim.cmd('source ' .. session_file)
    end
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip613)
***
# Title: Create and Submit Vim Patches Easily
# Category: file_operations
# Tags: version-control, contributing, diff
---
Learn how to generate patches for Vim source files using diff and prepare them for submission to the vim-dev mailing list

```vim
:set patchmode=.orig
```
```lua
vim.o.patchmode = '.orig'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip618)
***
# Title: Compile LaTeX with Rubber and Make in Vim
# Category: file_operations
# Tags: latex, compilation, quickfix
---
Easily compile LaTeX documents using Rubber and Make, with automatic error handling and quickfix integration

```vim
if filereadable('Makefile')
  setlocal makeprg=make
else
  exec "setlocal makeprg=make\ -f\ ~/academic/tools/latex.mk\ " . substitute(bufname("%"),"tex$","pdf", "")
endif

setlocal errorformat=%f:%l:\ %m,%f:%l-%\d%\+:\ %m
```
```lua
vim.api.nvim_create_autocmd('BufEnter', {
  pattern = '*.tex',
  callback = function()
    if vim.fn.filereadable('Makefile') == 1 then
      vim.opt_local.makeprg = 'make'
    else
      vim.opt_local.makeprg = string.format('make -f ~/academic/tools/latex.mk %s',
        vim.fn.expand('%:r') .. '.pdf')
    end
    vim.opt_local.errorformat = '%f:%l: %m,%f:%l-%d: %m'
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip627)
***
# Title: Transparently Edit Encrypted GPG Files in Vim
# Category: file_operations
# Tags: encryption, security, file-handling
---
Automatically decrypt and encrypt GPG files when opening and saving, simplifying secure file editing

```vim
if has("autocmd")
  augroup GPGASCII
    au!
    au BufReadPost *.asc :%!gpg -q -d
    au BufReadPost *.asc |redraw
    au BufWritePre *.asc :%!gpg -q -e -a
    au BufWritePost *.asc u
    au VimLeave *.asc :!clear
  augroup END
endif
```
```lua
vim.api.nvim_create_augroup('GPGEncryption', { clear = true })

vim.api.nvim_create_autocmd({'BufReadPost'}, {
  group = 'GPGEncryption',
  pattern = '*.asc',
  callback = function()
    vim.cmd('!gpg -q -d')
    vim.cmd('redraw')
  end
})

vim.api.nvim_create_autocmd({'BufWritePre'}, {
  group = 'GPGEncryption',
  pattern = '*.asc',
  callback = function()
    vim.cmd('!gpg -q -e -a')
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip651)
***
# Title: Quick Vim Directory Navigation
# Category: file_operations
# Tags: navigation, windows, file-explorer
---
Create a Vim shortcut that opens directly to root directory for quick file access without using Windows Explorer

```vim
"C:\Program Files\gvim\vim62\gvim.exe" "c:/"
```
```lua
-- Lua equivalent for launching Neovim in root directory
vim.fn.system('nvim c:/')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip676)
***
# Title: Open Files via URLs in Vim
# Category: file_operations
# Tags: file-handling, autocmd, url-parsing
---
Allows opening files from URLs, specifically file:/// URLs on Windows by using an autocmd to handle file URL parsing

```vim
au BufReadCmd file:///* exe "bd!|edit ".substitute(expand("<afile>"),"file:/*","","")
```
```lua
vim.api.nvim_create_autocmd('BufReadCmd', {
  pattern = 'file:///*',
  callback = function()
    local file_path = vim.fn.substitute(vim.fn.expand('<afile>'), 'file:/*', '', '')
    vim.cmd('bd!')
    vim.cmd('edit ' .. file_path)
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip691)
***
# Title: Preserve Cursor Position on Save
# Category: file_operations
# Tags: autocmd, file, save, whitespace
---
Suppose that you want to trim trailing white space on file save. That's easy (and already explained elsewhere): just create auto-command that will do the job before writing the file. But after the file is saved, you will often notice that the cursor jumps wildly accros the screen. The situation is even worse if you have some plugins that also interfere with file save operation (like `prettier`, popular javascript formatter). You need some way to remember the cursor position before the save and restore it afterwards. The simplest approach would be to put mark at cursor position before the save and move to the mark after the save. However, such mark often gets lost in the process. Here is the right approach:

```lua
-- Remove trailing whitespace on save
-- Save and restore cursor position across write operations
local cursor_position = {}

vim.api.nvim_create_autocmd("BufWritePre", {
  callback = function()
    -- Save the current window view (cursor position, topline, etc.)
    cursor_position[vim.api.nvim_get_current_buf()] = vim.fn.winsaveview()
    -- trim whitespace
    vim.cmd([[%s/\s\+$//e]])
  end,
})

vim.api.nvim_create_autocmd("BufWritePost", {
  callback = function()
    -- Restore the saved window view
    local bufnr = vim.api.nvim_get_current_buf()
    if cursor_position[bufnr] then
      vim.fn.winrestview(cursor_position[bufnr])
      cursor_position[bufnr] = nil -- Clean up
    end
  end,
})
```

Just put the code into your `init.lua` file.

**Source:** [Claude](https://claude.ai/new)
***
