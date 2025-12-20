# Title: Open new tab
# Category: Tabs
# Tags: tab, new, open
---
Use `gt` to go to next tab, `gT` to go to previous tab, or `{number}gt` to go to specific tab.

```vim
gt   " next tab
gT   " previous tab
2gt  " go to tab 2
```
***
# Title: Close tab
# Category: Tabs
# Tags: tab, close, exit
---
Use `:tabclose` to close current tab.

```vim
:tabclose
```
***
# Title: Open commands in new tabs
# Category: Tabs
# Tags: tab, command, open, prefix
---
Use `:tab {command}` to open any command in a new tab instead of current window.

```vim
:tab split        " open split in new tab
:tab help motion  " open help in new tab
:tab edit file.txt " open file in new tab
:tab ball         " open all buffers in tabs
```
***
