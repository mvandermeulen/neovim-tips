# Title: Lua require and module system
# Category: Advanced Neovim
# Tags: lua, require, module, package
---
Use Lua's require system to load and organize Neovim configuration modules with automatic caching and reloading.

```vim
" Create ~/.config/nvim/lua/config/keymaps.lua
:lua require('config.keymaps')
:lua package.loaded['config.keymaps'] = nil  " force reload
:lua R = function(name) package.loaded[name] = nil; return require(name) end
```

**Source:** ** Community contributed
***
# Title: Extmarks for persistent highlighting
# Category: Advanced Neovim
# Tags: extmarks, highlight, persistent, namespace
---
Use extmarks to create persistent, trackable highlights that survive buffer changes, unlike matchadd().

```vim
:lua ns = vim.api.nvim_create_namespace('my_highlights')
:lua vim.api.nvim_buf_set_extmark(0, ns, 0, 0, {
  end_col=10, hl_group='Search', priority=100
})
:lua vim.api.nvim_buf_clear_namespace(0, ns, 0, -1)  " clear all
```

**Source:** ** Community contributed
***
# Title: Virtual text annotations
# Category: Advanced Neovim
# Tags: virtual, text, annotations, inline
---
Use virtual text to display inline annotations like diagnostics, git blame, or documentation without modifying buffer content.

```vim
:lua vim.api.nvim_buf_set_extmark(0, ns, vim.fn.line('.')-1, 0, {
  virt_text = {{'← This is a note', 'Comment'}},
  virt_text_pos = 'eol'
})
" Adds virtual text at end of current line
```

**Source:** ** Community contributed
***
# Title: Buffer-local variables with vim.b
# Category: Advanced Neovim
# Tags: buffer, local, variables, vim.b
---
Use `vim.b` to access buffer-local variables from Lua, providing cleaner syntax than traditional vim variables.

```vim
:lua vim.b.my_setting = 'value'
:lua print(vim.b.my_setting)
:lua vim.b[0].setting = 'buffer 0 specific'
" Cleaner than :let b:my_setting = 'value'
```

**Source:** ** Community contributed
***
# Title: Window-local variables with vim.w
# Category: Advanced Neovim
# Tags: window, local, variables, vim.w
---
Use `vim.w` to manage window-local variables from Lua for window-specific settings and state.

```vim
:lua vim.w.quickfix_title = 'My Results'
:lua vim.w[1001].custom_setting = true  " specific window ID
:lua for winid, vars in pairs(vim.w) do print(winid, vim.inspect(vars)) end
```

**Source:** ** Community contributed
***
# Title: Global variables with vim.g
# Category: Advanced Neovim
# Tags: global, variables, vim.g, configuration
---
Use `vim.g` to manage global variables from Lua, providing type-safe access to vim global variables.

```vim
:lua vim.g.mapleader = ' '
:lua vim.g.loaded_netrw = 1        " disable netrw
:lua vim.g.python3_host_prog = '/usr/bin/python3'
" Equivalent to :let g:mapleader = ' '
```

**Source:** ** Community contributed
***
# Title: Tab-local variables with vim.t
# Category: Advanced Neovim
# Tags: tab, local, variables, vim.t
---
Use `vim.t` to manage tab-local variables for tab-specific settings and state management.

```vim
:lua vim.t.project_root = vim.fn.getcwd()
:lua vim.t[2].custom_title = 'Tab 2'  " specific tab
:lua print('Current tab project:', vim.t.project_root)
```

**Source:** ** Community contributed
***
# Title: Lua heredoc syntax
# Category: Advanced Neovim
# Tags: lua, heredoc, multiline, syntax
---
Use Lua heredoc syntax in vimscript for clean multiline Lua code blocks within vim configuration.

```vim
lua << EOF
local function my_function()
  print("This is a multiline Lua function")
  vim.cmd('echo "Mixed Lua and Vim commands"')
end
my_function()
EOF
```

**Source:** ** Community contributed
***
# Title: Keymap API with descriptions
# Category: Advanced Neovim
# Tags: keymap, api, description, which-key
---
Use `vim.keymap.set()` to create keymaps with descriptions and options, supporting which-key integration.

```vim
:lua vim.keymap.set('n', '<leader>f', '<cmd>find<CR>', {
  desc = 'Find file', silent = true, buffer = 0
})
:lua vim.keymap.del('n', '<leader>f')  " delete keymap
```

**Source:** ** Community contributed
***
# Title: User commands with Lua
# Category: Advanced Neovim
# Tags: user, command, lua, api
---
Use `vim.api.nvim_create_user_command()` to create custom commands with Lua functions and completion.

```vim
:lua vim.api.nvim_create_user_command('Hello', 
  function(opts) print('Hello ' .. opts.args) end,
  {nargs = 1, desc = 'Greet someone'}
)
:Hello World  " prints 'Hello World'
```

**Source:** ** Community contributed
***
# Title: Option management with vim.opt
# Category: Advanced Neovim
# Tags: options, vim.opt, configuration, lua
---
Use `vim.opt` for intuitive option management from Lua with proper data types and operations.

```vim
:lua vim.opt.number = true
:lua vim.opt.tabstop = 4
:lua vim.opt.path:append('**')     " add to path
:lua vim.opt.wildignore:append('*.pyc')  " add to ignore list
```

**Source:** ** Community contributed
***
# Title: Filetype detection API
# Category: Advanced Neovim
# Tags: filetype, detection, api, lua
---
Use `vim.filetype.add()` to register custom filetype detection patterns and functions.

```vim
:lua vim.filetype.add({
  extension = { log = 'log', conf = 'conf' },
  filename = { ['.eslintrc'] = 'json' },
  pattern = { ['.*%.env%..*'] = 'sh' }
})
```

**Source:** ** Community contributed
***
# Title: Highlight group API
# Category: Advanced Neovim
# Tags: highlight, api, colors, groups
---
Use `vim.api.nvim_set_hl()` to programmatically define and modify highlight groups from Lua.

```vim
:lua vim.api.nvim_set_hl(0, 'MyHighlight', {
  fg = '#ff0000', bg = '#000000', bold = true
})
:lua local hl = vim.api.nvim_get_hl(0, {name = 'Comment'})
:lua print(vim.inspect(hl))
```

**Source:** ** Community contributed
***
# Title: Snippet expansion API
# Category: Advanced Neovim
# Tags: snippet, expansion, api, completion
---
Use `vim.snippet` API for snippet expansion and navigation without external snippet engines.

```vim
:lua vim.snippet.expand('for var in iterable:\n\tpass')
:lua if vim.snippet.active() then vim.snippet.jump(1) end
" Built-in snippet support in Neovim 0.10+
```

**Source:** ** Community contributed
***
# Title: Event loop and scheduling
# Category: Advanced Neovim
# Tags: event, loop, schedule, async
---
Use `vim.schedule()` to defer function execution to the next event loop iteration for async operations.

```vim
:lua vim.schedule(function()
  print('This runs in the next event loop')
  vim.cmd('echo "Deferred execution"')
end)
" Useful for async operations and avoiding blocking
```

**Source:** ** Community contributed
***
# Title: Ring buffer for undo history
# Category: Advanced Neovim
# Tags: undo, history, ring, buffer
---
Use Neovim's enhanced undo system with ring buffer capabilities for advanced undo tree navigation.

```vim
:lua print(vim.fn.undotree())  " inspect undo tree
:earlier 1f  " go back 1 file write
:later 1f    " go forward 1 file write  
:undolist    " show numbered undo states
```

**Source:** ** Community contributed
***
# Title: Treesitter API access
# Category: Advanced Neovim
# Tags: treesitter, api, ast, parsing
---
Use `vim.treesitter` API to query and manipulate the abstract syntax tree programmatically.

```vim
:lua local parser = vim.treesitter.get_parser(0, 'lua')
:lua local tree = parser:parse()[1]
:lua local query = vim.treesitter.query.parse('lua', '(function_declaration) @func')
:lua for id, node in query:iter_captures(tree:root(), 0) do print(node:type()) end
```

**Source:** ** Community contributed
***
# Title: RPC and job control (vim.system)
# Category: Advanced Neovim
# Tags: rpc, job, control, async
---
Use `vim.system()` for modern job control and `vim.rpcnotify()` for RPC communication with external processes.

```vim
:lua local job = vim.system({'ls', '-la'}, {
  text = true,
  stdout = function(err, data) print(data) end
})
:lua job:wait()  " wait for completion
```

**Source:** ** Community contributed
***
# Title: UI events and hooks
# Category: Advanced Neovim
# Tags: ui, events, hooks, interface
---
Use UI event hooks to customize Neovim's behavior for different UI clients and frontends.

```vim
:lua vim.api.nvim_set_option_value('guifont', 'Monospace:h12', {})
:lua if vim.g.neovide then vim.g.neovide_cursor_animation_length = 0.1 end
:lua print(vim.loop.os_uname().sysname)  " detect OS
```

**Source:** ** Community contributed
***
# Title: Namespace management
# Category: Advanced Neovim
# Tags: namespace, management, api, isolation
---
Use namespaces to isolate highlights, extmarks, and diagnostics from different sources or plugins.

```vim
:lua local ns1 = vim.api.nvim_create_namespace('source1')
:lua local ns2 = vim.api.nvim_create_namespace('source2')
:lua vim.api.nvim_buf_set_extmark(0, ns1, 0, 0, {hl_group = 'Search'})
:lua vim.api.nvim_buf_clear_namespace(0, ns1, 0, -1)  " clear ns1 only
```

**Source:** ** Community contributed
***
# Title: Deep inspection with vim.inspect
# Category: Advanced Neovim
# Tags: inspect, debug, pretty, print
---
Use `vim.inspect()` to pretty-print complex Lua data structures for debugging and development.

```vim
:lua local data = {a = {b = {c = 'nested'}}, list = {1, 2, 3}}
:lua print(vim.inspect(data))
:lua print(vim.inspect(vim.bo, {depth = 1}))  " buffer options
:lua print(vim.inspect(vim.api, {depth = 1}))  " API structure
```

**Source:** ** Community contributed
***
# Title: Secure mode and restrictions
# Category: Advanced Neovim
# Tags: secure, mode, restrictions, safety
---
Use secure mode and option restrictions to safely execute untrusted vim configurations and scripts.

```vim
:set secure               " enable secure mode
:set exrc                 " allow local .vimrc files
:lua vim.o.secure = true  " Lua equivalent
" Restricts dangerous commands in local configs
```

**Source:** ** Community contributed
***
# Title: Runtime path manipulation
# Category: Advanced Neovim
# Tags: runtime, path, rtp, manipulation
---
Use runtime path manipulation to dynamically load configurations and plugins at runtime.

```vim
:lua vim.opt.rtp:prepend('~/my-custom-config')
:lua vim.opt.rtp:append('~/additional-plugins')  
:lua for path in vim.gsplit(vim.o.rtp, ',') do print(path) end
" Runtime paths searched for configs and plugins
```

**Source:** ** Community contributed
***
# Title: Custom completion sources
# Category: Advanced Neovim
# Tags: completion, custom, source, omnifunc
---
Use `vim.lsp.omnifunc` and custom completion functions to create intelligent completion sources.

```vim
" Vimscript:
function! MyCompletion(findstart, base)
  if a:findstart
    return col('.') - 1
  else
    return ['custom1', 'custom2', 'custom3']
  endif
endfunction
:set omnifunc=MyCompletion
```
```lua
-- Lua:
local function my_completion(findstart, base)
  if findstart == 1 then
    return vim.fn.col('.') - 1
  else
    return {'custom1', 'custom2', 'custom3'}
  end
end

vim.opt.omnifunc = 'v:lua.my_completion'
-- Or set it globally:
_G.my_completion = my_completion
vim.opt.omnifunc = 'v:lua.my_completion'
```

**Source:** ** Community contributed
***
# Title: Window configuration API
# Category: Advanced Neovim
# Tags: window, configuration, api, layout
---
Use window configuration API for advanced window management and layout control.

```vim
:lua vim.api.nvim_win_set_config(0, {
  relative = 'win', win = vim.api.nvim_get_current_win(),
  width = 50, height = 20, row = 5, col = 10
})
:lua local config = vim.api.nvim_win_get_config(0)
:lua print(vim.inspect(config))
```

**Source:** ** Community contributed
***
# Title: Health check system
# Category: Advanced Neovim
# Tags: health, check, system, diagnostic
---
Use Neovim's health check system to create custom health checks for your configurations and environments.

```vim
:checkhealth            " run all health checks
:checkhealth vim.lsp    " check specific component
" Create ~/.config/nvim/lua/health/myconfig.lua
" with check() function for custom health checks
```

**Source:** ** Community contributed
***
# Title: Command preview and substitution
# Category: Advanced Neovim
# Tags: command, preview, substitution, inccommand
---
Use `inccommand` for live preview of Ex commands, especially substitution with real-time feedback.

```vim
" Vimscript:
:set inccommand=split     " preview in split window
:set inccommand=nosplit   " preview inline
:%s/old/new/g            " shows live preview while typing
" Preview works with :substitute, :global, :sort, etc.
```
```lua
-- Lua:
vim.opt.inccommand = 'split'     -- preview in split window
vim.opt.inccommand = 'nosplit'   -- preview inline
-- Then use: :%s/old/new/g to see live preview while typing
-- Preview works with :substitute, :global, :sort, etc.
```

**Source:** ** Community contributed
***
# Title: Git Merge Conflict Resolution with Vimdiff
# Category: advanced_neovim
# Tags: git, merge-conflicts, diff-tool
---
Efficiently resolve Git merge conflicts using a custom Vimdiff layout that focuses on two-way diffs and provides a clearer view of conflicts

```vim
# Git configuration for custom mergetool
git config --global merge.tool diffconflicts
git config --global mergetool.diffconflicts.cmd 'diffconflicts vim $BASE $LOCAL $REMOTE $MERGED'
git config --global mergetool.diffconflicts.trustExitCode true
git config --global mergetool.keepBackup false
```
```lua
-- Git configuration can remain the same
-- Use with a custom diffconflicts script
-- Key is to set up a three-tab layout for conflict resolution
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/A_better_Vimdiff_Git_mergetool)
***
# Title: Quick Number Value Inspection
# Category: advanced_neovim
# Tags: number-conversion, inspection, debugging
---
Add a custom mapping to quickly inspect decimal and hexadecimal values of a number under the cursor

```vim
function! DecAndHex(number)
  if a:number =~? '^[-+]?\d\+$'
    let dec = a:number
    echo dec . printf('  ->  0x%X, -(0x%X)', dec, -dec)
  elseif a:number =~? '^0x\x\+$'
    let hex = substitute(a:number, '0x', '', '')
    echo '0x' . hex . printf('  ->  %d', eval('0x'.hex))
  endif
endfunction

nnoremap gn :call DecAndHex(expand("<cWORD>"))<CR>
```
```lua
local function dec_and_hex(number)
  local dec = tonumber(number)
  local hex = tonumber(number, 16)
  
  if dec then
    print(string.format('%d -> 0x%X, -(0x%X)', dec, dec, -dec))
  elseif hex then
    print(string.format('0x%X -> %d', hex, hex))
  else
    print('Not a valid number')
  end
end

vim.keymap.set('n', 'gn', function()
  local word = vim.fn.expand('<cWORD>')
  dec_and_hex(word)
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Convert_between_hex_and_decimal)
***
# Title: Custom Keyword Completion with Wildcards
# Category: advanced_neovim
# Tags: completion, custom-functions, text-editing
---
Implement a custom keyword completion function that allows flexible matching using wildcards, useful for completing identifiers with mixed case or complex naming patterns

```vim
" Custom keyword completion script
setlocal completefunc=MKwCompleteId

" Usage: Type part of a keyword and use CTRL-X CTRL-U to complete
```
```lua
-- Lua equivalent for custom keyword completion
function MKwCompleteId(findstart, base)
  if findstart == 1 then
    -- Find start of keyword match
    local line = vim.api.nvim_get_current_line()
    local col = vim.api.nvim_win_get_cursor(0)[2]
    local start = vim.fn.match(line:sub(1, col), '\k*$')
    return start
  else
    -- Find matching keywords
    local matches = {}
    local pattern = '\<' .. base:gsub('.', '\k*%0') .. '\>'
    
    -- Search for matches in current buffer
    for _, line in ipairs(vim.api.nvim_buf_get_lines(0, 0, -1, false)) do
      for match in line:gmatch(pattern) do
        table.insert(matches, match)
      end
    end
    
    return matches
  end
end

-- Set the custom completion function
vim.bo.completefunc = 'v:lua.MKwCompleteId'
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Custom_keyword_completion)
***
# Title: Smart Function Signature Preview
# Category: advanced_neovim
# Tags: function-preview, autocomplete, code-insight
---
Automatically preview function signatures when typing, similar to IDE code insight features. This helps developers quickly understand function parameters without leaving the current editing context.

```vim
function! PreviewWord()
  if &previewwindow
    return
  endif
  let w = expand("<cword>")
  if w =~ '\i'
    exe "silent! ptag " . w
    silent! wincmd P
    if &previewwindow
      if has("folding")
        silent! .foldopen
      endif
      call search('\<\V' . w . '\>')
      hi previewWord term=bold ctermbg=green guibg=green
      exe 'match previewWord "\%' . line(".") . 'l\%' . col(".") . 'c\k*"'
      wincmd p
    endif
  endif
endfunction

au! CursorHold *.[ch] nested call PreviewWord()
```
```lua
local function preview_word()
  -- Check if already in preview window
  if vim.wo.previewwindow then
    return
  end

  -- Get word under cursor
  local word = vim.fn.expand('<cword>')
  
  -- Only process if word is a valid identifier
  if word:match('\w+') then
    -- Try to preview tag
    vim.cmd('silent! ptag ' .. word)
    
    -- Switch to preview window and highlight
    vim.cmd('silent! wincmd P')
    if vim.wo.previewwindow then
      -- Open any folded sections
      if vim.o.foldenable then
        vim.cmd('silent! .foldopen')
      end
      
      -- Highlight the word
      vim.api.nvim_buf_add_highlight(0, -1, 'PreviewWord', 0, 0, -1)
      vim.cmd('wincmd p')
    end
  end
end

-- Attach to C/H files
vim.api.nvim_create_autocmd('CursorHold', {
  pattern = {'*.c', '*.h'},
  callback = preview_word
})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Function_signature_previewer)
***
# Title: Advanced Syntax Group Identification Command
# Category: advanced_neovim
# Tags: syntax, command, highlight-debugging
---
Create a user command to easily check the syntax highlighting groups at the current cursor position

```vim
com! CheckHighlightUnderCursor echo {l,c,n ->
        \   'hi<'    . synIDattr(synID(l, c, 1), n)             . '> '
        \  .'trans<' . synIDattr(synID(l, c, 0), n)             . '> '
        \  .'lo<'    . synIDattr(synIDtrans(synID(l, c, 1)), n) . '> '
        \ }(line("."), col("."), "name")
```
```lua
vim.api.nvim_create_user_command('CheckHighlightUnderCursor', function()
  local line = vim.fn.line('.')
  local col = vim.fn.col('.')
  local synID = vim.fn.synID(line, col, 1)
  local transID = vim.fn.synID(line, col, 0)
  local loID = vim.fn.synIDtrans(synID)
  
  print(string.format(
    "hi<%s> trans<%s> lo<%s>", 
    vim.fn.synIDattr(synID, 'name'),
    vim.fn.synIDattr(transID, 'name'),
    vim.fn.synIDattr(loID, 'name')
  ))
end, {})
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Identify_the_syntax_highlighting_group_used_at_the_cursor)
***
# Title: Automatic Desktop-Specific Vim Instances
# Category: advanced_neovim
# Tags: server-mode, multi-desktop, automation
---
Create a script to launch Vim instances specific to the current desktop, ensuring better window management

```vim
# Bash script to manage desktop-specific Vim instances
exec /usr/bin/vim --servername $desktop --remote-tab-silent "$@"
```
```lua
-- Lua equivalent requires external script or system integration
-- Can use vim.fn.serverlist() and custom desktop detection logic
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Launch_files_in_new_tabs_under_Unix)
***
# Title: Use Lists for Handling Newlines in Vim Scripts
# Category: advanced_neovim
# Tags: vim-script, string-manipulation, lists
---
Prefer using lists over concatenated strings with newline separators to avoid NULL character issues when handling line breaks

```vim
" Vim way of handling newlines
call setline(".", ["a", "b"])

" Instead of
let @a = "a" . "\n" . "b"
```
```lua
-- Lua equivalent for handling newlines
vim.fn.setline(".", {"a", "b"})

-- Recommended list-based approach
local lines = {"a", "b"}
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Newlines_and_nulls_in_Vim_script)
***
# Title: Advanced PHP Documentation Lookup Function
# Category: advanced_neovim
# Tags: documentation, function-lookup, php
---
Create a sophisticated Vim function to fetch and display PHP function documentation in a preview window

```vim
function! OpenPhpFunction (keyword)
  let proc_keyword = substitute(a:keyword , '_', '-', 'g')
  exe 'pedit'
  exe 'wincmd P'
  exe 'enew'
  exe 'set buftype=nofile'
  exe 'silent r!lynx -dump http://php.net/'.proc_keyword
endfunction
```
```lua
function _G.open_php_function(keyword)
  local proc_keyword = keyword:gsub('_', '-')
  vim.cmd('pedit')
  vim.cmd('wincmd P')
  vim.cmd('enew')
  vim.bo.buftype = 'nofile'
  local result = vim.fn.systemlist('lynx -dump http://php.net/'..proc_keyword)
  vim.api.nvim_buf_set_lines(0, 0, -1, false, result)
end

-- Optional mapping
vim.keymap.set('n', '<C-p>', function()
  _G.open_php_function(vim.fn.expand('<cword>'))
end)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/VimTip598)
***
