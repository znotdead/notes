Title: Delete lines containing pattern
Date: 2012-12-10 19:01
Modified: 
Category: Vim
Tags: Vim
Slug: delete_lines_containing_pattern
Lang: en
Authors: znotdead
Summary: delete line by pattern

### Delete lines containing pattern

For example, I need to delete all lines containing "WORD"

To view all lines to be removed:
```vim
:g/WORD
```
To remove lines:
```vim
:g/WORD/d
```
Or negative:
```vim
:g!/profile/d
```
