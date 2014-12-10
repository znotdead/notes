Title: MYSQL: Error: 1329 No data - zero rows fetched, selected, or processed
Date: 2011-12-09 13:35
Modified: 
Category: Programming
Tags: MySQL
Slug: mysql_error_1329_no_data_zero_rows_fetched_selected_or_processed
Lang: en
Authors: znotdead
Summary: 1329 error

### MYSQL: Error: 1329 No data - zero rows fetched, selected, or processed

If you have an error in mysql on usual `DELETE FROM t WHERE in IN (12)`:
```
Error: 1329
 No data - zero rows fetched, selected, or processed
```
You simply should drop this table ( make back up if needed) and create it again. This is a strange bug in MySQL which I'm not able to repeat.
