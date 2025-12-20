# Title: Quick File Bookmarking with Context
# Category: marks
# Tags: bookmarking, file-tracking, context-capture
---
Create a custom function to bookmark current file location with timestamp, current directory, and line details

```vim
function! MoshBookmark()
  redir >> ~/.vims
  echo
  echo strftime("%Y-%b-%d %a %H:%M")
  echo "cd ". $PWD
  echo "vim ". expand("%:p").':'.line('.')
  echo ' word='.expand("<cword>")
  echo ' cline='.getline('.')
  redir END
endfunction
:command! MoshBookmark :call MoshBookmark()
```

```lua
function _G.mosh_bookmark()
  local file = io.open(vim.fn.expand('~/.vims'), 'a')
  if file then
    file:write('\n' .. os.date('%Y-%b-%d %a %H:%M') .. '\n')
    file:write('cd ' .. vim.fn.getcwd() .. '\n')
    file:write('vim ' .. vim.fn.expand('%:p') .. ':' .. vim.fn.line('.') .. '\n')
    file:write(' word=' .. vim.fn.expand('<cword>') .. '\n')
    file:write(' cline=' .. vim.fn.getline('.') .. '\n')
    file:close()
  end
end

vim.api.nvim_create_user_command('MoshBookmark', _G.mosh_bookmark, {})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Bookmark_files)
***
# Title: Cut or Copy Lines Without Line Counting
# Category: marks
# Tags: navigation, copying, editing
---
Easily copy or cut lines using marks without manually counting line numbers

```vim
mk      " Mark current line with 'k'
y'k     " Yank from mark to current position
d'k     " Delete from mark to current position
```

```lua
-- Mark current line with 'k'
vim.fn.setmark('k')
-- Yank from mark to current position
vim.cmd('normal y`k')
-- Delete from mark to current position
vim.cmd('normal d`k')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Cut_or_copy_lines_without_counting_the_lines)
***
# Title: Use Marks for Quick Navigation
# Category: marks
# Tags: navigation, bookmarks, file-jumping
---
Set and use marks to quickly jump between locations in files and across different files

```vim
" Set a local mark in current file
ma

" Set a global mark across files
mA

" Jump to marks
'a  " Jump to line of mark a
`a  " Jump to exact position of mark a
`A  " Jump to global mark A in its file
```

```lua
-- Set local mark
vim.cmd('ma')

-- Set global mark
vim.cmd('mA')

-- Jump to marks
vim.cmd("'a")  -- Jump to line of mark a
vim.cmd("`a")  -- Jump to exact position of mark a
vim.cmd("`A")  -- Jump to global mark A in its file
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mark)
***
# Title: Navigate Between Marks Efficiently
# Category: marks
# Tags: navigation, marks, movement
---
Quickly jump between marks using built-in navigation commands

```vim
" Jump to next/previous marked lines
]'  " Next line with a mark
['  " Previous line with a mark

" Jump to next/previous marks
]`  " Next mark
[`  " Previous mark
```

```lua
-- These are Ex commands, so use vim.cmd
-- Jump to next/previous marked lines
vim.cmd(']\'')
vim.cmd('[\'')  

-- Jump to next/previous marks
vim.cmd(']`')
vim.cmd('[`')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mark)
***
# Title: Useful Special Marks for Quick Navigation
# Category: marks
# Tags: navigation, special-marks, editing
---
Use special marks to quickly jump to recent editing locations

```vim
`` .  " Last change location
`` "  " Last exit location
`` 0  " Last file edited when exiting Vim
`` ''  " Previous jump location
`` `   " Previous exact location
```

```lua
-- Jump to special marks
vim.cmd('`.')
vim.cmd('`"')
vim.cmd('`0')
vim.cmd('``')  -- Previous jump location
vim.cmd('`^')  -- Last insertion point
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mark)
***
# Title: Master Vim Marks for Quick Navigation
# Category: marks
# Tags: navigation, bookmarks, jumping
---
Use special commands to jump between marks efficiently, with support for count-based jumps.

```vim
" Jump to next/previous lowercase mark
]'
['
```

```lua
-- Note: These are Vim commands that can be run in Lua
vim.cmd(']\'')
vim.cmd('[\'')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Marks)
***
# Title: Use Special Marks for Quick Reference
# Category: marks
# Tags: navigation, editing-history
---
Utilize Vim's built-in special marks to quickly jump to recent edit or change locations

```vim
" Jump to last edit location
`.

" Jump to last exit location
`"
```

```lua
-- These can be run as Vim commands in Lua
vim.cmd('`.')
vim.cmd('`"')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Marks)
***
# Title: Remember Last Position in Help Files
# Category: marks
# Tags: help-navigation, persistent-marks, workflow
---
Automatically mark the last position in Vim help files and easily return to it across sessions

```vim
au BufLeave * if &ft == "help" | mark H | endif
```

```lua
vim.api.nvim_create_autocmd('BufLeave', {
  callback = function()
    if vim.bo.filetype == 'help' then
      vim.cmd('mark H')
    end
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Remember_where_you_had_ended_reading_help)
***
