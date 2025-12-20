# Title: Change working directory
# Category: Navigation
# Tags: directory, cd, path, working, ex
---
Use `:cd` to change current working directory, `:pwd` to show current directory.

```vim
:cd ~/projects      " change to home/projects directory
:cd %:h             " change to directory of current file
:pwd                " show current working directory
:cd -               " change to previous directory
```
***
# Title: Create abbreviations
# Category: Text Input
# Tags: abbreviate, abbr, shortcut, expand, ex
---
Use `:abbreviate` or `:abbr` to create text shortcuts that expand automatically.

```vim
:abbr teh the       " auto-correct 'teh' to 'the'
:abbr @@ john@example.com  " expand @@ to email
:iabbr <buffer> fn function  " buffer-local abbreviation
:unabbr teh         " remove abbreviation
```
***
# Title: Show all marks
# Category: Navigation
# Tags: marks, list, show, position, ex
---
Use `:jumps` to display jump list with positions you can return to.
Use `Ctrl+o` to go back, `Ctrl+i` to go forward in jump list.

```vim
:jumps              " show jump list
:ju                 " shorter version
```
***
# Title: Show registers content
# Category: Registers
# Tags: registers, show, content, clipboard, ex
---
Use `:registers` or `:reg` to display contents of all registers.

```vim
:registers          " show all registers
:reg abc            " show only registers a, b, and c
:reg "              " show default register
:reg +              " show system clipboard register
```
***
# Title: Echo text and expressions
# Category: Scripting
# Tags: echo, print, expression, debug, ex
---
Use `:echo` to print text or evaluate expressions in command line.

```vim
:echo "Hello World" " print text
:echo &tabstop      " show value of tabstop option
:echo expand('%')   " show current filename
:echo line('.')     " show current line number
```
***
# Title: Show all messages
# Category: Information
# Tags: messages, history, errors, warnings, ex
---
Use `:messages` to display message history including errors and warnings.

```vim
:messages           " show all messages
:mes                " shorter version
:messages clear     " clear message history
```
***
# Title: Call functions
# Category: Scripting
# Tags: call, function, execute, script, ex
---
Use `:call` to execute functions and discard their return value.

```vim
:call search('pattern')  " call search function
:call setline('.', 'new text')  " replace current line
:call cursor(10, 5)      " move cursor to line 10, column 5
```
***
# Title: Define variables
# Category: Scripting
# Tags: let, variable, assign, define, ex
---
Use `:digraphs` to show available two-character combinations for special characters.
In insert mode, use `Ctrl+k` followed by two characters (e.g., `Ctrl+k a'` for á).

```vim
:digraphs           " show all digraphs
:dig                " shorter version
```
***
# Title: Runtime file loading
# Category: Configuration
# Tags: runtime, load, path, script, ex
---
Use `:runtime` to load script files from runtime path directories.

```vim
:runtime! plugin/**/*.vim  " load all plugins
:runtime syntax/python.vim " load Python syntax
:ru macros/matchit.vim     " load matchit macro
```
***
# Title: Check file path existence
# Category: File Operations
# Tags: checkpath, include, path, files, ex
---
Use `:checkpath` to verify all files in include path can be found.
Useful for debugging include paths in C/C++ projects.

```vim
:checkpath          " check all included files
:checkp!            " show files that cannot be found
```
***
# Title: Neovim health check
# Category: Diagnostics
# Tags: checkhealth, health, diagnostic, status, ex
---
Use `:checkhealth` to run diagnostic checks on Neovim installation and plugins.

```vim
:checkhealth        " check all health
:checkhealth nvim   " check only Neovim core health
:checkhealth vim    " check Vim compatibility
```
***
# Title: AutoGroup management
# Category: Scripting
# Tags: augroup, autocmd, group, event, ex
---
Use `:augroup` to group autocommands and manage them collectively.

```vim
:augroup MyGroup    " start group definition
:autocmd!           " clear existing autocmds in group
:autocmd BufRead * echo "File read"
:augroup END        " end group definition
```
***
# Title: Function definition
# Category: Scripting
# Tags: function, define, script, procedure, ex
---
Use `:match` to highlight patterns with specific colors in current window.

```vim
:match ErrorMsg /TODO/     " highlight TODO in red
:match Search /\<word\>/   " highlight whole word
:match none                " clear all matches
:2match Comment /pattern/  " second match group
```
***
# Title: Conditional execution
# Category: Scripting
# Tags: if, condition, branch, script, ex
---
Use `:if`, `:else`, `:endif` for conditional execution in scripts.

```vim
:if &filetype == 'python'
  echo "Python file"
:else
  echo "Not Python"
:endif
```
***
# Title: Menu creation
# Category: Interface
# Tags: menu, gui, interface, create, ex
---
Use `:menu` to create menu items (GUI mode).

```vim
:menu File.Save :w<CR>           " create Save menu item
:menu Edit.Find :promptfind<CR>  " create Find menu item
:unmenu File.Save                " remove menu item
```
***
# Title: Key mapping
# Category: Mapping
# Tags: map, key, mapping, shortcut, ex
---
Use `:map` to create key mappings, `:noremap` for non-recursive mappings.

```vim
:map <F2> :w<CR>          " map F2 to save
:nmap <leader>q :q<CR>    " normal mode mapping
:imap <C-s> <Esc>:w<CR>a  " insert mode mapping
:unmap <F2>               " remove mapping
```
***
# Title: Help search
# Category: Help
# Tags: helpgrep, help, search, documentation, ex
---
Use `:helpgrep` to search through all help files for patterns.

```vim
:helpgrep pattern   " search help for pattern
:helpg autocmd      " search for autocmd info
:cn                 " next help match
:cp                 " previous help match
```
***
# Title: Tag selection
# Category: Navigation
# Tags: tselect, tag, multiple, choose, ex
---
Use `:tselect` when multiple tag matches exist to choose from a list.

```vim
:tselect function   " show list of function tags
:ts MyClass         " show list of MyClass tags
:tnext              " go to next tag match
:tprev              " go to previous tag match
```
***
# Title: Include jump
# Category: Navigation
# Tags: ijump, include, file, search, ex
---
Use `:ijump` to jump to first line containing identifier in include files.

```vim
:ijump printf       " jump to printf definition in includes
:ij MyFunc          " jump to MyFunc in include files
```
***
# Title: Include list
# Category: Navigation
# Tags: ilist, include, search, show, ex
---
Use `:ilist` to list all lines containing identifier in include files.

```vim
:ilist printf       " list all printf occurrences
:il /pattern/       " list lines matching pattern
:il! MyFunc         " list including header files
```
***
# Title: Language settings
# Category: Configuration
# Tags: language, locale, encoding, international, ex
---
Use `:language` to set language for messages and time.

```vim
:language messages en_US.UTF-8  " set message language
:language time C                " set time language
:language                       " show current settings
```
***
# Title: Print lines
# Category: Display
# Tags: print, lines, show, output, ex
---
Use `:file` to show file information and optionally rename buffer.

```vim
:file              " show file info (name, lines, position)
:file newname.txt  " rename current buffer
:f                 " shorter version
```
***
# Title: Spell checking commands
# Category: Text Editing
# Tags: spell, check, dictionary, correction, ex
---
Use spell-related commands to manage spell checking.

```vim
:spell             " enable spell checking
:set spell         " same as :spell
:spellgood word    " add word to good word list
:spellwrong word   " add word as wrong word
:spelldump         " show all spell words
```
***
# Title: Introduction screen
# Category: Interface
# Tags: intro, welcome, screen, startup, ex
---
Use `:intro` to show the Neovim introduction/welcome screen.
Useful after clearing the screen or when you want to see version info.

```vim
:intro             " show introduction screen
```
***
# Title: Unlet variables
# Category: Scripting
# Tags: unlet, variable, delete, remove, ex
---
Use `:badd` to add file to buffer list without editing it.
Useful for preparing a list of files to work with.

```vim
:badd file.txt     " add file to buffer list
:badd *.py         " add all Python files
```
***
# Title: Make and build
# Category: Development
# Tags: make, build, compile, external, ex
---
Use `:make` to run external make command and capture errors.
Errors appear in quickfix list. Use `:cn` to navigate.

```vim
:make              " run make command
:make clean        " run make with clean target
:make -j4          " run make with 4 parallel jobs
```
***
