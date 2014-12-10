Title: NERDTree: show hidden files
Date: 2012-12-10 19:01
Modified: 
Category: Vim
Tags: Vim, NERDTree
Slug: nerdtree_show_hidden_files
Lang: en
Authors: znotdead
Summary: NERDTree

### NERDTree: show hidden files

from man:
`*'NERDTreeShowHidden'*`
Values: 0 or 1. Default: 0.

This option tells vim whether to display hidden files by default.
This option can be dynamically toggled, per tree, with the `|NERDTree-I|` mapping.
Use one of the follow lines to set this option:
```vim
> let NERDTreeShowHidden=0
> let NERDTreeShowHidden=1
```
