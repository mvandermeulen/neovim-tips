# Title: Session management
# Category: Session
# Tags: session, save, restore
---
Use `:mksession!` to save session and `:source Session.vim` to restore it.

```vim
:mksession!        " save session
:source Session.vim " restore session
```

**Source:** Community contributed
***
# Title: Ex commands - session options
# Category: Session
# Tags: ex, session, options, save, restore
---
Use `:set sessionoptions` to control what gets saved, `:mksession {file}` for custom filename, `:source` to restore.

```vim
:set sessionoptions=buffers,curdir,folds,help,tabpages,winsize
:mksession mysession.vim  " save to custom file (fails if the file already exists)
:mksession mysession.vim! " save with custom name (overwrites possibly existing file)
:source mysession.vim     " restore specific session
```

**Source:** Community contributed
***
# Title: Ex commands - viminfo and shada
# Category: Session
# Tags: ex, viminfo, shada, history, persistent
---
Use `:wviminfo` to write viminfo, `:rviminfo` to read, `:wshada` and `:rshada` for Neovim's shada file.

```vim
:wshada          " write shada file
:rshada          " read shada file
:wshada backup.shada  " save to specific file
:rshada backup.shada  " read from specific file
```

**Source:** Community contributed
***
# Title: Ex commands - arglist and project files
# Category: Session
# Tags: ex, arglist, args, project, files
---
Use `:args` to set argument list, `:argadd` to add files, `:next`/`:prev` to navigate, `:argdo` for commands on all.

```vim
:args *.py       " set arglist to all Python files
:argadd test.py  " add file to arglist
:next            " go to next file in arglist
:prev            " go to previous file
:argdo %s/old/new/g  " run command on all files
```

**Source:** Community contributed
***
# Title: Ex commands - working with multiple files
# Category: Session
# Tags: ex, multiple, files, bufdo, windo, tabdo
---
Use `:bufdo` for all buffers, `:windo` for all windows, `:tabdo` for all tabs to execute commands across multiple contexts.

```vim
:bufdo %s/old/new/ge  " substitute in all buffers
:windo set number     " set line numbers in all windows
:tabdo close          " close all tabs
:argdo write          " save all files in arglist
```

**Source:** Community contributed
***
# Title: Save and Restore Vim Session
# Category: session-management
# Tags: session, file-history, persistence
---
Automatically save and restore Vim session when opening and closing without arguments

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
local session_file = vim.fn.expand('$HOME') .. '/.vim/Session.vim'

vim.api.nvim_create_autocmd('VimLeave', {
  nested = true,
  callback = function()
    if not vim.fn.isdirectory(vim.fn.expand('$HOME') .. '/.vim') then
      vim.fn.mkdir(vim.fn.expand('$HOME') .. '/.vim', 'p')
    end
    vim.cmd('mksession! ' .. session_file)
  end
})

vim.api.nvim_create_autocmd('VimEnter', {
  nested = true,
  callback = function()
    if vim.fn.argc() == 0 and vim.fn.filereadable(session_file) == 1 then
      vim.cmd('source ' .. session_file)
    end
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_the_last_edited_file)
***
