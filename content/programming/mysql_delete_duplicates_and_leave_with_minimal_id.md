Title: MYSQL: delete duplicates and leave with minimal id
Date: 2012-03-22 14:57
Modified: 
Category: Programming
Tags: MySQL
Slug: mysql_delete_duplicates_and_leave_with_minimal_id
Lang: en
Authors: znotdead
Summary: delete duplicates and leave with minimal id

### delete duplicates and leave with minimal id

SQL query to delete all duplicates.
```mysql
DELETE  i  FROM stats i
    JOIN (SELECT *, min(id) as minid
                FROM stats GROUP BY custom_id, code
                HAVING COUNT(*)>1) AS dups
    ON dups.custom_id=i.custom_id AND dups.code=i.code
    WHERE i.id <> dups.minid
```
