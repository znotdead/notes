Title: VISUAL MODE: Search and replace in selected
Date: 2012-12-10 19:02
Modified: 
Category: Vim
Tags: Vim, visual mode
Slug: visual_mode_search_and_replace_in_selected
Lang: en
Authors: znotdead
Summary: search and replace in visual mode

### VISUAL MODE: Search and replace in selected

on select there are
```vim
'< start line
`< start character
'> end line
`> end character
```
Imagine that you have visual region selected. so to replace press `:` and in command there is `:'<,'>` in command line already entered. So you should add to this `s/<word1>/<word2>/g`
or if You want to change in last selected region in Normal mode type:
```vim
:'<,'>  s/start/end/g
```
to search by only visual region you should in Normal mode:
```
:\%Vword1
```
