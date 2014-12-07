Title: MYSQL: select with many fields
Date: 2011-07-29 22:58
Modified: 
Category: Programming
Tags: MySQL
Slug: mysql_select_with_many_fields
Lang: en
Authors: znotdead
Summary: select with many fields

### MYSQL: select with many fields

When you make `select * from table` where many columns in CLI than you see ugly output

Solution:
change `;` to `\G` in your query and you receive list of pairs (column: value)

Example:
```
mysql> select * from user \G
```

or set another pager by next command:
```
mysql> pager less -n -i -S
```
