Title: MySQL: changing max connection for mysql server
Date: 2011-12-09 13:28
Modified: 
Category: Programming
Tags: MySQL
Slug: mysql_changing_max_connection_for_mysql_server
Lang: en
Authors: znotdead
Summary: 

### MySQL: changing max connection for mysql server
```sql
SHOW variables LIKE "max_connections";
```
On my client it was:
```sql
+-----------------+-------+ | Variable_name | Value | +-----------------+-------+ | max_connections | 151 | +-----------------+-------+
```
You can change the setting to e.g. 1000 by issuing the following command without having to restart the MySQL server:

```sql
SET global max_connections = 1001;
```

One connection I added for root which mysql reserves. And you should edit your config `/etc/mysql/my.cnf` and set `max_connections = 1001`.
