# Title: View registers
# Category: Registers
# Tags: registers, clipboard, view
---
Use `:registers` to show the contents of all registers.

```vim
:registers
```

**Source:** Community contributed
***
# Title: System clipboard
# Category: Registers
# Tags: clipboard, system, yank
---
Use `"+y` to yank to the system clipboard and `"+p` to paste from the system clipboard.

```vim
"+y  " yank to system clipboard
"+p  " paste from system clipboard
```

**Source:** Community contributed
***
# Title: Delete without affecting register
# Category: Registers
# Tags: delete, register, blackhole
---
Use `"_d` to delete text without affecting the default register (sends to blackhole register).

```vim
"_d  " delete to blackhole register
```

**Source:** Community contributed
***
# Title: Set register manually
# Category: Registers
# Tags: register, set, manual
---
Use `:let @a='text'` to manually set the contents of register a.

```vim
:let @a='hello world'  " set register a to 'hello world'
```

**Source:** Community contributed
***
# Title: Clear specific register
# Category: Registers
# Tags: register, clear, empty, macro
---
Use `q{register}q` to clear/empty a specific register by recording an empty macro.

```vim
qAq    " clear register 'A'
qaq    " clear register 'a'  
q1q    " clear register '1'
q:q    " clear command register
```

**Source:** Community contributed
***
# Title: Redirect Ex Command Output to Register
# Category: registers
# Tags: command-output, registers, ex-commands
---
Capture command output directly to a register for later use or pasting

```vim
:redir @a
:set all
:redir END
" now paste with "ap
```
```lua
-- Lua doesn't have direct :redir equivalent
-- Use vim.api.nvim_exec() instead
local output = vim.api.nvim_exec('set all', true)
vim.fn.setreg('a', output)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Capture_ex_command_output)
***
# Title: Smart Visual Mode Paste without Register Overwrite
# Category: registers
# Tags: visual-mode, registers, clipboard
---
A mapping that allows pasting over selected text without overwriting the current register, preserving the original copied text for multiple pastes

```vim
xnoremap <silent> p p:let @"=@0<CR>
```
```lua
vim.keymap.set('x', 'p', function()
  vim.fn.feedkeys('p', 'n')
  vim.fn.setreg('"', vim.fn.getreg('0'))
end, { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Change_visual_mode_paste_command_behaviour)
***
# Title: Cycle Through Vim Registers Easily
# Category: registers
# Tags: register-management, key-mapping, workflow
---
Create a mapping to easily swap and cycle through different registers, making register manipulation more convenient

```vim
" Cycle registers: unnamed, a, b
nnoremap <Leader>s :let @x=@" | let @"=@a | let @a=@b | let @b=@x<CR>
```
```lua
-- Cycle registers in Neovim
vim.keymap.set('n', '<Leader>s', function()
  local x = vim.fn.getreg('"')
  vim.fn.setreg('"', vim.fn.getreg('a'))
  vim.fn.setreg('a', vim.fn.getreg('b'))
  vim.fn.setreg('b', x)
end, { desc = 'Cycle through registers' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Comfortable_handling_of_registers)
***
# Title: Advanced Copy and Paste with Named Registers
# Category: registers
# Tags: copy, paste, registers, clipboard
---
Use named registers to store and recall multiple pieces of text across different operations

```vim
"ay  " copy text to register a
"by  " copy text to register b
"ap  " paste from register a after cursor
"bP  " paste from register b before cursor
```
```lua
-- Lua equivalents use vim.fn.setreg() and vim.fn.getreg()
-- Copy to register a
vim.fn.setreg('a', 'text to copy')

-- Paste from register a
vim.cmd('normal! "ap')  -- paste after cursor
vim.cmd('normal! "aP')  -- paste before cursor
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Copy,_cut_and_paste)
***
# Title: Reorder Lines Using Registers
# Category: registers
# Tags: line-manipulation, advanced-editing, registers
---
Efficiently reorder up to nine lines by using numbered registers and the dot command

```vim
" Delete lines in desired final order
" Then paste from numbered registers using dot command
"1P
........
```
```lua
-- Note: This technique relies on Vim's register mechanism
-- Equivalent in Lua would be to use vim.fn.setreg() and vim.fn.getreg()
-- The specific implementation would mirror the Vimscript approach
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Copy_multiple_lines/words_to_a_specified_position)
***
# Title: Quick Macro Recording and Playback
# Category: registers
# Tags: macro, recording, productivity
---
Simplifies macro recording by using 'q' register and mapping 'Q' to playback

```vim
nnoremap Q @q
```
```lua
vim.keymap.set('n', 'Q', '@q', { desc = 'Playback macro from q register' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Delete_to_the_end_of_the_line)
***
# Title: Paste from Clipboard with Precise Cursor Placement
# Category: registers
# Tags: clipboard, cursor-movement, advanced-paste
---
Paste from clipboard before cursor and set marks for the pasted text

```vim
"+P
```
```lua
vim.api.nvim_put(vim.fn.getreg('+'), 'c', true, true)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Did_you_know/2009)
***
# Title: Record, Edit, and Reuse Vim Macros
# Category: registers
# Tags: macros, productivity, automation
---
Efficiently record, edit, and replay complex editing sequences across multiple files or lines

```vim
" Record macro to register d
qd
" Perform editing commands
q

" Replay macro
@d

" Replay on multiple lines
:normal @q
```
```lua
-- Note: Macro recording is largely the same in Neovim
-- Record macro: qq (start recording to q register)
-- Stop recording: q
-- Replay macro: vim.fn.feedkeys('@q')

-- Replay macro on visual selection
vim.cmd('normal! gv:normal @q')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Edit_a_previously_recorded_macro)
***
# Title: Append or Modify Existing Macros
# Category: registers
# Tags: macros, editing-tricks
---
Easily extend an existing macro without re-recording the entire sequence

```vim
" Original macro in lowercase register
qa...q
" Append to macro using uppercase register
qA...q
```
```lua
-- Same approach works in Neovim
-- First macro: vim.fn.setreg('a', 'original_macro_commands')
-- Append to macro: vim.fn.setreg('A', 'additional_commands', 'a')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Edit_a_previously_recorded_macro)
***
# Title: Get Current Filename in Vim
# Category: registers
# Tags: filename, buffer, expansion
---
Multiple ways to extract and manipulate the current filename using registers and expand() function

```vim
" Get filename relative to current directory
:echo @%
" Get just the filename
:echo expand('%:t')
" Get full path
:echo expand('%:p')
" Get directory of current file
:echo expand('%:p:h')
```
```lua
-- Get filename relative to current directory
print(vim.fn.expand('%'))
-- Get just the filename
print(vim.fn.expand('%:t'))
-- Get full path
print(vim.fn.expand('%:p'))
-- Get directory of current file
print(vim.fn.expand('%:p:h'))
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Get_the_name_of_the_current_file)
***
# Title: Insert Register Content Across Multiple Lines
# Category: registers
# Tags: register-manipulation, multi-line-editing, clipboard
---
Insert contents of a register (like clipboard) across multiple lines in visual block mode

```vim
" In visual block mode:
" I Ctrl-R + - Insert clipboard content
" I Ctrl-R " - Insert unnamed register
```
```lua
-- Same approach works in Neovim
-- Use Ctrl-V to select block
-- I Ctrl-R + to insert from clipboard
-- I Ctrl-R " to insert from unnamed register
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Inserting_text_in_multiple_lines)
***
# Title: Advanced Text Manipulation with Registers
# Category: registers
# Tags: copy-paste, text-manipulation, buffers
---
Use named registers for more flexible text copying and pasting

```lua
-- Register manipulation
vim.keymap.set('n', 'y', 'y', { desc = 'Yank (copy) text' })
vim.keymap.set('n', 'p', 'p', { desc = 'Paste after cursor' })
vim.keymap.set('n', 'P', 'P', { desc = 'Paste before cursor' })
-- Named register example
vim.keymap.set('n', '"ay5dd', '"ay5dd', { desc = 'Delete 5 lines to register a' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Introduction_to_display_editing_using_vi)
***
# Title: Record and Replay Macros Efficiently
# Category: registers
# Tags: macro, automation, recording
---
Quickly record a sequence of commands to a register and replay them across multiple lines or the entire file

```vim
" Record macro to register d
qd
... commands ...
q

" Replay macro
@d
" Replay on multiple lines
:normal @d
```
```lua
-- Record macro to register d
-- Use vim.fn.feedkeys() to simulate recording
-- Replay macro
vim.cmd('normal @d')

-- Replay on visual selection
vim.cmd('normal! gv:normal @d<CR>')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Macros)
***
# Title: Append to Existing Macros
# Category: registers
# Tags: macro, editing, productivity
---
Easily extend an existing macro without re-recording the entire sequence

```vim
" Initial macro recording
qa
... commands ...
q

" Append to existing macro
qA
... additional commands ...
q
```
```lua
-- Note: In Neovim, you can still use vim command mode for macro recording
-- Use uppercase register letter to append to existing macro
-- For more advanced macro manipulation, consider using vim.fn.setreg()
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Macros)
***
# Title: Record and Replay Powerful Text Transformation Macros
# Category: registers
# Tags: macro-recording, text-transformation, automation
---
Quickly record complex text editing sequences that can be replayed across multiple lines or files

```vim
qd  # Start recording macro to register d
...[editing commands]...
q   # Stop recording
@d  # Replay macro
2@@ # Replay macro twice
```
```lua
-- Macro recording in Lua is same as Vim
-- Use vim.fn.feedkeys() to simulate macro recording if needed
vim.cmd('qd')  -- Start macro recording
-- Perform editing commands
vim.cmd('q')   -- Stop recording
vim.cmd('@d')  -- Replay macro
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Make_a_Macro)
***
# Title: Run Macro Across Visual Selection
# Category: registers
# Tags: macro-execution, bulk-editing, visual-mode
---
Execute a macro on every line in a visual selection, enabling rapid bulk transformations

```vim
:normal @q  # Run macro from register q on each selected line
```
```lua
-- Run macro on visual selection
vim.cmd('normal! @q')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Make_a_Macro)
***
# Title: Record and Execute Vim Macros Efficiently
# Category: registers
# Tags: macros, productivity, recording, automation
---
Learn to record, run, and manage Vim macros across multiple lines and registers

```vim
" Record macro to register d
qd
" Your complex commands here
q

" Execute macro
@d
" Repeat last macro
@@

" Run macro on visual selection
:normal @q
```
```lua
-- Recording macro to register d
-- Use normal mode mapping to simulate qd
vim.keymap.set('n', 'qd', 'qd', { desc = 'Start recording macro in d register' })

-- Execute macro
vim.keymap.set('n', '<leader>m', '@d', { desc = 'Execute macro from d register' })

-- Run macro on visual selection
vim.keymap.set('x', '<leader>m', ':normal @q<CR>', { desc = 'Run macro on visual selection' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mapping_for_quicker_access_to_macros)
***
# Title: Append Multiple Lines to a Register
# Category: registers
# Tags: text-manipulation, advanced-editing
---
Technique for collecting multiple lines into a single register by using uppercase register names

```vim
"add    " Delete first line to register a
"Add    " Append next line to register a
"ap     " Paste contents of register a
```
```lua
-- Manual register manipulation can be done in Lua via vim.fn.setreg()
-- Example of appending to a register
vim.fn.setreg('A', vim.fn.getline('.'), 'l')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Moving_lines_up_or_down)
***
# Title: Translate Null Characters in Vim Registers
# Category: registers
# Tags: debugging, register-manipulation, string-translation
---
Use strtrans() to visualize and understand how null characters are represented in Vim registers

```vim
" Translate register contents
:echo strtrans(@a)
```
```lua
-- Lua equivalent for translating register contents
print(vim.fn.strtrans(vim.fn.getreg('a')))
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Newlines_and_nulls_in_Vim_script)
***
# Title: Paste Registers in Command and Search Lines
# Category: registers
# Tags: command-line, search, registers
---
Quickly insert register contents into command or search lines using Ctrl-R, avoiding clipboard operations

```vim
" In command or search mode, press Ctrl-R then register name
" Example: Ctrl-R a to paste contents of register a
" Ctrl-R " to paste unnamed register
```
```lua
-- In Neovim, this works the same way in command and search modes
-- Use <C-r> followed by register name in command or search prompt
-- Example in Lua: No direct translation needed, built-in functionality
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Paste_registers_in_search_or_colon_commands_instead_of_using_the_clipboard)
***
# Title: Paste from Different Vim Registers Safely
# Category: registers
# Tags: clipboard, register-manipulation, paste
---
Safely paste contents from various Vim registers in different modes, with special focus on clipboard security

```vim
" Paste from clipboard register in normal mode
"*p

" Paste last search or command
"/p
":p

" Safely paste in insert mode
inoremap <C-R>+ <C-R><C-R>+
```
```lua
-- Paste from clipboard in normal mode
vim.keymap.set('n', '<leader>p', '"*p', { desc = 'Paste from clipboard' })

-- Safely paste in insert mode
vim.keymap.set('i', '<C-R>+', '<C-R><C-R>+', { desc = 'Safely paste from clipboard' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Pasting_registers)
***
# Title: Prevent Clipboard Hijacking in Vim
# Category: registers
# Tags: security, clipboard, insert-mode
---
Protect against potential malicious clipboard content that could execute unintended commands

```vim
" Prevent clipboard hijacking
inoremap <C-R>+ <C-R><C-R>+
" Alternative safe paste methods
inoremap <C-R>+ <C-R><C-O>+
```
```lua
-- Prevent clipboard hijacking
vim.keymap.set('i', '<C-R>+', '<C-R><C-R>+', { desc = 'Safe clipboard paste' })
-- Alternative safe paste method
vim.keymap.set('i', '<C-R>+', '<C-R><C-O>+', { desc = 'Alternative safe clipboard paste' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Pasting_registers)
***
# Title: Preload Vim Registers with Frequently Used Commands
# Category: registers
# Tags: command-macros, productivity, configuration
---
Preload registers with frequently used command sequences to quickly execute complex commands with a single keystroke

```vim
" Preload registers with common commands
let @m=":'a,'bs/"
let @s=":%!sort -u"

" Interesting recursive yank macro
let @y='yy@"'
```
```lua
-- Preload registers with common commands
vim.g.registers = {
  m = ":'a,'bs/",  -- Example find/replace between marks
  s = ":%!sort -u",  -- Sort unique lines
  y = 'yy@"'  -- Recursive yank macro
}

-- To use the preloaded register
-- Execute with @m, @s, etc.
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Preloading_registers)
***
# Title: Append to Macro Registers Safely
# Category: registers
# Tags: macro-recording, register-manipulation
---
Use uppercase register names to safely append to existing macros without overwriting previous content

```vim
" Append to 'q' register
qQ    " Start appending to register q
@q    " Execute existing macro
q     " Stop recording
```
```lua
-- Lua macro appending (still uses Vim commands)
-- vim.cmd('qQ')   " Start appending
-- vim.cmd('@q')   " Execute existing macro
-- vim.cmd('q')    " Stop recording
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Record_a_recursive_macro)
***
# Title: Create Recursive Macros for Bulk Text Manipulation
# Category: registers
# Tags: macro, text-processing, automation
---
Record a macro that calls itself to perform repetitive transformations across an entire file, allowing complex text editing without complex regex

```vim
" Record recursive macro steps
qqq   " Clear register q
qq    " Start recording
f2    " Find '2' character
D     " Delete rest of line
Fr    " Find last 'r'
p     " Paste deleted text
j     " Move to next line
@q    " Execute macro recursively
q     " Stop recording
```
```lua
-- Lua equivalent requires manual implementation
-- Use vim.fn.execute() for macro playback
-- Recommended to use :normal for similar tasks in Neovim
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Record_a_recursive_marco)
***
# Title: Edit and Modify Recorded Macros
# Category: registers
# Tags: macro-editing, register-manipulation
---
Multiple ways to edit and modify recorded macros using registers

```vim
qxq     # Clear register x
:let @x = ''  # Clear register x

# Edit macro by pasting into buffer
:new
"xp     # Paste macro
[edit]
0"xy$   # Yank modified macro back
```
```lua
-- Clear a register
vim.fn.setreg('x', '')

-- Edit macro programmatically
-- Create a new buffer
vim.cmd('new')

-- Paste macro content
vim.fn.setreg('"', vim.fn.getreg('x'))
vim.cmd('normal! p')

-- After editing, you can save back to register
vim.fn.setreg('x', vim.fn.getline(1))
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Recording_keys_for_repeated_jobs)
***
# Title: Recover Recently Deleted Text in Insert Mode
# Category: registers
# Tags: text-recovery, registers, insert-mode
---
Use the '.' register to recover text deleted by Ctrl-U or Ctrl-W

```vim
:let @a = @.
"aP
```
```lua
vim.fn.setreg('a', vim.fn.getreg('.'))
vim.api.nvim_paste(vim.fn.getreg('a'), true, -1)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Recover_from_accidental_Ctrl-U)
***
# Title: Recover Previous Deletes Using Numbered Registers
# Category: registers
# Tags: yank, delete, clipboard, recovery
---
Vim keeps previous deletes/yanks in numbered registers, allowing you to recover text even after accidentally overwriting the default register

```vim
" List all registers
:reg

" Paste from register 2
"2p  " Paste after cursor
"2P  " Paste before cursor
```
```lua
-- List all registers
vim.cmd('reg')

-- Paste from specific numbered register
vim.api.nvim_put(vim.fn.getreg('2'), '', true, true)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Remembering_previous_deletes/yanks)
***
# Title: Cycle Through Numbered Registers
# Category: registers
# Tags: navigation, text-recovery, undo
---
Quickly cycle through previous yanks/deletes using repeat and undo commands

```vim
"1p....  " Paste and cycle through registers
u.     " Undo last paste and paste next register
```
```lua
-- Note: Direct Lua equivalent requires more complex implementation
-- Recommended to use Vim commands or create a custom function
vim.cmd('"1p....')
vim.cmd('u.')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Remembering_previous_deletes/yanks)
***
# Title: Execute Macro Across Visual Block Selection
# Category: registers
# Tags: macros, visual-block, advanced-editing
---
Executes a macro stored in register 'a' across all lines in a visual block selection, enabling quick multi-line transformations

```vim
" make ` execute the contents of the a register across visual selection
vnoremap ` :normal @a<CR>
```
```lua
vim.keymap.set('v', '`', ':normal @a<CR>', { desc = 'Execute macro from register a on visual block lines' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Repeat_command_on_each_line_in_visual_block)
***
# Title: Paste Over Text Without Losing Register
# Category: registers
# Tags: paste, text-replacement, key-mapping
---
Create a mapping to paste over text while preserving the original yank register, preventing unwanted register overwrite

```vim
xnoremap <silent> p p:let @"=@0<CR>
```
```lua
vim.keymap.set('x', 'p', function()
  vim.cmd('normal! p')
  vim.fn.setreg('"', vim.fn.getreg('0'))
end, { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Replace_a_word_with_yanked_text)
***
# Title: Get Current File Name in Different Formats
# Category: registers
# Tags: file-operations, command-line, registers
---
Multiple ways to extract and display the current file's name, path, or components using expand() function and registers

```vim
:echo @%           " Relative file path
:echo expand('%:t') " Filename only
:echo expand('%:p') " Full file path
:echo expand('%:p:h') " Directory containing file
:echo expand('%:r')  " Filename without extension
```
```lua
-- Get current file details
print(vim.fn.expand('%'))      -- Relative file path
print(vim.fn.expand('%:t'))    -- Filename only
print(vim.fn.expand('%:p'))    -- Full file path
print(vim.fn.expand('%:p:h'))  -- Directory containing file
print(vim.fn.expand('%:r'))    -- Filename without extension
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip530)
***
# Title: Paste Text as Separate Line with Easy Mapping
# Category: registers
# Tags: pasting, register, key-mapping
---
Easily paste text from the default register as a separate line above or below the current line

```vim
nnoremap ,p :put "<CR>
nnoremap ,P :put! "<CR>
```
```lua
vim.keymap.set('n', ',p', ':put "<CR>', { desc = 'Paste below current line' })
vim.keymap.set('n', ',P', ':put! "<CR>', { desc = 'Paste above current line' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip586)
***
# Title: Easy Word Replacement Using Registers
# Category: registers
# Tags: editing, registers, clipboard
---
Efficiently replace words using Vim registers without losing the original copied content

```vim
" Remap visual mode paste to preserve original register
xnoremap <silent> p p:let @"=@0<CR>
```
```lua
-- Lua equivalent for preserving register during paste
vim.keymap.set('x', 'p', function()
  vim.fn.feedkeys('p', 'n')
  vim.fn.setreg('"', vim.fn.getreg('0'))
end, { noremap = true, silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip605)
***
