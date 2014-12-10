Title: MYSQL: execute string
Date: 2011-12-09 13:36
Modified: 
Category: Programming
Tags: MySQL
Slug: mysql_execute_string
Lang: en
Authors: znotdead
Summary: exec string

### MYSQL: execute string

Sometimes we need to execute dynamic sql. This is recipe:
```sql
PREPARE stmt FROM 'UPDATE stat
SET r_? = r_? - 1, l = l - 1, p_? = p_? - OLD.value
WHERE date(OLD.datetime) = date;';
EXECUTE stmt USING @old_status, @old_status, @old_status, @old_status;
```
But you can't use it in triggers and fuctions, but in procedures you can.

There is no workaround to use dynamic SQL in triggers by calling procedures. MySQL knows it! But variable helps me =)
