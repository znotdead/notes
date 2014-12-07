Title: MYSQL: unauthenticated user
Date: 2011-07-29 03:23
Modified: 2011-07-29 3:30
Category: Programming
Tags: MySQL
Slug: mysql_unauthenticated_user
Lang: en
Authors: znotdead
Summary: unauthenticated user

### MYSQL: unauthenticated user

Once MySQL became works to slowly. SHOW PROCESSLIST; shows many entries like :
```
4654225 | unauthenticated user | 127.0.0.1:39812 | NULL    | Connect | NULL | login | NULL
```

In this case `--skip-name-resolve`

From docs:
The thread takes the IP address and resolves it to a host name (using gethostbyaddr()). It then takes that host name and resolves it back to the IP address (using gethostbyname()) and compares to ensure it is the original IP address.


i.e. we need to add option `skip-name-resolve` to `[mysqld]` section in `my.cnf` and restart mysql. All requests became much faster.
