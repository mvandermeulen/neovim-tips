# Title: Advanced PHP Function Documentation Viewer
# Category: advanced_functions
# Tags: documentation, function-lookup, split-window
---
Create a custom function to open PHP function documentation in a preview window with clean formatting

```vim
function! OpenPhpFunction (keyword)
  let proc_keyword = substitute(a:keyword , '_', '-', 'g')
  exe 'pedit'
  exe 'wincmd P'
  exe 'enew'
  exe "set buftype=nofile"
  exe 'silent r!lynx -dump -nolist http://php.net/'.proc_keyword
  " Additional formatting commands...
endfunction
```
```lua
function _G.open_php_function(keyword)
  local proc_keyword = keyword:gsub('_', '-')
  vim.cmd('pedit')
  vim.cmd('wincmd P')
  vim.cmd('enew')
  vim.bo.buftype = 'nofile'
  vim.fn.system('lynx -dump -nolist http://php.net/' .. proc_keyword)
end

-- Map to a key in PHP files
vim.api.nvim_create_autocmd('FileType', {
  pattern = 'php',
  callback = function()
    vim.keymap.set('n', 'K', function()
      _G.open_php_function(vim.fn.expand('<cword>'))
    end, { buffer = true })
  end
})
```

**Source:** ** https://vim.fandom.com/wiki/(PHP)_on_line_help
***
# Title: Automatic Java Import Generation
# Category: advanced_functions
# Tags: java, import-management, productivity
---
Quickly insert Java import statements for classes under cursor using a custom function with error handling and preview window management

```vim
function! JavaInsertImport()
  exe "normal mz"
  let cur_class = expand("<cword>")
  try
    if search('^\s*import\s.*\.' . cur_class . '\s*;') > 0
      throw getline('.') . ": import already exist!"
    endif
    wincmd }
    wincmd P
    1
    if search('^\s*public.*\s\%(class\|interface\)\s\+' . cur_class) > 0
      1
      if search('^\s*package\s') > 0
        yank y
      else
        throw "Package definition not found!"
      endif
    else
      throw cur_class . ": class not found!"
    endif
    wincmd p
    normal! G
    if search('^\s*import\s', 'b') > 0
      put y
    else
      1
      put! y
    endif
    substitute/^\s*package/import/g
    substitute/\s\+/ /g
    exe "normal! 2ER." . cur_class . ";\<Esc>lD"
  catch /.*/
    echoerr v:exception
  finally
    silent! wincmd P
    if &previewwindow
      bwipeout
    endif
    exe "normal! `z"
  endtry
endfunction

noremap <F5> :call JavaInsertImport()<CR>
```
```lua
function _G.java_insert_import()
  local cur_class = vim.fn.expand('<cword>')
  
  local ok, result = pcall(function()
    -- Check if import already exists
    if vim.fn.search('^\s*import\s.*\.' .. cur_class .. '\s*;') > 0 then
      error('Import already exists')
    end
    
    -- Open preview window with tag
    vim.cmd('wincmd }')
    vim.cmd('wincmd P')
    
    -- Find package and class/interface definition
    vim.cmd('normal! 1G')
    if vim.fn.search('^\s*public.*\s\%(class\|interface\)\s\+' .. cur_class) == 0 then
      error('Class/interface not found')
    end
    
    local package_line = vim.fn.search('^\s*package\s')
    if package_line == 0 then
      error('Package definition not found')
    end
    
    -- Copy package line and convert to import
    local package = vim.fn.getline(package_line)
    local import_line = package:gsub('^%s*package', 'import'):gsub(';$', '') .. '.' .. cur_class .. ';'
    
    -- Return to original window and insert import
    vim.cmd('wincmd p')
    vim.cmd('normal! G')
    
    local import_pos = vim.fn.search('^\s*import\s', 'b')
    if import_pos > 0 then
      vim.fn.append(import_pos, import_line)
    else
      vim.fn.append(0, import_line)
    end
  end)
  
  if not ok then
    print('Error: ' .. result)
  end
  
  -- Clean up preview window
  vim.cmd('silent! wincmd P')
  if vim.wo.previewwindow then
    vim.cmd('bwipeout')
  end
end

vim.keymap.set('n', '<F5>', _G.java_insert_import, { desc = 'Insert Java Import' })
```

**Source:** ** https://vim.fandom.com/wiki/Add_Java_import_statements_automatically
***
# Title: Flexible Heading Underline Function
# Category: advanced_functions
# Tags: text-formatting, custom-function, user-command
---
Create a flexible function to underline text with various characters, adaptable to different document styles

```vim
function! s:Underline(chars)
  let chars = empty(a:chars) ? '-' : a:chars
  let nr_columns = virtcol('$') - 1
  let uline = repeat(chars, (nr_columns / len(chars)) + 1)
  put =strpart(uline, 0, nr_columns)
endfunction
command! -nargs=? Underline call s:Underline(<q-args>)
```
```lua
-- Flexible underline function in Lua
local function underline(chars)
  chars = chars or '-'
  local line = vim.api.nvim_get_current_line()
  local line_length = vim.fn.virtcol('$') - 1
  
  -- Create underline repeating the character(s)
  local uline = string.rep(chars, math.floor(line_length / #chars) + 1)
  uline = uline:sub(1, line_length)
  
  -- Insert underline after current line
  vim.api.nvim_buf_set_lines(0, vim.fn.line('.'), vim.fn.line('.'), false, {line, uline})
end

-- Create user command
vim.api.nvim_create_user_command('Underline', function(opts)
  underline(opts.args ~= '' and opts.args or nil)
end, { nargs = '?' })
```

**Source:** ** https://vim.fandom.com/wiki/Add_a_dashed_line_under_a_title_in_text_documents
***
# Title: Smart Preprocessor Directive Commenter
# Category: advanced_functions
# Tags: code-commenting, preprocessor, c-language
---
Automatically adds contextual comments to preprocessor directives like #endif and #else, improving code readability by explaining the purpose of conditional compilation blocks

```vim
function! SmartPreProcCommenter()
  mark y
  let saved_wrapscan=&wrapscan
  set nowrapscan
  let elsecomment=""
  let endcomment=""
  try
    $?^\s*#if
    while 1
      let content=getline('.')
      let elsecomment=BuildElseComment(content,elsecomment)
      let endcomment=BuildEndComment(content,endcomment)
      s/^\s*\zs#/##
      /^\s*#\(elif\|else\|endif\)
      let content=getline('.')
      if match(content,'^\s*#elif') != -1
        continue
      elseif match(content,'^\s*#else') != -1
        call setline('.',ReplaceComment(content,elsecomment))
        s/^\s*\zs#/##
        /^\s*#endif
      endif
      call setline('.',ReplaceComment(getline('.'),endcomment))
      s/^\s*\zs#/##
      ?^\s*#if
    endwhile
  catch /search hit TOP/
    silent! %s/^\s*\zs##/#
  endtry
  let &wrapscan=saved_wrapscan
  normal `y
endfunc
```
```lua
function SmartPreProcCommenter()
  vim.cmd('mark y')
  local saved_wrapscan = vim.o.wrapscan
  vim.o.wrapscan = false
  local elsecomment = ""
  local endcomment = ""
  
  local ok, err = pcall(function()
    vim.cmd('$?^\s*#if')
    while true do
      local content = vim.fn.getline('.')
      elsecomment = BuildElseComment(content, elsecomment)
      endcomment = BuildEndComment(content, endcomment)
      
      vim.cmd('s/^\s*\zs#/##')
      vim.cmd('/^\s*#\(elif\|else\|endif\)')
      
      content = vim.fn.getline('.')
      if content:match('^\s*#elif') then
        -- continue
      elseif content:match('^\s*#else') then
        vim.fn.setline('.', ReplaceComment(content, elsecomment))
        vim.cmd('s/^\s*\zs#/##')
        vim.cmd('/^\s*#endif')
      end
      
      vim.fn.setline('.', ReplaceComment(vim.fn.getline('.'), endcomment))
      vim.cmd('s/^\s*\zs#/##')
      vim.cmd('?^\s*#if')
    end
  end)
  
  if not ok and err:match('search hit TOP') then
    vim.cmd('silent! %s/^\s*\zs##/#')
  end
  
  vim.o.wrapscan = saved_wrapscan
  vim.cmd('normal `y')
end
```

**Source:** ** https://vim.fandom.com/wiki/Automatic_Commenting_of_Preprocessor_Directives_in_C
***
# Title: Generate Web Forum Compatible HTML Snippet
# Category: advanced_functions
# Tags: html, code-export, custom-function
---
Create a function to generate HTML code snippets that work across different web platforms

```vim
function! MyToHtml(line1, line2)
  let g:html_use_css = 0
  exec a:line1.','.a:line2.'TOhtml'
  %g/<body/normal k$dgg
  %s/<body\s*\(bgcolor="[^"]*"\)\s*text=\("[^"]*"\)\s*>/<table \1 cellPadding=0><tr><td><font color=\2>/
  %s#</body>\(.|\n\)*</html>#\='</font></td></tr></table>'#i
endfunction
command! -range=% MyToHtml :call MyToHtml(<line1>,<line2>)
```
```lua
function _G.my_to_html(line1, line2)
  vim.g.html_use_css = 0
  vim.cmd(string.format('%d,%dTOhtml', line1, line2))
  -- Additional HTML manipulation logic would be translated here
end

vim.api.nvim_create_user_command('MyToHtml', function(opts)
  _G.my_to_html(opts.line1, opts.line2)
end, { range = true })
```

**Source:** ** https://vim.fandom.com/wiki/Convert_selected_text_to_HTML
***
# Title: Advanced CSV Column Navigation and Manipulation
# Category: advanced_functions
# Tags: csv, data-processing, text-manipulation
---
Provides powerful navigation and manipulation features for CSV files, including column highlighting, searching within columns, and sorting by specific columns

```vim
function! CSVH(colnr)
  if a:colnr > 1
    let n = a:colnr - 1
    execute 'match Keyword /^\([^,]*,\)\{'.n.'}\zs[^,]*'
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
    vim.cmd(string.format('match Keyword /^([^,]*,){%d}\\zs[^,]*/', n))
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

**Source:** ** https://vim.fandom.com/wiki/Csv
***
# Title: Dynamically Display Current Function Name
# Category: advanced_functions
# Tags: function-detection, code-navigation, cursor-context
---
A function to detect and display the name of the current function, even in nested contexts like control statements or nested functions

```vim
function WhatFunctionAreWeIn()
  let strList = ["while", "foreach", "ifelse", "if else", "for", "if", "else", "try", "catch", "case", "switch"]
  let foundcontrol = 1
  let position = ""
  let pos=getpos(".")
  let view=winsaveview()
  while (foundcontrol)
    let foundcontrol = 0
    normal [{
    call search('\S','bW')
    let tempchar = getline(".")[col(".") - 1]
    if (match(tempchar, ")") >=0 )
      normal %
      call search('\S','bW')
    endif
    let tempstring = getline(".")
    for item in strList
      if( match(tempstring,item) >= 0 )
        let position = item . " - " . position
        let foundcontrol = 1
        break
      endif
    endfor
    if(foundcontrol == 0)
      call cursor(pos)
      call winrestview(view)
      return tempstring.position
    endif
  endwhile
  call cursor(pos)
  call winrestview(view)
  return tempstring.position
endfunction
```
```lua
function _G.WhatFunctionAreWeIn()
  local strList = {"while", "foreach", "ifelse", "if else", "for", "if", "else", "try", "catch", "case", "switch"}
  local foundcontrol = true
  local position = ""
  local pos = vim.fn.getpos(".")
  local view = vim.fn.winsaveview()
  
  while foundcontrol do
    foundcontrol = false
    vim.cmd('normal! [')
    vim.fn.search('\S', 'bW')
    local tempchar = vim.fn.getline("."):sub(vim.fn.col("."), vim.fn.col("."))
    
    if tempchar:match(")") then
      vim.cmd('normal! %')
      vim.fn.search('\S', 'bW')
    end
    
    local tempstring = vim.fn.getline(".")
    for _, item in ipairs(strList) do
      if tempstring:find(item) then
        position = item .. " - " .. position
        foundcontrol = true
        break
      end
    end
    
    if not foundcontrol then
      vim.fn.cursor(pos[2], pos[3])
      vim.fn.winrestview(view)
      return tempstring .. position
    end
  end
  
  vim.fn.cursor(pos[2], pos[3])
  vim.fn.winrestview(view)
  return tempstring .. position
end

-- Optional: Create a command to call the function
vim.api.nvim_create_user_command('ShowCurrentFunction', function()
  print(_G.WhatFunctionAreWeIn())
end, {})
```

**Source:** ** https://vim.fandom.com/wiki/Display_the_name_of_the_function_you_are_editing
***
# Title: Screen-Aware Command Execution
# Category: advanced_functions
# Tags: terminal, command-execution, screen
---
Dynamically modify command execution based on whether Screen is running

```vim
if match($TERM, "screen")!=-1
  let g:GNU_Screen_used = 1
else
  let g:GNU_Screen_used = 0
endif

function InScreen(command)
  return g:GNU_Screen_used ? 'screen '.a:command : a:command
endfunction
```
```lua
local function is_screen_running()
  return vim.env.TERM:match("screen") ~= nil
end

vim.g.gnu_screen_used = is_screen_running()

local function in_screen(command)
  return vim.g.gnu_screen_used and "screen " .. command or command
end
```

**Source:** ** https://vim.fandom.com/wiki/GNU_Screen_integration
***
# Title: Generate Java Bean Getters and Setters
# Category: advanced_functions
# Tags: java, code-generation, text-manipulation
---
Quickly generate Java bean getter and setter methods for a variable by prompting for name and type

```vim
function! s:AddBean()
  let line = line('.')
  let name = inputdialog('Enter the name of the variable: ')
  let type = inputdialog('Enter the type of the variable: ')
  let upperName = substitute(name, '^(\w)(.*)
$', '\u\1\2', '')
  call append(line, "\t}")
  call append(line, "\t\tthis.".name." = ".name.";")
  call append(line, "\tpublic void set".upperName."(".type." ".name.") {")
  call append(line, "")
  call append(line, "\t}")
  call append(line, "\t\treturn (this.".name.");")
  call append(line, "\tpublic ".type." get""".upperName."() { ")
  call append(line, "")
  call append(line, "\tprivate ".type." ".name.";")
  call append(line, "\t//".name)
  return line
endfunction

nnoremap <buffer> <silent>dc :call <SID>AddBean()<CR>
```
```lua
local function add_bean()
  local line = vim.fn.line('.')
  local name = vim.fn.input('Enter the name of the variable: ')
  local type = vim.fn.input('Enter the type of the variable: ')
  local upper_name = name:gsub('^%l', string.upper)

  local bean_lines = {
    string.format('	private %s %s;', type, name),
    string.format('	//%s', name),
    string.format('	public %s get%s() {', type, upper_name),
    '		return this.' .. name .. ';',
    '	}',
    string.format('	public void set%s(%s %s) {', upper_name, type, name),
    '		this.' .. name .. ' = ' .. name .. ';',
    '	}'
  }

  vim.api.nvim_buf_set_lines(0, line, line, false, bean_lines)
end

vim.keymap.set('n', 'dc', add_bean, { buffer = true, silent = true })
```

**Source:** ** https://vim.fandom.com/wiki/JavaBeans_helper_function
***
# Title: Dynamic Footnote Insertion with Vim Function
# Category: advanced_functions
# Tags: text-editing, markdown, functions, footnotes
---
A flexible Vim function to insert and manage footnotes dynamically, with numbering and positioning near signatures

```vim
function! VimFootnotes()
  if exists("b:vimfootnotenumber")
    let b:vimfootnotenumber = b:vimfootnotenumber + 1
    let cr = ""
  else
    let b:vimfootnotenumber = 0
    let cr = "\<CR>"
  endif
  let b:pos = line('.') . ' | normal! ' . virtcol('.') . '|' . '4l'
  exe "normal a[" . b:vimfootnotenumber . "]\<Esc>G"
  if search("-- $", "b")
    exe "normal O" . cr . "[" . b:vimfootnotenumber . "] "
  else
    exe "normal o" . cr . "[" . b:vimfootnotenumber . "] "
  endif
  startinsert!
endfunction
```
```lua
function _G.vim_footnotes()
  local footnote_number = vim.b.vimfootnotenumber or 0
  local cr = footnote_number == 0 and '\n' or ''
  
  footnote_number = footnote_number + 1
  vim.b.vimfootnotenumber = footnote_number

  -- Insert footnote marker
  vim.api.nvim_feedkeys(string.format('[%d]', footnote_number), 'n', false)
  vim.api.nvim_command('normal! G')

  -- Check for signature and place footnote appropriately
  if vim.fn.search('-- $', 'b') > 0 then
    vim.api.nvim_command('normal! O' .. cr .. string.format('[%d] ', footnote_number))
  else
    vim.api.nvim_command('normal! o' .. cr .. string.format('[%d] ', footnote_number))
  end

  vim.cmd('startinsert!')
end

-- Map to a key (example)
vim.keymap.set('i', '<C-f>', _G.vim_footnotes, { desc = 'Insert Footnote' })
```

**Source:** ** https://vim.fandom.com/wiki/Make_footnotes_in_vim
***
# Title: Flexible Compilation Function
# Category: advanced_functions
# Tags: compilation, file-management, automation
---
Create a flexible function to compile files in the current directory, with automatic directory handling

```vim
function! Make()
  let curr_dir = expand('%:h')
  if curr_dir == ''
    let curr_dir = '.'
  endif
  execute 'lcd ' . curr_dir
  execute 'make %:r.o'
  execute 'lcd -'
endfunction

nnoremap <F7> :update<CR>:call Make()<CR>
```
```lua
function _G.compile_current_file()
  local curr_dir = vim.fn.expand('%:h')
  if curr_dir == '' then curr_dir = '.' end
  
  vim.cmd.lcd(curr_dir)
  vim.cmd.make(vim.fn.expand('%:r') .. '.o')
  vim.cmd.lcd('-')
end

vim.keymap.set('n', '<F7>', function()
  vim.cmd.write()
  _G.compile_current_file()
end, { desc = 'Compile current file in project directory' })
```

**Source:** ** https://vim.fandom.com/wiki/Map_function_keys_to_compile_and_run_your_code
***
# Title: Move Characters to Specific Column Range
# Category: advanced_functions
# Tags: text-manipulation, range-commands, advanced-editing
---
Custom Vim function to move specified characters to a specific column within a line range, useful for text alignment and formatting

```vim
function! MCCB (num_occr, mv_char, col_num) range
    if (a:firstline <= a:lastline)
        nmap s 80i <ESC>
        let line_num = a:firstline
        while line_num <= a:lastline
            execute "normal " . line_num . "G0" . a:num_occr . "f" . a:mv_char . "s" . a:col_num . "|dw"
            let line_num = line_num + 1
        endwhile
        nunmap s
    else
        execute printf('ERROR : Start line %d is higher than End line %d', a:firstline, a:lastline)
    endif
endfunction
```
```lua
function _G.move_chars_to_column(first_line, last_line, occurrence, move_char, col_num)
    if first_line <= last_line then
        for line_num = first_line, last_line do
            vim.cmd(string.format('normal! %dG0%df%ss%d|dw', line_num, occurrence, move_char, col_num))
        end
    else
        print(string.format('ERROR: Start line %d is higher than End line %d', first_line, last_line))
    end
end

-- Usage example
-- :lua move_chars_to_column(5, 11, 1, '=', 8)
```

**Source:** ** https://vim.fandom.com/wiki/Moving_specified_Characters_in_a_given_range_of_line_to_specified_Column
***
# Title: Extract Text from HTML Files
# Category: advanced_functions
# Tags: html-parsing, text-extraction, utility-function
---
Create a function to extract and view plain text from HTML files or URLs using a text-based browser like elinks

```vim
function! ViewHtmlText(url)
  if !empty(a:url)
    new
    setlocal buftype=nofile bufhidden=hide noswapfile
    execute 'r !elinks ' . a:url . ' -dump -dump-width ' . winwidth(0)
    1d
  endif
endfunction

" Map to preview HTML file or URL
nnoremap <Leader>H :update<Bar>call ViewHtmlText(expand('%:p'))<CR>
```
```lua
local function view_html_text(url)
  if url and url ~= '' then
    vim.cmd('new')
    vim.api.nvim_buf_set_option(0, 'buftype', 'nofile')
    vim.api.nvim_buf_set_option(0, 'bufhidden', 'hide')
    vim.api.nvim_buf_set_option(0, 'swapfile', false)
    
    local output = vim.fn.systemlist('elinks ' .. url .. ' -dump -dump-width ' .. vim.fn.winwidth(0))
    vim.api.nvim_buf_set_lines(0, 0, -1, false, output)
    vim.cmd('normal! gg')
  end
end

-- Map to preview HTML file or URL
vim.keymap.set('n', '<Leader>H', function()
  vim.cmd.update()
  view_html_text(vim.fn.expand('%:p'))
end, { desc = 'Preview HTML file text' })
```

**Source:** ** https://vim.fandom.com/wiki/Opening_current_Vim_file_in_your_Windows_browser
***
# Title: Advanced PHP Function Documentation Viewer
# Category: advanced_functions
# Tags: php, documentation, custom-function, preview-window
---
Create a sophisticated function to fetch and display PHP documentation in a preview window with smart parsing

```vim
function! OpenPhpFunction (keyword)
  let proc_keyword = substitute(a:keyword , '_', '-', 'g')
  exe 'pedit'
  exe 'wincmd P'
  exe 'enew'
  exe "set buftype=nofile"
  exe 'silent r!lynx -dump -nolist http://php.net/'.proc_keyword
  exe 'norm gg'
  exe 'call search("____________________________________")'
  exe 'norm dgg'
  exe 'call search("User Contributed Notes")'
  exe 'norm dGgg'
endfunction
```
```lua
local function open_php_function(keyword)
  -- Replace underscores with hyphens
  local proc_keyword = keyword:gsub('_', '-')
  
  -- Open preview window
  vim.cmd('pedit')
  vim.cmd('wincmd P')
  
  -- Create new buffer
  vim.cmd('enew')
  vim.bo.buftype = 'nofile'
  
  -- Fetch documentation
  local cmd = string.format('lynx -dump -nolist http://php.net/%s', proc_keyword)
  local output = vim.fn.systemlist(cmd)
  
  -- Clean up output
  local cleaned_output = {}
  local start_index = nil
  for i, line in ipairs(output) do
    if line:match('____________________________________') then
      start_index = i
      break
    end
  end
  
  if start_index then
    for i = start_index + 1, #output do
      if line:match('User Contributed Notes') then
        break
      end
      table.insert(cleaned_output, output[i])
    end
  end
  
  -- Set buffer contents
  vim.api.nvim_buf_set_lines(0, 0, -1, false, cleaned_output)
  vim.cmd('norm gg')
end

-- Create a command and mapping
vim.api.nvim_create_user_command('PhpDoc', function()
  local word = vim.fn.expand('<cword>')
  open_php_function(word)
end, {})

vim.keymap.set('n', '<leader>pd', ':PhpDoc<CR>', { desc = 'PHP Function Documentation' })
```

**Source:** ** https://vim.fandom.com/wiki/PHP_online_help
***
# Title: Extract Text from HTML Files
# Category: advanced_functions
# Tags: html, text-extraction, utility
---
Use a text-based browser to extract readable text from HTML files or URLs

```vim
function! ViewHtmlText(url)
  if !empty(a:url)
    new
    setlocal buftype=nofile bufhidden=hide noswapfile
    execute 'r !elinks ' . a:url . ' -dump -dump-width ' . winwidth(0)
    1d
  endif
endfunction

" Mappings for different preview scenarios
nnoremap <Leader>H :update<Bar>call ViewHtmlText(expand('%:p'))<CR>
vnoremap <Leader>h y:call ViewHtmlText(@@)<CR>
nnoremap <Leader>h :call ViewHtmlText(@+)<CR>
```
```lua
function _G.view_html_text(url)
  if url and url ~= '' then
    vim.cmd('new')
    vim.api.nvim_buf_set_option(0, 'buftype', 'nofile')
    vim.api.nvim_buf_set_option(0, 'bufhidden', 'hide')
    vim.api.nvim_buf_set_option(0, 'swapfile', false)
    
    local output = vim.fn.systemlist(string.format('elinks %s -dump -dump-width %d', url, vim.o.columns))
    vim.api.nvim_buf_set_lines(0, 0, -1, false, output)
    vim.cmd('normal! gg')
  end
end

-- Mappings
vim.keymap.set('n', '<Leader>H', function()
  vim.cmd.update()
  _G.view_html_text(vim.fn.expand('%:p'))
end, { desc = 'Preview current HTML file text' })

vim.keymap.set('v', '<Leader>h', function()
  local selected_text = vim.fn.getreg('@')
  _G.view_html_text(selected_text)
end, { desc = 'Preview selected HTML/URL' })

vim.keymap.set('n', '<Leader>h', function()
  _G.view_html_text(vim.fn.getreg('+'))
end, { desc = 'Preview clipboard HTML/URL' })
```

**Source:** ** https://vim.fandom.com/wiki/Preview_HTML_files_quickly
***
# Title: Text Extraction from HTML/URL
# Category: advanced_functions
# Tags: text-extraction, web-preview, custom-function
---
Extract text from HTML files or URLs using a text-based browser like elinks, creating a new buffer for preview

```vim
function! ViewHtmlText(url)
  if !empty(a:url)
    new
    setlocal buftype=nofile bufhidden=hide noswapfile
    execute 'r !elinks ' . a:url . ' -dump -dump-width ' . winwidth(0)
    1d
  endif
endfunction

nnoremap <Leader>H :update<Bar>call ViewHtmlText(expand('%:p'))<CR>
```
```lua
function _G.view_html_text(url)
  if url ~= '' then
    vim.cmd('new')
    vim.api.nvim_buf_set_option(0, 'buftype', 'nofile')
    vim.api.nvim_buf_set_option(0, 'bufhidden', 'hide')
    vim.api.nvim_buf_set_option(0, 'swapfile', false)
    
    local output = vim.fn.system('elinks ' .. url .. ' -dump -dump-width ' .. vim.fn.winwidth(0))
    vim.api.nvim_buf_set_lines(0, 0, 1, false, vim.split(output, '\n'))
  end
end

vim.keymap.set('n', '<Leader>H', function()
  vim.cmd.update()
  _G.view_html_text(vim.fn.expand('%:p'))
end)
```

**Source:** ** https://vim.fandom.com/wiki/Preview_current_file_in_Mozilla_through_localhost
***
# Title: Custom Function to Open File in Visual Studio
# Category: advanced_functions
# Tags: integration, windows, external-tools
---
Create a Vim function to open the current file and line number in Visual Studio using a custom script (Windows-specific)

```vim
function! DevEnvDDE()
  let cmd = '!devenvdden.pl %:p ' . line(".")
  silent execute cmd
endfunction
```
```lua
function _G.open_file_in_visual_studio()
  local file_path = vim.fn.expand('%:p')
  local line_number = vim.fn.line('.')
  local cmd = string.format('!devenvdden.pl %s %d', file_path, line_number)
  vim.cmd(cmd)
end

-- Optional: Map to a keybinding
vim.keymap.set('n', '<leader>vs', _G.open_file_in_visual_studio, { desc = 'Open current file in Visual Studio' })
```

**Source:** ** https://vim.fandom.com/wiki/VimTip580
***
# Title: Flexible Underline Command
# Category: advanced_functions
# Tags: text-formatting, user-command, customization
---
Create a flexible user command to underline text with custom characters

```vim
function! s:Underline(chars)
  let chars = empty(a:chars) ? '-' : a:chars
  let nr_columns = virtcol('$') - 1
  let uline = repeat(chars, (nr_columns / len(chars)) + 1)
  put =strpart(uline, 0, nr_columns)
endfunction
command! -nargs=? Underline call s:Underline(<q-args>)
```
```lua
local function underline(chars)
  chars = chars == '' and '-' or chars
  local columns = vim.fn.virtcol('$') - 1
  local uline = chars:rep(math.floor(columns / #chars) + 1)
  uline = uline:sub(1, columns)
  
  -- Insert the underline
  vim.api.nvim_put({uline}, 'l', true, false)
end

-- Create user command
vim.api.nvim_create_user_command('Underline', function(opts)
  underline(opts.args)
end, { nargs = '?' })
```

**Source:** ** https://vim.fandom.com/wiki/VimTip724
***
# Title: Flexible Underline Function
# Category: advanced_functions
# Tags: text-formatting, user-command, customization
---
Create a custom command to underline text with various characters, adapting to the current line's length

```vim
function! s:Underline(chars)
  let chars = empty(a:chars) ? '-' : a:chars
  let nr_columns = virtcol('$') - 1
  let uline = repeat(chars, (nr_columns / len(chars)) + 1)
  put =strpart(uline, 0, nr_columns)
endfunction
command! -nargs=? Underline call s:Underline(<q-args>)
```
```lua
function _G.underline_text(chars)
  chars = chars or '-'
  local nr_columns = vim.fn.virtcol('$') - 1
  local uline = chars:rep(math.floor(nr_columns / #chars) + 1)
  uline = uline:sub(1, nr_columns)
  vim.api.nvim_put({uline}, 'l', true, false)
end

vim.api.nvim_create_user_command('Underline', function(opts)
  _G.underline_text(opts.args ~= '' and opts.args or nil)
end, { nargs = '?' })
```

**Source:** ** https://vim.fandom.com/wiki/VimTip750
***
