# Title: View jump list
# Category: Navigation
# Tags: jump, list, view
---
Use `:jumps` to show the jump list with all stored positions.

```vim
:jumps  " show jump list
```

**Source:** Community contributed
***
# Title: LSP go to references
# Category: Navigation
# Tags: lsp, references, goto
---
Use `gr` to go to references of symbol under cursor (requires LSP server).

```vim
gr  " go to references
```

**Source:** Community contributed
***
# Title: Go to declaration
# Category: Navigation
# Tags: lsp, declaration, goto
---
Use `gD` to go to declaration of symbol under cursor.

```vim
gD  " go to declaration
```

**Source:** Community contributed
***
# Title: Jump to block boundaries
# Category: Navigation
# Tags: block, boundaries, jump
---
Use `[{` to jump to start of current block and `]}` to jump to end of current block.

```vim
[{  " jump to block start
]}  " jump to block end
```

**Source:** Community contributed
***
# Title: Jump between functions
# Category: Navigation
# Tags: function, jump, treesitter
---
Use `]m` to jump to next function start and `[m` to jump to previous function start.

```vim
]m  " next function start
[m  " previous function start
```

**Source:** Community contributed
***
# Title: Navigate to alternate file
# Category: Navigation
# Tags: alternate, file, header, source
---
Use `:A` to switch to alternate file (e.g., .h to .c), or `Ctrl+^` to switch to previous buffer.

```vim
:A      " alternate file
Ctrl+^  " previous buffer
```

**Source:** Community contributed
***
# Title: Buffer switching shortcuts
# Category: Navigation
# Tags: buffer, switching, shortcuts, quick
---
Use `:ls` to list buffers, `:b#` for previous buffer, or create mappings for quick buffer navigation.

```vim
:ls         " list all buffers
:b#         " switch to previous buffer
Ctrl+^      " alternate between current and previous buffer
:b partial  " switch to buffer matching partial name
```

**Source:** Community contributed
***
# Title: Fast buffer access
# Category: Navigation
# Tags: buffer, fast, access, number
---
Create mappings to quickly access first nine buffers using leader key combinations.

```vim
nnoremap <leader>1 :1b<CR>
nnoremap <leader>2 :2b<CR>
nnoremap <leader>3 :3b<CR>
nnoremap <leader>4 :4b<CR>
nnoremap <leader>5 :5b<CR>
" Continue for buffers 6-9
```

**Source:** Community contributed
***
# Title: Square bracket navigation - unmatched brackets
# Category: Navigation
# Tags: bracket, unmatched, navigation
---
Use `[(` and `])` to jump to unmatched parentheses, `[{` and `]}` to jump to unmatched braces.

```vim
[(  " jump to previous unmatched (
])  " jump to next unmatched )
[{  " jump to previous unmatched {
]}  " jump to next unmatched }
```

**Source:** Community contributed
***
# Title: Square bracket navigation - sections
# Category: Navigation
# Tags: section, navigation, document
---
Use `[[` and `]]` to jump between sections, `[]` and `][` to jump between SECTIONS (different formatting).

```vim
[[  " jump to previous section
]]  " jump to next section
[]  " jump to previous SECTION
][  " jump to next SECTION
```

**Source:** Community contributed
***
# Title: Square bracket navigation - C comments
# Category: Navigation
# Tags: comment, C, navigation
---
Use `[/` and `]/` to jump to start/end of C-style comments. Use `[*` as alternative to `[/`.

```vim
[/  " jump to previous start of C comment
]/  " jump to next end of C comment
[*  " same as [/ (alternative)
]*  " same as ]/ (alternative)
```

**Source:** Community contributed
***
# Title: Square bracket navigation - preprocessing
# Category: Navigation
# Tags: preprocessing, define, include
---
Use `[#` and `]#` to jump between #if/#else/#endif blocks.

```vim
[#  " jump to previous #if, #else, or #ifdef
]#  " jump to next #endif or #else
```

**Source:** Community contributed
***
# Title: Square bracket navigation - definitions and includes
# Category: Navigation
# Tags: definition, include, search
---
Use `[Ctrl+d`/`]Ctrl+d` to jump to #define, `[Ctrl+i`/`]Ctrl+i` to jump to lines containing word under cursor.

```vim
[Ctrl+d  " jump to previous #define matching word
]Ctrl+d  " jump to next #define matching word
[Ctrl+i  " jump to previous line containing word
]Ctrl+i  " jump to next line containing word
```

**Source:** Community contributed
***
# Title: Square bracket navigation - list definitions
# Category: Navigation
# Tags: list, definition, search, include
---
Use `[D`/`]D` to list all #defines, `[I`/`]I` to list all lines containing word under cursor.

```vim
[D  " list all #defines matching word under cursor
]D  " list all #defines matching word under cursor  
[I  " list all lines containing word under cursor
]I  " list all lines containing word under cursor
```

**Source:** Community contributed
***
# Title: Square bracket navigation - show definitions
# Category: Navigation
# Tags: show, definition, preview
---
Use `[d`/`]d` to show first #define, `[i`/`]i` to show first line containing word under cursor.

```vim
[d  " show first #define matching word
]d  " show first #define matching word
[i  " show first line containing word
]i  " show first line containing word
```

**Source:** Community contributed
***
# Title: Square bracket navigation - changes and diffs
# Category: Navigation
# Tags: change, diff, navigation
---
Use `[c` and `]c` to jump between changes in diff mode.

```vim
[c  " jump to previous change
]c  " jump to next change
```

**Source:** Community contributed
***
# Title: Square bracket navigation - spelling
# Category: Navigation
# Tags: spelling, error, navigation
---
Use `[s` and `]s` to jump between misspelled words.

```vim
[s  " jump to previous misspelled word
]s  " jump to next misspelled word
```

**Source:** Community contributed
***
# Title: Square bracket navigation - folds
# Category: Navigation
# Tags: fold, navigation, code
---
Use `[z` and `]z` to jump to start/end of open fold.

```vim
[z  " jump to start of open fold
]z  " jump to end of open fold
```

**Source:** Community contributed
***
# Title: Square bracket navigation - member functions
# Category: Navigation
# Tags: function, member, class, navigation
---
Use `[m` and `]m` to jump between member function starts.

```vim
[m  " jump to previous start of member function
]m  " jump to next start of member function
```

**Source:** Community contributed
***
# Title: Toggle netrw file explorer
# Category: Navigation
# Tags: netrw, explorer, toggle, file, browser
---
Use `:Lexplore` to toggle the netrw file explorer in a vertical split on the left side.

```vim
:Lexplore    " toggle left explorer
:Vexplore    " open explorer in vertical split
:Sexplore    " open explorer in horizontal split
:Explore     " open explorer in current window
```

**Source:** Community contributed
***
# Title: Enhanced navigation with Flash.nvim
# Category: Navigation
# Tags: plugin, flash, leap, jump, motion, search
---
Use Flash.nvim plugin to enhance native Neovim motions like `f`, `t`, `w` with multi-line, labeled jumping.

```lua
-- Install with lazy.nvim:
{
  "folke/flash.nvim",
  event = "VeryLazy",
  opts = {
    modes = {
      char = {
        enabled = true,  -- Enable for f, F, t, T motions
        jump_labels = true
      }
    }
  },
  keys = {
    { "s", mode = { "n", "x", "o" }, function() require("flash").jump() end, desc = "Flash" },
    { "S", mode = { "n", "x", "o" }, function() require("flash").treesitter() end, desc = "Flash Treesitter" },
    { "r", mode = "o", function() require("flash").remote() end, desc = "Remote Flash" },
    { "R", mode = { "o", "x" }, function() require("flash").treesitter_search() end, desc = "Treesitter Search" },
  },
}

-- Usage:
-- Press 's' followed by characters to search
-- Press 'S' for treesitter-aware selection
-- Use enhanced f/t/w motions with labels
```

**Source:** Community contributed
***
# Title: Quick PHP Variable Navigation
# Category: navigation
# Tags: php, key-mapping, text-objects
---
Easily jump between PHP variables on the same line using custom key mappings

```vim
noremap L f$
noremap H F$
```
```lua
vim.keymap.set('n', 'L', 'f$', { desc = 'Jump to next PHP variable' })
vim.keymap.set('n', 'H', 'F$', { desc = 'Jump to previous PHP variable' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/$_instead_of_4)
***
# Title: Smart Middle of Line Movement
# Category: navigation
# Tags: cursor-movement, text-editing
---
Move cursor to the middle of the physical line, ignoring leading/trailing whitespace

```vim
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
local function gm()
  vim.cmd('normal! ^')
  local first_col = vim.fn.virtcol('.')
  vim.cmd('normal! g_')
  local last_col = vim.fn.virtcol('.')
  vim.cmd('normal! ' .. math.floor((first_col + last_col) / 2) .. '|')
end

vim.keymap.set('n', 'gm', gm, { silent = true })
vim.keymap.set('o', 'gm', gm, { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/A_better_gm_command)
***
# Title: Master Vim Movement Shortcuts
# Category: navigation
# Tags: movement, cursor-navigation, efficiency
---
Comprehensive collection of efficient cursor movement commands in Vim/Neovim, enabling faster text navigation

```lua
-- Movement shortcuts
-- Basic navigation
vim.keymap.set('n', 'w', 'w', { desc = 'Move to next word' })
vim.keymap.set('n', 'b', 'b', { desc = 'Move to previous word' })
vim.keymap.set('n', '0', '0', { desc = 'Move to start of line' })
vim.keymap.set('n', '$', '$', { desc = 'Move to end of line' })

-- Screen-based navigation
vim.keymap.set('n', 'H', 'H', { desc = 'Move to top of screen' })
vim.keymap.set('n', 'M', 'M', { desc = 'Move to middle of screen' })
vim.keymap.set('n', 'L', 'L', { desc = 'Move to bottom of screen' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/All_the_right_moves)
***
# Title: Efficient Tab Navigation Shortcuts
# Category: navigation
# Tags: key-mapping, tab-management, productivity
---
Create convenient keymappings for navigating and managing tabs using easy-to-remember shortcuts

```vim
" Navigate tabs
nnoremap <C-S-tab> :tabprevious<CR>
nnoremap <C-tab>   :tabnext<CR>
nnoremap <C-t>     :tabnew<CR>

" Use H and L to cycle tabs
nnoremap H gT
nnoremap L gt
```
```lua
-- Tab navigation shortcuts
vim.keymap.set('n', '<C-S-Tab>', ':tabprevious<CR>', { noremap = true, silent = true })
vim.keymap.set('n', '<C-Tab>', ':tabnext<CR>', { noremap = true, silent = true })
vim.keymap.set('n', '<C-t>', ':tabnew<CR>', { noremap = true, silent = true })

-- Cycle tabs with H and L
vim.keymap.set('n', 'H', 'gT', { noremap = true })
vim.keymap.set('n', 'L', 'gt', { noremap = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Alternative_tab_navigation)
***
# Title: Generate and Use Custom Tag Files
# Category: navigation
# Tags: file-navigation, tags, project-management
---
Generate a custom tags file for quick navigation between files, especially useful for large projects with many files of the same type

```vim
# Generate tags file for .jsp files
# Terminal command:
find -name '*.jsp' -printf '%f\t%P\t1\n' |sort > jsp.tags

# In Vim:
:set tags+=jsp.tags
:tag file.jsp  # Quick file navigation
```
```lua
-- Lua doesn't change the core functionality, but you can use vim.fn to run shell commands
-- Generate tags file
vim.fn.system('find -name "*.jsp" -printf "%f\t%P\t1\n" | sort > jsp.tags')

-- Add tags file
vim.opt.tags:append('jsp.tags')

-- Use :tag as before
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Arbitrary_tags_for_file_names)
***
# Title: Recursive File Finding with Path Option
# Category: navigation
# Tags: file-search, project-navigation, recursive-search
---
Easily search and open files across multiple directories using Vim's path option with recursive search

```vim
:set path+=./**
:find filename.txt  # Find file in current and subdirectories
:sfind filename.txt  # Open in split window
```
```lua
-- Set recursive path
vim.opt.path:append('./**')

-- Lua doesn't change :find syntax, but you can use vim.cmd
vim.cmd('find filename.txt')
vim.cmd('sfind filename.txt')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Arbitrary_tags_for_file_names)
***
# Title: Wrap Cursor Movement Between Lines
# Category: navigation
# Tags: cursor-movement, key-mapping, configuration
---
Allows left/right cursor keys and h/l to wrap to previous/next line when reaching line boundaries, improving navigation fluidity

```vim
set whichwrap+=<,>,h,l,[,]
```
```lua
vim.opt.whichwrap:append '<,>h,l,[,]'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Automatically_wrap_left_and_right)
***
# Title: Use Alt/Meta Keys in Terminal Vim
# Category: navigation
# Tags: terminal, key-mapping, productivity
---
Leverage Alt/Meta keys to quickly switch modes and perform actions without Escape

```vim
" No direct Vimscript implementation - depends on terminal configuration
```
```lua
-- Configure terminal to send Alt/Meta key events
-- Specific implementation depends on terminal settings
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Avoid_the_escape_key)
***
# Title: Navigate Lines with Same Indentation
# Category: navigation
# Tags: indentation, movement, code-navigation
---
Quickly jump between lines with the same or lower indentation level, useful in Python, XML, and other indentation-sensitive languages

```vim
" Jump between lines with same or lower indentation
nnoremap <silent> [l :call NextIndent(0, 0, 0, 1)<CR>
nnoremap <silent> ]l :call NextIndent(0, 1, 0, 1)<CR>
nnoremap <silent> [L :call NextIndent(0, 0, 1, 1)<CR>
nnoremap <silent> ]L :call NextIndent(0, 1, 1, 1)<CR>
```
```lua
-- Create a Lua function to replicate NextIndent behavior
local function next_indent(exclusive, fwd, lower_level, skip_blanks)
  local line = vim.fn.line('.')
  local column = vim.fn.col('.')
  local last_line = vim.fn.line('$')
  local indent = vim.fn.indent(line)
  local step = fwd and 1 or -1

  while line > 0 and line <= last_line do
    line = line + step
    local current_indent = vim.fn.indent(line)
    local line_not_blank = vim.fn.strlen(vim.fn.getline(line)) > 0

    if (not lower_level and current_indent == indent) or
       (lower_level and current_indent < indent) then
      if not skip_blanks or line_not_blank then
        if exclusive then
          line = line - step
        end
        vim.cmd(tostring(line))
        vim.cmd('normal! ' .. column .. '|')
        return
      end
    end
  end
end

-- Set up keymappings in Neovim
vim.keymap.set('n', '[l', function() next_indent(false, false, false, true) end, { silent = true })
vim.keymap.set('n', ']l', function() next_indent(false, true, false, true) end, { silent = true })
vim.keymap.set('n', '[L', function() next_indent(false, false, true, true) end, { silent = true })
vim.keymap.set('n', ']L', function() next_indent(false, true, true, true) end, { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Back_and_forth_between_indented_lines_again)
***
# Title: Quick Indentation Level Navigation
# Category: navigation
# Tags: indentation, code-navigation, movement
---
Simple Alt-key mappings to quickly move between lines with the same indentation

```vim
nnoremap <M-,> :call search('^'. matchstr(getline('.'), '(^\s*)').'\%<' . line('.') . 'l\S', 'be')<CR>
nnoremap <M-.> :call search('^'. matchstr(getline('.'), '(^\s*)').'\%>' . line('.') . 'l\S', 'e')<CR>
```
```lua
vim.keymap.set('n', '<M-,>', function()
  local current_line = vim.fn.getline('.')
  local indent = current_line:match('^%s*')
  vim.cmd('call search("^' .. indent .. '\\%<' .. vim.fn.line('.') .. 'l\\S", "be")')
end)

vim.keymap.set('n', '<M-.>', function()
  local current_line = vim.fn.getline('.')
  local indent = current_line:match('^%s*')
  vim.cmd('call search("^' .. indent .. '\\%>' .. vim.fn.line('.') .. 'l\\S", "e")')
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Back_and_forth_between_indented_lines_again)
***
# Title: Powerful Text Editing with Vim Motions
# Category: navigation
# Tags: text-objects, editing, motion-commands
---
Learn to combine movement commands with actions for efficient text manipulation

```vim
# Examples of powerful text editing motions
# Delete 2 words forward
d2w
# Change 3 words backward
c3b
# Yank everything to next parenthesis
y/)
```
```lua
-- While Lua doesn't directly implement these, you can use vim.api to create similar mappings
-- Example of creating a wrapper for text object manipulation
vim.keymap.set('n', '<leader>d2w', 'd2w', { desc = 'Delete 2 words forward' })
vim.keymap.set('n', '<leader>c3b', 'c3b', { desc = 'Change 3 words backward' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Beginners_guide)
***
# Title: Advanced Find and Till Commands
# Category: navigation
# Tags: search, motion, text-editing
---
Use 'find' and 'till' commands to quickly move and manipulate text within a line

```vim
# Find and till command examples
fx   # Find next 'x' in line
tC   # Move till just before next 'C'
ctx  # Change till next 'x'
```
```lua
-- Vim's built-in find commands work the same in Neovim
-- You can create custom keymaps to enhance these motions
vim.keymap.set('n', '<leader>fx', 'fx', { desc = 'Find next x in line' })
vim.keymap.set('n', '<leader>tc', 'tC', { desc = 'Move till just before next C' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Beginners_guide)
***
# Title: Advanced File and Buffer Navigation
# Category: navigation
# Tags: buffer-management, file-navigation, marks
---
Powerful navigation techniques using marks and movement history

```vim
'.       " jump to last modification line
`.       " jump to exact spot in last modification line
<C-O>    " retrace movements backward
<C-I>    " retrace movements forward
:ju(mps) " list of your movements
```
```lua
-- Lua equivalents for advanced navigation
-- These are primarily Vim native commands, so use vim.cmd
vim.keymap.set('n', "'.", "'.", { desc = 'Jump to last modification line' })
vim.keymap.set('n', '`.', '`.', { desc = 'Jump to exact modification spot' })
vim.keymap.set('n', '<C-o>', '<C-o>', { desc = 'Navigate backward in jump history' })
vim.keymap.set('n', '<C-i>', '<C-i>', { desc = 'Navigate forward in jump history' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Best_Vim_Tips)
***
# Title: Advanced Search and Movement
# Category: navigation
# Tags: search, movement, cursor
---
Enhanced word searching and cursor movement techniques

```vim
* # g* g#     " find word under cursor (forwards/backwards)
%             " match brackets {}[]()
'. `. " jump to last modification line
```
```lua
-- Lua alternatives for advanced search and movement
-- Most of these are vim commands that work in Neovim
-- vim.cmd('normal! *')   -- search forward for word under cursor
-- vim.cmd('normal! #')   -- search backward for word under cursor
-- vim.cmd('normal! %')   -- match corresponding bracket
-- vim.cmd('normal! `.'   -- jump to last modification
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Best_of_VIM_Tips_(VIM%27s_best_Features))
***
# Title: Efficient Tag Navigation in Vim/Neovim
# Category: navigation
# Tags: tags, code-navigation, jump-to-definition
---
Quickly navigate between code definitions using tags with multiple flexible methods

```vim
" Jump to tag definition
Ctrl-]

" List multiple tag matches
g]

" Preview tag without leaving current window
Ctrl-W }
```
```lua
-- Jump to tag definition
vim.keymap.set('n', '<C-]>', '<cmd>tag<CR>', { desc = 'Jump to tag definition' })

-- List multiple tag matches
vim.keymap.set('n', 'g]', '<cmd>tselect<CR>', { desc = 'List tag matches' })

-- Preview tag in preview window
vim.keymap.set('n', '<C-W>}', '<cmd>ptag<CR>', { desc = 'Preview tag' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Browsing_programs_with_tags)
***
# Title: Advanced Tag Search and Browsing
# Category: navigation
# Tags: tags, code-search, fuzzy-finding
---
Use pattern matching and flexible tag browsing techniques to explore code efficiently

```vim
" Search tags with pattern
:tag /<pattern>

" Browse tag list
:tfirst    " Go to first tag
:tnext     " Go to next tag
:tprevious " Go to previous tag
```
```lua
-- Search tags with pattern
-- Note: Requires setting up a tags file first
vim.keymap.set('n', '<leader>tp', function()
  vim.cmd('tag /' .. vim.fn.input('Tag pattern: '))
end, { desc = 'Search tags by pattern' })

-- Tag list navigation helpers
vim.keymap.set('n', '<leader>tf', '<cmd>tfirst<CR>', { desc = 'First tag' })
vim.keymap.set('n', '<leader>tn', '<cmd>tnext<CR>', { desc = 'Next tag' })
vim.keymap.set('n', '<leader>tp', '<cmd>tprevious<CR>', { desc = 'Previous tag' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Browsing_programs_with_tags)
***
# Title: Configure Matchit for ColdFusion Tag Jumping
# Category: navigation
# Tags: matchit, language-support, tag-navigation
---
Enable % key to jump between matching ColdFusion tags like <cfif> and </cfif>

```vim
" In ~/.vim/ftplugin/cf.vim
if exists("loaded_matchit")
    let b:match_words = '<cfif\>:\<cfelseif\>:\<cfelse\>:\</cfif>,'
                    \ . '<cfloop\>:\</cfloop>,'
                    \ . '<cfoutput\>:\</cfoutput>'
endif
```
```lua
-- In ~/.config/nvim/ftplugin/cf.lua
if vim.g.loaded_matchit then
  vim.b.match_words = table.concat({
    '<cfif\>:<cfelseif\>:<cfelse\>:</cfif>',
    '<cfloop\>:</cfloop>',
    '<cfoutput\>:</cfoutput>'
  }, ',')
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/ColdFusion_and_matchit)
***
# Title: Scroll Without Moving Cursor
# Category: navigation
# Tags: scroll, cursor-position, screen-movement
---
Scroll the screen up or down while keeping the cursor on the same screen line, providing a smooth reading experience

```vim
function! s:Saving_scroll(cmd)
  let save_scroll = &scroll
  execute 'normal! ' . a:cmd
  let &scroll = save_scroll
endfunction

nnoremap <C-J> :call <SID>Saving_scroll("1<C-V><C-D>")<CR>
vnoremap <C-J> <Esc>:call <SID>Saving_scroll("gv1<C-V><C-D>")<CR>
nnoremap <C-K> :call <SID>Saving_scroll("1<C-V><C-U>")<CR>
vnoremap <C-K> <Esc>:call <SID>Saving_scroll("gv1<C-V><C-U>")<CR>
```
```lua
local function saving_scroll(cmd)
  local save_scroll = vim.o.scroll
  vim.cmd('normal! ' .. cmd)
  vim.o.scroll = save_scroll
end

vim.keymap.set('n', '<C-J>', function() saving_scroll('1\<C-D>') end)
vim.keymap.set('v', '<C-J>', function() saving_scroll('gv1\<C-D>') end)
vim.keymap.set('n', '<C-K>', function() saving_scroll('1\<C-U>') end)
vim.keymap.set('v', '<C-K>', function() saving_scroll('gv1\<C-U>') end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Combining_move_and_scroll)
***
# Title: Efficient Cscope Navigation in Vim/Neovim
# Category: navigation
# Tags: code-navigation, c-development, project-management
---
Configure Vim/Neovim to use Cscope for advanced code navigation, allowing quick symbol, definition, and reference searches across large codebases

```vim
if has('cscope')
  set cscopetag cscopeverbose

  if has('quickfix')
    set cscopequickfix=s-,c-,d-,i-,t-,e-
  endif

  cnoreabbrev csa cs add
  cnoreabbrev csf cs find
  cnoreabbrev csk cs kill
  cnoreabbrev csr cs reset
  cnoreabbrev css cs show
  cnoreabbrev csh cs help
endif
```
```lua
if vim.fn.has('cscope') == 1 then
  vim.opt.cscopetag = true
  vim.opt.cscopeverbose = true

  if vim.fn.has('quickfix') == 1 then
    vim.opt.cscopequickfix = 's-,c-,d-,i-,t-,e-'
  end

  -- Create commands/abbreviations using Neovim command creation
  vim.cmd[[
    cnoreabbrev csa cs add
    cnoreabbrev csf cs find
    cnoreabbrev csk cs kill
    cnoreabbrev csr cs reset
    cnoreabbrev css cs show
    cnoreabbrev csh cs help
  ]]
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Cscope)
***
# Title: Easy Help Navigation on AZERTY Keyboards
# Category: navigation
# Tags: help, keyboard-mapping, key-navigation
---
Alternative key mapping for following help links on AZERTY keyboards, where Ctrl-] doesn't work

```vim
" Remap help navigation for AZERTY keyboards
nmap <F9> <C-]>
map! <F9> <C-]>
```
```lua
-- Remap help navigation for AZERTY keyboards
vim.keymap.set('n', '<F9>', '<C-]>', { desc = 'Follow help link' })
vim.keymap.set({'i', 'c'}, '<F9>', '<C-]>', { desc = 'Follow help link' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/De_hulp_bevaren_met_een_AZERTY_toetsenbord)
***
# Title: Move Word Under Cursor with Alt-Arrows
# Category: navigation
# Tags: text-movement, word-editing, key-mapping
---
Move the word under the cursor in different directions without explicitly selecting it first

```vim
nnoremap <A-Right> viwm`w``xwzvP`[1v<Space>
nnoremap <A-Left> viwm`bb``xbzvP`[1v<Space>
nnoremap <A-Down> viwjkxjzvP`[1v<Space>
nnoremap <A-Up> viwkjxkzvP`[1v<Space>
```
```lua
vim.keymap.set('n', '<A-Right>', 'viwm`w``xwzvP`[1v<Space>', { noremap = true })
vim.keymap.set('n', '<A-Left>', 'viwm`bb``xbzvP`[1v<Space>', { noremap = true })
vim.keymap.set('n', '<A-Down>', 'viwjkxjzvP`[1v<Space>', { noremap = true })
vim.keymap.set('n', '<A-Up>', 'viwkjxkzvP`[1v<Space>', { noremap = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Drag_words_with_Ctrl-left/right)
***
# Title: Advanced Movement and Modification Markers
# Category: navigation
# Tags: marks, navigation, cursor-movement
---
Jump to last modification and retrace movement history

```vim
'.     " jump to last modification line
`.     " jump to exact spot in last modification line
<C-O>  " retrace movements backward
<C-I>  " retrace movements forward
:ju(mps)  " list of your movements
```
```lua
-- Most of these are built-in Vim commands
-- For more advanced mark management in Neovim
vim.keymap.set('n', '<leader>m', function()
  vim.cmd('marks')  -- Show mark list
end, { desc = 'Show marks' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Easter_eggs)
***
# Title: Open Files Under Cursor in Different Windows
# Category: navigation
# Tags: file-navigation, window-management, productivity
---
Quickly open files referenced under the cursor in different window modes using built-in Vim commands

```vim
" Open file in same window
gf

" Open file in new horizontal split
<c-w>f

" Open file in new tab
<c-w>gf
```
```lua
-- Lua doesn't need explicit mapping, these are built-in Vim commands
-- Can be used directly in Neovim
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Edit_file_under_cursor_after_a_horizontal_split)
***
# Title: Use Environment Variables for Dynamic File Paths
# Category: navigation
# Tags: file-navigation, environment
---
Define environment variables to simplify file path references across different systems

```vim
let $mydir = 'C:/Documents and Settings/My Name/My Documents'
```
```lua
-- Set environment variable for file paths
vim.env.mydir = 'C:/Documents and Settings/My Name/My Documents'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Edit_file_under_cursor_after_a_horizontal_split)
***
# Title: Fast Jump to PHP Variables on a Line
# Category: navigation
# Tags: php, movement, key-mapping
---
Quickly jump between PHP variables on the same line using custom mappings

```vim
noremap L f$
noremap H F$
```
```lua
vim.keymap.set('n', 'L', 'f$', { desc = 'Jump to next PHP variable' })
vim.keymap.set('n', 'H', 'F$', { desc = 'Jump to previous PHP variable' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Fast_jump_to_next_PHP_variable_on_current_line)
***
# Title: Fast Window Scrolling with Alt Key Mappings
# Category: navigation
# Tags: key-mapping, scrolling, window-management
---
Quick mappings to scroll windows horizontally and vertically using Alt key combinations

```vim
" Horizontal and vertical window scrolling
nmap <A-l> 4zl
nmap <A-h> 4zh
nmap <A-k> <C-y>
nmap <A-j> <C-e>
```
```lua
-- Scroll window horizontally and vertically
vim.keymap.set('n', '<A-l>', '4zl', { desc = 'Scroll window right' })
vim.keymap.set('n', '<A-h>', '4zh', { desc = 'Scroll window left' })
vim.keymap.set('n', '<A-k>', '<C-y>', { desc = 'Scroll window up' })
vim.keymap.set('n', '<A-j>', '<C-e>', { desc = 'Scroll window down' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Fast_scroll_mappings)
***
# Title: Recursive File Search with Fuzzy Matching
# Category: navigation
# Tags: file-search, fuzzy-finder, productivity
---
Quickly search and open files recursively in the current directory tree using fuzzy matching

```vim
nmap <F5> :FuzzyFinderFile **/<CR>
map <Leader>t :FufFile **/<CR>
```
```lua
vim.keymap.set('n', '<F5>', function()
  require('fzf-lua').files({ cwd = vim.fn.getcwd() })
end, { desc = 'Recursive file search' })

vim.keymap.set('n', '<leader>t', function()
  require('fzf-lua').files({ cwd = vim.fn.getcwd() })
end, { desc = 'Recursive file search' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/File_search_similar_to_cmd-t_in_TextMate)
***
# Title: Enhanced Word Search with Smart Matching
# Category: navigation
# Tags: search, word-navigation, mapping
---
Custom mappings for word search that respect smartcase and whole word boundaries

```vim
nnoremap * /\<<C-R>=expand('<cword>')\>\><CR>
nnoremap # ?\<<C-R>=expand('<cword>')\>\><CR>
```
```lua
vim.keymap.set('n', '*', function()
  local word = vim.fn.expand('<cword>')
  vim.fn.search('\<' .. word .. '\>')
end)

vim.keymap.set('n', '#', function()
  local word = vim.fn.expand('<cword>')
  vim.fn.search('\<' .. word .. '\>', 'b')
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Find)
***
# Title: Create Custom Help-Style Tags in Source Code
# Category: navigation
# Tags: ctags, custom-tags, code-navigation
---
Use Ctags to create custom help-style tag navigation in non-help files by defining a new tag type

```vim
" Add to ~/.ctags
--regex-java=/\*([A-Za-z0-9_\-]*)\*/\1/h,htag/

" Add to ~/.vimrc for taglist support
let tlist_java_settings = 'java;p:package;c:class;i:interface;' .
                             \ 'f:field;m:method;h:htag'
```
```lua
-- Equivalent configuration would typically be done in ctags config
-- For Neovim, you can use telescope or LSP for advanced navigation

-- Example of setting up custom tag navigation in Lua
require('telescope').setup({
  extensions = {
    -- Configure custom tag navigation
  }
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Follow_Help_Tags_Using_Ctags)
***
# Title: Alternative Tag Navigation
# Category: navigation
# Tags: tags, window-management
---
Use built-in Vim command to open tag in a new window

```lua
-- Use CTRL-W ] to open tag in a new split window
-- This is a built-in Vim/Neovim feature
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Follow_tag_in_new_window)
***
# Title: Flexible File Navigation
# Category: navigation
# Tags: file-navigation, goto-file, path-searching
---
Enhance 'goto file' command with configurable file name and path detection

```vim
set path+=**
set isfname+=32
set suffixesadd+=.js,.py
```
```lua
vim.opt.path:append('**')
vim.opt.isfname:append(32)
vim.opt.suffixesadd:append({'.js', '.py'})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/From_Vim_Help/2008)
***
# Title: Fuzzy Search Multiple Vim Contexts
# Category: navigation
# Tags: fuzzy-search, fzf, productivity
---
Create powerful fuzzy search mappings for various Vim contexts like buffers, commands, mappings, and more using FZF

```vim
" Fuzzy search mappings
nnoremap <silent> <C-a>b :call FZFOpen(':Buffers')<CR>
nnoremap <silent> <C-a>c :call fzf#run({'source': GetCommands(), 'sink': function('HandleCommand'), 'options': '-m'})<CR>
nnoremap <silent> <C-a>m :call fzf#run({'source': GetMappings(), 'options': '-m -n 2'})<CR>
```
```lua
-- Lua equivalent requires fzf.vim plugin setup
local fzf = require('fzf-lua')

vim.keymap.set('n', '<C-a>b', function()
  fzf.buffers()
end, { desc = 'Fuzzy search buffers' })

vim.keymap.set('n', '<C-a>c', function()
  fzf.command_history()
end, { desc = 'Fuzzy search command history' })

vim.keymap.set('n', '<C-a>m', function()
  fzf.keymaps()
end, { desc = 'Fuzzy search key mappings' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Fuzzy_mappings_of_everything!)
***
# Title: Track and Search Recently Visited Directories
# Category: navigation
# Tags: directory-tracking, autocmd, productivity
---
Automatically track and cache visited directories for quick fuzzy navigation

```vim
" Track visited directories
autocmd DirChanged * call SaveLastDir()

function! SaveLastDir()
  if !exists('g:dirs')
    call LoadDir()
    let g:lastdir = ''
  endif

  let reg = getcwd()
  if reg == g:lastdir
    return
  endif
  call add(g:dirs, reg)
endfunction
```
```lua
-- Lua implementation of directory tracking
vim.api.nvim_create_autocmd('DirChanged', {
  callback = function()
    local current_dir = vim.fn.getcwd()
    if not vim.g.dirs then
      vim.g.dirs = {}
    end
    
    if current_dir ~= vim.g.last_dir then
      table.insert(vim.g.dirs, current_dir)
      vim.g.last_dir = current_dir
    end
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Fuzzy_mappings_of_everything!)
***
# Title: Quick Change to Current File's Directory
# Category: navigation
# Tags: file-navigation, directory-management
---
Quickly change Vim's current directory to the directory of the active file

```vim
com Fcd cd %:p:h
```
```lua
vim.api.nvim_create_user_command('Fcd', 'cd %:p:h', {})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Get_a_shell_command_for_changing_to_the_current_directory)
***
# Title: Quickly Get Current Function Name
# Category: navigation
# Tags: function-navigation, code-browsing, mapping
---
Easily retrieve the name of the current function you're in using a custom mapping that searches backwards to the function definition

```vim
map _F ma[[k"xy$`a:echo @x<CR>
```
```lua
vim.keymap.set('n', '_F', function()
  -- Move to previous '{' in first column
  vim.cmd('normal! ma[[k"xy$`a')
  -- Echo the function name
  print(vim.fn.getreg('x'))
end, { desc = 'Show current function name' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Getting_name_of_the_function)
***
# Title: Navigate to Function Start and Back
# Category: navigation
# Tags: function-navigation, marks
---
Use built-in Vim commands to navigate to function start and return to original position

```vim
Press [[ to go to function start
Press '' to return to previous position
```
```lua
-- Built-in Vim commands, no specific Lua implementation needed
-- [[  : Go to previous function start
-- ''  : Return to previous mark
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Getting_name_of_the_function)
***
# Title: Jump to Random Line in Buffer
# Category: navigation
# Tags: random, line-jumping, utility
---
Create a command to jump to a random line in the current buffer, useful for testing or exploring large files

```vim
function! RandomLine() range
  let first_line = a:firstline
  let last_line = a:lastline
  execute 'normal! '.(system('od -vAn -N3 -tu4 /dev/urandom') % (last_line - first_line + 1) + first_line).'G'
endfunction
command! -range=% RandomLine <line1>,<line2>call RandomLine()
```
```lua
function _G.random_line(first_line, last_line)
  local total_lines = last_line - first_line + 1
  local random_line = first_line + math.random(total_lines - 1)
  vim.api.nvim_win_set_cursor(0, {random_line, 0})
end

vim.api.nvim_create_user_command('RandomLine', function(opts)
  local first_line = opts.line1
  local last_line = opts.line2
  _G.random_line(first_line, last_line)
end, {range = true})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/GoTo_a_Random_Line)
***
# Title: Use g_ to Navigate End of Line in Langmap
# Category: navigation
# Tags: langmap, cursor-movement, keyboard-layout
---
When using a non-English keyboard layout that lacks the $ symbol, use g_ to move to the last non-blank character in the line

```vim
" No specific code needed, just use g_ motion
```
```lua
-- Use g_ motion to navigate to end of line
-- Works with any keyboard layout
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Go_to_end-of-line_when_using_langmap)
***
# Title: Multiple Ways to Navigate to a Specific Line
# Category: navigation
# Tags: line-navigation, cursor-movement
---
Multiple methods to quickly jump to a specific line number in Vim/Neovim

```vim
42G
42gg
:42<CR>
exe 42
```
```lua
-- Jump to line 42
vim.cmd('42')

-- Alternative methods
vim.cmd('normal! 42G')
vim.cmd('normal! 42gg')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Go_to_line)
***
# Title: Use Alt/Meta Keys for Quick Navigation
# Category: navigation
# Tags: terminal, key-mapping, navigation
---
In terminal Vim, use Alt/Meta + key combinations to quickly switch modes and navigate without pressing Escape

```vim
" Use Alt keys for quick navigation in terminal Vim
" Alt+h, Alt+j, Alt+k, Alt+l for movement
" Alt+o to open line below
" Alt+A to append to end of line
```
```lua
-- Terminal Vim navigation (configurable in init.lua)
-- Requires terminal to send appropriate escape sequences
vim.g.terminal_alt_key_navigation = true
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Insert_and_back)
***
# Title: Efficient Text Navigation and Manipulation
# Category: navigation
# Tags: movement, text-objects, editing
---
Powerful cursor movement and text editing commands that work across words, sentences, and paragraphs

```lua
-- Word movement
vim.keymap.set('n', 'w', 'w')  -- Move forward by word
vim.keymap.set('n', 'b', 'b')  -- Move backward by word
vim.keymap.set('n', 'e', 'e')  -- Move to end of word

-- Sentence and paragraph movement
vim.keymap.set('n', '(', '(')  -- Move to previous sentence
vim.keymap.set('n', ')', ')')  -- Move to next sentence
vim.keymap.set('n', '{', '{')  -- Move to previous paragraph
vim.keymap.set('n', '}', '}')  -- Move to next paragraph
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Introduction_to_display_editing_using_vi)
***
# Title: Quick Recovery When Spell Checking
# Category: navigation
# Tags: spell-checking, text-editing, navigation
---
When accidentally marking a misspelled word as correct during spell checking, use Ctrl-O to jump back and then zug to mark the word as not found.

```vim
" Navigate back in jump list
Ctrl-O
" Mark word as not found
zug
```
```lua
-- Vim's built-in navigation and spell checking works similarly in Neovim
-- Ctrl-O to jump back
-- Use vim.cmd to execute Vim commands
vim.cmd('normal! \<C-O>')
vim.cmd('normal! zug')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Jump_back_to_spell_checked_words)
***
# Title: Quick Navigation Between C++ Methods
# Category: navigation
# Tags: key-mapping, c++, search
---
Easily jump to next or previous method in C++ files using Alt+J/K key mappings with a regex pattern

```vim
nnoremap <M-J> /\v^(\w+\s+)?\w+::\w+\(.*\)
nnoremap <M-K> ?\v^(\w+\s+)?\w+::\w+\(.*\)
```
```lua
vim.keymap.set('n', '<M-J>', '/\v^(\w+\s+)?\w+::\w+\(.*\)<CR>', { desc = 'Jump to next C++ method' })
vim.keymap.set('n', '<M-K>', '?\v^(\w+\s+)?\w+::\w+\(.*\)<CR>', { desc = 'Jump to previous C++ method' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Jump_between_methods_in_C%2B%2B)
***
# Title: Open Files with Line Numbers
# Category: navigation
# Tags: file-navigation, cursor-movement
---
Open files directly to a specific line number using uppercase commands

```vim
" Open file and go to line number
gF  " Same window
<c-w>F  " New window
<c-w>gF  " New tab
```
```lua
-- Open file and go to line number
vim.keymap.set('n', 'gF', 'gF', { desc = 'Open file at line number' })
vim.keymap.set('n', '<c-w>F', '<c-w>F', { desc = 'Open file at line number in split' })
vim.keymap.set('n', '<c-w>gF', '<c-w>gF', { desc = 'Open file at line number in new tab' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Jump_to_a_file_to_a_certain_line_number)
***
# Title: Quick Jump to Function Definition
# Category: navigation
# Tags: search, code-navigation, key-mapping
---
Quickly jump to a function definition by placing cursor on function name and using a custom mapping

```vim
nmap gx yiw/^\(sub\<Bar>function\)\s\+<C-R>"<CR>
```
```lua
vim.keymap.set('n', 'gx', function()
  -- Yank current word
  vim.cmd('normal! yiw')
  
  -- Search for function definition
  local search_term = vim.fn.getreg('"')
  vim.cmd('/' .. '^(sub\\|function)\\s\\+' .. search_term)
end, { desc = 'Jump to function definition' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Jump_to_a_function_from_where_it_is_called)
***
# Title: Jump to a Random Line in Buffer
# Category: navigation
# Tags: random, jumping, buffer-navigation
---
Provides multiple methods to jump to a random line in the current buffer using different random number generation techniques

```vim
command! RandomLine execute 'normal! '.(system('/bin/bash -c "echo -n $RANDOM"') % line('$')).'G'
```
```lua
vim.api.nvim_create_user_command('RandomLine', function()
  local total_lines = vim.fn.line('$')
  local random_line = math.random(total_lines)
  vim.cmd(string.format('normal! %dG', random_line))
end, {})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Jump_to_a_random_line)
***
# Title: Random Line Selection with Range Support
# Category: navigation
# Tags: random, range-selection, ruby
---
Advanced random line selection that supports specifying a range for random line jumping

```vim
function! RandomLine() range
  ruby first_line = (VIM::evaluate 'a:firstline').to_i
  ruby last_line = (VIM::evaluate 'a:lastline').to_i
  ruby VIM::command(((rand last_line - first_line + 1) + first_line).to_s)
endfunction
command! -range=% RandomLine <line1>,<line2>call RandomLine()
```
```lua
vim.api.nvim_create_user_command('RandomLine', function(opts)
  local first_line = opts.line1
  local last_line = opts.line2
  local random_line = math.random(first_line, last_line)
  vim.cmd(string.format('%d', random_line))
end, { range = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Jump_to_a_random_line)
***
# Title: Quick Entity Definition Jump in DTDs
# Category: navigation
# Tags: search, mapping, dtd
---
Quickly jump to entity definitions in DTD files by searching backwards for the entity name

```vim
:map <Leader>e yiw ?<!ENTITY % <C-R>"<CR>
```
```lua
vim.keymap.set('n', '<Leader>e', function()
  -- Yank word under cursor
  vim.cmd('yiw')
  -- Search backwards for entity definition
  vim.cmd('?<!ENTITY % ' .. vim.fn.getreg('"') .. '\n')
end, { desc = 'Jump to Entity Definition' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Jump_to_definition_of_entity_under_cursor)
***
# Title: Jump to File from Diff View
# Category: navigation
# Tags: diff, file-navigation, key-mapping
---
Adds a mapping to jump from a diff view to the original file at the corresponding line, making code review and comparison easier

```vim
function! DiffJumpToFile()
  let a=line(".")
  let b=search("^\(---\|\*\*\*\) ", "b")
  let c=getline(b)
  let d=strpart(c, 4, match(c, ",")-4)
  let f=search("^\(---\|\*\*\*\) .*\t", "b")
  let g=getline(f)
  let h=match(g, "\t", 4)
  let i=strpart(g, 4, h-4)
  execute ":b " . i
  execute "normal " . (d+a-b-1) . "G"
endfunction
nmap <buffer> <CR> :call DiffJumpToFile()<CR>
```
```lua
function _G.diff_jump_to_file()
  local current_line = vim.fn.line('.')
  local header_line = vim.fn.search('^(---|\*\*\*) ', 'b')
  local header_text = vim.fn.getline(header_line)
  local first_line_num = tonumber(header_text:match('(%d+),'))
  local file_header_line = vim.fn.search('^(---|\*\*\*) .*	', 'b')
  local file_header_text = vim.fn.getline(file_header_line)
  local filename = file_header_text:match('(.-)	')
  
  vim.cmd('buffer ' .. filename)
  vim.cmd(tostring(first_line_num + current_line - header_line - 1) .. 'G')
end

vim.api.nvim_create_autocmd('FileType', {
  pattern = 'diff',
  callback = function()
    vim.keymap.set('n', '<CR>', _G.diff_jump_to_file, { buffer = true })
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Jump_to_file_from_CVSDiff_output)
***
# Title: Jump Between C++ Methods Quickly
# Category: navigation
# Tags: c++, search, key-mapping
---
Easily navigate between methods in C++ files using Alt-Shift-J/K key mappings with a regex-based search

```vim
nnoremap <M-J> /\v^(\w+\s+)?\w+::\w+\(.*\)
nnoremap <M-K> ?\v^(\w+\s+)?\w+::\w+\(.*\)
```
```lua
vim.keymap.set('n', '<M-J>', function()
  vim.fn.search('\v^(\w+\s+)?\w+::\w+\(.*\)')
end, { desc = 'Jump to next C++ method' })

vim.keymap.set('n', '<M-K>', function()
  vim.fn.search('\v^(\w+\s+)?\w+::\w+\(.*\)', 'b')
end, { desc = 'Jump to previous C++ method' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Jump_to_next/previous_method_in_C%2B%2B)
***
# Title: Easy Help Tag Navigation for German Keyboards
# Category: navigation
# Tags: key-mapping, help-navigation
---
Provide alternative key mappings to jump to help tags on German keyboards where ']' is difficult to access

```vim
" Option 1: Map to 't' key
nnoremap t <C-]>

" Option 2: Map to umlaut key
nnoremap ü <C-]>
nnoremap Ü <C-O>
```
```lua
-- Option 1: Map to 't' key
vim.keymap.set('n', 't', '<C-]>', { desc = 'Jump to help tag' })

-- Option 2: Map to umlaut key
vim.keymap.set('n', 'ü', '<C-]>', { desc = 'Jump to help tag' })
vim.keymap.set('n', 'Ü', '<C-O>', { desc = 'Jump back from help tag' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Jump_to_tag_(help_topic)_with_German_keyboard)
***
# Title: Use g; and g, for Edit Location Navigation
# Category: navigation
# Tags: edit-locations, movement
---
Move backward and forward through edit locations within a file

```vim
" g; - go to previous edit location
" g, - go to next edit location
```
```lua
-- Built-in Vim/Neovim commands work as-is
-- Recommended mapping for clarity
vim.keymap.set('n', 'g;', 'g;', { desc = 'Go to previous edit location' })
vim.keymap.set('n', 'g,', 'g,', { desc = 'Go to next edit location' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Jumping_to_previously_visited_locations)
***
# Title: Jump to Variable Declaration
# Category: navigation
# Tags: code-navigation, programming, search
---
Quickly jump to local or global variable declarations in source code

```vim
" Jump to local variable declaration
gd  " Normal mode command

" Jump to global variable declaration
gD  " Normal mode command
```
```lua
-- These Vim commands work natively in Neovim
-- No specific Lua conversion needed
-- Use gd and gD in normal mode
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Jumping_to_the_declaration_of_a_local/global_variable)
***
# Title: Function Definition Search
# Category: navigation
# Tags: code-search, programming, function-navigation
---
Custom function to search for function definitions more precisely

```vim
function! GotoDefinition()
  let n = search("\<".expand("<cword>")."\>[^(]*([^)]*)\s*\n*\s*{")
endfunction
map <F4> :call GotoDefinition()<CR>
imap <F4> <c-o>:call GotoDefinition()<CR>
```
```lua
function _G.goto_definition()
  vim.fn.search(vim.fn.expand('<cword>') .. '[^(]*([^)]*)\s*\n*\s*{')
end

vim.keymap.set('n', '<F4>', _G.goto_definition, { desc = 'Go to function definition' })
vim.keymap.set('i', '<F4>', '<c-o>:lua _G.goto_definition()<CR>', { desc = 'Go to function definition' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Jumping_to_the_declaration_of_a_local/global_variable)
***
# Title: Jump to Local and Global Definitions Easily
# Category: navigation
# Tags: definition-jumping, code-navigation, key-mapping
---
Combines local and global variable/function definition jumping into a single key mapping, first trying local search, then falling back to global tags

```vim
function! GoDefinition()
  let l:pos = getpos('.')
  normal! gd
  if getpos('.') == l:pos
    execute 'tag' expand('<cword>')
  endif
endfunction
nnoremap <C-]> :<C-U>call GoDefinition()<CR>
```
```lua
function _G.go_definition()
  local original_pos = vim.fn.getpos('.')
  vim.cmd('normal! gd')
  local new_pos = vim.fn.getpos('.')
  
  if vim.fn.list2str(original_pos) == vim.fn.list2str(new_pos) then
    local word = vim.fn.expand('<cword>')
    vim.cmd('tag ' .. word)
  end
end

vim.keymap.set('n', '<C-]>', _G.go_definition, { desc = 'Jump to local or global definition' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Jumps_to_a_local/global_definition_by_same_key)
***
# Title: Center Cursor on Movement
# Category: navigation
# Tags: key-mapping, movement
---
Automatically center the screen whenever moving up or down with j/k keys

```vim
" Center cursor on movement
nnoremap j jzz
nnoremap k kzz
```
```lua
-- Center cursor on movement
vim.keymap.set('n', 'j', 'jzz', { noremap = true })
vim.keymap.set('n', 'k', 'kzz', { noremap = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Keep_your_cursor_centered_vertically_on_the_screen)
***
# Title: Improve Last Position Jump for Easy Vim
# Category: navigation
# Tags: cursor-position, vim-improvement, last-jump
---
Enhance the last position jump functionality in Easy Vim to restore cursor position, even beyond the end of line (EOL)

```lua
-- For Neovim, this can be achieved with an autocmd
vim.api.nvim_create_autocmd('BufReadPost', {
  callback = function()
    local last_pos = vim.fn.line("'\"") -- Get last known position
    if last_pos > 0 and last_pos <= vim.fn.line('$') then
      vim.cmd('normal! g`"')
    end
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Last_position_jump_improved_for_Easy_Vim)
***
# Title: Navigate File Change History
# Category: navigation
# Tags: change-list, navigation, editing-history
---
Easily jump between previous change locations in a file using built-in change list navigation

```vim
" Jump to previous change
g;

" Jump to next change
g,

" View change list
:changes
```
```lua
-- Jump to previous change
vim.keymap.set('n', 'g;', 'g;', { desc = 'Go to previous change' })

-- Jump to next change
vim.keymap.set('n', 'g,', 'g,', { desc = 'Go to next change' })

-- View change list
vim.api.nvim_command('changes')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/List_changes_to_the_current_file)
***
# Title: Fuzzy Search Tags with Regular Expressions
# Category: navigation
# Tags: tags, search, regular-expressions
---
Use regular expressions to flexibly search and find tags when you're not sure of the exact function name

```vim
:tj /handle.*event<C-D>
```
```lua
-- Lua equivalent for tag searching
-- Note: Requires having tags file generated
vim.cmd('tj /handle.*event')
-- Use <C-D> for command-line completion
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Look_up_tags_using_regular_expressions)
***
# Title: Center Screen on Search Navigation
# Category: navigation
# Tags: search, screen-positioning, key-mapping
---
Automatically center the screen when navigating search results, improving readability and focus

```vim
" Map search navigation keys to always center screen
nnoremap n nzz
nnoremap N Nzz
nnoremap * *zz
nnoremap # #zz
nnoremap g* g*zz
nnoremap g# g#zz
```
```lua
-- Center screen on search navigation
vim.keymap.set('n', 'n', 'nzz', { desc = 'Next search result, center screen' })
vim.keymap.set('n', 'N', 'Nzz', { desc = 'Previous search result, center screen' })
vim.keymap.set('n', '*', '*zz', { desc = 'Search word forward, center screen' })
vim.keymap.set('n', '#', '#zz', { desc = 'Search word backward, center screen' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Make_search_results_appear_in_the_middle_of_the_screen)
***
# Title: Quick Navigation in Help Buffers
# Category: navigation
# Tags: key-mapping, help-buffer, custom-navigation
---
Remap Enter/Backspace to quickly navigate help documentation, making it more intuitive to follow links and go back

```vim
" Remap help buffer navigation
if exists("b:did_ftplugin")
  finish
endif

" Map Enter to follow help links
nnoremap <buffer><CR> <c-]>

" Map Backspace to go back
nnoremap <buffer><BS> <c-T>
```
```lua
-- Lua equivalent for help buffer navigation
vim.api.nvim_create_autocmd('FileType', {
  pattern = 'help',
  callback = function()
    vim.keymap.set('n', '<CR>', '<C-]>', { buffer = true })
    vim.keymap.set('n', '<BS>', '<C-T>', { buffer = true })
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mapping_to_quickly_browse_help)
***
# Title: Navigate Help Labels with Tab Keys
# Category: navigation
# Tags: help-buffer, key-mapping, search
---
Add Tab/Shift-Tab mappings to quickly jump between |labels| in help documentation

```vim
" Navigate between help labels
nnoremap <buffer> <Tab> /<Bar>\zs\k*\ze<Bar><CR>
nnoremap <buffer> <S-Tab> ?<Bar>\zs\k*\ze<Bar><CR>
```
```lua
-- Lua equivalent for navigating help labels
vim.api.nvim_create_autocmd('FileType', {
  pattern = 'help',
  callback = function()
    vim.keymap.set('n', '<Tab>', '/<Bar>\zs\k*\ze<Bar><CR>', { buffer = true })
    vim.keymap.set('n', '<S-Tab>', '?<Bar>\zs\k*\ze<Bar><CR>', { buffer = true })
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mapping_to_quickly_browse_help)
***
# Title: Enhanced Matching with % Key
# Category: navigation
# Tags: motion, text-objects, programming
---
Expand the % key functionality to jump between matching elements beyond just brackets, including code blocks, comments, and preprocessor conditionals

```vim
" Enable matchit plugin
runtime macros/matchit.vim
```
```lua
-- In Neovim, can use built-in matchit or treesitter for enhanced matching
-- Recommend installing nvim-treesitter for advanced language-aware matching
require('nvim-treesitter.configs').setup {
  matchup = {
    enable = true,
  }
}
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Match_It_Plugin)
***
# Title: Enhanced Bracket and Brace Navigation
# Category: navigation
# Tags: movement, text-objects, matching
---
Use % key to jump between matching braces, brackets, and more advanced language constructs

```vim
" Enable extended matching with matchit.vim
runtime macros/matchit.vim
```
```lua
-- For Neovim, you can use built-in matchit or a Lua equivalent plugin
-- Add matchit.vim or use a Lua-based matching plugin
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Match_it)
***
# Title: Move Cursor by Display Lines in Wrapped Text
# Category: navigation
# Tags: cursor-movement, text-wrapping, key-mapping
---
Remap navigation keys to move by displayed lines instead of physical lines when text wrapping is enabled, improving readability and navigation in wrapped text

```vim
" Remap j, k, and arrow keys to move by display lines
noremap <silent> k gk
noremap <silent> j gj
noremap <silent> 0 g0
noremap <silent> $ g$

" Support for operator-pending mode
onoremap <silent> j gj
onoremap <silent> k gk
```
```lua
-- Remap movement keys to navigate by display lines
vim.keymap.set('n', 'k', 'gk', { silent = true })
vim.keymap.set('n', 'j', 'gj', { silent = true })
vim.keymap.set('n', '0', 'g0', { silent = true })
vim.keymap.set('n', '$', 'g$', { silent = true })

-- Support for operator-pending mode
vim.keymap.set('o', 'j', 'gj', { silent = true })
vim.keymap.set('o', 'k', 'gk', { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Move_cursor_by_display_lines_when_wrapping)
***
# Title: Efficient Tab Navigation and Management
# Category: navigation
# Tags: tabs, key-mapping, window-management
---
Enhanced tab navigation and management with custom key mappings for moving between tabs and repositioning tabs

```vim
" Navigate tabs
nnoremap <C-Left> :tabprevious<CR>
nnoremap <C-Right> :tabnext<CR>

" Move current tab
nnoremap <silent> <A-Left> :tabm -1<CR>
nnoremap <silent> <A-Right> :tabm +1<CR>
```
```lua
-- Navigate tabs
vim.keymap.set('n', '<C-Left>', ':tabprevious<CR>', { silent = true })
vim.keymap.set('n', '<C-Right>', ':tabnext<CR>', { silent = true })

-- Move current tab
vim.keymap.set('n', '<A-Left>', ':tabm -1<CR>', { silent = true })
vim.keymap.set('n', '<A-Right>', ':tabm +1<CR>', { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Move_the_current_tabpage_forward_or_backward)
***
# Title: Efficient Tab Page Navigation
# Category: navigation
# Tags: tab-management, key-mapping, window-management
---
Enhanced tab navigation with keyboard shortcuts for quickly moving between and managing tab pages

```vim
" Tab navigation shortcuts
nnoremap <C-Left> :tabprevious<CR>
nnoremap <C-Right> :tabnext<CR>
nnoremap <silent> <A-Left> :tabm -1<CR>
nnoremap <silent> <A-Right> :tabm +1<CR>
```
```lua
-- Tab navigation shortcuts
vim.keymap.set('n', '<C-Left>', ':tabprevious<CR>', { noremap = true, silent = true })
vim.keymap.set('n', '<C-Right>', ':tabnext<CR>', { noremap = true, silent = true })
vim.keymap.set('n', '<A-Left>', ':tabm -1<CR>', { noremap = true, silent = true })
vim.keymap.set('n', '<A-Right>', ':tabm +1<CR>', { noremap = true, silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Move_through_the_buffer_list_without_wrecking_your_window/tab_layout)
***
# Title: Jump to Lines with Same/Lower Indentation
# Category: navigation
# Tags: indentation, movement, programming
---
Quickly navigate between lines with the same or lower indentation level, which is especially useful in languages like Python, Haskell, or when editing XML

```vim
function! NextIndent(exclusive, fwd, lowerlevel, skipblanks)
  let line = line('.')
  let column = col('.')
  let lastline = line('$')
  let indent = indent(line)
  let stepvalue = a:fwd ? 1 : -1
  while (line > 0 && line <= lastline)
    let line = line + stepvalue
    if ( ! a:lowerlevel && indent(line) == indent ||
          \ a:lowerlevel && indent(line) < indent)
      if (! a:skipblanks || strlen(getline(line)) > 0)
        if (a:exclusive)
          let line = line - stepvalue
        endif
        exe line
        exe "normal " column . "|"
        return
      endif
    endif
  endwhile
endfunction

" Normal mode mappings
nnoremap <silent> [l :call NextIndent(0, 0, 0, 1)<CR>
nnoremap <silent> ]l :call NextIndent(0, 1, 0, 1)<CR>
nnoremap <silent> [L :call NextIndent(0, 0, 1, 1)<CR>
nnoremap <silent> ]L :call NextIndent(0, 1, 1, 1)<CR>
```
```lua
function _G.next_indent(exclusive, fwd, lowerlevel, skipblanks)
  local line = vim.fn.line('.')
  local column = vim.fn.col('.')
  local lastline = vim.fn.line('$')
  local indent = vim.fn.indent(line)
  local stepvalue = fwd and 1 or -1

  while line > 0 and line <= lastline do
    line = line + stepvalue
    local current_indent = vim.fn.indent(line)
    local line_content = vim.fn.getline(line)

    if (not lowerlevel and current_indent == indent) or
       (lowerlevel and current_indent < indent) then
      if not skipblanks or #line_content > 0 then
        if exclusive then
          line = line - stepvalue
        end
        vim.fn.cursor(line, column)
        return
      end
    end
  end
end

-- Set up keymappings
vim.keymap.set('n', '[l', function() _G.next_indent(false, false, false, true) end, { silent = true })
vim.keymap.set('n', ']l', function() _G.next_indent(false, true, false, true) end, { silent = true })
vim.keymap.set('n', '[L', function() _G.next_indent(false, false, true, true) end, { silent = true })
vim.keymap.set('n', ']L', function() _G.next_indent(false, true, true, true) end, { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Move_to_next/previous_line_with_same_indentation)
***
# Title: Efficient Text Navigation Commands
# Category: navigation
# Tags: movement, text-objects, cursor-navigation
---
Powerful movement commands to quickly navigate through text without using arrow keys

```vim
" Movement commands
" e - end of word
" w - start of next word
" b - back to start of word
" ) - next sentence
" } - next paragraph
```
```lua
-- Neovim movement commands are built-in
-- Use native Vim movement keys
-- Example: Add custom mapping for safer navigation
vim.keymap.set('n', '<leader>w', 'w', { desc = 'Move to next word start' })
vim.keymap.set('n', '<leader>e', 'e', { desc = 'Move to word end' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Moving_around)
***
# Title: Advanced Cursor Jumping Techniques
# Category: navigation
# Tags: marks, jump-list, cursor-movement
---
Use marks and jump list to quickly navigate between different locations in a file

```vim
" Set mark with mx
" Jump to mark with 'x
" Return to previous jump with ''
```
```lua
-- Set a mark
vim.cmd('normal! mx')

-- Jump to a specific mark
vim.cmd('normal! `x')

-- Return to previous jump
vim.cmd('normal! \'\'') -- Two single quotes
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Moving_around)
***
# Title: Screen-Based Movement Commands
# Category: navigation
# Tags: screen-movement, viewport, scrolling
---
Quick ways to move through the viewport without using mouse or scrollbar

```vim
" H - top of screen
" M - middle of screen
" L - bottom of screen
" 10<PageUp> - move 10 pages up
```
```lua
-- Screen movement is native in Neovim
-- Can wrap with custom mappings for enhanced control
vim.keymap.set('n', '<leader>H', 'H', { desc = 'Move to top of screen' })
vim.keymap.set('n', '<leader>M', 'M', { desc = 'Move to middle of screen' })
vim.keymap.set('n', '<leader>L', 'L', { desc = 'Move to bottom of screen' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Moving_around)
***
# Title: Jump to Matching Braces and Syntax Elements
# Category: navigation
# Tags: movement, syntax-navigation, text-objects
---
Use % key to jump between matching syntax elements, including braces, comments, and language-specific constructs

```vim
" Built-in % navigation
" Works with (), [], {}, comments, preprocessor blocks
```
```lua
-- Recommend using built-in % key
-- Can be enhanced with matchit plugin
-- No specific Lua configuration needed
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Moving_to_matching_braces)
***
# Title: Move Between Words in Insert Mode
# Category: navigation
# Tags: insert-mode, word-movement, key-mapping
---
Quick navigation between words while in insert mode using keyboard shortcuts

```vim
" Built-in shortcuts
" Shift + Right Arrow: Move to next word
" Shift + Left Arrow: Move to previous word
" Ctrl + Right/Left Arrow also work across different vim behaviors
```
```lua
-- These are built-in Neovim behaviors
-- No specific Lua configuration needed
-- Equivalent to Vim's native word movement in insert mode
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Moving_to_the_next_word_in_insert_mode)
***
# Title: Enable Caret Browsing for Vim-Like Text Navigation
# Category: navigation
# Tags: browser, keyboard-navigation
---
Firefox's caret browsing mode allows keyboard-based text cursor movement similar to Vim's navigation

```lua
-- In Firefox, press F7 to toggle caret browsing
-- Enables moving through text with keyboard like in Vim
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mozilla_Vim_Keybindings)
***
# Title: Highlight and Navigate CSV Columns Easily
# Category: navigation
# Tags: csv, data-parsing, text-manipulation
---
Provides functions to highlight specific columns in CSV files and navigate between columns with easy commands

```vim
function! CSVH(colnr)
  if a:colnr > 1
    let n = a:colnr - 1
    execute 'match Keyword /^([^,]*,)\{'.n.'}\zs[^,]*/' 
    execute 'normal! 0'.n.'f,'
  elseif a:colnr == 1
    match Keyword /^[^,]*/
    normal! 0
  else
    match
  endif
endfunction
command! -nargs=1 Csv :call CSVH(<args>)
```
```lua
local function csv_highlight(colnr)
  if colnr > 1 then
    local n = colnr - 1
    vim.cmd('match Keyword /^([^,]*,){' .. n .. '}\\zs[^,]*/')
    vim.cmd('normal! 0' .. n .. 'f,')
  elseif colnr == 1 then
    vim.cmd('match Keyword /^[^,]*/')
    vim.cmd('normal! 0')
  else
    vim.cmd('match')
  end
end

vim.api.nvim_create_user_command('Csv', function(opts)
  csv_highlight(tonumber(opts.args))
end, { nargs = 1 })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Navigate_large_CSV_files_more_easily)
***
# Title: Navigate to Next/Previous Open Fold
# Category: navigation
# Tags: folding, key-mapping, navigation
---
Custom function to move between open folds more intuitively, using ]z and [z mappings

```vim
function! GoToOpenFold(direction)
  let start = line('.')
  if (a:direction == "next")
    while (foldclosed(start) != -1)
      let start = start + 1
    endwhile
  else
    while (foldclosed(start) != -1)
      let start = start - 1
    endwhile
  endif
  call cursor(start, 0)
endfunction
nmap ]z :cal GoToOpenFold("next")
nmap [z :cal GoToOpenFold("prev")
```
```lua
function _G.go_to_open_fold(direction)
  local start = vim.fn.line('.')
  if direction == 'next' then
    while vim.fn.foldclosed(start) ~= -1 do
      start = start + 1
    end
  else
    while vim.fn.foldclosed(start) ~= -1 do
      start = start - 1
    end
  end
  vim.fn.cursor(start, 0)
end

vim.keymap.set('n', ']z', function() _G.go_to_open_fold('next') end)
vim.keymap.set('n', '[z', function() _G.go_to_open_fold('prev') end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Navigate_to_the_next_open_fold)
***
# Title: Navigate Vim Help on AZERTY Keyboards
# Category: navigation
# Tags: help, keyboard-mapping, azerty
---
Alternative key mapping for navigating Vim help on AZERTY keyboards where Ctrl+] doesn't work

```vim
" Map F9 to follow help tags and links
nmap <F9> <C-]>
map! <F9> <C-]>
```
```lua
-- Map F9 to follow help tags and links in Neovim
vim.keymap.set('n', '<F9>', '<C-]>', { desc = 'Follow help tag' })
vim.keymap.set({'i', 'c'}, '<F9>', '<C-]>', { desc = 'Follow help tag' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Naviguer_dans_l%27aide_avec_un_clavier_AZERTY)
***
# Title: Alternative Help Navigation Mapping
# Category: navigation
# Tags: help, key-mapping, navigation
---
Additional key mappings for navigating help documentation using Alt keys

```lua
-- Alternative help navigation using Alt keys
vim.keymap.set('n', '<M-left>', '<C-o>', { desc = 'Go back in help navigation' })
vim.keymap.set('n', '<M-down>', '<C-]>', { desc = 'Follow help link' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Naviguer_dans_l%27aide_avec_un_clavier_AZERTY)
***
# Title: Efficient Vim Navigation and Editing Basics
# Category: navigation
# Tags: beginner, key-mapping, text-editing
---
Key tips for new Vim users to get started with basic navigation and editing

```vim
# Basic Vim navigation and editing
# Enter insert mode
i
# Exit and save
:w myfile.txt
# Exit without saving
:q
```
```lua
-- Lua equivalents (conceptual)
-- Enter insert mode
vim.cmd('startinsert')
-- Save file
vim.cmd('write myfile.txt')
-- Exit without saving
vim.cmd('quit')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/New_to_Vim)
***
# Title: Quick Open Perl Module Source
# Category: navigation
# Tags: perl, file-operations, key-mapping
---
Quickly open the source file for a Perl module by placing cursor on module name and using a custom mapping

```vim
nnoremap <Leader>pm :call LoadPerlModule()<CR>

function! LoadPerlModule()
  execute 'e `perldoc -l ' . expand("<cWORD>") . '`'
endfunction
```
```lua
vim.keymap.set('n', '<Leader>pm', function()
  local module = vim.fn.expand('<cWORD>')
  local cmd = string.format('e `perldoc -l %s`', module)
  vim.cmd(cmd)
end, { desc = 'Open Perl Module Source' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_a_Perl_module_from_its_module_name)
***
# Title: Open Man Pages for Word Under Cursor
# Category: navigation
# Tags: man-pages, documentation, key-mapping
---
Quickly open man pages for the word under the cursor using the K key in Vim/Neovim

```vim
fun! ReadMan()
  let s:man_word = expand('<cword>')
  :exe ":wincmd n"
  :exe ":r!man " . s:man_word . " | col -b"
  :exe ":goto"
  :exe ":delete"
  :exe ":set filetype=man"
endfun
map K :call ReadMan()<CR>
```
```lua
function _G.read_man()
  local man_word = vim.fn.expand('<cword>')
  vim.cmd('new')
  vim.cmd('read !man ' .. man_word .. ' | col -b')
  vim.cmd('norm! gg')
  vim.cmd('delete')
  vim.bo.filetype = 'man'
end

vim.keymap.set('n', 'K', _G.read_man, { desc = 'Open man page for word under cursor' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_a_window_with_the_man_page_for_the_word_under_the_cursor)
***
# Title: Open Files Using Filename Under Cursor
# Category: navigation
# Tags: file-operations, navigation, productivity
---
Quickly open files by placing cursor on filename and using built-in commands

```vim
" Open file in current window
gf

" Open file in new window
<c-w>f

" Open file in new tab
<c-w>gf
```
```lua
-- These are built-in Vim/Neovim commands, no specific Lua translation needed
-- Use as-is in normal mode
-- gf: Open file under cursor in current window
-- <C-w>f: Open file under cursor in new horizontal split
-- <C-w>gf: Open file under cursor in new tab
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_file_under_cursor)
***
# Title: Open Files Under Cursor with Multiple Methods
# Category: navigation
# Tags: file-navigation, cursor-movement, buffer-management
---
Multiple ways to open files referenced under the cursor, including in same window, new window, or new tab

```vim
" Open file under cursor in different ways
gf             " Open in current window
<c-w>f         " Open in new horizontal split
<c-w>gf        " Open in new tab
```
```lua
-- Open file under cursor
-- Vim's default gf, <C-w>f, and <C-w>gf work in Neovim
-- For explicit mapping if needed:
vim.keymap.set('n', '<leader>f', 'gf', { desc = 'Open file under cursor' })
vim.keymap.set('n', '<leader>sf', '<C-w>f', { desc = 'Open file in horizontal split' })
vim.keymap.set('n', '<leader>tf', '<C-w>gf', { desc = 'Open file in new tab' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_filenames_containing_spaces_with_gf)
***
# Title: Jump to PDF Page from LaTeX File
# Category: navigation
# Tags: latex, pdf, workflow, file-navigation
---
Automatically open a PDF viewer to the corresponding page of the current LaTeX file, making document navigation easier

```vim
function! EvinceNearestLabel()
  let line = search("\\label{", "bnW")
  if line > 0
    let m = matchstr(getline(line), '\\label{\zs[^}]*\ze}')
    if !empty(m)
      call LoadEvinceByLabel(m)
    endif
  endif
endfunction

nnoremap <buffer> <LocalLeader>e :call EvinceNearestLabel()<CR>
```
```lua
function _G.nearest_label_pdf()
  local line_nr = vim.fn.search('\\label{', 'bnW')
  if line_nr > 0 then
    local line = vim.fn.getline(line_nr)
    local label = line:match('\\label{([^}]+)}')
    if label and label ~= '' then
      vim.fn.LoadEvinceByLabel(label)
    end
  end
end

vim.keymap.set('n', '<LocalLeader>e', _G.nearest_label_pdf, { buffer = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Open_pdf_to_the_current_location_in_a_LaTeX_file)
***
# Title: Use K to View PHP Function Help
# Category: navigation
# Tags: php, documentation, key-mapping
---
Configure Vim to show PHP function documentation when pressing K on a function name

```vim
" In ftplugin/php.vim
set keywordprg=:help
```
```lua
-- In lua/ftplugin/php.lua
vim.opt.keywordprg = ':help'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/PHP_manual_in_Vim_help_format)
***
# Title: Page Up/Down While Keeping Cursor Position
# Category: navigation
# Tags: scrolling, cursor-position, key-mapping
---
Scroll page up/down while maintaining the cursor's relative screen position, similar to Borland-style scrolling

```vim
function! MyPageUp()
  let visible_lines = GetNumberOfVisibleLines()
  execute "normal " . visible_lines . "\<C-U>:set scroll=0\r"
endfunction

function! MyPageDown()
  let visible_lines = GetNumberOfVisibleLines()
  execute "normal " . visible_lines . "\<C-D>:set scroll=0\r"
endfunction

noremap <PageUp> :call MyPageUp()<CR>
noremap <PageDown> :call MyPageDown()<CR>
```
```lua
local function get_visible_lines()
  local cur_line = vim.fn.line('.')
  local cur_col = vim.fn.virtcol('.')
  vim.cmd('normal H')
  local top_line = vim.fn.line('.')
  vim.cmd('normal L')
  local bot_line = vim.fn.line('.')
  vim.cmd('normal ' .. cur_line .. 'G')
  vim.cmd('normal ' .. cur_col .. '|')
  return bot_line - top_line
end

vim.keymap.set('n', '<PageUp>', function()
  local visible_lines = get_visible_lines()
  vim.cmd('normal ' .. visible_lines .. '\<C-U>')
  vim.o.scroll = 0
end)

vim.keymap.set('n', '<PageDown>', function()
  local visible_lines = get_visible_lines()
  vim.cmd('normal ' .. visible_lines .. '\<C-D>')
  vim.o.scroll = 0
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Page_up/down_and_keep_cursor_position)
***
# Title: Quick Man Page Lookup for Word Under Cursor
# Category: navigation
# Tags: man-pages, documentation, quick-lookup
---
Press K in normal mode to instantly view the man page for the word under the cursor, providing quick documentation access

```vim
" Optional: Configure man page lookup
set keywordprg=man\ -a
```
```lua
-- Configure man page lookup
vim.opt.keywordprg = 'man -a'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Power_K)
***
# Title: View Multiple Man Page Chapters
# Category: navigation
# Tags: man-pages, documentation, advanced-lookup
---
Prefix the chapter number before pressing K to view specific sections of a man page

```vim
" Example: 3 K would look up chapter 3 man pages
```
```lua
-- No direct Lua equivalent, relies on Vim's built-in man page lookup
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Power_K)
***
# Title: Quick Navigation with Word Labels
# Category: navigation
# Tags: motion, jump, labeling
---
Dynamically label words on screen for rapid, precise navigation without using a mouse

```vim
let LABEL = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",
"t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I",
"J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y",
"Z","1","2","3","4","5","6","7","8","9","0"]

function! GoTo(range)
    normal! Hmt
    for i in range(0,a:range)
        exe 'normal! Wr' . g:LABEL[i%len(g:LABEL)]
    endfor
    normal! 'tzt
    echo "Index?"
    redraw
    let label=nr2char(getchar())
    normal! u'tzt
    for i in range(0,a:range)
        exe 'normal! Wr' . (1+i/len(g:LABEL))
    endfor
    normal! 'tzt
    echo "Number?"
    redraw
    let offset=getchar()
    let offset=(49 <= offset && offset <= 57) ? offset-48 : 1
    normal! u'tzt
    let index=index(g:LABEL,label)
    exe 'normal! ' . ((offset-1)*len(g:LABEL)+index+1) . 'W'
endfu
nnoremap <TAB> :call GoTo(248)<CR>
```
```lua
-- Lua implementation of word labeling navigation
local function goto_labeled_word(range)
    range = range or 248
    -- Implement similar logic using Neovim Lua APIs
    -- Note: This is a complex translation and would require more detailed implementation
    vim.keymap.set('n', '<Tab>', function()
        -- Placeholder for dynamic word labeling navigation
        vim.notify('Word labeling navigation', vim.log.levels.INFO)
    end)
end

goto_labeled_word()
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Precise_Jumps_Without_Mouse)
***
# Title: Navigate Jump List Efficiently
# Category: navigation
# Tags: jump-list, navigation, cursor-movement
---
Quickly move between previous and next jump locations in Vim/Neovim, similar to browser navigation

```vim
" Jump navigation
noremap <C-o> Jump back to previous location
noremap <C-i> Jump forward to next location
:jumps  " Display jump list
```
```lua
-- Jump navigation
vim.keymap.set('n', '<C-o>', '<C-o>', { desc = 'Jump back to previous location' })
vim.keymap.set('n', '<C-i>', '<C-i>', { desc = 'Jump forward to next location' })
-- Display jump list
vim.api.nvim_command('jumps')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Prev_and_Next)
***
# Title: Interactive Jump List Selection
# Category: navigation
# Tags: jump-list, custom-function, interactive
---
Create a custom function to interactively select and navigate jump list locations

```vim
function! GotoJump()
  jumps
  let j = input('Please select your jump: ')
  if j != ''
    let pattern = '\v\c^\+'
    if j =~ pattern
      let j = substitute(j, pattern, '', 'g')
      execute "normal " . j . "\<c-i>"
    else
      execute "normal " . j . "\<c-o>"
    endif
  endif
endfunction

" Optional mapping
nmap <Leader>j :call GotoJump()<CR>
```
```lua
function _G.goto_jump()
  vim.cmd('jumps')
  local jump = vim.fn.input('Please select your jump: ')
  if jump ~= '' then
    local pattern = '^+'
    if jump:match(pattern) then
      jump = jump:gsub(pattern, '')
      vim.api.nvim_feedkeys(jump .. '\<C-i>', 'n', true)
    else
      vim.api.nvim_feedkeys(jump .. '\<C-o>', 'n', true)
    end
  end
end

-- Optional mapping
vim.keymap.set('n', '<Leader>j', _G.goto_jump, { desc = 'Interactive jump list navigation' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Prev_and_Next)
***
# Title: Recursive Project File Finding
# Category: navigation
# Tags: project-management, file-search, productivity
---
Quickly find files in a project by setting recursive path search, enabling fast file navigation across deep directory structures

```vim
set path=$PWD/**
```
```lua
vim.opt.path = vim.fn.getcwd() .. '/**'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Project_browsing_using_find)
***
# Title: Quick Tab Navigation and Management
# Category: navigation
# Tags: tab-management, key-mapping, buffer-navigation
---
Efficient ways to navigate and manage tabs in Vim/Neovim, including quick key mappings for switching and moving tabs

```vim
" Navigate tabs
nnoremap <C-Left> :tabprevious<CR>
nnoremap <C-Right> :tabnext<CR>

" Move tabs
nnoremap <silent> <A-Left> :tabm -1<CR>
nnoremap <silent> <A-Right> :tabm +1<CR>

" Toggle buffer display in tabs
let notabs = 0
nnoremap <silent> <F8> :let notabs=!notabs<Bar>:if notabs<Bar>:tabo<Bar>:else<Bar>:tab ball<Bar>:tabn<Bar>:endif<CR>
```
```lua
-- Navigate tabs
vim.keymap.set('n', '<C-Left>', ':tabprevious<CR>', { noremap = true, silent = true })
vim.keymap.set('n', '<C-Right>', ':tabnext<CR>', { noremap = true, silent = true })

-- Move tabs
vim.keymap.set('n', '<A-Left>', ':tabm -1<CR>', { noremap = true, silent = true })
vim.keymap.set('n', '<A-Right>', ':tabm +1<CR>', { noremap = true, silent = true })

-- Toggle buffer display in tabs
vim.api.nvim_set_var('notabs', 0)
vim.keymap.set('n', '<F8>', function()
  local notabs = vim.g.notabs
  vim.g.notabs = notabs == 0 and 1 or 0
  if notabs == 0 then
    vim.cmd('tabo')
  else
    vim.cmd('tab ball')
    vim.cmd('tabn')
  end
end, { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Quick_tab_navigation_and_opening)
***
# Title: Quick Reference Documents in Tabs
# Category: navigation
# Tags: help, documentation, tabs
---
Open help pages and reference documents in separate tabs for easy access without disrupting current workspace

```vim
:tab help toc
:tab help <topic>
```
```lua
-- Open help in a new tab
vim.cmd('tab help toc')
vim.cmd('tab help ' .. topic)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Quick_tips_for_using_tab_pages)
***
# Title: Open Files Under Cursor Quickly
# Category: navigation
# Tags: file-operations, navigation, productivity
---
Provides multiple ways to open files referenced under the cursor, including opening in same window, split, or tab

```vim
" Open file in current window
gf

" Open file in new window
<c-w>f

" Open file in new tab
<c-w>gf
```
```lua
-- These are built-in Vim/Neovim commands, so no direct Lua translation needed
-- Can be used directly in Neovim
-- Recommend setting up additional keymaps if desired
vim.keymap.set('n', '<leader>f', 'gf', { desc = 'Open file under cursor' })
vim.keymap.set('n', '<leader>sf', '<C-w>f', { desc = 'Open file in split' })
vim.keymap.set('n', '<leader>tf', '<C-w>gf', { desc = 'Open file in new tab' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Quickly_Get_Files_in_your_Environment)
***
# Title: Quickly Search Vim Help Topics
# Category: navigation
# Tags: help, search, documentation
---
Multiple efficient methods to search and navigate Vim help topics, including using wildcard completion and built-in search commands

```vim
" Search help topics with partial match
:he shell<c-d>

" Use helpgrep to search help files
:helpgrep shell
:copen

" Create a custom help search command
:command! -nargs=+ -complete=tag Helpt :Tselect /.*<args>.*
```
```lua
-- Built-in help search
-- Use vim.cmd to run help commands in Lua
vim.cmd('helpgrep shell')
vim.cmd('copen')

-- Create a custom help search function
vim.api.nvim_create_user_command('Helpt', function(opts)
  vim.cmd('Tselect /.*' .. opts.args .. '.*')
end, { nargs = '+', complete = 'tag' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Quickly_look_up_Vim_help)
***
# Title: Advanced Tab Navigation Shortcuts
# Category: navigation
# Tags: tabs, key-mapping, window-management
---
Powerful tab navigation mappings to quickly move between and manage tabs

```vim
" Tab navigation mappings
nnoremap <C-Left> :tabprevious<CR>
nnoremap <C-Right> :tabnext<CR>
nnoremap <silent> <A-Left> :tabm -1<CR>
nnoremap <silent> <A-Right> :tabm +1<CR>
```
```lua
-- Tab navigation mappings
vim.keymap.set('n', '<C-Left>', ':tabprevious<CR>', { noremap = true, silent = true })
vim.keymap.set('n', '<C-Right>', ':tabnext<CR>', { noremap = true, silent = true })
vim.keymap.set('n', '<A-Left>', ':tabm -1<CR>', { noremap = true, silent = true })
vim.keymap.set('n', '<A-Right>', ':tabm +1<CR>', { noremap = true, silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Read_(but_not_write)_file_in_new_tab)
***
# Title: Read Javadoc Directly in Vim
# Category: navigation
# Tags: documentation, java, help
---
Use a custom doclet to generate Vim help files for Java documentation, allowing quick access to Javadoc within Vim

```vim
" Set keywordprg to blank to use 'K' for quick Javadoc lookup
set keywordprg=
" Use :help to access Javadoc
:help String
:help java.util.List
```
```lua
-- Configure keywordprg for quick Javadoc lookup
vim.o.keywordprg = ''
-- Access Javadoc using :help
-- Requires installing Vim Doclet from vimdoclet.sourceforge.net
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Read_Javadoc_In_Vim)
***
# Title: Dynamically Build Tags from Path
# Category: navigation
# Tags: tags, development, path-management
---
Automatically build tag files from all directories in your path, making it easier to navigate large codebases with multiple include directories

```vim
function! BuildTagsFromPath()
python << EOF
import sys
import vim
paths = vim.eval("&path")
pathsSplit = paths.split(",")

tags = vim.eval("&tags")
for path in pathsSplit:
  tags += "%s/tags," % (path)
cmdSetTags = "set tags=%s" % tags
vim.command(cmdSetTags)
EOF
endfunction

call BuildTagsFromPath()
```
```lua
local function build_tags_from_path()
  local paths = vim.o.path
  local path_list = vim.split(paths, ",")
  
  local tags = vim.o.tags
  for _, path in ipairs(path_list) do
    tags = tags .. path .. "/tags,"
  end
  
  vim.o.tags = tags
end

vim.api.nvim_create_user_command('BuildTagsFromPath', build_tags_from_path, {})

-- Call the function when setting up
build_tags_from_path()
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Read_tag_files_from_all_directories_in_your_path)
***
# Title: Powerful Tag Navigation in Vim/Neovim
# Category: navigation
# Tags: tags, code-browsing, jump-to-definition
---
Efficiently navigate code by jumping to tag definitions using multiple methods

```vim
" Jump to tag
Ctrl-]

" List multiple tag matches
g]

" Preview tag without leaving current window
Ctrl-W }
```
```lua
-- Jump to tag definition
vim.keymap.set('n', '<C-]>', '<cmd>tag<CR>', { desc = 'Jump to tag' })

-- List multiple tag matches
vim.keymap.set('n', 'g]', '<cmd>tselect<CR>', { desc = 'List tag matches' })

-- Preview tag in preview window
vim.keymap.set('n', '<C-w>}', '<cmd>ptag<CR>', { desc = 'Preview tag' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip453)
***
# Title: Flexible Tag Search and Navigation
# Category: navigation
# Tags: tag-search, code-exploration, fuzzy-finding
---
Advanced tag searching with pattern matching and browsing multiple matches

```vim
" Search tags with a pattern
:tag /<pattern>

" Jump to tag only if single match, otherwise list
:tjump <tagname>
```
```lua
-- Search tags with a pattern
vim.cmd.tag('/' .. pattern)

-- Conditional tag jumping
vim.keymap.set('n', '<leader>tj', function()
  vim.cmd('tjump ' .. vim.fn.expand('<cword>'))
end, { desc = 'Conditional tag jump' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip453)
***
# Title: Quickly Open Perl Module Source
# Category: navigation
# Tags: perl, file-operations, productivity
---
Quickly open the source file for a Perl module by cursor position or command

```vim
nnoremap <Leader>pm :call LoadPerlModule()<CR>

function! LoadPerlModule()
  execute 'e `perldoc -l ' . expand("<cWORD>") . '`'
endfunction
```
```lua
vim.keymap.set('n', '<Leader>pm', function()
  local module = vim.fn.expand('<cWORD>')
  local cmd = string.format('e `perldoc -l %s`', module)
  vim.cmd(cmd)
end, { desc = 'Open Perl Module Source' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip461)
***
# Title: Quickfix Window Navigation Mappings
# Category: navigation
# Tags: quickfix, key-mapping, navigation
---
Add convenient mappings to navigate through quickfix list with easy key bindings

```vim
nnoremap <kPlus>     :cnext<CR> :norm! zz<CR>
nnoremap <kMinus>    :cprev<CR> :norm! zz<CR>
nnoremap <kMultiply> :cc<CR> :norm! zz<CR>
```
```lua
vim.keymap.set('n', '<kPlus>', ':cnext<CR>zz', { silent = true })
vim.keymap.set('n', '<kMinus>', ':cprev<CR>zz', { silent = true })
vim.keymap.set('n', '<kMultiply>', ':cc<CR>zz', { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip483)
***
# Title: Navigate LaTeX Sections Efficiently
# Category: navigation
# Tags: latex, section-jumping, text-objects
---
Custom mapping to jump between LaTeX sections (part, chapter, section) with support for forward/backward movement and count repetitions

```vim
" section jumping
noremap <buffer> <silent> ]] :<c-u>call TexJump2Section( v:count1, '' )<CR>
noremap <buffer> <silent> [[ :<c-u>call TexJump2Section( v:count1, 'b' )<CR>

function! TexJump2Section( cnt, dir )
  let i = 0
  let pat = '^\s*\\\(part\|chapter\|\(sub\)*section\|paragraph\)\>\|\%$\|\%^'
  let flags = 'W' . a:dir
  while i < a:cnt && search( pat, flags ) > 0
    let i = i+1
  endwhile
  let @/ = pat
endfunction
```
```lua
local function tex_jump_to_section(count, direction)
  local pattern = '^\s*\\(part\|chapter\|(sub)*section\|paragraph)\>\|\%$\|\%^'
  local flags = 'W' .. (direction or '')
  
  for _ = 1, count do
    vim.fn.search(pattern, flags)
  end
  
  vim.fn.setreg('/', pattern)
end

vim.keymap.set('n', ']]', function()
  tex_jump_to_section(vim.v.count1, '')
end, { buffer = true, silent = true })

vim.keymap.set('n', '[[', function()
  tex_jump_to_section(vim.v.count1, 'b')
end, { buffer = true, silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip489)
***
# Title: Find Current Verilog Module Name
# Category: navigation
# Tags: search, module-navigation, verilog
---
Quickly identify the current Verilog module by searching backwards and echoing the module name

```vim
map ` ma?module<CR>Wyiw'a:echo "module -->" @0<CR>
```
```lua
vim.keymap.set('n', '`', function()
  -- Save current position
  vim.cmd('normal! ma')
  
  -- Search backwards for module definition
  vim.cmd('?module')
  
  -- Yank module name and return to mark
  vim.cmd('normal! Wyiw`a')
  
  -- Echo module name
  local module_name = vim.fn.getreg('0')
  print("module --> " .. module_name)
end, { desc = 'Find current Verilog module' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip534)
***
# Title: Context-Sensitive H/L Movement
# Category: navigation
# Tags: key-mapping, window-navigation, scroll
---
Enhance H and L keys to act as context-sensitive page up/down when at window edges, providing more efficient window navigation

```vim
function! Hcontext()
  if (winline() == 1 && line('.') != 1)
    exe "normal! \<pageup>H"
  else
    exe "normal! H"
  endif
endfunc

function! Lcontext()
  if (winline() == winheight(0) && line('.') != line('$'))
    exe "normal! \<pagedown>L"
  else
    exe "normal! L"
  endif
endfunc

noremap H :call Hcontext()<CR>
noremap L :call Lcontext()<CR>
```
```lua
function _G.hcontext()
  if (vim.fn.winline() == 1 and vim.fn.line('.') ~= 1) then
    vim.cmd('normal! \<PageUp>H')
  else
    vim.cmd('normal! H')
  end
end

function _G.lcontext()
  if (vim.fn.winline() == vim.fn.winheight(0) and vim.fn.line('.') ~= vim.fn.line('$')) then
    vim.cmd('normal! \<PageDown>L')
  else
    vim.cmd('normal! L')
  end
end

vim.keymap.set('n', 'H', _G.hcontext)
vim.keymap.set('n', 'L', _G.lcontext)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip548)
***
# Title: Navigate Jump List with Keyboard Shortcuts
# Category: navigation
# Tags: jump-list, navigation, motion
---
Quickly move between previously visited locations in Vim/Neovim using built-in jump list navigation shortcuts

```vim
" Navigate jump list
Ctrl-O  " Jump back to previous location
Ctrl-I  " Jump forward to newer location
:jumps  " Display jump list
```
```lua
-- Jump list navigation can be used directly in Neovim
-- Ctrl-O and Ctrl-I work the same way
-- Use :jumps to view jump history
vim.keymap.set('n', '<C-o>', '<C-o>', { desc = 'Jump back in jump list' })
vim.keymap.set('n', '<C-i>', '<C-i>', { desc = 'Jump forward in jump list' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip553)
***
# Title: Quick Navigation to Current Day in Calendar
# Category: navigation
# Tags: calendar, search, quick-navigation
---
Function to quickly jump to the current month and day in a pre-generated calendar file

```vim
function! Today()
  let calfile = g:cal
  if (bufnr(calfile) > 0)
    exe ":bu " . bufnr(calfile)
  else
    exe "edit " . calfile
  endif
  let a = search("- " . strftime("%b %Y") . " -", "w")
  let a = search("^.. " . strftime("%d"), "w")
endfunction

map <S-F4> :call Today()<CR>
```
```lua
function _G.goto_today()
  local calfile = vim.g.cal
  local buf_exists = vim.fn.bufnr(calfile) > 0
  
  if buf_exists then
    vim.cmd('buffer ' .. vim.fn.bufnr(calfile))
  else
    vim.cmd('edit ' .. calfile)
  end
  
  local current_month = os.date('%b %Y')
  local current_day = os.date('%d')
  
  vim.fn.search('- ' .. current_month .. ' -', 'w')
  vim.fn.search('^.. ' .. current_day, 'w')
end

vim.keymap.set('n', '<S-F4>', _G.goto_today)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip560)
***
# Title: Quick Jump to Keyword Occurrences
# Category: navigation
# Tags: search, jump, keyword, navigation
---
Easily list and jump to occurrences of a keyword in the current file and included files

```vim
" List occurrences of keyword under cursor, and
" jump to selected occurrence.
function! s:JumpOccurrence()
  let v:errmsg = ""
  exe "normal [I"
  if strlen(v:errmsg) == 0
    let nr = input("Which one: ")
    if nr =~ '\d\+'
      exe "normal! " . nr . "[\t"
    endif
  endif
endfunction

" List occurrences of keyword entered at prompt, and
" jump to selected occurrence.
function! s:JumpPrompt()
  let keyword = input("Keyword to find: ")
  if strlen(keyword) > 0
    let v:errmsg = ""
    exe "ilist! " . keyword
    if strlen(v:errmsg) == 0
      let nr = input("Which one: ")
      if nr =~ '\d\+'
        exe "ijump! " . nr . keyword
      endif
    endif
  endif
endfunction

nnoremap <Leader>j :call <SID>JumpOccurrence()<CR>
nnoremap <Leader>p :call <SID>JumpPrompt()<CR>
```
```lua
local function jump_occurrence()
  vim.cmd('normal! [I')
  local nr = vim.fn.input('Which one: ')
  if nr ~= '' and tonumber(nr) then
    vim.cmd('normal! ' .. nr .. '[\t')
  end
end

local function jump_prompt()
  local keyword = vim.fn.input('Keyword to find: ')
  if keyword ~= '' then
    vim.cmd('ilist! ' .. keyword)
    local nr = vim.fn.input('Which one: ')
    if nr ~= '' and tonumber(nr) then
      vim.cmd('ijump! ' .. nr .. keyword)
    end
  end
end

vim.keymap.set('n', '<Leader>j', jump_occurrence, { desc = 'Jump to keyword occurrence' })
vim.keymap.set('n', '<Leader>p', jump_prompt, { desc = 'Prompt and jump to keyword' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip563)
***
# Title: Jump to Matching Braces and Code Blocks
# Category: navigation
# Tags: movement, code-navigation, editing
---
Use the % key to quickly jump between matching braces, brackets, and other code block delimiters across multiple programming languages

```vim
" Default behavior
" % jumps to matching brace/bracket/parenthesis
set matchtime=3
set showmatch
```
```lua
-- Configure matching brace highlighting
vim.opt.matchtime = 3
vim.opt.showmatch = true
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip6)
***
# Title: Create Custom Tags with Line and Column Precision
# Category: navigation
# Tags: ctags, tag-navigation, custom-indexing
---
Generate a custom tags file that allows precise jumping to specific line and column positions in files, useful for complex project navigation

```vim
function! MakeTags(filespec, pattern)
  let tags = []
  for file in glob(a:filespec, 0, 1)
    for hit in SearchFile(file, a:pattern)
      call add(tags, printf("%s\t%s\t/\%%%dl\%%%dc/", hit[2], file, hit[0], hit[1]))
    endfor
  endfor
  return sort(tags)
endfunction
```
```lua
function MakeTags(filespec, pattern)
  local tags = {}
  local files = vim.fn.glob(filespec, false, true)
  for _, file in ipairs(files) do
    local hits = SearchFile(file, pattern)
    for _, hit in ipairs(hits) do
      table.insert(tags, string.format('%s\t%s\t/\%%%dl\%%%dc/', hit[3], file, hit[1], hit[2]))
    end
  end
  table.sort(tags)
  return tags
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip601)
***
# Title: View Man Pages Directly in Vim/Neovim
# Category: navigation
# Tags: man-pages, documentation, help
---
Quickly view man pages within Vim/Neovim without leaving the editor

```vim
runtime ftplugin/man.vim
:Man <command>
set keywordprg=:Man
```
```lua
-- Enable man page viewer
vim.cmd.runtime('ftplugin/man.vim')

-- Open man page
vim.cmd.Man('<command>')

-- Set K to use :Man by default
vim.o.keywordprg = ':Man'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip606)
***
# Title: Quick Python Module-Test File Switching
# Category: navigation
# Tags: python, file-navigation, productivity
---
Quickly switch between Python source files and their corresponding test files using a custom function that looks for a special comment with the test file path

```vim
fun! JumpToTestFile()
  let line = getline("$")
  if line =~ "^### testfile: "
    let filename = strpart(line, 14)
    execute ":e " . filename
  else
    echo "TEST PATTERN ### testfile: NOT FOUND!"
  endif
endfun

nmap <buffer> <F5> :call JumpToTestFile()<CR>
```
```lua
function JumpToTestFile()
  local last_line = vim.fn.getline('$')
  if last_line:match('^### testfile: ') then
    local filename = last_line:sub(15)
    vim.cmd('edit ' .. filename)
  else
    print('TEST PATTERN ### testfile: NOT FOUND!')
  end
end

vim.api.nvim_create_autocmd('FileType', {
  pattern = 'python',
  callback = function()
    vim.keymap.set('n', '<F5>', JumpToTestFile, { buffer = true })
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip658)
***
# Title: Flexible Python Test File Toggle
# Category: navigation
# Tags: python, file-navigation, buffer-management
---
Toggle between source and test files with a smart mechanism that checks existing buffers and handles different file naming patterns

```vim
function! UTestToggle()
python << EOF
import vim
from os import path

UTEST_PREFIX='test/utest_'
curfile = vim.current.buffer.name
if curfile:
  if UTEST_PREFIX in curfile:
    vim.command('e %s' % curfile.replace(UTEST_PREFIX, ''))
  else:
    filepath, filename = path.split(curfile)
    vim.command('e %s' % path.join(filepath, UTEST_PREFIX+filename))
EOF
endfunction

nnoremap <M-t> :call UTestToggle()<CR>
```
```lua
function UTestToggle()
  local UTEST_PREFIX = 'test/utest_'
  local curfile = vim.fn.expand('%:p')
  
  if curfile:match(UTEST_PREFIX) then
    local source_file = curfile:gsub(UTEST_PREFIX, '')
    vim.cmd('edit ' .. source_file)
  else
    local filepath = vim.fn.expand('%:p:h')
    local filename = vim.fn.expand('%:t')
    local test_file = filepath .. '/' .. UTEST_PREFIX .. filename
    vim.cmd('edit ' .. test_file)
  end
end

vim.keymap.set('n', '<M-t>', UTestToggle, { desc = 'Toggle between source and test files' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip658)
***
# Title: Highlight and Navigate CSV Columns Efficiently
# Category: navigation
# Tags: csv, text-processing, highlighting
---
Provides advanced navigation and highlighting for CSV files, allowing easy column selection, searching, and manipulation

```vim
function! CSVH(colnr)
  if a:colnr > 1
    let n = a:colnr - 1
    execute 'match Keyword /^([^,]*,)\{'.n.'}\zs[^,]*/')
    execute 'normal! 0'.n.'f,'
  elseif a:colnr == 1
    match Keyword /^[^,]*/
    normal! 0
  else
    match
  endif
endfunction
command! -nargs=1 Csv :call CSVH(<args>)
```
```lua
function _G.highlight_csv_column(colnr)
  if colnr > 1 then
    local n = colnr - 1
    vim.cmd(string.format('match Keyword /^([^,]*,)\\{%d}\\zs[^,]*/', n))
    vim.cmd(string.format('normal! 0%df,', n))
  elseif colnr == 1 then
    vim.cmd('match Keyword /^[^,]*/')
    vim.cmd('normal! 0')
  else
    vim.cmd('match')
  end
end

vim.api.nvim_create_user_command('Csv', function(opts)
  _G.highlight_csv_column(tonumber(opts.args))
end, { nargs = 1 })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip667)
***
# Title: Generate Tags for Current File
# Category: navigation
# Tags: ctags, code-navigation, file-indexing
---
Use ctags to generate and display tags for the current file, helping quickly navigate function and variable definitions

```vim
map <M-l> <Esc>:!/usr/local/bin/vimlocals.sh % <CR>:
```
```lua
vim.keymap.set('n', '<M-l>', function()
  local current_file = vim.fn.expand('%')
  vim.cmd('!ctags -x -n ' .. current_file)
end, { desc = 'Show tags for current file' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip711)
***
# Title: Position Line at Screen Top/Middle/Bottom
# Category: navigation
# Tags: screen-positioning, cursor-placement
---
Methods to bring a specific line to the top, middle, or bottom of the screen

```vim
42G zt   " Line 42 at top
42G z.   " Line 42 at middle
42G zb   " Line 42 at bottom

" Screen positioning
H   " Move to top of screen
M   " Move to middle of screen
L   " Move to bottom of screen
```
```lua
-- Screen positioning methods
vim.cmd('42 normal! zt')  -- Line 42 at top
vim.cmd('42 normal! z.')  -- Line 42 at middle
vim.cmd('42 normal! zb')  -- Line 42 at bottom

-- Move cursor to screen regions
vim.cmd('normal! H')  -- Top of screen
vim.cmd('normal! M')  -- Middle of screen
vim.cmd('normal! L')  -- Bottom of screen
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip751)
***
# Title: Windows-like Ctrl+Left/Right Word Navigation
# Category: navigation
# Tags: key-mapping, windows-compatibility
---
Remap Ctrl+Left and Ctrl+Right to move by words, mimicking Windows text editing behavior

```vim
"Edit mapping for word navigation
nnoremap <C-Left> b
nnoremap <C-Right> w

"For visual and insert modes
vnoremap <C-S-Left> b
vnoremap <C-S-Right> w
inoremap <C-S-Left> <C-\><C-O>b
inoremap <C-S-Right> <C-\><C-O>w
```
```lua
-- Word navigation like Windows
vim.keymap.set('n', '<C-Left>', 'b', { noremap = true })
vim.keymap.set('n', '<C-Right>', 'w', { noremap = true })

-- Additional mappings for visual and insert modes
vim.keymap.set('v', '<C-S-Left>', 'b', { noremap = true })
vim.keymap.set('v', '<C-S-Right>', 'w', { noremap = true })
vim.keymap.set('i', '<C-S-Left>', '<C-\><C-O>b', { noremap = true })
vim.keymap.set('i', '<C-S-Right>', '<C-\><C-O>w', { noremap = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip752)
***
# Title: Inline Java Documentation Browsing
# Category: navigation
# Tags: documentation, java, productivity
---
Quickly view Java class and method documentation without leaving Vim, using generated help files

```vim
" Use :help to access Java docs
:help String
:help java.util.List
```
```lua
-- Similar navigation in Neovim
-- After setting up doclet help files
vim.cmd('help String')
vim.cmd('help java.util.List')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Vim_Doclet)
***
# Title: Vim-Style Browser Navigation Extensions
# Category: navigation
# Tags: browser-navigation, key-mapping, productivity
---
Several browser extensions allow Vim-like keyboard navigation, reducing mouse usage and improving browsing efficiency

```lua
-- Recommended browser extensions for Vim-like navigation:
-- Vimium (Chrome/Chromium)
-- Tridactyl (Firefox)
-- Surfingkeys (Cross-browser)
-- Vim Vixen (Firefox)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Vim_key_bindings_for_web_browsers)
***
# Title: Keyboard-Driven Web Browsers with Vim Keybindings
# Category: navigation
# Tags: browser, keyboard-navigation, productivity
---
Some specialized web browsers natively support Vim-like keyboard navigation

```lua
-- Recommended Vim-like browsers:
-- Qutebrowser (keyboard-driven)
-- Vimb (WebKit + GTK+)
-- Vieb (Electron-based)
-- Luakit (Lua + WebKit)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Vim_key_bindings_for_web_browsers)
***
# Title: Navigate Wrapped Lines Smoothly
# Category: navigation
# Tags: movement, wrapped-lines, visual-mode
---
Use visual line movement commands to navigate wrapped lines more intuitively, treating wrapped lines as visual lines instead of logical lines

```vim
" Movement commands for wrapped lines
nnoremap j gj
nnoremap k gk
nnoremap 0 g0
nnoremap $ g$
nnoremap ^ g^
```
```lua
-- Movement commands for wrapped lines
vim.keymap.set('n', 'j', 'gj', { noremap = true })
vim.keymap.set('n', 'k', 'gk', { noremap = true })
vim.keymap.set('n', '0', 'g0', { noremap = true })
vim.keymap.set('n', '$', 'g$', { noremap = true })
vim.keymap.set('n', '^', 'g^', { noremap = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Working_with_long_lines)
***
