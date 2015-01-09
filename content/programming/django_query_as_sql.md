Title: DJANGO: query as sql
Date: 2012-06-07 08:42
Modified: 
Category: Programming
Tags: Django
Slug: django_query_as_sql
Lang: en
Authors: znotdead
Summary: query as sql

### DJANGO: query as sql

To view a query as sql in shell
in versions before multiple db:
```
query.as_sql()
```
Now:
```
query.get_compiler('default').as_sql()
```
