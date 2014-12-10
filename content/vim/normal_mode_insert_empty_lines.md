Title: NORMAL_MODE: Insert empty lines
Date: 2012-12-10 19:03
Modified: 
Category: Vim
Tags: Vim, normal mode
Slug: insert_empty_lines_in_normal_mode
Lang: en
Authors: znotdead
Summary: Normal mode

### NORMAL MODE: Insert empty lines

I can't found any mapping for that and there are many recipes. pressing o or O ans then <Esc> not very convenient.
The easiest for me is:
```vim
:normal o
```
and
```vim
:normal O
```
you can map this command on anything you like

or you can map :
```vim
nnoremap <Enter> o<ESC>
```
