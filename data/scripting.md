# Title: Prevent Script Reloading with Function
# Category: scripting
# Tags: plugin-development, script-management, performance
---
Provides a simple function to prevent reloading of Vim scripts, which helps improve script loading performance and avoid duplicate definitions

```vim
function DontLoadTwice(globalIdentifier)
  let dltcmd ="if exists(\"g:".a:globalIdentifier."\")
"
  let dltcmd.=" finish\n"
  let dltcmd.="endif\n"
  let dltcmd.="let g:".a:globalIdentifier."=1\n"
  return dltcmd
endfunction
```
```lua
function _G.dont_load_twice(identifier)
  if vim.g[identifier] then
    return
  end
  vim.g[identifier] = true
end
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Load_my_script_only_once)
***
# Title: Handle UTF-8 Encoding in Python Vim Scripts
# Category: scripting
# Tags: python, unicode, encoding
---
Properly encode Unicode strings when passing them between Python and Vim to avoid encoding errors

```vim
python << EOS
uniStr = u"\u2026"
str = uniStr.encode( vim.eval("&encoding") )
print str
EOS
```
```lua
-- Lua equivalent for handling UTF-8 encoding
-- Note: Neovim has better Unicode support by default
local uniStr = "…"
local encodedStr = vim.fn.iconv(uniStr, "utf-8", vim.o.encoding)
print(encodedStr)
```

**Source:** [vim.fandom.com](https://vim.fandom.com/wiki/Python_script_utf8_encoding)
***
