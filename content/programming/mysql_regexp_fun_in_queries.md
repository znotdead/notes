Title: MYSQL: REGEXP fun in queries
Date: 2011-12-09 13:30
Modified: 
Category: Programming
Tags: MySQL
Slug: mysql_regexp_fun_in_queries
Lang: en
Authors: znotdead
Summary: regexp

### MYSQL: REGEXP fun in queries

if comment has notverybad or VeryBad than count this as bad_marks
Select below displays count of bad_marks by verybad and notverybad separately as:
```
class_id | count_of_marks | is_this_row_for_notverybad(0 or 1) | is_this_row_for_verybad(0 or 1)
1           | 123                   | 1                                       | 0
2           | 45                     | 1                                       | 0
5           | 67                     | 1                                       | 0
2           | 17                     | 0                                       | 1
3           | 12                     | 0                                       | 1
```
i.e.

notverybad:
1 class - 123 marks
2 - 45
5 - 67

verybad:
2 - 17
3 - 12
```sql
SELECT class_id, count(*) as marks, comment REGEXP 'notverybad' as notverybad, comment REGEXP 'verybad' as verybad
FROM marks
WHERE comment REGEXP 'notverybad|verybad'
GROUP BY class_id, notverybad, verybad
```
But if there is too many entries in table it can be much slower than make 2 requests:
```sql
SELECT class_id, count(*) as marks
FROM marks
WHERE comment like '%notverybad%'
GROUP BY class_id
```
and:
```sql
SELECT class_id, count(*) as marks
FROM marks
WHERE comment like '%verybad%'
GROUP BY class_id
```
