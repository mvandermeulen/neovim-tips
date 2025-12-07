# Title: Yank and delete in visual mode
# Category: Visual
# Tags: yank, delete, visual
---
Use `y` to yank (copy) selected text and `d` to delete selected text in visual mode.

```vim
y  " yank selected text
d  " delete selected text
```

**Source:** Community contributed
***
# Title: Yank highlighting
# Category: Visual
# Tags: yank, highlight, autocmd
---
Create an autocmd to highlight yanked text briefly for visual feedback.

```vim
:lua vim.api.nvim_create_autocmd("TextYankPost", {callback = function() vim.highlight.on_yank() end})
```

**Source:** Community contributed
***
# Title: Visual block append
# Category: Visual
# Tags: visual, block, append, column
---
Use `Ctrl+v` to select visual block, then `A` to append text to end of each selected line.

```vim
Ctrl+v  " select visual block
A       " append to end of all lines
text    " type text to append
Esc     " apply to all lines
```

**Source:** Community contributed
***
# Title: Visual mode - corner and edge movement
# Category: Visual
# Tags: visual, corner, block, movement
---
Use `o` to move cursor to opposite corner of selection, `O` to move to other corner in block mode.

```vim
" In visual mode:
o   " move cursor to opposite corner of selection
O   " move to other corner (block mode only)
```

**Source:** Community contributed
***
# Title: Visual mode - toggle and change types
# Category: Visual
# Tags: visual, toggle, change, type
---
Use `v`, `V`, `Ctrl+v` in visual mode to change selection type or exit. Use `Ctrl+g` to toggle between Visual and Select mode.

```vim
" In visual mode:
v       " change to character-wise or exit visual
V       " change to line-wise or exit visual  
Ctrl+v  " change to block-wise or exit visual
Ctrl+g  " toggle Visual/Select mode
```

**Source:** Community contributed
***
# Title: Visual mode - operators and transformations
# Category: Visual
# Tags: visual, operator, transform, case
---
Apply operators to visual selections: `c` (change), `d` (delete), `y` (yank), `~` (toggle case), `u` (lowercase), `U` (uppercase).

```vim
" After making visual selection:
c   " change selected text
d   " delete selected text
y   " yank selected text
~   " toggle case of selection
u   " make selection lowercase
U   " make selection uppercase
```

**Source:** Community contributed
***
# Title: Visual mode - joining and substitution
# Category: Visual
# Tags: visual, join, substitute, replace
---
Use `J` to join selected lines with spaces, `gJ` to join without spaces, `s` to substitute selection, `r` to replace each character.

```vim
" After making visual selection:
J    " join lines with spaces
gJ   " join lines without spaces
s    " substitute selected text
rx   " replace each character with 'x'
```

**Source:** Community contributed
***
# Title: Visual mode - paste and replace
# Category: Visual
# Tags: visual, paste, replace, register
---
Use `p` or `P` to replace visual selection with register contents. This is useful for swapping text.

```vim
" Copy text first, then select other text:
p   " replace selection with register contents
P   " same as p in visual mode
```

**Source:** Community contributed
***
# Title: Visual mode - tag and keyword operations
# Category: Visual
# Tags: visual, tag, keyword, jump
---
Use `Ctrl+]` to jump to tag of selected text, `K` to run keywordprg on selection.

```vim
" After selecting text:
Ctrl+]  " jump to tag of selected text
K       " run help/man on selected keyword
```

**Source:** Community contributed
***
# Title: Pad Lines for Easy Visual Block Editing
# Category: visual_mode
# Tags: text-manipulation, visual-block, editing-trick
---
Easily pad lines with trailing blanks to enable consistent visual block editing, especially when lines have different lengths

```vim
" Pad all lines with trailing blanks to 'limit' length
function! AtOnce( limit )
  norm mm
  g/^/norm 100A
  g/^/call Truncate( getline('.'), limit )
  let @/=""
  norm 'm
endfunc
```
```lua
function PadLinesTrailingBlanks(limit)
  local current_pos = vim.fn.getcurpos()
  vim.cmd('g/^/normal! 100A')
  vim.cmd('g/^/call cursor(line("."), ' .. limit .. ') | normal! d$')
  vim.fn.setpos('.', current_pos)
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Add_trailing_blanks_to_lines_for_easy_visual_blocks)
***
# Title: Use Virtual Edit for Block Selection
# Category: visual_mode
# Tags: virtual-edit, block-selection, editing-mode
---
Enable virtual edit mode to allow block selection beyond line endings, making column editing more flexible

```vim
set ve+=block  " Enable block virtual edit
```
```lua
vim.opt.virtualedit:append('block')  -- Enable block virtual edit
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Add_trailing_blanks_to_lines_for_easy_visual_blocks)
***
# Title: Apply Substitutions to Visual Block Selections
# Category: visual_mode
# Tags: substitution, visual-block, editing
---
Apply substitutions specifically to a visual block selection without affecting entire lines

```vim
:'<,'>B s/pattern/newtext/g
```
```lua
-- Using command-line mode for visual block substitution
-- Select block with <C-v>, then use:
-- :'<,'>B s/pattern/newtext/g
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Applying_substitutes_to_a_visual_block)
***
# Title: Quick Visual Block Commenting
# Category: visual_mode
# Tags: commenting, block-editing, productivity
---
Quickly comment/uncomment code using visual block mode

```vim
" Comment in visual block mode
<c-v>
... move around ...
0 (first column)
I (insert)
// (comment character)
<Esc>
```
```lua
-- In Lua, this is typically done via key mapping
vim.keymap.set('x', '<leader>c', function()
  local mode = vim.fn.mode()
  if mode == '\<C-V>' then
    vim.cmd('normal! I// ')
  end
end, { desc = 'Comment visual block' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Comment/UnComment_visually_selected_text)
***
# Title: Powerful Visual Selection and Paste Techniques
# Category: visual_mode
# Tags: visual-selection, copy-paste, editing
---
Comprehensive guide to using visual modes for efficient text selection, copying, and pasting with multiple options

```vim
" Visual selection modes
v   " character-based visual selection
V   " whole line visual selection
Ctrl-v " block visual selection

" Paste operations
p   " paste after cursor
P   " paste before cursor
```
```lua
-- Lua equivalents are built-in with Neovim's default keymappings
-- No additional configuration needed

-- To enhance visual selection, you might add:
vim.keymap.set('n', 'gv', '`[v`]', { desc = 'Restore previous visual selection' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Cut/copy_and_paste_using_visual_selection)
***
# Title: Block Replacement in Visual Mode
# Category: visual_mode
# Tags: block-edit, advanced-editing, replacement
---
Efficiently replace text in a visual block by changing the first line and applying to entire selection

```vim
" In visual block mode (Ctrl-v)
c   " Change first line
<Esc><Esc>  " Apply changes to entire block
```
```lua
-- Block replacement can be done directly in Neovim
-- No specific Lua configuration needed
-- The default Vim behavior works in Neovim
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Cut/copy_and_paste_using_visual_selection)
***
# Title: Flexible Line Selection with Visual Mode
# Category: visual_mode
# Tags: selection, editing, copying
---
Use visual mode to select and manipulate lines without precise line counting

```vim
V       " Enter visual line mode
        " Select range of lines
ay      " Yank selected lines
```
```lua
-- Enter visual line mode
vim.cmd('normal V')
-- Yank selected lines
vim.cmd('normal ay')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Cut_or_copy_lines_without_counting_the_lines)
***
# Title: Visual Mode Block Indent Preservation
# Category: visual_mode
# Tags: indentation, visual-mode, reselect
---
Keeps visual block selection active after indenting, allowing multiple indents

```vim
vmap > >gv
vmap < <gv
```
```lua
vim.keymap.set('v', '>', '>gv', { desc = 'Indent and reselect' })
vim.keymap.set('v', '<', '<gv', { desc = 'Unindent and reselect' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Delete_to_the_end_of_the_line)
***
# Title: Drag Text Using Arrow Key Mappings
# Category: visual_mode
# Tags: key-mapping, text-movement, visual-editing
---
Enhanced mappings to move selected text left, right, up, and down using arrow keys in visual mode

```vim
" Arrow key movements in visual mode
vnoremap <Left> h
vnoremap <Right> l
vnoremap <Up> k
vnoremap <Down> j

" Drag text with Ctrl-arrows
vnoremap <C-Right> lholhxp`[1v<Space>
vnoremap <C-Left> hlohlxhP`[1v<Space>
vnoremap <C-Down> jkojkxjzvP`[1v<Space>
vnoremap <C-Up> kjokjxkzvP`[1v<Space>
```
```lua
-- Arrow key movements in visual mode
vim.keymap.set('v', '<Left>', 'h', { noremap = true })
vim.keymap.set('v', '<Right>', 'l', { noremap = true })
vim.keymap.set('v', '<Up>', 'k', { noremap = true })
vim.keymap.set('v', '<Down>', 'j', { noremap = true })

-- Drag text with Ctrl-arrows
vim.keymap.set('v', '<C-Right>', 'lholhxp`[1v<Space>', { noremap = true })
vim.keymap.set('v', '<C-Left>', 'hlohlxhP`[1v<Space>', { noremap = true })
vim.keymap.set('v', '<C-Down>', 'jkojkxjzvP`[1v<Space>', { noremap = true })
vim.keymap.set('v', '<C-Up>', 'kjokjxkzvP`[1v<Space>', { noremap = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Drag_words_with_Ctrl-left/right)
***
# Title: Visual Mode Text Swapping
# Category: visual_mode
# Tags: text-manipulation, visual-mode, exchange
---
Easily swap two pieces of text using visual mode and Ctrl-X

```vim
" Swap visually selected text
:vnoremap <C-X> <Esc>`.``gvP``P
```
```lua
-- Swap visually selected text
vim.keymap.set('v', '<C-X>', function()
  local start_pos = vim.fn.getpos("'<")
  local end_pos = vim.fn.getpos("'>")
  local text1 = vim.fn.getline(start_pos[2], end_pos[2])
  vim.cmd('normal! gvp')
  vim.fn.setpos('.', start_pos)
  vim.fn.setline(start_pos[2], text1)
end, { desc = 'Swap visually selected text' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Exchange_columns)
***
# Title: Select Entire Function with Visual Commands
# Category: visual_mode
# Tags: text-selection, navigation, code-editing
---
Quickly select an entire function, including comments and body, using visual mode and search commands

```vim
V/{<CR>%  " Select function from comment to closing brace
```
```lua
vim.cmd('normal V/{<CR>%')  -- Select function from comment to closing brace
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Format_a_code_block)
***
# Title: Generate Incrementing Column Numbers
# Category: visual_mode
# Tags: column-editing, number-generation, visual-block
---
Easily create a column of incrementing numbers in a visual block selection

```vim
# In visual block mode (Ctrl-v), select column
:I   # Increments numbers starting from first line
```
```lua
-- Note: Requires visincr.vim plugin
-- In visual block mode, use :I to increment numbers
-- Additional variants:
-- :I #    - Increment by specified number
-- :II     - Left-pad numbers
-- :II #   - Left-pad and increment by number
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Generating_a_column_of_increasing_numbers)
***
# Title: Highlight Text Inside Matching Parentheses
# Category: visual_mode
# Tags: text-selection, navigation, key-mapping
---
Quickly highlight text inside matching parentheses or other block delimiters with a custom key mapping

```vim
" Highlight block and pause briefly
nmap <C-p> m[vab:sleep 350m<CR>`[
imap <C-p> <Esc>m[vab:sleep 350m<CR>`[a
```
```lua
-- Highlight block and pause briefly in Neovim
vim.keymap.set('n', '<C-p>', function()
  vim.cmd('normal! m[vab')
  vim.cmd('sleep 350m')
  vim.cmd('normal! `[')
end, { desc = 'Highlight matching block' })

vim.keymap.set('i', '<C-p>', function()
  vim.cmd('normal! <Esc>m[vab')
  vim.cmd('sleep 350m')
  vim.cmd('normal! `[a')
end, { desc = 'Highlight matching block in insert mode' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Highlight_text_inside_matching_parentheses)
***
# Title: Select Different Block Types Easily
# Category: visual_mode
# Tags: text-selection, block-navigation
---
Quick mappings to select different types of text blocks using Vim's text objects

```vim
" Mappings for selecting various block types
nmap <C-P>9 m[va(:sleep 350m<CR>`[
nmap <C-P>[ m[va[:sleep 350m<CR>`[
nmap <C-P>] m[va{:sleep 350m<CR>`[
nmap <C-P>, m[va<:sleep 350m<CR>`[
```
```lua
-- Mappings for selecting various block types in Neovim
local block_types = {
  ['9'] = '(',
  ['['] = '[',
  [']'] = '{',
  [','] = '<'
}

for key, block in pairs(block_types) do
  vim.keymap.set('n', '<C-P>' .. key, function()
    vim.cmd('normal! m[va' .. block)
    vim.cmd('sleep 350m')
    vim.cmd('normal! `[')
  end, { desc = 'Highlight ' .. block .. ' block' })
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Highlight_text_inside_matching_parentheses)
***
# Title: Insert Text Across Multiple Lines in Visual Block Mode
# Category: visual_mode
# Tags: multi-line-editing, text-manipulation, visual-block
---
Quickly insert or append text at the same column across multiple lines using visual block mode

```vim
" Select block with Ctrl-V, then:
" I - Insert at start of block
" A - Append at end of block
```
```lua
-- In Neovim, same key bindings work in visual block mode
-- Ctrl-V to enter visual block
-- I or A to insert/append text
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Inserting_text_in_multiple_lines)
***
# Title: Visual Mode Bracket Surrounding
# Category: visual_mode
# Tags: text-objects, editing, brackets
---
Quickly surround visually selected text with brackets or quotes

```vim
" Surround visually selected text with parentheses
:vnoremap _( <Esc>`>a)<Esc>`<i(<Esc>
```
```lua
-- Surround visual selection with brackets
vim.keymap.set('v', '_(',
  function()
    vim.cmd('normal! `>a)')
    vim.cmd('normal! `<i(')
  end,
  { desc = 'Surround with parentheses' }
)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Making_Parenthesis_And_Brackets_Handling_Easier)
***
# Title: Increment Numbers in Visual Block Mode
# Category: visual_mode
# Tags: number-increment, visual-block, editing-trick
---
Easily increment numbers in a visual block selection, creating sequential lists

```vim
" Normal mode: g Ctrl-A to create sequential numbers
" Vim 8+ supports Ctrl-A to increment first number
```
```lua
-- In Neovim, use same Vim keybindings
-- Ctrl-V to enter visual block mode
-- Select numbers
-- g Ctrl-A or Ctrl-A to increment
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Making_a_list)
***
# Title: Quick Brace Matching Visual Selection
# Category: visual_mode
# Tags: text-objects, selection
---
Efficient ways to select code blocks delimited by braces using different methods

```vim
" Select inside/around braces
viB  " inner block
vaB  " block with braces
```
```lua
-- Lua uses same Vim text objects
-- Can be combined with other Neovim features like treesitter selection
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Match_It_Plugin)
***
# Title: Select Blocks with % Motion
# Category: visual_mode
# Tags: text-objects, selection, advanced-navigation
---
Quickly select entire code blocks using % motion in visual mode

```vim
" Select block with v%
" Use viB for inner block
" Use vaB for block with braces
```
```lua
-- These motions work the same in Neovim
-- v% selects to matching brace
-- viB selects inner block
-- vaB selects block with braces
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Matchit)
***
# Title: Handle Shift Key Mistakes in Visual Mode
# Category: visual_mode
# Tags: key-mapping, visual-mode, navigation
---
Prevent cursor jumping and unexpected behavior when accidentally holding Shift key in visual mode

```vim
" Normalize Shift+arrow key behavior
nnoremap <S-Up> V
nnoremap <S-Down> V
xnoremap <S-Up> k
xnoremap <S-Down> j
```
```lua
-- Lua mappings to handle Shift key in visual mode
vim.keymap.set('n', '<S-Up>', 'V', { noremap = true })
vim.keymap.set('n', '<S-Down>', 'V', { noremap = true })
vim.keymap.set('x', '<S-Up>', 'k', { noremap = true })
vim.keymap.set('x', '<S-Down>', 'j', { noremap = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Prevent_the_cursor_from_jumping_around_when_pressing_%22V%22_for_visual_mode)
***
# Title: Repeat Last Edit Across Visual Block Selection
# Category: visual_mode
# Tags: editing, visual-block, productivity
---
Allows repeating the last edit (.) across all lines in a visual block selection, making multi-line editing faster and more efficient

```vim
" allow the . to execute once for each line of a visual selection
vnoremap . :normal .<CR>
```
```lua
vim.keymap.set('v', '.', ':normal .<CR>', { desc = 'Repeat last edit on visual block lines' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Repeat_command_on_each_line_in_visual_block)
***
# Title: Repeat Visual Block Changes Across Lines
# Category: visual_mode
# Tags: visual-mode, editing, productivity
---
Apply the same edit across multiple lines in a visual block selection

```vim
vnoremap <silent> . :normal .<CR>
```
```lua
vim.keymap.set('v', '.', function()
  vim.cmd('normal! .')
end, { desc = 'Repeat edit across visual block lines' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Repeat_last_command_and_put_cursor_at_start_of_change)
***
# Title: Replace Visual Block with Another Block
# Category: visual_mode
# Tags: visual-block, text-replacement, advanced-editing
---
Efficiently replace one visual block of text with another by using yank and paste operations in visual block mode

```vim
" Step 1: Select first block
ctrl-v move "ay

" Step 2: Select and replace second block
ctrl-v move c ctrl-o "aP <Esc>
```
```lua
-- Note: These are key sequences, so direct Lua translation isn't straightforward
-- But the concept involves visual block mode and register manipulation
-- Can be implemented with vim.fn.feedkeys() if needed
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Replace_a_visual-block_of_text_with_another_such_block)
***
# Title: Create Rectangular Block of Exact Size
# Category: visual_mode
# Tags: visual-block, precise-selection
---
Create a rectangular block selection of exactly the same size as a previous block, using current cursor as top-left corner

```vim
" Use 1<Ctrl-V> instead of <Ctrl-V> move
```
```lua
-- Key sequence translation, use with caution in multibyte encodings
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Replace_a_visual-block_of_text_with_another_such_block)
***
# Title: Quickly Reselect Last Visual Selection
# Category: visual_mode
# Tags: visual-mode, selection, productivity
---
Allows you to quickly reselect the last visual selection without having to manually recreate the selection

```vim
gv
```
```lua
vim.cmd('normal! gv')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Reselect_Visual_Block)
***
# Title: Reverse Selected Text in Visual Mode
# Category: visual_mode
# Tags: text-manipulation, visual-mode, mapping
---
Quickly reverse the characters in a visually selected text on a single line

```vim
vnoremap ;rv c<C-O>:set revins<CR><C-R>"<Esc>:set norevins<CR>
```
```lua
vim.keymap.set('v', ';rv', function()
  -- Save the current register content
  local original_reg = vim.fn.getreg('"')
  
  -- Reverse the selected text
  vim.cmd('normal! d')
  vim.o.revins = true
  vim.api.nvim_put({original_reg:reverse()}, '', true, true)
  vim.o.revins = false
end, { desc = 'Reverse selected text' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Reverse_selected_text)
***
# Title: Blockwise Edit Multiple Lines Simultaneously
# Category: visual_mode
# Tags: editing, multi-line, visual-block
---
Insert or modify text across multiple lines using visual block mode

```vim
^<Ctrl-v>jjjjI#<ESC>  # Add comment at start of multiple lines
```
```lua
-- Similar approach in Lua
-- Use vim.cmd to execute visual block commands
vim.cmd('normal! ^<C-v>jjjjI#<Esc>')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip63)
***
# Title: Easy Blockwise Mouse Selection in Vim
# Category: visual_mode
# Tags: mouse-selection, key-mapping, visual-mode
---
Simplify blockwise visual selection using Alt-Mouse or alternative modifier keys

```vim
noremap <M-LeftMouse> <LeftMouse><Esc><C-V>
noremap <M-LeftDrag> <LeftDrag>
```
```lua
vim.keymap.set('n', '<M-LeftMouse>', '<LeftMouse><Esc><C-V>', { noremap = true })
vim.keymap.set('n', '<M-LeftDrag>', '<LeftDrag>', { noremap = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip743)
***
# Title: Alternate Mouse Selection Method
# Category: visual_mode
# Tags: mouse-selection, key-mapping, visual-mode
---
Alternative method for blockwise selection using different modifiers

```vim
noremap <S-RightMouse> <LeftMouse><Esc><C-V>
noremap <S-RightDrag> <LeftDrag>
```
```lua
vim.keymap.set('n', '<S-RightMouse>', '<LeftMouse><Esc><C-V>', { noremap = true })
vim.keymap.set('n', '<S-RightDrag>', '<LeftDrag>', { noremap = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip743)
***
# Title: Select Recently Pasted Text Easily
# Category: visual_mode
# Tags: text-selection, mapping, paste
---
Create a quick mapping to select text just pasted, which is useful for further manipulation like indenting or formatting

```vim
nnoremap gp `[v`]
```
```lua
vim.keymap.set('n', 'gp', '`[v`]', { desc = 'Select last pasted text' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip759)
***
