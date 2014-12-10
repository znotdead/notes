Title: MYSQL: update tables from other tables
Date: 2011-12-09 13:36
Modified: 
Category: Programming
Tags: MySQL
Slug: mysql_update_tables_from_other_tables
Lang: en
Authors: znotdead
Summary: update tables

### MYSQL: update tables from other tables

If we want to insert new entries from other table
```sql
INSERT INTO stat (date, id, v, c, r)
SELECT date, id, SUM(v), SUM(c), SUM(r) FROM stat2
GROUP BY date, id ;
```
If we want to update some columns from values obtained from other column
```sql
UPDATE stat s, (SELECT date(datetime) AS date, id,
SUM(IF(status='good', value, 0)) AS v_g, SUM(IF(status='good', 1, 0)) AS c_a,
SUM(IF(status='bad', value, 0)) AS v_b, SUM(IF(status='bad', 1, 0)) AS c_p
FROM stat2
GROUP BY id, date) AS t
SET s.good = t.v_g, s.good_count = t.c_a,
s.bad = t.v_b, s.bad_count = t.c_p
WHERE s.date = t.date AND t.id = s.id;
```
Unfortunatly I don't find a way how to insert from table and on duplicate key update from t table without temporary table =( Or I misunderstand smth. =)
