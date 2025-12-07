# Title: Global search and replace
# Category: Search
# Tags: replace, global, substitute
---
Use `:%s/old/new/g` to replace all occurrences of 'old' with 'new' in the entire file.

```vim
:%s/foo/bar/g  " replace all 'foo' with 'bar'
```

**Source:** Community contributed
***
# Title: Remove search highlighting
# Category: Search
# Tags: search, highlight, remove
---
Use `:nohl` to remove search highlighting after performing a search.

```vim
:nohl
```

**Source:** Community contributed
***
# Title: Search in selection
# Category: Search
# Tags: replace, selection, range
---
Use `:'<,'>s/old/new/g` to replace only in visual selection.

```vim
:'<,'>s/foo/bar/g  " replace in selection
```

**Source:** Community contributed
***
# Title: Search backward
# Category: Search
# Tags: search, backward, reverse
---
Use `?pattern` to search backward for a pattern. Press `n` to go to next match and `N` for previous.

```vim
?hello  " search backward for 'hello'
n       " next match (backward)
N       " previous match (forward)
```

**Source:** Community contributed
***
# Title: Advanced search and replace with regex
# Category: Search
# Tags: replace, regex, advanced
---
Use `:%s/\v(foo|bar)/baz/g` to replace either 'foo' or 'bar' with 'baz' using very magic mode.

```vim
:%s/\v(foo|bar)/baz/g  " replace foo or bar with baz
```

**Source:** Community contributed
***
# Title: Repeat last search in substitution
# Category: Search
# Tags: substitute, repeat, search
---
Use `:%s//replacement/g` to use the last search pattern in substitution command.

```vim
:%s//new_text/g  " replace last searched pattern with new_text
```

**Source:** Community contributed
***
# Title: Search word boundaries with very magic
# Category: Search
# Tags: search, regex, word, boundary, magic
---
Use `\v` for very magic mode to make regex more intuitive, or `\<word\>` for exact word boundaries.

```vim
/\v(hello|world)  " search for 'hello' or 'world' (very magic)
/\<function\>     " search for exact word 'function'
/\vd+             " search for one or more digits
```

**Source:** Community contributed
***
# Title: Multi-line search pattern
# Category: Search
# Tags: search, multiline, pattern, regex
---
Use `\_s` for whitespace including newlines, `\_.*` to match across lines in search patterns.

```vim
/function\_s*name    " function followed by whitespace/newlines
/start\_.*end        " match start to end across lines
```

**Source:** Community contributed
***
# Title: Search with offset
# Category: Search
# Tags: search, offset, cursor, position
---
Use `/pattern/+n` to position cursor n lines after match, or `/pattern/-n` for n lines before.

```vim
/function/+2     " position cursor 2 lines after 'function'
/end/-1          " position cursor 1 line before 'end'
```

**Source:** Community contributed
***
# Title: Search and replace in multiple files (vimgrep+cdo)
# Category: Search
# Tags: replace, regex, search, vimgrep, cdo
---
Suppose that you have a set of .html documents and you want to find all <a> tags that have some attribute in it, for example: `text-red`. You want to replace that attribute with `text-blue`. Do the following:
This will create a quickfix list made of lines that match the regular expression and open the file with the first matching line highlighted. After that you can execute the substitution:
Thanks to `c` flag you'll have a cnahce to approve every change. Note that `cfdo` would perform changes on matched FILES, while `cdo` works on matched lines. Also in substitution command use `s/`, not `%s/` because the first one is executed on the current line and the second one would process the whole doucment.

```vim
:vimgrep /<a [^>]*text-red[^>]*>/gj **/*.html

:cdo s/text-red/text-blue/gc
```

**Source:** Community contributed
***
# Title: Avoid escaping slashes in search and replace operations
# Category: Search
# Tags: search, replace, escaping, vimgrep, regex, separator
---


```vim
%s/http:\/\//fpt:\/\//gc
```

**Source:** Community contributed
***
# Title: Insert Newlines Around Patterns Flexibly
# Category: search_replace
# Tags: text-manipulation, search, substitution
---
Dynamically insert newlines before or after specific patterns in text, useful for formatting code or text

```vim
command! -bang -nargs=* -range LineBreakAt <line1>,<line2>call LineBreakAt('<bang>', <f-args>)

function! LineBreakAt(bang, ...) range
  let save_search = @/
  if empty(a:bang)
    let before = ''
    let after = '\ze.'
    let repl = '&\r'
  else
    let before = '.\zs'
    let after = ''
    let repl = '\r&'
  endif
  let pat_list = map(deepcopy(a:000), "escape(v:val, '/\\.*$^~[')")
  let find = empty(pat_list) ? @/ : join(pat_list, '\|')
  let find = before . '\%(' . find . '\)' . after
  execute a:firstline . ',' . a:lastline . 's/'. find . '/' . repl . '/ge'
  let @/ = save_search
endfunction
```
```lua
function LineBreakAt(bang, ...)
  local save_search = vim.fn.getreg('/')
  local before = bang and '.\\zs' or ''
  local after = bang and '' or '\\ze.'
  local repl = bang and '\\r&' or '&\\r'

  local pat_list = vim.tbl_map(function(val)
    return vim.fn.escape(val, '/\.*$^~[')
  end, {...})

  local find = #pat_list > 0 and table.concat(pat_list, '\\|') or save_search
  find = before .. '\\%(' .. find .. '\\)' .. after

  vim.cmd(string.format('%s,%ss/%s/%s/ge', 
    vim.fn.line('.'), vim.fn.line('.'), find, repl))

  vim.fn.setreg('/', save_search)
end

-- Usage: 
-- :lua LineBreakAt(false, '(', ')')
-- :lua LineBreakAt(true, 'function')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Add_a_newline_after_given_patterns)
***
# Title: Use Alternate Delimiters in Search/Replace
# Category: search_replace
# Tags: search, replace, delimiter
---
Use alternative delimiters in search and replace commands to simplify working with paths or complex patterns that contain slashes

```vim
:s#/usr/local/#/opt/#
```
```lua
-- Example of using alternative delimiter in Neovim
vim.cmd('s#/usr/local/#/opt/#')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Alternate_delimiters_for_the_replace_command)
***
# Title: Search Only Within Visually Selected Range
# Category: search_replace
# Tags: visual-mode, search, custom-mapping
---
Implement a custom search function that limits search results to a visually selected range, allowing targeted searching within specific code blocks or regions

```vim
function FindNextRegionWork()
  let l:flags = g:sdir == "f" ? "w" : "wb"
  call search(g:searchstr, l:flags)
  let l:srw = line(".")
  let l:scl = col(".")
  while l:srw != 0
    if (l:srw == g:sbr && l:scl >= g:sbc) || 
       (l:srw == g:ser && l:scl <= g:sec) || 
       (l:srw > g:sbr && l:srw < g:ser)
      break
    endif
    call search(g:searchstr, l:flags)
    let l:srw = line(".")
    let l:scl = col(".")
  endwhile
endfunction
```
```lua
function _G.find_next_region_work()
  local flags = vim.g.sdir == 'f' and 'w' or 'wb'
  vim.fn.search(vim.g.searchstr, flags)
  local srw = vim.fn.line('.')
  local scl = vim.fn.col('.')
  while srw ~= 0 do
    if (srw == vim.g.sbr and scl >= vim.g.sbc) or
       (srw == vim.g.ser and scl <= vim.g.sec) or
       (srw > vim.g.sbr and srw < vim.g.ser) then
      break
    end
    vim.fn.search(vim.g.searchstr, flags)
    srw = vim.fn.line('.')
    scl = vim.fn.col('.')
  end
end

-- Add keymappings
vim.keymap.set('n', '<Leader>/', function()
  vim.ui.input({prompt = 'Find what?: '}, function(input)
    if input then
      vim.g.searchstr = input
      vim.g.sbr = vim.fn.line("'<")
      vim.g.sbc = vim.fn.col("'<")
      vim.g.ser = vim.fn.line("'>")
      vim.g.sec = vim.fn.col("'>")
      _G.find_next_region_work()
    end
  end)
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Another_%22Search_Only_In_a_Visually_Selected_Range%22)
***
# Title: Block-wise Visual Substitution Without Plugin
# Category: search_replace
# Tags: substitution, visual-selection
---
Use \%V to limit substitutions to visual selection area

```vim
:%s/\%V{pattern}/{string}/g
```
```lua
-- Limit substitution to visual selection area
-- vim.cmd(':%s/\%V{pattern}/{string}/g')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Applying_substitutes_to_a_visual_block)
***
# Title: Quick Search for Word Under Cursor
# Category: search_replace
# Tags: search, navigation, cursor
---
Use * and # to search for the word under the cursor forward and backward

```vim
* searches forward
# searches backward
```
```lua
-- Built-in Vim behavior, no specific Lua conversion needed
-- Can use vim.fn.expand('<cword>') to get word under cursor programmatically
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Best_Tips)
***
# Title: CSV Column Search and Manipulation
# Category: search_replace
# Tags: csv, search, column-operations
---
Advanced searching within specific columns and ability to copy or delete columns in CSV files

```vim
" Search within a specific column
:SC n=str  " Search 'str' in nth column
:SC str    " Search in current column

" Copy a column
:CC n x     " Copy nth column to register x

" Delete a column
:DC n       " Delete nth column
```
```lua
-- Note: This would typically require a custom Lua function or plugin
-- Example skeleton for column operations
local function csv_search_column(column, search_term)
  -- Implement column-specific search logic
end

local function csv_copy_column(column, register)
  -- Implement column copy logic
end

local function csv_delete_column(column)
  -- Implement column deletion logic
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/CSV)
***
# Title: Convert C++ Comments to C Comments
# Category: search_replace
# Tags: text-processing, regex, comment-conversion
---
Quickly convert single-line C++ comments (//) to multi-line C comments (/* */), useful for MISRA compliance or code style standardization

```vim
:map <F5> %s,//\(.*\),/*\1 */,
```
```lua
-- Lua equivalent for converting C++ comments to C comments
vim.keymap.set('n', '<F5>', function()
  vim.cmd('%s,//\\(.*\\),/*\1 */,')
end, { desc = 'Convert C++ comments to C comments' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Change_C%2B%2B_comments_to_C_comments)
***
# Title: Convert HTML Tags to Lowercase
# Category: search_replace
# Tags: html, regex, text-transformation
---
Efficiently convert HTML tag names to lowercase using a powerful Vim regex substitution command

```vim
:%s/<\/\?\zs\(\a\+\)\ze[ >]/\L\1/g
```
```lua
vim.cmd('%s/<\/\?\zs\(\a\+\)\ze[ >]/\L\1/g')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Changing_all_HTML_tags_to_lowercase)
***
# Title: Convert HTML Attributes to Lowercase
# Category: search_replace
# Tags: html, regex, text-transformation
---
Convert HTML tag attributes to lowercase while preserving attribute values

```vim
:%s/\(<[^>]*\)\@<=\<\(\a*\)\ze=['"]*/\L\2/g
```
```lua
vim.cmd('%s/\(<[^>]*\)\@<=\<\(\a*\)\ze=['"]*/\L\2/g')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Changing_all_HTML_tags_to_lowercase)
***
# Title: Change Case Using Regex Substitutions
# Category: search_replace
# Tags: regex, text-transformation, substitution
---
Powerful way to change text case using Vim's regex substitution with case modifiers

```vim
" Lowercase entire file
:%s/.*/\L&/

" Uppercase words after HTML tags
:%s/<\(\w*\)/<\U\1/g
```
```lua
-- Lowercase entire file
vim.cmd(':%s/.*/\L&/')

-- Uppercase words after HTML tags
vim.cmd(':%s/<\(\w*\)/<\U\1/g')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Changing_case_with_regular_expressions)
***
# Title: Alternative Delimiters for Substitution
# Category: search_replace
# Tags: substitution, search, text-manipulation
---
Use alternative delimiters in substitution commands to handle paths with multiple slashes

```vim
" Substitute using different delimiters
:s,/abc/def/ghi/,,en
```
```lua
-- Lua equivalent (directly use vim command)
vim.cmd.substitute(',/abc/def/ghi/,,e')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Command_for_searching_expressions_(paths)_wich_include_backslashes.)
***
# Title: Operate on Search Matches in Vim 7.4+
# Category: search_replace
# Tags: search, text-objects, editing
---
Use `gn` to visually select and operate on search matches easily. Works great with operators like delete, change, etc.

```vim
" After searching, use gn to select and operate on matches
" dgn - delete next match
" cgn - change next match
" Repeat with .
```
```lua
-- Lua doesn't require special configuration for gn
-- It's a built-in Vim/Neovim feature
-- Example workflow:
-- /pattern  -- search for something
-- cgn       -- change next match
-- .         -- repeat change
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Copy_or_change_search_hit)
***
# Title: Copy Search Matches Efficiently
# Category: search_replace
# Tags: search, registers, clipboard
---
Quickly copy all text matching a search pattern to a register or clipboard, supporting multiline matches

```vim
function! CopyMatches(reg)
  let hits = []
  %s//\=len(add(hits, submatch(0))) ? submatch(0) : ''/gne
  let reg = empty(a:reg) ? '+' : a:reg
  execute 'let @'.reg.' = join(hits, "\n") . "\n"'
endfunction
command! -register CopyMatches call CopyMatches(<q-reg>)
```
```lua
function _G.copy_matches(reg)
  local hits = {}
  local view = vim.fn.winsaveview()
  vim.cmd('normal! ggyiG')
  vim.fn.winrestview(view)
  
  vim.fn.setreg(reg or '+', table.concat(hits, '\n') .. '\n')
end

vim.api.nvim_create_user_command('CopyMatches', function(opts)
  _G.copy_matches(opts.args)
end, { nargs = '?' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Copy_search_matches)
***
# Title: Copy Search Matches to Clipboard
# Category: search_replace
# Tags: search, clipboard, register
---
Efficiently copy search matches or matching lines to clipboard or registers, supporting multiline matches

```vim
function! CopyMatches(reg)
  let hits = []
  %s//\=len(add(hits, submatch(0))) ? submatch(0) : ''/gne
  let reg = empty(a:reg) ? '+' : a:reg
  execute 'let @'.reg.' = join(hits, "\n") . "\n"'
endfunction
command! -register CopyMatches call CopyMatches(<q-reg>)
```
```lua
function CopyMatches(reg)
  local hits = {}
  vim.cmd('keepjumps %substitute//\=luaeval("table.insert(hits, vim.fn.submatch(0)) or vim.fn.submatch(0)")/ne')
  local register = reg == '' and '+' or reg
  vim.fn.setreg(register, table.concat(hits, '\n') .. '\n')
end

vim.api.nvim_create_user_command('CopyMatches', function(opts)
  CopyMatches(opts.args)
end, { nargs = '?' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Copy_the_search_results_into_clipboard)
***
# Title: Delete Lines Containing Search Matches
# Category: search_replace
# Tags: search, deletion, filtering
---
Safely delete lines containing search matches, including support for multiline patterns

```vim
function! DeleteLines(pattern) range
  let delid = '<!DELETE!LINE!ID!>'
  if search(delid, 'cnw') > 0
    echo 'Error: buffer contains pattern used to delete lines'
    return
  endif
  let pattern = empty(a:pattern) ? @/ : a:pattern
  let sub = a:firstline . ',' . a:lastline . 's/' . escape(pattern, '/')
  let rep = '/\=delid . (submatch(0) =~ "\n$" ? "\r" : "")/e'
  execute sub . rep . (&gdefault ? '' : 'g')
  execute 'g/\C' . delid . '/' . 'd'
endfunction
command! -nargs=? -range=% DeleteLines k'|<line1>,<line2>call DeleteLines(<q-args>)
```
```lua
function DeleteLines(pattern, line1, line2)
  local delid = '<!DELETE!LINE!ID!>'
  if vim.fn.search(delid, 'cnw') > 0 then
    print('Error: buffer contains pattern used to delete lines')
    return
  end
  
  local search_pattern = pattern == '' and vim.fn.getreg('/') or pattern
  local cmd = string.format('%d,%ds/%s/%s/e%s', 
    line1, line2, 
    vim.fn.escape(search_pattern, '/'), 
    delid .. (string.match(vim.fn.submatch(0), '\n$') and '\r' or ''), 
    vim.o.gdefault and '' or 'g')
  
  vim.cmd(cmd)
  vim.cmd('global/\C' .. delid .. '/delete')
end

vim.api.nvim_create_user_command('DeleteLines', function(opts)
  DeleteLines(opts.args, opts.line1, opts.line2)
end, { nargs = '?', range = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Copy_the_search_results_into_clipboard)
***
# Title: Convert Decimal Encoded Characters
# Category: search_replace
# Tags: text-processing, character-encoding, substitution
---
Quickly convert decimal-encoded characters (like \nnn or &#nnn;) to their actual character representation in text

```vim
:%s/\\\([0-9]*\)/\=nr2char(submatch(1))/g
:%s/&#\([0-9]*\);/\=nr2char(submatch(1))/g
```
```lua
vim.cmd(':%s/\\\([0-9]*\)/\=nr2char(submatch(1))/g')
vim.cmd(':%s/&#\([0-9]*\);/\=nr2char(submatch(1))/g')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Correcting_accented_characters)
***
# Title: Count Pattern Matches in Buffer
# Category: search_replace
# Tags: search, count, pattern-matching
---
Quickly count the number of occurrences of a pattern in the current buffer using substitute command with 'n' flag

```vim
:%s/pattern//gn  " Count all matches
:%s/pattern//n   " Count lines with matches
```
```lua
-- Use ex command from Lua
vim.cmd(':%s/pattern//gn')  -- Count all matches
vim.cmd(':%s/pattern//n')   -- Count lines with matches
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Count_number_of_matches_of_a_pattern)
***
# Title: Quick Count of Word Under Cursor
# Category: search_replace
# Tags: search, cursor-word, mapping
---
Create a quick mapping to count occurrences of the word under the cursor

```vim
map ,* *<C-O>:%s///gn<CR>
```
```lua
vim.keymap.set('n', ',*', '*<C-O>:%s///gn<CR>', { desc = 'Count word occurrences' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Count_number_of_matches_of_a_pattern)
***
# Title: CSV Search Within Specific Column
# Category: search_replace
# Tags: csv, search, data-processing
---
Search for a specific value within a designated column in a CSV file

```vim
" Search within a specific column
" :SC 2=john  " search for john in the 2nd column
" :SC john    " search in currently highlighted column
```
```lua
-- Note: Full implementation would require a custom Lua function
-- This is a conceptual representation
vim.api.nvim_create_user_command('SC', function(opts)
  local args = opts.args
  local column, search_term
  
  if args:match('=%w+') then
    column, search_term = args:match('(%d+)=(.+)')
  else
    search_term = args
  end
  
  -- Implement column-specific search logic
  print(string.format('Searching for %s in column %s', search_term, column or 'current'))
end, { nargs = '+' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Csv)
***
# Title: Advanced Pattern Matching with Global Command
# Category: search_replace
# Tags: regex, text-filtering, pattern-matching
---
Use \| (or) to filter lines based on multiple patterns, keeping only specific matches

```vim
" Keep only lines with error, warn, or fail
:v/error\|warn\|fail/d
```
```lua
-- Keep only lines with error, warn, or fail
vim.cmd('v/error\|warn\|fail/d')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Delete_all_lines_containing_a_pattern)
***
# Title: Search and Find Lines Longer Than 80 Characters
# Category: search_replace
# Tags: search, text-analysis, regex
---
Quickly locate lines that exceed 80 characters in length, useful for code style checks

```vim
/\%>80v.\+
```
```lua
vim.fn.search('\%>80v.\+')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Did_you_know/2009)
***
# Title: Convenient Search and Highlight Clearing
# Category: search_replace
# Tags: key-mapping, search, highlight
---
Map Ctrl-L to clear search highlighting, making it easy to temporarily remove highlight after searching

```vim
" Clear search highlighting with Ctrl-L
nnoremap <C-L> :nohl<CR><C-L>
```
```lua
-- Clear search highlighting
vim.keymap.set('n', '<C-L>', ':nohl<CR><C-L>', { noremap = true, silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Example_vimrc)
***
# Title: Swap Adjacent Words with Regex
# Category: search_replace
# Tags: regex, text-manipulation, advanced-editing
---
Use a sophisticated regex pattern to swap adjacent words, including handling line breaks and preserving surrounding characters

```vim
" Swap next word
s/\v(<\k*%#\k*>)(\_.\.{-})(<\k+>)/\3\2\1/

" Swap previous word
s/\v(<\k+>)(.{-})(<\k*%#\k*>)/\3\2\1/
```
```lua
-- Swap next word with cursor position
vim.cmd('s/\v(<\k*%#\k*>)(\_.\.{-})(<\k+>)/\3\2\1/')

-- Swap previous word with cursor position
vim.cmd('s/\v(<\k+>)(.{-})(<\k*%#\k*>)/\3\2\1/')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Exchanging/swapping_adjacent_words)
***
# Title: Incremental Search with Live Preview
# Category: search_replace
# Tags: search, ui, productivity
---
Enable live search preview that moves cursor while typing search pattern, helping visualize matches in real-time

```vim
set incsearch
```
```lua
vim.opt.incsearch = true
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Find)
***
# Title: Advanced Search and Replace with Confirmation
# Category: search_replace
# Tags: search, substitution, global-command
---
Perform global search and replace with interactive confirmation across entire file

```vim
:%s/foo/bar/gc
```
```lua
vim.cmd('%s/foo/bar/gc')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Find_and_Replace)
***
# Title: Case-Sensitive and Insensitive Search Replace
# Category: search_replace
# Tags: search, replace, case-sensitivity
---
Control case sensitivity during search and replace operations

```vim
:%s/foo/bar/gci   # Case insensitive
:%s/foo/bar/gcI   # Case sensitive
```
```lua
vim.cmd(':%s/foo/bar/gci')    -- Case insensitive
vim.cmd(':%s/foo/bar/gcI')    -- Case sensitive
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Find_and_replace)
***
# Title: Precise Word Replacement
# Category: search_replace
# Tags: search, replace, word-boundary
---
Replace only whole word matches to prevent partial word replacements

```vim
:%s/\<foo\>/bar/gc
```
```lua
vim.cmd(':%s/\<foo\>/bar/gc')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Find_and_replace)
***
# Title: Speed Up Recursive Searches
# Category: search_replace
# Tags: performance, search, optimization
---
Use noautocmd to significantly speed up recursive file searches by disabling autocommands

```vim
:noautocmd vimgrep /{pattern}/[flags] {file(s)}
```
```lua
vim.cmd('noautocmd vimgrep /{pattern}/[flags] {file(s)}')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Find_in_files_recursively)
***
# Title: Recursive File Search with Vim
# Category: search_replace
# Tags: file-search, grep, recursive-search
---
Search recursively through files using `**` wildcard, which enables searching in parent and subdirectories

```vim
:vimgrep /dostuff()/j ../**/*.c
```
```lua
-- Lua equivalent (using vim.fn.execute)
vim.fn.execute('vimgrep /dostuff()/j ../**/*.c')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Find_in_files_within_Vim)
***
# Title: Find and Remove Duplicate Words
# Category: search_replace
# Tags: regex, text-cleanup, pattern-matching
---
Find and identify accidentally duplicated words in text

```vim
" Find duplicated words
/\(\<\w\+\>\)\s*\<\1\>
```
```lua
-- Find duplicated words
vim.fn.search('\(\<\w\+\>\)\s*\<\1\>')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Find_two_words_in_either_order)
***
# Title: Advanced Search with Case Sensitivity
# Category: search_replace
# Tags: search, case-sensitivity, configuration
---
Configure intelligent case-sensitive searching that adapts to your input pattern

```vim
set ignorecase
set smartcase

" Force case sensitivity per search
" /the\c (always case-insensitive)
" /the\C (always case-sensitive)
```
```lua
vim.opt.ignorecase = true
vim.opt.smartcase = true

-- Note: \c and \C modifiers work the same in Lua search
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Findlast_occurrence_of_an_item)
***
# Title: Advanced Word Search Mappings
# Category: search_replace
# Tags: search, key-mapping, word-navigation
---
Custom mappings for word search that respect smartcase behavior

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

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Findlast_occurrence_of_an_item)
***
# Title: Smart Case Sensitivity in Search
# Category: search_replace
# Tags: search, case-sensitivity, configuration
---
Automatically detect whether to ignore case during searches based on query

```vim
set smartcase
```
```lua
vim.opt.smartcase = true
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/From_Vim_Help)
***
# Title: Smart Case-Sensitive Search
# Category: search_replace
# Tags: search, case-sensitivity, intelligent-search
---
Automatically detect case sensitivity in searches for more flexible searching

```vim
set smartcase
```
```lua
vim.opt.smartcase = true
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/From_Vim_Help/2008)
***
# Title: Remove Duplicate Lines Efficiently
# Category: search_replace
# Tags: text-processing, deduplication
---
Remove consecutive duplicate lines from a file using global command or unique filter

```vim
# Remove duplicate consecutive lines
:g/^\(.*\)\(\r\?\n\1\)\+$/d
# Alternative method using uniq
:%!uniq
```
```lua
-- Remove duplicate consecutive lines
vim.cmd('g/^\(.*\)\(\r\?\n\1\)\+$/d')
-- Alternative method using uniq filter
vim.cmd('%!uniq')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/G)
***
# Title: Compress Multiple Blank Lines
# Category: search_replace
# Tags: text-cleaning, whitespace
---
Reduce multiple consecutive blank lines to a single blank line

```vim
# Collapse multiple blank lines
:v/./,/./-j
# Alternative substitution method
:%s/^$\n^$//g
```
```lua
-- Collapse multiple blank lines
vim.cmd('v/./,/./-j')
-- Alternative substitution method
vim.cmd('%s/^$\n^$//g')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/G)
***
# Title: Flexible Word Search Under Cursor
# Category: search_replace
# Tags: searching, text-objects, pattern-matching
---
Perform more flexible searches for words under the cursor, including partial matches

```vim
" g* - search for word (including partial matches)
" g# - search backwards for word
```
```lua
-- These default Vim search commands work in Neovim
-- Useful for finding related words or partial matches
-- Can be enhanced with telescope or other search plugins
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Go_to_definition_using_g)
***
# Title: Hex/Decimal Conversion Across Text
# Category: search_replace
# Tags: number-conversion, text-manipulation, search-replace
---
User commands to convert decimal and hexadecimal numbers across text ranges, supporting visual selections

```vim
command! -nargs=? -range Dec2hex call s:Dec2hex(<line1>, <line2>, '<args>')
function! s:Dec2hex(line1, line2, arg) range
  if empty(a:arg)
    let cmd = 's/\<\d\+\>/\=printf("0x%x",submatch(0)+0)/g'
    execute a:line1 . ',' . a:line2 . cmd
  else
    echo printf('%x', a:arg + 0)
  endif
endfunction
```
```lua
vim.api.nvim_create_user_command('Dec2hex', function(opts)
  local line1, line2 = opts.line1, opts.line2
  local arg = opts.args
  
  if arg == '' then
    local cmd = 's/\d\+/\=printf("0x%x", submatch(0) + 0)/g'
    vim.cmd(line1 .. ',' .. line2 .. cmd)
  else
    print(string.format('%x', tonumber(arg)))
  end
end, { nargs = '?', range = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Hex_or_unhex_strings)
***
# Title: Toggle Search Highlighting Easily
# Category: search_replace
# Tags: search, highlight, key-mapping
---
Add a quick way to toggle search highlighting and clear messages

```vim
" Press Space to turn off highlighting and clear messages
nnoremap <silent> <Space> :nohlsearch<Bar>:echo<CR>
```
```lua
vim.keymap.set('n', '<Space>', function()
  vim.cmd.nohlsearch()
  vim.cmd.echo()
end, { silent = true, desc = 'Clear search highlighting' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Highlight_all_search_pattern_matches)
***
# Title: Highlight Current Word Without Moving
# Category: search_replace
# Tags: search, highlight, word-selection
---
Highlight all occurrences of the current word without jumping to next match

```vim
nnoremap <F8> :let @/='\<<C-R>=expand("<cword>")<CR>\>'<CR>:set hls<CR>
```
```lua
vim.keymap.set('n', '<F8>', function()
  local cword = vim.fn.expand('<cword>')
  vim.fn.setreg('/', '\<' .. cword .. '\>')
  vim.opt.hlsearch = true
end, { desc = 'Highlight current word' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Highlight_all_search_pattern_matches)
***
# Title: Toggle Highlighting for Current Word
# Category: search_replace
# Tags: search, highlight, toggle
---
Toggle highlighting on and off for the current word under cursor

```vim
let g:highlighting = 0
function! Highlighting()
  if g:highlighting == 1 && @/ =~ '^\<'.expand('<cword>').'\>$'
    let g:highlighting = 0
    return ":silent nohlsearch\<CR>"
  endif
  let @/ = '\<'.expand('<cword>').'\'>
  let g:highlighting = 1
  return ":silent set hlsearch\<CR>"
endfunction
nnoremap <silent> <expr> <CR> Highlighting()
```
```lua
vim.g.highlighting = false

local function toggle_highlighting()
  local cword = vim.fn.expand('<cword>')
  local current_search = vim.fn.getreg('/')
  
  if vim.g.highlighting and current_search:match('^\<' .. cword .. '\>$') then
    vim.g.highlighting = false
    vim.cmd.nohlsearch()
  else
    vim.fn.setreg('/', '\<' .. cword .. '\>')
    vim.g.highlighting = true
    vim.opt.hlsearch = true
  end
end

vim.keymap.set('n', '<CR>', toggle_highlighting, { silent = true, desc = 'Toggle word highlighting' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Highlight_all_search_pattern_matches)
***
# Title: Advanced Word Highlight Search Navigation
# Category: search_replace
# Tags: search, navigation, highlight
---
Navigate between highlighted words with custom forward and backward search commands

```vim
" Search next/previous highlighted word
map <leader>f :call FindNextHighlight()<CR>
map <leader>F :call FindPrevHighlight()<CR>
```
```lua
vim.keymap.set('n', '<leader>f', function()
  -- Find next highlighted word
end, { desc = 'Find next highlighted word' })

vim.keymap.set('n', '<leader>F', function()
  -- Find previous highlighted word
end, { desc = 'Find previous highlighted word' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Highlight_multiple_words)
***
# Title: Highlight Only Current Search Result
# Category: search_replace
# Tags: search, highlight, navigation
---
Customize search highlighting to focus only on the current match instead of all matches

```vim
set nohlsearch

" highlight only current result of forward search when pressing n
:nnoremap <silent> <nowait> n <Esc>gn
:vnoremap <silent> <nowait> n <Esc>gn

" highlight the entire word of <cword> forward search result with *
:nnoremap <silent> <nowait> * <Esc>*gN
:vnoremap <silent> <nowait> * <Esc>*gN
```
```lua
-- Disable default highlight search
vim.opt.hlsearch = false

-- Highlight only current search result
vim.keymap.set('n', 'n', 'gn', { silent = true })
vim.keymap.set('v', 'n', 'gn', { silent = true })

vim.keymap.set('n', '*', '*gN', { silent = true })
vim.keymap.set('v', '*', '*gN', { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Highlight_only_the_current_search_result)
***
# Title: Quick Text Replacement Using Command Line
# Category: search_replace
# Tags: substitution, text-editing, search
---
Efficiently replace long strings by inserting text from buffer into substitute command

```vim
" 1. Start substitute command
" 2. Highlight text
" 3. Use Ctrl-R Ctrl-W to insert current word
```
```lua
-- Example of inserting current word in substitute command
vim.keymap.set('n', '<leader>s', function()
  local word = vim.fn.expand('<cword>')
  vim.api.nvim_feedkeys(':%s/' .. word .. '//g', 'n', true)
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/How_to_insert_the_contents_of_a_buffer_into_the_command_line)
***
# Title: Quick Multi-Line Text Substitution
# Category: search_replace
# Tags: text-manipulation, substitution, global-edit
---
Use substitute commands to insert or modify text across multiple lines

```vim
":s/^/new text /  " Insert at line start
":s/$/new text/  " Append at line end
":s/old/new/g  " Replace all occurrences
```
```lua
-- Similar substitution can be done in Neovim
-- Can use vim.cmd for Ex commands
vim.cmd('s/^/new text /')  -- Insert at start
vim.cmd('s/$/new text/')  -- Append at end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Inserting_text_in_multiple_lines)
***
# Title: Replace Word Under Cursor Quickly
# Category: search_replace
# Tags: cursor-word, substitution, refactoring
---
Quickly replace all instances of the word under the cursor in the entire buffer

```vim
:map <S-F4> :%s/<C-r><C-w>//gc<Left><Left><Left>
```
```lua
vim.keymap.set('n', '<S-F4>', ':%s/<C-r><C-w>//gc<Left><Left><Left>', { desc = 'Replace word under cursor globally' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Keystroke_Saving_Substituting_and_Searching)
***
# Title: Highlight Search Pattern in Line Listing
# Category: search_replace
# Tags: search, highlighting, custom-command
---
Create a custom command to print lines matching a search pattern with the match highlighted

```vim
" Custom command to print lines with search pattern highlighted
command! -nargs=? -range -bar PP :call PrintWithSearchHighlighted(<line1>,<line2>,<q-args>)
function! PrintWithSearchHighlighted(line1,line2,arg)
  let line=a:line1
  while line <= a:line2
    echo ""
    if a:arg =~ "#"
      echohl LineNr
      echo strpart(" ",0,7-strlen(line)).line."\t"
      echohl None
    endif
    let l=getline(line)
    let index=0
    while 1
      let b=match(l,@/,index)
      if b==-1 |
        echon strpart(l,index)
        break
      endif
      let e=matchend(l,@/,index) |
      echon strpart(l,index,b-index)
      echohl Search
      echon strpart(l,b,e-b)
      echohl None
      let index = e
    endw
    let line=line+1
  endw
endfunction
```
```lua
-- Lua equivalent for highlighting search pattern in line listing
function _G.print_with_search_highlighted(line1, line2, arg)
  for line = line1, line2 do
    local l = vim.fn.getline(line)
    local index = 1
    local output = {}

    -- Print line number if # arg is provided
    if arg and arg:find("#") then
      print(string.format("%6d\t", line))
    end

    -- Highlight matching patterns
    while true do
      local start, finish = l:find(vim.fn.getreg("/"), index)
      if not start then
        table.insert(output, l:sub(index))
        break
      end

      -- Add text before match
      table.insert(output, l:sub(index, start-1))
      
      -- Add highlighted match
      table.insert(output, {vim.fn.matchstr(l, vim.fn.getreg("/"), index), "Search"})
      
      index = finish + 1
    end

    -- Print with highlighting
    vim.api.nvim_echo(output, false, {})
    print("") -- Add newline between results
  end
end

-- Create command
vim.api.nvim_create_user_command('PP', function(opts)
  _G.print_with_search_highlighted(opts.line1, opts.line2, opts.args)
end, { nargs = '?', range = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/List_lines_with_current_search_pattern_highlighted)
***
# Title: Flexible Keyword Search and Jump
# Category: search_replace
# Tags: search, keyword-navigation, prompt
---
Interactively search for keywords across files and jump to specific occurrences

```vim
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

nnoremap <Leader>p :call <SID>JumpPrompt()<CR>
```
```lua
local function jump_prompt()
  local keyword = vim.fn.input('Keyword to find: ')
  if #keyword > 0 then
    vim.cmd('ilist! ' .. keyword)
    local nr = vim.fn.input('Which one: ')
    if nr:match('^%d+$') then
      vim.cmd('ijump! ' .. nr .. keyword)
    end
  end
end

vim.keymap.set('n', '<Leader>p', jump_prompt, { desc = 'Prompt for keyword and jump' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/List_lines_with_keyword_and_prompt_for_jump)
***
# Title: Create Outline Using Vimgrep
# Category: search_replace
# Tags: search, navigation, outline
---
Quick way to generate an outline of a file using vimgrep, especially useful for files with fold markers

```vim
:vimgrep /{{{/j %
:copen
```
```lua
vim.cmd('vimgrep /{{{/j %')
vim.cmd('copen')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/List_of_Scripts_for_Outlining)
***
# Title: Dynamic Number Substitution
# Category: search_replace
# Tags: substitution, search-replace, incremental-numbering
---
Replace text with incrementing numbers using a custom function

```vim
function Inc(...)
  let result = g:i
  let g:i += a:0 > 0 ? a:1 : 1
  return result
endfunction

" Replace 'abc' with 'xyz_N'
:let i = 1 | %s/abc/\='xyz_' . Inc()/g
```
```lua
-- Lua equivalent
local i = 1
vim.cmd(':%s/abc/xyz_' .. i .. '/g')
-- Note: More complex incremental logic would require custom Lua function
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Making_a_list)
***
# Title: Cross-Buffer Text Replacement via Substitute
# Category: search_replace
# Tags: search, global-replace, registers
---
Replace all instances of last searched text with last yanked text across entire buffer

```vim
:%s//\=@"/g
```
```lua
vim.cmd('%%s//\\=@"/g')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Mappings_and_commands_for_visual_mode)
***
# Title: Exclude Lines Containing Specific Pattern
# Category: search_replace
# Tags: search, filtering, regex
---
Use :v command to filter out lines matching a pattern, useful for log file analysis or text processing

```vim
:v/Warning/p

:sav junk.log
:v/warning/d
```
```lua
-- Filter out lines not matching a pattern
-- Print lines not containing 'Warning'
vim.cmd('v/Warning/p')

-- Save filtered version of file
vim.cmd('sav junk.log')
vim.cmd('v/warning/d')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Match_every_word_except_foo)
***
# Title: Advanced Negative Lookahead Searches
# Category: search_replace
# Tags: regex, advanced-search, pattern-matching
---
Use regex with negative lookahead to find words or lines excluding specific patterns

```vim
/\<\(foo\>\)\@!\k\+\>

/\(foo.*\)\@<!bar
```
```lua
-- Find words excluding 'foo'
vim.fn.search('\<\(foo\>\)\@!\k\+\>', 'n')

-- Find 'bar' without preceding 'foo'
vim.fn.search('\(foo.*\)\@<!bar', 'n')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Match_every_word_except_foo)
***
# Title: Comment Lines Matching a Pattern
# Category: search_replace
# Tags: pattern-matching, line-editing, search-and-replace
---
Modify lines matching a specific pattern by adding a comment character or transforming text across multiple lines

```vim
:'a,.g/foo/normal I*
```
```lua
-- Lua equivalent for commenting lines matching 'foo'
vim.cmd('g/foo/normal I*')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Modifying_a_line_and_all_subsequent_lines_matching_a_pattern)
***
# Title: Dynamic Highlight Search and Navigation
# Category: search_replace
# Tags: search, navigation, highlight
---
Add custom search commands to find next/previous highlighted words across the buffer, with flexible navigation options

```vim
" Search next/previous highlighted words
map <leader>f :call FindNextHighlight()<CR>
map <leader>F :call FindPrevHighlight()<CR>
```
```lua
vim.keymap.set('n', '<leader>f', function()
  -- Find next highlighted word
end, { desc = 'Find next highlighted word' })

vim.keymap.set('n', '<leader>F', function()
  -- Find previous highlighted word
end, { desc = 'Find previous highlighted word' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Multiple_Hilighted_Search)
***
# Title: Use Perl-Style Regex in Vim Substitutions
# Category: search_replace
# Tags: regex, substitution, advanced-search
---
Leverage Perl-compatible regular expressions for more powerful text substitutions using external Perl processing

```vim
" Define a custom Perl substitution command
function s:Substitute(line1, line2, sstring)
  let l:lines=getline(a:line1, a:line2)
  let l:sysresult=system("perl -e 'use utf8;' -e '#line 1 ""perl substitution""' -pe ".shellescape("s".escape(a:sstring,"%!").";"), l:lines)
  if v:shell_error
    echo l:sysresult
    return
  endif
  let l:result=split(l:sysresult, "\n", 1)
  execute a:line1.",".a:line2." normal ""_dd"
  call append(a:line1-1, l:result)
  call cursor(a:line1, 1)
endfunction

command -range -nargs=1 S call s:Substitute(<line1>, <line2>, <q-args>)
```
```lua
-- Lua equivalent of Perl substitution function
local function perl_substitute(line1, line2, sstring)
  -- Get lines from the specified range
  local lines = vim.api.nvim_buf_get_lines(0, line1-1, line2, false)
  
  -- Prepare Perl command
  local cmd = string.format("perl -e 'use utf8;' -e '#line 1 "perl substitution"' -pe 's%s;'", sstring)
  
  -- Execute Perl command
  local result = vim.fn.system(cmd, lines)
  
  -- Check for shell errors
  if vim.v.shell_error ~= 0 then
    print(result)
    return
  end
  
  -- Split and replace lines
  local new_lines = vim.split(result, "\n", {plain=true})
  vim.api.nvim_buf_set_lines(0, line1-1, line2, false, new_lines)
end

-- Create a command for Perl substitution
vim.api.nvim_create_user_command('S', function(opts)
  perl_substitute(opts.line1, opts.line2, opts.args)
end, {range = true, nargs = 1})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Perl_compatible_regular_expressions)
***
# Title: Use Very-Magic Regex Mode
# Category: search_replace
# Tags: regex, search, advanced-patterns
---
Enable Perl-like regex behavior with \v, making regular expressions more intuitive and less escape-heavy

```vim
" Use very-magic mode for more natural regex
nnoremap / /\v
nnoremap ,/ /
```
```lua
-- Set up very-magic mode mapping
vim.keymap.set('n', '/', '/\v', { desc = 'Search with very-magic regex' })
vim.keymap.set('n', ',/', '/', { desc = 'Normal search' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Perl_compatible_regular_expressions)
***
# Title: Global Command for Powerful Text Manipulation
# Category: search_replace
# Tags: ex-commands, global-command, text-processing
---
Use :g to perform complex operations on lines matching a pattern, such as deleting, copying, or modifying lines globally

```vim
" Delete all lines containing 'pattern'
:g/pattern/d

" Delete all lines NOT containing 'pattern'
:g!/pattern/d

" Double space the entire file
:g/^/pu ="\n"
```
```lua
-- Lua equivalents require using vim.cmd for Ex commands
-- Delete lines containing pattern
vim.cmd('g/pattern/d')

-- Delete lines NOT containing pattern
vim.cmd('g!/pattern/d')

-- Double space file
vim.cmd('g/^/pu ="\n"')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Power_of)
***
# Title: Perform Operation on Matching Lines
# Category: search_replace
# Tags: macro, global-command, text-processing
---
Run a macro on all lines matching a specific pattern

```vim
" Run macro 'q' on all lines matching 'pattern'
:g/pattern/normal @q
```
```lua
-- Run macro on matching lines
-- Note: Requires recording macro first
vim.cmd('g/pattern/normal @q')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Power_of)
***
# Title: Replace Spaces with Tabs Globally
# Category: search_replace
# Tags: whitespace, text-manipulation, global-replace
---
Replace all spaces with tabs, respecting current tabstop width

```vim
:%s/ /\t/g
```
```lua
vim.cmd('%s/ /\t/g')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Preexisting_code_indentation)
***
# Title: Quick HTML Attribute Quoting
# Category: search_replace
# Tags: html, regex, text-transformation
---
Automatically add quotes to unquoted HTML attributes using a regex search and replace

```vim
map <F9> :%s/\([^&^?]\)\(\<[[:alnum:]-]\{-}\)=\([[:alnum:]-#%]\+\)/\1\2="\3"/g<CR>
```
```lua
vim.keymap.set('n', '<F9>', ':%s/\([^&^?]\)\(\<[[:alnum:]-]\{-}\)=\([[:alnum:]-#%]\+\)/\1\2="\3"/g<CR>', { desc = 'Quote unquoted HTML attributes' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Quote_unquoted_HTML_attributes)
***
# Title: Abbreviated HTML Attribute Quoting
# Category: search_replace
# Tags: html, abbreviation, text-transformation
---
Create a command-line abbreviation for quoting HTML attributes with confirmation

```vim
cabbrev reg1 %s/=\([^"][^> ]\{0,40\}\)/="\1"/gc
```
```lua
vim.cmd('cabbrev reg1 %s/=\([^"][^> ]\{0,40\}\)/="\1"/gc')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Quote_unquoted_HTML_attributes)
***
# Title: Advanced Range Selection Techniques
# Category: search_replace
# Tags: visual-mode, marks, pattern-matching
---
Use visual selection, marks, and search patterns to define flexible text editing ranges

```vim
" Select paragraph and substitute
vip:s/old/new/g

" Using marks for range selection
ma  " Mark start of range
mb  " Mark end of range
:'a,'bs/old/new/g  " Substitute between marks
```
```lua
-- Similar approaches in Neovim
-- Visual paragraph selection and substitution
vim.cmd('normal vips/old/new/g')

-- Using marks for range selection
vim.cmd('ma')   -- Mark start of range
vim.cmd('mb')   -- Mark end of range
vim.cmd("'a,'bs/old/new/g")  -- Substitute between marks
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Ranges)
***
# Title: Quickly Filter and List Search Matches
# Category: search_replace
# Tags: search, filtering, command-line
---
Create a custom command to filter and display lines matching a search pattern in a new buffer

```vim
command! -nargs=? Filter let @a='' | execute 'g/<args>/y A' | new | setlocal bt=nofile | put! a
```
```lua
vim.api.nvim_create_user_command('Filter', function(opts)
  -- Clear register a
  vim.fn.setreg('a', '')
  
  -- Execute global command to yank matching lines to register a
  vim.cmd('g/' .. (opts.args or vim.fn.getreg('/') or '') .. '/y A')
  
  -- Create new scratch buffer and paste results
  vim.cmd('new')
  vim.wo.buftype = 'nofile'
  vim.cmd('put! a')
end, { nargs = '?' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Redirect_g_search_output)
***
# Title: Redirect Search Results to a New Window
# Category: search_replace
# Tags: search, mapping, output-redirection
---
Create a mapping to redirect global search results to a new window using register redirection

```vim
nnoremap <silent> <F3> :redir @a<CR>:g//<CR>:redir END<CR>:new<CR>:put! a<CR>
```
```lua
vim.keymap.set('n', '<F3>', function()
  -- Redirect output to register a
  vim.cmd('redir @a')
  -- Repeat last global command
  vim.cmd('g//')
  -- End redirection
  vim.cmd('redir END')
  -- Create new window and paste register contents
  vim.cmd('new')
  vim.cmd('put! a')
end, { silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Redirect_g_search_output)
***
# Title: Find Whole Words in Search
# Category: search_replace
# Tags: regex, search, text-navigation
---
Use \<word\> to search for exact whole word matches, avoiding partial word matches

```vim
# Search for whole word 'i'
/\<i\>
```
```lua
-- In Neovim, can use same regex pattern
vim.fn.search('\<i\>', 'n')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Regex)
***
# Title: Flexible Multi-Word Search
# Category: search_replace
# Tags: regex, search, text-navigation
---
Use \| to search for multiple alternative whole words in a single pattern

```vim
# Search for whole words 'red', 'green', or 'blue'
/\<\(red\|green\|blue\)\>
```
```lua
-- Lua regex search for whole words
vim.fn.search('\v<(red|green|blue)>', 'n')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Regex)
***
# Title: Regex Lookahead and Lookbehind
# Category: search_replace
# Tags: regex, advanced-search, pattern-matching
---
Advanced regex techniques to match patterns with conditional context using lookahead and lookbehind assertions

```vim
" Positive lookahead: match 'bar' only if preceded by 'foo'
/\(foo\)\@<=bar\(baz\)\@=
```
```lua
-- In Neovim, use vim.fn.search() with magic regex
vim.fn.search('\v(foo)@<=bar(baz)@=')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Regex_lookahead_and_lookbehind)
***
# Title: Zero-Width Matching with \zs and \ze
# Category: search_replace
# Tags: regex, pattern-matching, zero-width
---
Most performant way to do lookaround matching, marking start/end of match without including those parts

```vim
" Match 'bar' between 'foo' and 'baz'
/foo\zsbar\ze baz
```
```lua
-- Use similar regex pattern with Lua search functions
vim.fn.search('foo\zsbar\ze baz')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Regex_lookahead_and_lookbehind)
***
# Title: Advanced Search with OR Patterns
# Category: search_replace
# Tags: regex, search, text-matching
---
Use \| to search for multiple whole words, with precise word boundary matching

```vim
" Search for whole words 'red', 'green', 'blue'
/\<\(red\|green\|blue\)\>
```
```lua
-- Neovim search with multiple whole word options
vim.fn.search('\<\(red\|green\|blue\)\>')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Regexp_to_strip_redundant_zeroes_in_decimal_fractions)
***
# Title: Advanced Word Searching with Regular Expressions
# Category: search_replace
# Tags: regex, searching, word-boundary
---
Find whole words precisely using word boundary markers \< and \>

```vim
" Search for whole word 'i'
/\<i\>

" Find words starting or ending with 'i'
/\<i
/i\>
```
```lua
-- Lua doesn't change regex syntax, use same patterns
-- Can use vim.fn.search() for programmatic searches
vim.fn.search('\<i\>')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Regular_expression)
***
# Title: Flexible Multi-Word Search and Replace
# Category: search_replace
# Tags: regex, substitution, pattern-matching
---
Search or replace multiple whole words using OR operator

```vim
" Search for multiple whole words
/\<\(red\|green\|blue\)\>

" Replace multiple words
:%s/\<\(red\|green\|blue\)\>/purple/g
```
```lua
-- Use vim.cmd for ex commands
vim.cmd(':%s/\<\(red\|green\|blue\)\>/purple/g')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Regular_expression)
***
# Title: Highlight and Remove Unwanted Whitespace
# Category: search_replace
# Tags: whitespace, highlighting, text-cleanup
---
Easily display or remove whitespace at the end of lines or before tabs

```vim
function ShowSpaces()
  let @/='\v(\s+$)|( +\ze\t)'
  let &hlsearch=!&hlsearch
endfunction

nnoremap <F12> :call ShowSpaces()<CR>
```
```lua
vim.keymap.set('n', '<F12>', function()
  vim.o.hlsearch = not vim.o.hlsearch
  vim.fn.setreg('/', '\v(\s+$)|( +\ze\t)')
end, { desc = 'Toggle whitespace highlighting' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Remove_unwanted_spaces)
***
# Title: Remove File Path Prefix with Advanced Search/Replace
# Category: search_replace
# Tags: regex, file-manipulation, global-command
---
Quickly remove path prefixes from file lists using a flexible regex substitution that preserves desired portions of file paths

```vim
:%s/^.\{-}\ze///
```
```lua
vim.cmd('%s/^.\\{-}\\ze///g')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Remove_up_to_the_nth_slash_to_clean_file_lists)
***
# Title: Remove Multiple Path Levels in File Lists
# Category: search_replace
# Tags: regex, file-manipulation, global-command
---
Remove multiple directory levels from file paths by adjusting regex quantifier

```vim
:%s/^\((.\{-}\ze\/\)\{3}//
```
```lua
vim.cmd('%s/^\\((.\\{-}\\ze\\/\\)\\{3}//g')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Remove_up_to_the_nth_slash_to_clean_file_lists)
***
# Title: Powerful Multi-File Search and Replace
# Category: search_replace
# Tags: search, replace, multi-file
---
Perform a search and replace across multiple files with additional flags for comprehensive editing

```vim
" Search and replace with global, ignore case, and error-tolerant flags
:%s/\<pig\>/cow/gie|:update|:next
```
```lua
-- Equivalent multi-file search and replace
-- Note: This would typically be done with more modern Neovim methods like telescope or quickfix
vim.cmd('%s/\<pig\>/cow/gie')
vim.cmd('update')
vim.cmd('next')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Repeat_last_colon_command)
***
# Title: Grep Search Across Files with Quickfix Navigation
# Category: search_replace
# Tags: search, grep, quickfix, navigation
---
Extends Vim's search capabilities by using grep to search across files and navigate results using quickfix list

```vim
" Set grep program with recursive, case-insensitive search
:set grepprg=grep\ -rinsE

function! Mosh_grep(...)
  if a:0 == 0
    :exec "grep '".@/."' *.*"
  elseif a:0 == 1
    :exec "grep '".@/."' " a:1
  elseif a:0 == 2
    :exec "grep" a:2 " " a:1
  endif
  :map <c-n> :cnext<CR>
  :map <c-p> :cprev<CR>
  :copen
endfunction

" Map g/ to trigger grep search
:map g/ :call Mosh_grep()<CR>
```
```lua
-- Set grep program
vim.opt.grepprg = 'grep -rinsE'

function _G.mosh_grep(dir, pattern)
  local search_pattern = pattern or vim.fn.getreg('/')
  local search_dir = dir or '*.*'
  
  vim.cmd('grep ' .. vim.fn.shellescape(search_pattern) .. ' ' .. search_dir)
  vim.cmd('copen')
  
  -- Map navigation keys
  vim.keymap.set('n', '<C-n>', ':cnext<CR>', {noremap = true, silent = true})
  vim.keymap.set('n', '<C-p>', ':cprev<CR>', {noremap = true, silent = true})
end

-- Map g/ to trigger grep search
vim.keymap.set('n', 'g/', function() _G.mosh_grep() end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Repeat_search_using_grep)
***
# Title: Repeat Substitution from Cursor Position
# Category: search_replace
# Tags: substitute, custom-command, advanced-editing
---
Create a custom command to repeat substitution from the current cursor position, allowing more flexible text replacement

```vim
" RS: repeat substitution command
com! -range -nargs=* RS call RepeatSubst(<q-args>)

fun! RepeatSubst(subexpr)
  if a:subexpr != ""
    let g:repeatsubst= a:subexpr
  endif
  let curcol= col(".")
  let sep = strpart(g:repeatsubst,0,1)
  let pat = substitute(g:repeatsubst,'^.\(.*\)'.sep.'.*$','\1','')
  s/\%#./\r&/
  let curcol= curcol + matchend(getline("."),pat)
  exe "s".g:repeatsubst
  norm! k
  j!
  exe 'norm! '.curcol.'|'
endfun
```
```lua
-- Lua implementation of repeat substitution
function RepeatSubst(subexpr)
  if subexpr ~= "" then
    vim.g.repeatsubst = subexpr
  end
  
  local curcol = vim.fn.col('.')
  local sep = string.sub(vim.g.repeatsubst, 1, 1)
  local pat = string.match(vim.g.repeatsubst, '^.(.-)' .. sep)
  
  -- Perform substitution from current cursor position
  vim.cmd('s/\%#./\r&/')
  curcol = curcol + vim.fn.matchend(vim.fn.getline('.'), pat)
  vim.cmd('s' .. vim.g.repeatsubst)
  vim.cmd('norm! k')
  vim.cmd('j!')
  vim.cmd('norm! ' .. curcol .. '|')
end

-- Create a custom command
vim.api.nvim_create_user_command('RS', function(opts)
  RepeatSubst(opts.args)
end, { nargs = '*', range = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Repeating_a_substitute_from_current_cursor_position)
***
# Title: Word Replacement with Confirmation
# Category: search_replace
# Tags: search, replace, confirmation, global
---
Replace all occurrences of the word under the cursor with global confirmation

```vim
nnoremap <Leader>s :%s/\<<C-r><C-w>\>//g<Left><Left>
```
```lua
vim.keymap.set('n', '<Leader>s', function()
  local word = vim.fn.expand('<cword>')
  vim.cmd(':%s/\<' .. word .. '\>//g')
end, { desc = 'Replace word with confirmation' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip464)
***
# Title: Quick Word Search in Current File
# Category: search_replace
# Tags: search, quickfix, navigation
---
Define a command to search for the current word under the cursor in the current file and open results in quickfix window

```vim
command GREP :execute 'vimgrep '.expand('<cword>').' '.expand('%') | :copen | :cc
```
```lua
vim.api.nvim_create_user_command('GREP', function()
  vim.cmd('vimgrep ' .. vim.fn.expand('<cword>') .. ' ' .. vim.fn.expand('%'))
  vim.cmd('copen')
  vim.cmd('cc')
end, {})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip483)
***
# Title: Toggle Search Highlight with Single Keypress
# Category: search_replace
# Tags: search, highlight, mapping
---
Add a quick way to toggle search highlighting on and off, improving code readability and focus

```vim
" Press F4 to toggle highlighting on/off, and show current value.
:noremap <F4> :set hlsearch! hlsearch?<CR>
```
```lua
vim.keymap.set('n', '<F4>', function()
  vim.o.hlsearch = not vim.o.hlsearch
  print('hlsearch: ' .. tostring(vim.o.hlsearch))
end, { desc = 'Toggle search highlighting' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip486)
***
# Title: Title Case Conversion with Substitute
# Category: search_replace
# Tags: text-transformation, regex, substitution
---
Advanced substitution command to convert text to title case, preserving first letter of each word as uppercase

```vim
" Convert line to Title Case
:s/\<\(\w\)\(\w*\)\>/\u\1\L\2/g
```
```lua
-- Lua equivalent using vim.cmd for Ex command
vim.cmd('s/\v(\w)(\S*)/\u\1\L\2/g')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip49)
***
# Title: Flexible Multiple Word Search
# Category: search_replace
# Tags: regex, search, text-processing
---
Search for multiple whole words using the \| (or) operator with word boundaries

```vim
" Search for 'red', 'green', or 'blue' as whole words
/\<\(red\|green\|blue\)\>
```
```lua
-- Lua equivalent for multiple whole word search
local pattern = '\v<(red|green|blue)>'
vim.fn.search(pattern, 'n')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip516)
***
# Title: Advanced Duplicate Line Removal
# Category: search_replace
# Tags: text-manipulation, regex
---
Remove duplicate lines with more complex regex-based methods, preserving line order

```vim
%s/^\(.*\)\(\n\1\)\+$/\1/
```
```lua
vim.cmd('%s/^\(.*\)(\n\1)+$/\1/')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip648)
***
# Title: Advanced Substitution with Capture Groups
# Category: search_replace
# Tags: regex, substitution, pattern-matching
---
Use capture groups to perform complex search and replace operations by referencing matched subpatterns

```vim
:g/\(M\)\([0-9]\)\([0-9]\)/s//\1[\2][\3]/g
```
```lua
-- In Lua, use vim.cmd for complex substitution
vim.cmd('g/\(M\)\([0-9]\)\([0-9]\)/s//\1[\2][\3]/g')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip654)
***
# Title: Simple Regex Substitution with Capture Groups
# Category: search_replace
# Tags: regex, substitution, pattern-matching
---
Easily transform patterns using capture groups and references

```vim
%s/\v(\d)(\d)/[\1][\2]
```
```lua
-- Use very magic mode for simplified regex
vim.cmd('%s/\v(\d)(\d)/[\1][\2]')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip654)
***
# Title: Flexible CSV Column Search and Manipulation
# Category: search_replace
# Tags: csv, search, column-operations
---
Advanced CSV column search, allowing searching within specific columns and performing operations like copying or deleting columns

```vim
" Search within a specific column
:SC n=str  " search for 'str' in nth column

" Copy a specific column
:CC n x     " copy nth column to register x

" Delete a specific column
:DC n       " delete nth column
```
```lua
-- Implemented via custom Lua functions
-- Example search within column
function _G.search_column(column, search_term)
  local pattern = string.format('^([^,]*,){%d}[^,]*%s', column-1, search_term)
  vim.cmd('/' .. pattern)
end

-- Copy column function
function _G.copy_column(column, register)
  register = register or '"'
  -- Implement column extraction and copying logic
end

-- Delete column function
function _G.delete_column(column)
  -- Implement column deletion logic
end

-- Create user commands
vim.api.nvim_create_user_command('SC', function(opts)
  local args = opts.args:match('(%d*)=?(.*)') or 0
  _G.search_column(tonumber(args) or 0, args)
end, { nargs = 1 })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip667)
***
# Title: Delete Lines with Selective Filtering
# Category: search_replace
# Tags: global-command, filtering, line-deletion
---
Efficiently delete lines matching a pattern while preserving exceptions using Vim's global command with conditional deletion

```vim
:global:^./help/:if (match(getline(line(".")), '^./help/de/') == -1) | delete | endif
```
```lua
-- Delete help files except German ones
vim.api.nvim_exec([[g!/\.\/help\/de/d]], false)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip670)
***
# Title: Advanced Global Command Line Filtering
# Category: search_replace
# Tags: regex, global-command, line-filtering
---
Use lookahead-like global command to selectively delete lines based on complex pattern matching

```vim
g#\(^\./help/\)\(de/\)\@!#d
```
```lua
-- Delete help lines not starting with './help/de/'
vim.api.nvim_exec([[g#\(^\.\/help\/\)\(de\/\)\@!#d]], false)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip670)
***
# Title: Quick Toggle to Remove Search Highlights
# Category: search_replace
# Tags: search, highlights, utility
---
Easily turn off search highlighting during editing sessions

```vim
set nohlsearch
```
```lua
vim.opt.hlsearch = false
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip675)
***
# Title: Advanced Search with Case Sensitivity Controls
# Category: search_replace
# Tags: search, case-sensitivity, pattern-matching
---
Configure intelligent case-sensitive searching with smart case detection and custom mappings

```vim
" Enable case-insensitive searching
set ignorecase
set smartcase

" Custom * search with smart case behavior
:nnoremap * /\<<C-R>=expand('<cword>')\>\><CR>
```
```lua
-- Enable case-insensitive and smart case searching
vim.opt.ignorecase = true
vim.opt.smartcase = true

-- Custom * search with smart case behavior
vim.keymap.set('n', '*', function()
  local word = vim.fn.expand('<cword>')
  vim.fn.search('\<' .. word .. '\>', 'n')
end, { desc = 'Smart word search' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip679)
***
# Title: Search Paths Without Escaping Slashes
# Category: search_replace
# Tags: search, command-line, text-editing
---
Use alternative delimiters like '?' or other characters to search file paths without escaping slashes

```vim
" Search with alternative delimiters
:g ?c:/tmp/x/y/z/? d
```
```lua
-- Lua equivalent for alternative search delimiters
-- Note: Use vim.cmd for Ex commands
vim.cmd('g ?c:/tmp/x/y/z/? d')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip685)
***
# Title: Flexible Search and Replace Delimiters
# Category: search_replace
# Tags: search, substitution, text-manipulation
---
Use different characters for search and replace operations to avoid escaping complex paths

```vim
" Use different delimiters for search and replace
:g#/tmp/#s//#tmp#/
```
```lua
-- Lua equivalent for flexible search/replace
-- Note: Use vim.cmd for Ex commands
vim.cmd('g#/tmp/#s//#tmp#/')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip685)
***
# Title: Use Expressions in Substitute Commands
# Category: search_replace
# Tags: substitution, advanced-editing, expressions
---
Use \'=' in substitute commands to evaluate expressions dynamically, enabling powerful text transformations

```vim
:%s/^/\=line('.')."\t"/
:10,20s/^/\=line('.')."\t"/
```
```lua
-- Number all lines with line number
vim.cmd(':%s/^/\\=line(".")."\t"/')

-- Number lines 10-20 with line number
vim.cmd(':10,20s/^/\\=line(".")."\t"/')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip755)
***
# Title: Sequential Line Numbering with Counter
# Category: search_replace
# Tags: numbering, global-command, text-manipulation
---
Sequentially number lines in a range starting from 1 using a counter variable

```vim
:let counter=0|10,20g/^/let counter=counter+1|s/^/\=counter."\t"
```
```lua
-- Initialize counter and number lines sequentially
vim.g.counter = 0
vim.cmd(':10,20g/^/let counter=counter+1')
vim.cmd(':10,20s/^/\\=g:counter."\t"')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip755)
***
# Title: Sort Lines by Selected Substring
# Category: search_replace
# Tags: selection, sorting, text-manipulation
---
Quickly sort log files or text by a selected substring using visual mode mappings

```vim
" Sort by selection
:vmap 0 :<BS><BS><BS><BS><BS>g<M-x>\M<S-Insert><M-x>m0<CR>
:vmap $ :<BS><BS><BS><BS><BS>g<M-x>\M<S-Insert><M-x>m$<CR>
:vmap p :<BS><BS><BS><BS><BS>g<M-x>\M<S-Insert><M-x>p<CR>
```
```lua
-- Sort lines by selected text to top/bottom
vim.keymap.set('v', 'm0', function()
  local selected_text = vim.fn.getreg('*')
  vim.cmd('g/' .. selected_text .. '/m0')
end, { desc = 'Move matching lines to top' })

vim.keymap.set('v', 'm$', function()
  local selected_text = vim.fn.getreg('*')
  vim.cmd('g/' .. selected_text .. '/m$')
end, { desc = 'Move matching lines to bottom' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip758)
***
