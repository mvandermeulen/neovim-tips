# Title: Format with Treesitter
# Category: Formatting
# Tags: treesitter, format, syntax
---
Use `=ap` to format syntax-aware regions using Treesitter (when available).

```vim
=ap  " format around paragraph with Treesitter
```

**Source:** Community contributed
***
# Title: Comment lines by filetype
# Category: Formatting
# Tags: comment, filetype, toggle
---
Automatically comment/uncomment lines based on current file type.

```vim
" Vimscript:
function CommentIt()
  if &filetype == "vim"
    vmap +# :s/^/"/<CR>
    vmap -# :s/^"//<CR>
  elseif &filetype == "python"
    vmap +# :s/^/#/<CR>
    vmap -# :s/^#//<CR>
  endif
endfunction
autocmd BufEnter * call CommentIt()
```

```lua
-- Lua:
local function comment_it()
  local ft = vim.bo.filetype
  if ft == 'vim' then
    vim.keymap.set('v', '+#', ':s/^/"/<CR>', { buffer = true })
    vim.keymap.set('v', '-#', ':s/^"//<CR>', { buffer = true })
  elseif ft == 'python' then
    vim.keymap.set('v', '+#', ':s/^/#/<CR>', { buffer = true })
    vim.keymap.set('v', '-#', ':s/^#//<CR>', { buffer = true })
  end
end

vim.api.nvim_create_autocmd('BufEnter', {
  pattern = '*',
  callback = comment_it,
  desc = 'Setup comment mappings by filetype'
})
```

**Source:** Community contributed
***
# Title: Poor men's JSON formatter
# Category: Formatting
# Tags: text, format, json
---
A poor men's json formatter using `vim.json.decode` + `vim.json.encode`:
You can put it in `ftplugin/json.lua`. Only works for the whole file, e.g. with `gggqG`
[Credits: yochem](https://github.com/neovim/neovim/discussions/35683)

```lua
function _G.json_formatter()
	-- from $VIMRUNTIME/lua/vim/lsp.lua
	if vim.list_contains({ 'i', 'R', 'ic', 'ix' }, vim.fn.mode()) then
		return 1
	end
	local indent = vim.bo.expandtab and '\t' or string.rep(' ', vim.o.tabstop)

	local lines = vim.api.nvim_buf_get_lines(0, vim.v.lnum - 1, vim.v.count, true)
	local deco = vim.json.decode(table.concat(lines, '\n'))
	local enco = vim.json.encode(deco, { indent = indent })
	local split = vim.split(enco, '\n')
	vim.api.nvim_buf_set_lines(0, vim.v.lnum - 1, vim.v.count, true, split)

	return 0
end

vim.bo.formatexpr = 'v:lua.json_formatter()'
```

**Source:** Community contributed
***
# Title: Wrap Lines at 80 Chars Without Breaking Words
# Category: formatting
# Tags: text-formatting, line-wrap, editing
---
Format text to wrap at 80 characters without breaking words mid-line, useful for maintaining readable code or text

```vim
set formatoptions+=w
set tw=80
gggqG

" Mapping to format current paragraph
nnoremap Q gqip
```

```lua
-- Set text width and format options
vim.opt.formatoptions:append('w')
vim.opt.textwidth = 80

-- Format entire file
vim.cmd('normal! gggqG')

-- Mapping to format current paragraph
vim.keymap.set('n', 'Q', 'gqip', { desc = 'Format current paragraph' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/80_character_line_wrap_without_broken_words)
***
# Title: Align Numbers at Decimal Point
# Category: formatting
# Tags: text-alignment, number-formatting, substitution
---
Easily align text into columns using an external Perl script, helpful for formatting code or config files

```vim
:vmap <A-a> !perl ~/perl/align -c:=
```

```lua
-- Note: Requires external Perl script
vim.keymap.set('v', '<A-a>', function()
  vim.cmd('!perl ~/perl/align -c:=')
end, { desc = 'Align text into columns' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Align_text_into_a_table)
***
# Title: Automatic Text Wrapping for Plain Text
# Category: formatting
# Tags: text-formatting, writing, configuration
---
Set text width to automatically break lines at a specified character length, useful for plain text editing

```vim
" Set text width to 60 characters
:setlocal textwidth=60
:setl tw=60
```

```lua
-- Set text width to 60 characters
vim.opt.textwidth = 60
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Automatic_formatting_of_paragraphs)
***
# Title: Automatically Indent XML Files
# Category: formatting
# Tags: xml, indentation, autocmd
---
Automatically indent XML files using XSLT or a simple text replacement method

```vim
if version >= 540
  augroup filetype
    autocmd FileType xml '[,']!xsltproc indent.xsl %
  augroup END
endif
```

```lua
vim.api.nvim_create_autocmd('FileType', {
  pattern = 'xml',
  callback = function()
    -- Use xsltproc to indent XML file
    vim.cmd('!xsltproc indent.xsl %')
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Automatically_indent_an_XML_file_using_XSLT)
***
# Title: Quick XML Indentation Without XSLT
# Category: formatting
# Tags: xml, text-replacement
---
Simple method to indent XML/HTML files using search and replace followed by auto-indentation

```vim
:%s/></>
</g
gg=G
```

```lua
function IndentXML()
  -- Replace ><, add newline, then auto-indent entire file
  vim.cmd('%%s/></>
</g')
  vim.cmd('normal! gg=G')
end

-- Optional: create a command
vim.api.nvim_create_user_command('IndentXML', IndentXML, {})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Automatically_indent_an_XML_file_using_XSLT)
***
# Title: Powerful Text Formatting with Par
# Category: formatting
# Tags: text-processing, external-tool, formatting
---
Use the 'par' external tool for advanced text formatting and justification within Vim/Neovim

```vim
set formatprg=par\ -w60
map <A-q> {v}!par -jw60<CR>
vmap <A-q> !par -jw60<CR>
```

```lua
vim.opt.formatprg = 'par -w60'
vim.keymap.set({'n', 'v'}, '<A-q>', function()
  vim.cmd('normal! {v}!par -jw60\<CR>')
end, { desc = 'Format text with Par' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Awesome_text_formatter)
***
# Title: Clean Up HTML Files with Tidy
# Category: formatting
# Tags: html, formatting, external-tool
---
Use the Tidy external tool to automatically format and clean up HTML and XML files directly in Vim/Neovim

```vim
" Tidy mapping for HTML cleanup
:vmap ,x :!tidy -q -i --show-errors 0<CR>

" Command to tidy entire HTML file
:command Thtml :%!tidy -q -i --show-errors 0
```

```lua
-- Tidy mapping for HTML cleanup
vim.keymap.set('v', ',x', function()
  vim.cmd('!tidy -q -i --show-errors 0')
end, { desc = 'Tidy HTML formatting' })

-- Command to tidy entire HTML file
vim.api.nvim_create_user_command('Thtml', '%!tidy -q -i --show-errors 0', {})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Cleanup_your_HTML)
***
# Title: Convert Code to Syntax-Highlighted HTML
# Category: formatting
# Tags: html, syntax-highlighting, code-export
---
Easily convert Vim/Neovim buffer to HTML with syntax coloring for sharing code in emails or forums

```vim
:TOhtml

" Optional: Switch to light colorscheme first
:colorscheme default
```

```lua
-- Use built-in :TOhtml command
-- For light background before conversion
vim.cmd('colorscheme default')
vim.cmd('TOhtml')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Convert_selected_text_to_HTML)
***
# Title: Clean Paragraphs for Copy-Paste to Word
# Category: formatting
# Tags: text-manipulation, copy-paste, formatting
---
Remove single newlines while preserving paragraph breaks when copying text to Word or other applications

```vim
vmap <C-C> '+y:let @+ = substitute(@+, "\n\n\n*", "±", "g")\|:let @+ = substitute(@+, "\n", " ", "g")\|:let @+ = substitute(@+, "±", "\n", "g")<CR>\|'<
```

```lua
vim.keymap.set('v', '<C-C>', function()
  -- Copy visual selection
  vim.cmd('normal! "+y')
  local text = vim.fn.getreg('+')
  
  -- Remove single newlines, preserve paragraph breaks
  text = text:gsub('\n\n+', '±')
  text = text:gsub('\n', ' ')
  text = text:gsub('±', '\n')
  
  vim.fn.setreg('+', text)
end, { desc = 'Clean paragraphs for Word copy' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Copy_paragraphs_without_excess_newlines_to_MS_Word)
***
# Title: Collapse Multi-Line Paragraphs
# Category: formatting
# Tags: text-manipulation, global-command
---
Quickly join lines within paragraphs, removing unnecessary line breaks

```vim
:v/^\s*$/norm vipJ
```

```lua
vim.cmd(':%s/\v(\S+)\n(\S+)/\1 \2/ge')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Copy_paragraphs_without_excess_newlines_to_MS_Word)
***
# Title: Expand Tabs to Spaces in Entire File
# Category: formatting
# Tags: indentation, whitespace, code-style
---
Convert all tab indents to spaces in the current file

```vim
:set et|retab
```

```lua
vim.opt.expandtab = true
vim.cmd('retab!')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Did_you_know/2009)
***
# Title: Reformat Email Quotations Quickly
# Category: formatting
# Tags: email, text-formatting, text-objects
---
Quickly fix indentation for entire file or selected text using built-in = operator

```vim
" Reindent entire file
gg=G

" Reindent selected text in visual mode
V=

" Quick mapping to reindent and return to original position
map <F7> gg=G<C-o><C-o>
```

```lua
-- Reindent entire file
vim.cmd('normal! gg=G')

-- Reindent in visual mode
vim.cmd('normal! gv=')

-- Quick mapping to reindent file and return to original position
vim.keymap.set('n', '<F7>', function()
  vim.cmd('normal! gg=G')
  vim.cmd('normal! \<C-o>\<C-o>')
end, { desc = 'Reindent entire file' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Fix_indentation)
***
# Title: Format Code Blocks and Functions Easily
# Category: formatting
# Tags: text-objects, code-formatting, indentation
---
Use text objects to quickly format code blocks, functions, or entire files with built-in formatting operators

```vim
=i{  " Format inner code block
gg=G  " Format entire buffer
```

```lua
vim.cmd('normal =i{')  -- Format inner code block
vim.cmd('normal gg=G')  -- Format entire buffer
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Format_a_code_block)
***
# Title: Format Only Long Lines in Text
# Category: formatting
# Tags: text-formatting, text-manipulation, line-wrapping
---
Intelligently format only lines longer than a specified width without merging short lines

```vim
:g/./ normal gqq

# Alternative for lines 80 chars or longer
:g/\{80,\}/ .!par w70
```

```lua
-- Format only lines with content
vim.cmd('g/./ normal gqq')

-- Format lines 80 chars or longer using external tool
vim.cmd('g/\{80,\}/ .!par w70')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Format_only_long_lines)
***
# Title: Format Paragraph Without Moving Cursor
# Category: formatting
# Tags: text-formatting, cursor-position
---
Format the current paragraph while keeping the cursor in its original position

```vim
gqap  " Format paragraph
gwap  " Format paragraph and restore cursor
```

```lua
vim.cmd('normal! gwap')  -- Format paragraph and restore cursor position
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Format_paragraph_without_changing_the_cursor_position)
***
# Title: Format XML Files Using xmllint
# Category: formatting
# Tags: xml, external-tools, formatting
---
Automatically format XML files using xmllint, which can clean up and standardize XML document indentation

```vim
au FileType xml exe ":silent %!xmllint --format --recover - 2>/dev/null"
```

```lua
vim.api.nvim_create_autocmd('FileType', {
  pattern = 'xml',
  callback = function()
    vim.cmd('silent %!xmllint --format --recover - 2>/dev/null')
  end
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Format_your_xml_document_using_xmllint)
***
# Title: Environment-Aware Paragraph Formatting in LaTeX
# Category: formatting
# Tags: latex, text-formatting, mapping
---
Provides a custom mapping to format LaTeX paragraphs while respecting environments like equations and labels

```vim
map \gq ?^$\|^\s*\(\\begin\|\\end\|\\label\)?1<CR>gq//-1<CR>
omap lp ?^$\|^\s*\(\\begin\|\\end\|\\label\)?1<CR>//-1<CR>.<CR>
```

```lua
vim.keymap.set('n', '<leader>gq', function()
  -- Use Vim's search and formatting commands
  vim.cmd('?^$\|^\s*\(\\begin\|\\end\|\\label\)\|\n?1')
  vim.cmd('normal! gq')
  vim.cmd('/')
end, { desc = 'Format LaTeX paragraph respecting environments' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Formatting_paragraphs_in_LaTeX:_an_%22environment-aware_gqap%22)
***
# Title: Flexible Line Formatting
# Category: formatting
# Tags: text-formatting, key-mapping
---
Quickly format a block of text to a specific width using a custom mapping

```vim
map st :set tw=70<CR>v<S-}>gq<End>
```

```lua
vim.keymap.set('n', 'st', function()
  vim.opt.textwidth = 70
  -- Equivalent of visual select block and format
  vim.cmd('normal! v}gq')
end, { desc = 'Format text block to 70 characters' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Formatting_stuff)
***
# Title: Convert CSV to Readable Columns
# Category: formatting
# Tags: csv, text-manipulation, data-parsing
---
Easily convert CSV data into more readable columnar format by setting fixed-width columns

```vim
let width = 20
let fill = repeat(' ', width)
:%s/([^,]*),\=/\=strpart(submatch(1).fill, 0, width)/ge
:%s/\s\+$//ge
```

```lua
local function format_csv_columns(width)
  width = width or 20
  local fill = string.rep(' ', width)
  vim.cmd(':%s/([^,]*),\\=/\\=strpart(submatch(1).."' .. fill .. '", 0, ' .. width .. ')/ge')
  vim.cmd(':%s/\\s\\+$//ge')
end

-- Usage: :lua format_csv_columns(20)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Navigate_large_CSV_files_more_easily)
***
# Title: Unicode Text Formatting Workaround
# Category: formatting
# Tags: unicode, text-processing, encoding
---
Handle Unicode text formatting with iconv when using 'par'

```vim
# Unicode conversion for par formatting
# cat file | iconv -f utf-8 -t <encoding> | par <options> | iconv -f <encoding> -t utf-8
```

```lua
-- Unicode formatting function (example)
function format_unicode_text(file, from_encoding, to_encoding, par_options)
  local cmd = string.format(
    'cat %s | iconv -f %s -t %s | par %s | iconv -f %s -t utf-8',
    file, from_encoding, to_encoding, par_options, to_encoding
  )
  return vim.fn.system(cmd)
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Par_text_reformatter)
***
# Title: Convert Spaces to Tabs Efficiently
# Category: formatting
# Tags: indentation, file-formatting, whitespace
---
Quickly convert spaces to tabs with consistent indentation across different tab sizes

```vim
:ret! 2
:x
```

```lua
vim.cmd('ret! 2')
vim.cmd('x')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Preexisting_code_indentation)
***
# Title: Pretty Format XML with External Tools
# Category: formatting
# Tags: xml, external-tools, text-processing
---
Easily format XML files using external tools like xmllint or Python, with support for both whole file and visual range formatting

```vim
function! DoPrettyXML()
  let l:origft = &ft
  set ft=
  1s/<?xml .*?>//e
  0put ='<PrettyXML>'
  $put ='</PrettyXML>'
  silent %!xmllint --format -
  2d
  $d
  silent %<
  1
  exe "set ft=" . l:origft
endfunction
command! PrettyXML call DoPrettyXML()
```

```lua
function _G.pretty_xml()
  local orig_ft = vim.bo.filetype
  vim.bo.filetype = ''
  
  -- Remove XML header
  vim.cmd('1s/<?xml .*?>//e')
  
  -- Add fake tags
  vim.api.nvim_buf_set_lines(0, 0, 0, false, {'<PrettyXML>'})
  vim.api.nvim_buf_set_lines(0, -1, -1, false, {'</PrettyXML>'})
  
  -- Format with xmllint
  vim.fn.systemlist('xmllint --format -')
  
  -- Remove fake tags
  vim.cmd('2d')
  vim.cmd('$d')
  
  -- Restore filetype
  vim.bo.filetype = orig_ft
end

vim.api.nvim_create_user_command('PrettyXML', _G.pretty_xml, {})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Pretty-formatting_XML)
***
# Title: Quick XML Formatting with Python
# Category: formatting
# Tags: xml, text-processing, python
---
Simple one-line command to format XML using Python's minidom, with a convenient mapping

```vim
com! FormatXML :%!python3 -c "import xml.dom.minidom, sys; print(xml.dom.minidom.parse(sys.stdin).toprettyxml())"

nnoremap = :FormatXML<Cr>
```

```lua
vim.api.nvim_create_user_command('FormatXML', function()
  vim.cmd("%!python3 -c 'import xml.dom.minidom, sys; print(xml.dom.minidom.parse(sys.stdin).toprettyxml())'") 
end, {})

vim.keymap.set('n', '=', ':FormatXML<CR>', { noremap = true, silent = true })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Pretty-formatting_XML)
***
# Title: Regex-Based Text Alignment Function
# Category: formatting
# Tags: text-alignment, regex, editing
---
Dynamically align text based on a regex pattern, such as aligning assignment statements or function declarations

```vim
function! AlignSection(regex) range
  let extra = 1
  let sep = empty(a:regex) ? '=' : a:regex
  let maxpos = 0
  let section = getline(a:firstline, a:lastline)
  for line in section
    let pos = match(line, ' *'.sep)
    if maxpos < pos
      let maxpos = pos
    endif
  endfor
  call map(section, 'AlignLine(v:val, sep, maxpos, extra)')
  call setline(a:firstline, section)
endfunction
```

```lua
function M.align_section(regex)
  local extra = 1
  local sep = vim.fn.empty(regex) and '=' or regex
  local maxpos = 0
  local section = vim.api.nvim_buf_get_lines(0, vim.fn.line('.')-1, vim.fn.line('v')-1, false)
  
  for _, line in ipairs(section) do
    local pos = line:find(' *'..sep)
    maxpos = math.max(maxpos, pos or 0)
  end

  -- Implementation would require additional helper functions for full conversion
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Regex-based_text_alignment)
***
# Title: Quick XML/HTML Indentation Trick
# Category: formatting
# Tags: xml, indentation, text-manipulation
---
Simple method to indent XML/HTML files without external tools

```vim
:%s/></>
</g
gg=G
```

```lua
-- Split tags onto new lines and then indent
vim.api.nvim_command(':%s/></>
</g')
vim.api.nvim_command('gg=G')
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip551)
***
# Title: Automatic Table Field Alignment
# Category: formatting
# Tags: text-alignment, tables, editing
---
Automatically realign table rows to match the heading row's field widths, making table editing more consistent

```vim
" Alignment mapping
map <Leader>ta :AlignTableFields<CR>
```

```lua
-- Lua conceptual implementation
function _G.align_table_fields()
  -- Implement table field alignment logic
end

vim.keymap.set('n', '<Leader>ta', _G.align_table_fields)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip554)
***
# Title: Add Line Numbers Using Perl Filter
# Category: formatting
# Tags: line-numbering, external-filter, text-manipulation
---
Quickly add line numbers to the entire file using a Perl one-liner within Vim

```vim
:amenu Mo1.Format.NumberLines<Tab>:!perl :1,$!perl -ne "printf("%3d:%s",$.,$$_);"
```

```lua
vim.keymap.set('n', '<Leader>nl', function()
  vim.cmd(':%!perl -ne "printf("%3d:%s",$.,$$_)"')
end, { desc = 'Number lines' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip569)
***
# Title: Align Text into Columns Automatically
# Category: formatting
# Tags: text-alignment, formatting, perl-script
---
Quickly align text with equal spacing around a delimiter (like '=') using an external Perl script

```vim
:vmap <A-a> !perl ~/perl/align -c:=
```

```lua
-- Note: Requires external Perl script
-- Can be implemented with more modern Lua alignment plugins
vim.keymap.set('v', '<A-a>', '!perl ~/perl/align -c:=', { desc = 'Align text columns' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip570)
***
# Title: Chop Long Lines Using fmt Command
# Category: formatting
# Tags: text-formatting, command-line, external-tools
---
Easily break long lines to a specified width using the external fmt command in Vim, with multiple application methods

```vim
" Chop lines 1-10 to default width
:1,10!fmt

" In visual block mode
'v' to select block
'!fmt<Enter>'
```

```lua
-- For lines 1-10
vim.cmd('1,10!fmt')

-- In Neovim, can use vim.fn.feedkeys for visual block fmt
vim.keymap.set('v', '<leader>f', function()
  vim.fn.feedkeys('!fmt\<CR>', 'n')
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip575)
***
# Title: Quick Line Formatting with gqq
# Category: formatting
# Tags: text-formatting, built-in-commands
---
Native Vim method to break long lines without external tools or regex

```vim
gqq  " Format current line
```

```lua
-- Equivalent native Neovim formatting
vim.cmd('normal gqq')

-- Or using keymap
vim.keymap.set('n', '<leader>q', 'gqq', { desc = 'Format current line' })
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip575)
***
