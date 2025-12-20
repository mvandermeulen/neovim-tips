# Title: Toggle fold
# Category: Folding
# Tags: fold, toggle, code
---
Use `za` to toggle fold under cursor open/closed.

```vim
za  " toggle fold under cursor
```

**Source:** Community contributed
***
# Title: Open and close all folds
# Category: Folding
# Tags: fold, all, global
---
Use `zR` to open all folds in buffer and `zM` to close all folds in buffer.

```vim
zR  " open all folds
zM  " close all folds
```

**Source:** Community contributed
***
# Title: Create fold from selection
# Category: Folding
# Tags: fold, create, selection
---
Use `zf` to create a fold from visual selection or with motion (e.g., `zf5j` to fold 5 lines down).

```vim
zf5j  " create fold 5 lines down
zf    " create fold from visual selection
```

**Source:** Community contributed
***
# Title: Fold levels
# Category: Folding
# Tags: fold, level, depth
---
Use `zm` to increase fold level (close more folds) and `zr` to reduce fold level (open more folds).

```vim
zm  " increase fold level
zr  " reduce fold level
```

**Source:** Community contributed
***
# Title: Z-commands - create folds
# Category: Folding
# Tags: fold, create, lines
---
Use `zF` to create fold for N lines or `zf{motion}` to create fold with motion.

```vim
5zF   " create fold for 5 lines
zf3j  " create fold from cursor down 3 lines
zfip  " create fold for inner paragraph
```

**Source:** Community contributed
***
# Title: Open All Folds Automatically on File Open
# Category: folding
# Tags: folds, file-loading, configuration
---
Automatically open most folds when opening a file, with flexibility for different file types

```vim
set foldmethod=indent
set foldlevelstart=20

" Open all folds for specific file types
autocmd Syntax c,cpp,vim,xml,html,xhtml setlocal foldmethod=syntax
autocmd Syntax c,cpp,vim,xml,html,xhtml,perl normal zR
```

```lua
-- Set fold method and default open level
vim.opt.foldmethod = 'indent'
vim.opt.foldlevelstart = 20

-- Automatically open folds for specific file types
vim.api.nvim_create_augroup('FoldConfig', { clear = true })
vim.api.nvim_create_autocmd('Syntax', {
  group = 'FoldConfig',
  pattern = {'c', 'cpp', 'vim', 'xml', 'html', 'xhtml', 'perl'},
  callback = function()
    vim.opt_local.foldmethod = 'syntax'
    vim.cmd('normal zR')
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/All_folds_open_when_open_a_file)
***
# Title: Automatically Fold Perl Subroutines
# Category: folding
# Tags: perl, syntax-folding, code-organization
---
Enable automatic folding for Perl subroutines using built-in syntax folding

```vim
let perl_fold = 1
```

```lua
vim.g.perl_fold = 1
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Auto-fold_Perl_subs)
***
# Title: Custom Perl Folding with Fold Expression
# Category: folding
# Tags: custom-folding, perl, advanced-folding
---
Create a custom fold expression to intelligently fold Perl subroutines

```vim
function GetPerlFold()
  if getline(v:lnum) =~ '^\s*sub\s'
    return ">1"
  elseif getline(v:lnum) =~ '\}\s*$'
    let my_perlnum = v:lnum
    let my_perlmax = line("$")
    while (1)
      let my_perlnum = my_perlnum + 1
      if my_perlnum > my_perlmax
        return "<1"
      endif
      let my_perldata = getline(my_perlnum)
      if my_perldata =~ '^\s*\(\#.*\)\?$'
        " do nothing
      elseif my_perldata =~ '^\s*sub\s'
        return "<1"
      else
        return "="
      endif
    endwhile
  else
    return "="
  endif
endfunction
setlocal foldexpr=GetPerlFold()
setlocal foldmethod=expr
```

```lua
local function get_perl_fold(lnum)
  local line = vim.fn.getline(lnum)
  if line:match('^%s*sub%s') then
    return '>1'
  elseif line:match('}%s*$') then
    local perlnum = lnum
    local perlmax = vim.fn.line('$')
    while true do
      perlnum = perlnum + 1
      if perlnum > perlmax then
        return '<1'
      end
      local perldata = vim.fn.getline(perlnum)
      if perldata:match('^%s*(#.*)?$') then
        -- do nothing
      elseif perldata:match('^%s*sub%s') then
        return '<1'
      else
        return '='
      end
    end
  else
    return '='
  end
end

vim.wo.foldexpr = 'v:lua.get_perl_fold(v:lnum)'
vim.wo.foldmethod = 'expr'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Auto-fold_Perl_subs)
***
# Title: Customize Fold Text with Advanced Display
# Category: folding
# Tags: folding, display, code-readability
---
Create a custom fold text function that improves code readability by handling comments and braces intelligently, and right-aligning line count

```vim
function! MyFoldText()
  let line = getline(v:foldstart)
  let n = v:foldend - v:foldstart + 1
  let info = " " . n . " lines"
  let sub = line
  let startbrace = substitute(line, '^.*{[ \t]*$', '{', 'g')
  if startbrace == '{'
    let line = getline(v:foldend)
    let endbrace = substitute(line, '^[ \t]*}\(.*\)$', '}', 'g')
    if endbrace == '}'
      let sub = sub.substitute(line, '^[ \t]*}\(.*\)$', '...}\1', 'g')
    endif
  endif
  return sub . info
endfunction

set foldtext=MyFoldText()
```

```lua
function _G.custom_fold_text()
  local start_line = vim.fn.getline(vim.v.foldstart)
  local line_count = vim.v.foldend - vim.v.foldstart + 1
  local info = " " .. line_count .. " lines"
  
  local sub = start_line
  local start_brace = start_line:match('^.*{[ \t]*$') and '{' or start_line
  
  if start_brace == '{' then
    local end_line = vim.fn.getline(vim.v.foldend)
    local end_brace = end_line:match('^[ \t]*}') and '}' or end_line
    
    if end_brace == '}' then
      sub = sub .. end_line:gsub('^[ \t]*}(.*)', '...}%1')
    end
  end
  
  return sub .. info
end

vim.o.foldtext = 'v:lua.custom_fold_text()'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Customize_text_for_closed_folds)
***
# Title: Prevent Syntax Folding Disruptions in Insert Mode
# Category: folding
# Tags: folding, insert-mode, performance
---
Temporarily switch to manual folding during insert mode to prevent syntax folding slowdowns and unexpected fold opening

```vim
" Don't disrupt folds when inserting text
autocmd InsertEnter * if !exists('w:last_fdm') | let w:last_fdm=&foldmethod | setlocal foldmethod=manual | endif
autocmd InsertLeave,WinLeave * if exists('w:last_fdm') | let &l:foldmethod=w:last_fdm | unlet w:last_fdm | endif
```

```lua
vim.api.nvim_create_augroup('FoldMethodToggle', { clear = true })

vim.api.nvim_create_autocmd({'InsertEnter'}, {
  group = 'FoldMethodToggle',
  callback = function()
    if vim.w.last_fdm == nil then
      vim.w.last_fdm = vim.wo.foldmethod
      vim.wo.foldmethod = 'manual'
    end
  end
})

vim.api.nvim_create_autocmd({'InsertLeave', 'WinLeave'}, {
  group = 'FoldMethodToggle',
  callback = function()
    if vim.w.last_fdm ~= nil then
      vim.wo.foldmethod = vim.w.last_fdm
      vim.w.last_fdm = nil
    end
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Disable_folding_in_insert_mode)
***
# Title: Fold INI File Sections Automatically
# Category: folding
# Tags: syntax, configuration, file-management
---
Enable automatic folding for INI file sections, making large configuration files more readable

```vim
syn region dosiniSection start="^\[" end="\(\n\+\[\)\@=" contains=dosiniLabel,dosiniHeader,dosiniComment keepend fold
setlocal foldmethod=syntax
setlocal foldlevel=20
```

```lua
vim.cmd([[syn region dosiniSection start="^\[" end="\(\n\+\[\)\@=" contains=dosiniLabel,dosiniHeader,dosiniComment keepend fold]])
vim.wo.foldmethod = 'syntax'
vim.wo.foldlevel = 20
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Dosini_files)
***
# Title: Double-Click to Toggle Folds
# Category: folding
# Tags: key-mapping, folding, user-interface
---
Add a convenient double-click mouse mapping to open and close code folds in Vim/Neovim

```vim
:noremap <2-LeftMouse> za
```

```lua
vim.keymap.set({'n', 'v'}, '<2-LeftMouse>', 'za', { desc = 'Toggle fold with double-click' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Double-click_to_open/close_a_fold)
***
# Title: Dynamic Indent and Manual Folding
# Category: folding
# Tags: autocmd, folding, configuration
---
Automatically set initial folding to indent, then allow manual fold creation while editing

```vim
augroup vimrc
  au BufReadPre * setlocal foldmethod=indent
  au BufWinEnter * if &fdm == 'indent' | setlocal foldmethod=manual | endif
augroup END
```

```lua
vim.api.nvim_create_augroup('foldconfig', { clear = true })
vim.api.nvim_create_autocmd({'BufReadPre'}, {
  group = 'foldconfig',
  callback = function()
    vim.opt_local.foldmethod = 'indent'
  end
})
vim.api.nvim_create_autocmd({'BufWinEnter'}, {
  group = 'foldconfig',
  callback = function()
    if vim.opt_local.foldmethod:get() == 'indent' then
      vim.opt_local.foldmethod = 'manual'
    end
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Easily_add_folds_in_code)
***
# Title: Advanced Folding Techniques in Vim/Neovim
# Category: folding
# Tags: folding, code-navigation, productivity
---
Provides flexible folding methods to improve code readability and navigation by hiding complex sections of code

```vim
" Indent folding with manual override
augroup vimrc
  au BufReadPre * setlocal foldmethod=indent
  au BufWinEnter * if &fdm == 'indent' | setlocal foldmethod=manual | endif
augroup END
```

```lua
-- Indent folding with manual override
vim.api.nvim_create_augroup('folding', { clear = true })
vim.api.nvim_create_autocmd({'BufReadPre'}, {
  group = 'folding',
  callback = function()
    vim.wo.foldmethod = 'indent'
  end
})

vim.api.nvim_create_autocmd({'BufWinEnter'}, {
  group = 'folding',
  callback = function()
    if vim.wo.foldmethod == 'indent' then
      vim.wo.foldmethod = 'manual'
    end
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Easily_open_and_close_folds)
***
# Title: MoinMoin Wiki Folding with Vim
# Category: folding
# Tags: file-type, syntax, editing
---
Create custom folding for MoinMoin wiki files based on section headings, with dynamic fold levels

```vim
" Define folding based on wiki headings; start with all folds open.
setlocal foldlevel=20
setlocal foldmethod=expr
setlocal foldexpr=HeadingLevel(v:lnum)

function HeadingLevel(lnum)
  let n = strlen(substitute(getline(a:lnum), '[^=].*', '', ''))
  return (n == 0) ? '=' : '>' . n
endfunction
```

```lua
vim.api.nvim_create_autocmd('FileType', {
  pattern = 'moin',
  callback = function()
    vim.wo.foldlevel = 20
    vim.wo.foldmethod = 'expr'
    vim.wo.foldexpr = 'v:lua.MoinHeadingLevel(v:lnum)'
  end
})

_G.MoinHeadingLevel = function(lnum)
  local line = vim.fn.getline(lnum)
  local n = #line:match('^(=+)') or 0
  return n == 0 and '=' or '>' .. n
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Edit_MoinMoin_wiki_files_with_folding)
***
# Title: Navigate XML Project Hierarchies with Folds
# Category: folding
# Tags: xml, navigation, project-structure
---
Quickly navigate complex XML project files by creating folds based on a specific attribute and moving between parent nodes

```vim
function! FoldMoveToParentNode()
  normal! zc
  let curNodeIndent = indent(foldclosed('.'))
  let nodeIndent = curNodeIndent
  let curLine = line('.')
  let line = -1
  while nodeIndent >= curNodeIndent
    normal! zkzc
    let line = line('.')
    if line == curLine
      break
    endif
    let nodeIndent = indent(foldclosed('.'))
  endwhile
endfunction
```

```lua
function _G.fold_move_to_parent_node()
  vim.cmd('normal! zc')
  local cur_node_indent = vim.fn.indent(vim.fn.foldclosed('.'))
  local node_indent = cur_node_indent
  local cur_line = vim.fn.line('.')
  local line = -1
  
  while node_indent >= cur_node_indent do
    vim.cmd('normal! zkzc')
    line = vim.fn.line('.')
    if line == cur_line then
      break
    end
    node_indent = vim.fn.indent(vim.fn.foldclosed('.'))
  end
end

-- Optional mapping
vim.keymap.set('n', '<leader>fdp', _G.fold_move_to_parent_node, { desc = 'Move to parent node in XML' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Finding_your_way_around_in_an_installshiled_project_XML_file)
***
# Title: Fold C-Style Comments Automatically
# Category: folding
# Tags: syntax-folding, c-languages, comments
---
Automatically create folds for multi-line C-style comments in source code files

```vim
au BufNewFile,BufRead *.cpp,*.c,*.h,*.java syn region myCComment start="/\*" end="\*/" fold keepend transparent
```

```lua
vim.api.nvim_create_autocmd({"BufNewFile", "BufRead"}, {
  pattern = {"*.cpp", "*.c", "*.h", "*.java"},
  callback = function()
    vim.cmd([[syn region myCComment start="/\*" end="\*/" fold keepend transparent]])
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Fold_C-style_comments)
***
# Title: Custom Fold Text for Comments
# Category: folding
# Tags: fold-text, custom-display, comments
---
Customize fold display to show comment start and number of lines

```vim
set foldtext=MyFoldText()
function MyFoldText()
  let line = getline(v:foldstart)
  let sub = substitute(line, '^[\t ]*', '', '')
  let nlines = v:foldend - v:foldstart + 1
  return "+-" . v:folddashes . nlines . ": " . sub
endfunction
```

```lua
function _G.custom_fold_text()
  local first_line = vim.api.nvim_buf_get_lines(0, vim.v.foldstart - 1, vim.v.foldstart, false)[1]
  local line_count = vim.v.foldend - vim.v.foldstart + 1
  return string.format("+-(%d lines): %s", line_count, first_line:gsub("^%s*", ""))
end

vim.o.foldtext = 'v:lua.custom_fold_text()'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Fold_C-style_comments)
***
# Title: Fold C# Regions Easily
# Category: folding
# Tags: code-folding, language-specific, navigation
---
Automatically fold C# #region blocks using matchit and custom matchwords

```vim
let b:match_words = '\s*#\s*region.*$:\s*#\s*endregion'
```

```lua
vim.g.match_words = '\s*#\s*region.*$:\s*#\s*endregion'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Fold_a_C_sharp_region)
***
# Title: Fold Multiple Empty Lines in a File
# Category: folding
# Tags: syntax, folding, whitespace
---
Automatically fold sequences of two or more empty lines to reduce visual clutter and improve readability

```vim
syn match MyEmptyLines "(^\s*\n)\+" fold
syn sync fromstart
setlocal foldmethod=syntax
```

```lua
vim.cmd('syn match MyEmptyLines "(^\\s*\\n)\\+" fold')
vim.cmd('syn sync fromstart')
vim.opt.foldmethod = 'syntax'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Fold_away_empty_lines)
***
# Title: Custom Java Folding with Expression Function
# Category: folding
# Tags: custom-folding, java, code-organization
---
Create intelligent fold levels for Java code based on comments and code structure

```vim
function! MyFoldLevel(lineNumber)
  let thisLine = getline(a:lineNumber)
  if (thisLine =~ '\%(\%(/\*\*\).*\%(\*/\)\)\|\%({.*}\)')
    return '='
  elseif (thisLine =~ '\%(^\s*/\*\*\s*$\)\|{'
    return "a1"
  elseif (thisLine =~ '\%(^\s*\*/\s*$\)\|}'
    return "s1"
  endif
  return '='
endfunction
setlocal foldexpr=MyFoldLevel(v:lnum)
setlocal foldmethod=expr
```

```lua
function _G.java_fold_level(linenum)
  local line = vim.fn.getline(linenum)
  if line:match('(/\*\*.*\*/)|({.*})')
    return '='
  elseif line:match('^%s*/\*\*%s*$') or line:match('{')
    return 'a1'
  elseif line:match('^%s*\*/') or line:match('}')
    return 's1'
  end
  return '='
end

vim.wo.foldexpr = 'v:lua.java_fold_level(v:lnum)'
vim.wo.foldmethod = 'expr'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Fold_braces_and_javadoc)
***
# Title: Fold Text by Regex Search Pattern
# Category: folding
# Tags: search, folding, regex
---
Configure Vim to use indent-based folding by default, but allow manual fold creation during editing

```vim
augroup vimrc
  au BufReadPre * setlocal foldmethod=indent
  au BufWinEnter * if &fdm == 'indent' | setlocal foldmethod=manual | endif
augroup END
```

```lua
vim.api.nvim_create_augroup('folding', { clear = true })
vim.api.nvim_create_autocmd('BufReadPre', {
  group = 'folding',
  callback = function() vim.wo.foldmethod = 'indent' end
})
vim.api.nvim_create_autocmd('BufWinEnter', {
  group = 'folding',
  callback = function()
    if vim.wo.foldmethod == 'indent' then
      vim.wo.foldmethod = 'manual'
    end
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Folding)
***
# Title: Smart Folding for Diff Files
# Category: folding
# Tags: diff, file-parsing, custom-folding
---
Create a custom folding function for diff files that automatically folds diff headers, file changes, and hunks for better readability

```vim
setlocal foldmethod=expr foldexpr=DiffFold(v:lnum)
function! DiffFold(lnum)
  let line = getline(a:lnum)
  if line =~ '^\(diff\|---\|+++\|@@\) '
    return 1
  elseif line[0] =~ '[-+ ]'
    return 2
  else
    return 0
  endif
endfunction
```

```lua
vim.api.nvim_create_autocmd('FileType', {
  pattern = 'diff',
  callback = function()
    vim.wo.foldmethod = 'expr'
    vim.wo.foldexpr = 'v:lua.DiffFold(v:lnum)'
  end
})

function _G.DiffFold(lnum)
  local line = vim.fn.getline(lnum)
  if line:match('^(diff|---|+++|@@) ') then
    return 1
  elseif line:match('^[-+ ]') then
    return 2
  else
    return 0
  end
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Folding_for_diff_files)
***
# Title: Indent-Based Folding for Plain Text
# Category: folding
# Tags: folding, text-organization, hierarchy
---
Create dynamic folds in plain text files based on indentation levels, allowing hierarchical text organization with minimal formatting

```vim
setlocal foldmethod=expr
setlocal foldexpr=(getline(v:lnum)=~'^$')?-1:((indent(v:lnum)<indent(v:lnum+1))?('>'.indent(v:lnum+1)):indent(v:lnum))
set foldtext=getline(v:foldstart)
set fillchars=fold:\ 
highlight Folded ctermfg=DarkGreen ctermbg=Black
```

```lua
vim.opt_local.foldmethod = 'expr'
vim.opt_local.foldexpr = [[v:lua.custom_fold_expr()]]

function _G.custom_fold_expr()
  local line = vim.fn.getline(vim.v.lnum)
  local next_line = vim.fn.getline(vim.v.lnum + 1)
  
  if line:match('^%s*$') then return -1 end
  
  local current_indent = vim.fn.indent(vim.v.lnum)
  local next_indent = vim.fn.indent(vim.v.lnum + 1)
  
  return current_indent < next_indent and '>' .. next_indent or current_indent
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Folding_for_plain_text_files_based_on_indentation)
***
# Title: Custom Function Folding in C/C++
# Category: folding
# Tags: folding, custom-functions, syntax
---
Create a custom fold expression that includes function prototypes and handles brace placement in C/C++ files

```vim
function FoldBrace()
  if getline(v:lnum+1)[0] == '{'
    return '>1'
  endif
  if getline(v:lnum)[0] == '}'
    return '<1'
  endif
  return foldlevel(v:lnum-1)
endfunction
set foldexpr=FoldBrace()
set foldmethod=expr
```

```lua
function _G.custom_fold()
  local next_line = vim.fn.getline(vim.v.lnum + 1)
  local current_line = vim.fn.getline(vim.v.lnum)
  
  if next_line:sub(1,1) == '{' then
    return '>1'
  end
  
  if current_line:sub(1,1) == '}' then
    return '<1'
  end
  
  return vim.fn.foldlevel(vim.v.lnum - 1)
end

vim.o.foldexpr = 'v:lua.custom_fold()'
vim.o.foldmethod = 'expr'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Folding_functions_with_the_prototype_included)
***
# Title: Fold VB.NET Code with Region Markers
# Category: folding
# Tags: region-folding, language-specific, code-organization
---
Create custom folding for Visual Basic .NET files using region markers, allowing collapsible code sections similar to Visual Studio

```vim
fu! VBFold(lnum)
    if getline(a:lnum) =~# '^\s*#Region'
        return '>1'
    elseif getline(a:lnum) =~# '^\s*#End Region'
        return  '<1'
    else
        return '='
    endif
endfu

fu! VBFoldText()
    return substitute(v:folddashes,'-',' ','g'). matchstr(getline(v:foldstart), '^\s*#Region\s\+\zs.*')
endfu

setl foldenable foldmethod=expr foldexpr=VBFold(v:lnum) foldtext=VBFoldText()
```

```lua
local function vb_fold(lnum)
    local line = vim.fn.getline(lnum)
    if line:match('^%s*#Region') then
        return '>1'
    elseif line:match('^%s*#End Region') then
        return '<1'
    else
        return '='
    end
end

local function vb_fold_text()
    local fold_start_line = vim.fn.getline(vim.v.foldstart)
    local region_name = fold_start_line:match('^%s*#Region%s+(.+)')
    return vim.fn.substitute(vim.v.folddashes, '-', ' ', 'g') .. (region_name or '')
end

vim.opt_local.foldenable = true
vim.opt_local.foldmethod = 'expr'
vim.opt_local.foldexpr = 'v:lua.vb_fold(v:lnum)'
vim.opt_local.foldtext = 'v:lua.vb_fold_text()'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Folding_like_in_Visual_Basic_.NET)
***
# Title: Fold File Listings with Dynamic Hierarchy
# Category: folding
# Tags: file-browsing, hierarchy, output-visualization
---
Create dynamic folding for file listings from find, locate, or tar commands, allowing easy navigation of complex directory structures

```vim
set mouse=a
set foldminlines=1 foldcolumn=2 fillchars="+" foldlevel=0
set foldmethod=expr
set foldexpr=FileBrowserFoldExpr()
set foldtext=FileBrowserFoldText()

function FileBrowserFoldExpr()
  let line=getline(v:lnum)
  let n=strlen(substitute(line,'[^/]*','','g'))
  if (line=~'^.*/$')
    return '>'.n
  elseif (strpart(getline(v:lnum+1),0,strlen(line)+1)==line.'/')
    return '>'.(n+1)
  endif
  return n
endfunction

function FileBrowserFoldText()
  return getline(v:foldstart) . '    ... [' . (v:foldend-v:foldstart+1) . ' lines]'
endfunction
```

```lua
vim.opt.mouse = 'a'
vim.opt.foldminlines = 1
vim.opt.foldcolumn = '2'
vim.opt.fillchars = { fold = '+' }
vim.opt.foldlevel = 0
vim.opt.foldmethod = 'expr'

vim.g.FileBrowserFoldExpr = function()
  local line = vim.fn.getline(vim.v.lnum)
  local n = #line:gsub('[^/]*', '')
  if line:match('^.*/$') then
    return '>' .. n
  elseif vim.fn.getline(vim.v.lnum + 1):sub(1, #line + 1) == line .. '/' then
    return '>' .. (n + 1)
  end
  return n
end

vim.opt.foldexpr = 'v:lua.vim.g.FileBrowserFoldExpr()'

vim.g.FileBrowserFoldText = function()
  return vim.fn.getline(vim.v.foldstart) .. '    ... [' .. (vim.v.foldend - vim.v.foldstart + 1) .. ' lines]'
end

vim.opt.foldtext = 'v:lua.vim.g.FileBrowserFoldText()'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Folding_of_find_locate_tar-tf_output)
***
# Title: Fold Lines Matching Search Pattern
# Category: folding
# Tags: search, folding, regex
---
Create a fold that shows only lines matching a search pattern with optional context lines

```vim
nnoremap \z :setlocal foldexpr=(getline(v:lnum)=~@/)?0:(getline(v:lnum-1)=~@/)||(getline(v:lnum+1)=~@/)?1:2 foldmethod=expr foldlevel=0 foldcolumn=2<CR>
```

```lua
vim.keymap.set('n', '<leader>zf', function()
  vim.wo.foldexpr = 'v:lua.custom_fold_expr()'
  vim.wo.foldmethod = 'expr'
  vim.wo.foldlevel = 0
  vim.wo.foldcolumn = '2'
end, { desc = 'Fold lines matching search' })

function _G.custom_fold_expr()
  local line = vim.fn.getline(vim.v.lnum)
  local prev_line = vim.fn.getline(vim.v.lnum - 1)
  local next_line = vim.fn.getline(vim.v.lnum + 1)
  local search_pattern = vim.fn.getreg('/')
  
  if line:match(search_pattern) then
    return 0
  elseif prev_line:match(search_pattern) or next_line:match(search_pattern) then
    return 1
  else
    return 2
  end
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Folding_with_Regular_Expression)
***
# Title: Quick Java API View via Folding
# Category: folding
# Tags: folding, code-navigation, source-analysis
---
Create a quick overview of methods and variables in a Java source file using regex folding

```vim
command! Japi Foldsearch public\s\|protected\s\|private\s
```

```lua
vim.api.nvim_create_user_command('Japi', function()
  vim.cmd('Foldsearch public\\s\\|protected\\s\\|private\\s')
end, {})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Folding_with_regex)
***
# Title: Flexible Folding Methods in Neovim
# Category: folding
# Tags: folding, code-navigation, productivity
---
Vim/Neovim supports multiple folding methods to help organize and navigate code, including syntax, indent, and manual folding techniques.

```vim
" Set folding method
set foldmethod=syntax

" Limit fold nesting
set foldnestmax=3
```

```lua
-- Set folding method
vim.opt.foldmethod = 'syntax'

-- Limit fold nesting
vim.opt.foldnestmax = 3
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Hide_all_functions_in_your_code)
***
# Title: Advanced Syntax Folding for Java Files
# Category: folding
# Tags: syntax-folding, code-organization, java
---
Custom syntax folding for Java files that intelligently folds methods, constructors, enums, and comments with support for annotations

```vim
" Place in ~/.vim/after/syntax/java.vim

" Fold method definitions with annotations
syn region javaFuncDef start="^\z(\s*\)\%(@[A-Z]\k*\%((\_.\{-}\))\?\s*\)*\%(.\+\)\s\+\%([a-zA-Z$0-9_][$A-Za-z0-9_]*\)\s*(\_.*)\s*{" end="^\z1}\s*$" keepend transparent fold

" Fold multi-line comments
syn region javaMultiLineComment start="/[*]\{1,}" end="[*]/" keepend transparent fold
```

```lua
-- Use in init.lua or after/syntax/java.lua

local api = vim.api

-- Create custom syntax folding for Java
api.nvim_create_autocmd('FileType', {
  pattern = 'java',
  callback = function()
    vim.cmd[[
      syn region javaFuncDef start="^\z(\s*\)\%(@[A-Z]\k*\%((\_.\{-}\))\?\s*\)*\%(.\+\)\s\+\%([a-zA-Z$0-9_][$A-Za-z0-9_]*\)\s*(\_.*)\s*{" end="^\z1}\s*$" keepend transparent fold
      syn region javaMultiLineComment start="/[*]\{1,}" end="[*]/" keepend transparent fold
    ]]
    vim.opt.foldmethod = 'syntax'
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Java/C/C%2B%2B_folding)
***
# Title: Flexible Java Code Folding with Expression
# Category: folding
# Tags: custom-folding, expression-folding, java
---
Custom fold expression function that intelligently handles multi-line JavaDoc comments and code blocks

```vim
function! MyFoldLevel(lineNumber)
  let thisLine = getline(a:lineNumber)
  if (thisLine =~ '\%(\%(/\*\*\).*\%(\/\)\)\|\%({.*}\)')
    return '='
  elseif (thisLine =~ '\%(^\s*/\*\*\s*$\)\|{')
    return "a1"
  elseif (thisLine =~ '\%(^\s*\*/\s*$\)\|}'))
    return "s1"
  endif
  return '='
endfunction
setlocal foldexpr=MyFoldLevel(v:lnum)
setlocal foldmethod=expr
```

```lua
function _G.java_fold_level(line_nr)
  local line = vim.fn.getline(line_nr)
  if line:match('(/\*\*.*%*/)')  -- One-line JavaDoc
    or line:match('{.*}')  -- Single line block
    then
    return '='
  elseif line:match('^%s*/\*\*%s*$') or line:match('{') then
    return 'a1'  -- Start a fold
  elseif line:match('^%s*%*/') or line:match('}') then
    return 's1'  -- End a fold
  end
  return '='
end

vim.cmd.setlocal('foldexpr=v:lua.java_fold_level(v:lnum)')
vim.cmd.setlocal('foldmethod=expr')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Java/C/C%2B%2B_folding)
***
# Title: Dynamic Folding for Java Code Blocks
# Category: folding
# Tags: syntax-folding, code-navigation
---
Implement custom folding for different code structures like methods, loops, try-catch blocks, and comments

```vim
syn region javaMethod start="^\z(\s*\)\(public\|private\|protected\)\(\_.*)\*{\s*$" end="^\z1}\s*$" transparent fold keepend
syn region javaLoop start="^\z(\s*\)\(for\|if\|while\|switch\).*{\s*$" end="^\z1}\s*$" transparent fold keepend
syn region javadoc start="^\s*/\*\*" end="^.*\*/" transparent fold keepend
```

```lua
vim.api.nvim_create_autocmd('FileType', {
  pattern = 'java',
  callback = function()
    vim.cmd([[
      syn region javaMethod start="^\z(\s*\)\(public\|private\|protected\)\(\_.*)\*{\s*$" end="^\z1}\s*$" transparent fold keepend
      syn region javaLoop start="^\z(\s*\)\(for\|if\|while\|switch\).*{\s*$" end="^\z1}\s*$" transparent fold keepend
      syn region javadoc start="^\s*/\*\*" end="^.*\*/" transparent fold keepend
    ]]
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Java/C/Cpp_folding)
***
# Title: Use Vim-Style Folding in Documentation
# Category: folding
# Tags: documentation, folding, text-organization
---
Use marker-based folding to create collapsible sections in text files, making large documents more manageable

```vim
" Modeline for folding
vim:fdm=marker:tw=78:isk=!-~,^*,^\|,^":ts=8:ft=help:norl:

" Example section with folding
==================================================
Commands {{{1
==================================================
```

```lua
-- Set folding method
vim.o.foldmethod = 'marker'

-- Create a buffer with foldable sections
vim.api.nvim_buf_set_lines(0, 0, -1, false, {
  '==================================================',
  'Commands {{{1',
  '=================================================='  
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Keep_a_to-do_memo_file_with_links_as_in_Vim_help)
***
# Title: Use Built-in Folding for Outlining
# Category: folding
# Tags: navigation, text-editing, productivity
---
Leverage Vim's built-in folding functionality for creating document outlines, with multiple plugin options available

```vim
set foldmethod=indent  # Example folding setup
zf  # Create fold
zo  # Open fold
zc  # Close fold
```

```lua
vim.opt.foldmethod = 'indent'
-- Fold commands remain the same in Neovim
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/List_of_Scripts_for_Outlining)
***
# Title: Quick Fold Marker Wrapping
# Category: folding
# Tags: fold-markers, visual-mode, text-editing
---
Create fold markers around a visual selection quickly, useful for organizing code sections

```vim
vmap <Leader>fold mz:<Esc>'<O// {{{<Esc>'>o// }}}<Esc>`z?{{{<CR>A<Space>
```

```lua
vim.keymap.set('v', '<Leader>fold', function()
  -- Save current cursor position
  vim.cmd('normal! mz')
  -- Add fold markers at start and end of visual selection
  vim.cmd('normal! O// {{{\<Esc>j')
  vim.cmd('normal! o// }}}')
  vim.cmd('normal! `z')
  vim.cmd('normal! ?{{{\<CR>A ')
end, { desc = 'Wrap visual selection with fold markers' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip475)
***
# Title: VB.NET Style Folding in Vim/Neovim
# Category: folding
# Tags: folding, language-specific, code-organization
---
Create custom folding for Visual Basic .NET files based on #Region and #End Region markers

```vim
fu! VBFold(lnum)
    if getline(a:lnum) =~# '^\s*#Region'
        return '>1'
    elseif getline(a:lnum) =~# '^\s*#End Region'
        return  '<1'
    else
        return '='
    endif
endfu

fu! VBFoldText()
    return substitute(v:folddashes,'-',' ','g'). matchstr(getline(v:foldstart), '^\s*#Region\s\+\zs.*')
endfu

setl foldenable foldmethod=expr foldexpr=VBFold(v:lnum) foldtext=VBFoldText()
```

```lua
local function vb_fold(lnum)
    local line = vim.fn.getline(lnum)
    if line:match('^%s*#Region') then
        return '>1'
    elseif line:match('^%s*#End Region') then
        return '<1'
    else
        return '='
    end
end

local function vb_fold_text()
    local fold_start_line = vim.fn.getline(vim.v.foldstart)
    local region_name = fold_start_line:match('^%s*#Region%s+(.+)')
    return string.gsub(vim.v.folddashes, '-', ' ') .. (region_name or '')
end

vim.wo.foldenable = true
vim.wo.foldmethod = 'expr'
vim.wo.foldexpr = 'v:lua.vb_fold(v:lnum)'
vim.wo.foldtext = 'v:lua.vb_fold_text()'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip519)
***
# Title: Fold C/C++ Functions Including Prototypes
# Category: folding
# Tags: code-folding, c-language, syntax
---
Custom folding function for C/C++ that includes function prototypes in code folding, allowing more comprehensive code collapse

```vim
function FoldBrace()
  if getline(v:lnum+1)[0] == '{'
    return '>1'
  endif
  if getline(v:lnum)[0] == '}'
    return '<1'
  endif
  return foldlevel(v:lnum-1)
endfunction
set foldexpr=FoldBrace()
set foldmethod=expr
```

```lua
function _G.custom_fold_expr(lnum)
  local next_line = vim.fn.getline(lnum + 1)
  local current_line = vim.fn.getline(lnum)
  
  if next_line:sub(1,1) == '{' then
    return '>1'
  end
  
  if current_line:sub(1,1) == '}' then
    return '<1'
  end
  
  return vim.fn.foldlevel(lnum - 1)
end

vim.opt.foldexpr = 'v:lua.custom_fold_expr(v:lnum)'
vim.opt.foldmethod = 'expr'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip523)
***
# Title: XML Syntax Folding in Vim
# Category: folding
# Tags: xml, syntax-folding, file-type
---
Automatically enable syntax-based folding for XML files

```vim
let g:xml_syntax_folding=1
au FileType xml setlocal foldmethod=syntax
```

```lua
vim.g.xml_syntax_folding = 1
vim.api.nvim_create_autocmd('FileType', {
  pattern = 'xml',
  callback = function()
    vim.wo.foldmethod = 'syntax'
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip583)
***
# Title: Use Vim as a Powerful Outline Processor
# Category: folding
# Tags: outline, folding, indentation
---
Leverage Vim's built-in folding and indentation features to create and manage outlines efficiently

```vim
set ai
set foldmethod=indent

" Promote/demote headlines
:map << to promote
:map >> to demote
```

```lua
vim.opt.autoindent = true
vim.opt.foldmethod = 'indent'

-- Promote/demote can be done with < and > in normal/visual mode
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip74)
***
# Title: Fold Away Lines Not in Quickfix List
# Category: folding
# Tags: quickfix, error-handling, code-navigation
---
Automatically fold lines in the current buffer that are not present in the quickfix or location list, helping focus on relevant code sections with errors or matches

```vim
function! s:FoldMisses(list, context)
  setlocal foldmethod=manual
  normal! zE
  let extra = a:context == 99999 ? g:foldmisses_context : a:context
  let last = 0
  for lnum in s:GetHitLineNumbers(a:list)
    let start = last==0 ? 1 : last+1+extra
    call s:Fold(start, lnum-1-extra)
    let last = lnum
  endfor
  call s:Fold(last+1+extra, line('$'))
endfunction

command! -bar -count=99999 FoldMisses call s:FoldMisses(getqflist(), <count>)
```

```lua
local function fold_misses(list, context)
  vim.wo.foldmethod = 'manual'
  vim.cmd('normal! zE')
  local extra = context == 99999 and vim.g.foldmisses_context or context
  local last = 0
  
  for _, item in ipairs(list) do
    if item.valid and item.bufnr == vim.fn.bufnr('') then
      local start = last == 0 and 1 or last + 1 + extra
      local end_line = item.lnum - 1 - extra
      
      if start < end_line then
        vim.cmd(string.format('%d,%dfold', start, end_line))
      end
      
      last = item.lnum
    end
  end
  
  if last > 0 then
    vim.cmd(string.format('%d,$fold', last + 1 + extra))
  end
end

vim.api.nvim_create_user_command('FoldMisses', function(opts)
  fold_misses(vim.fn.getqflist(), opts.count)
end, { bar = true, count = 99999 })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip76)
***
