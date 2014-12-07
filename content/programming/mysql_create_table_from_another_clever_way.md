Title: MYSQL: create table from another clever way
Date: 2012-07-24 06:48
Modified: 2012-07-24 07:00
Category: Programming
Tags: MySQL
Slug: mysql_create_table_from_another_clever_way
Lang: en
Authors: znotdead
Summary: create table from another

### create table from another clever way

If you need create table on basis of another you do not need to search types and so on.

```mysql
CREATE TABLE name_birthday_backup (KEY(name))
    SELECT name, birthday
    FROM users
    WHERE name is not null and birthday is null;
```

Request above creates table with names and birthdays for users who specified their names and not specified their birthday with index on name. Types of columns will be the same.
