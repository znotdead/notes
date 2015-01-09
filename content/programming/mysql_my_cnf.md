Title: MYSQL: my.cnf
Date: 2014-09-01 12:17
Modified: 
Category: Programming
Tags: MySQL
Slug: my_cnf
Lang: en
Authors: znotdead
Summary: Change default collation to UTF-8 and default engine to InnoDB

### MYSQL: my.cnf
    :::ini
    [client]
    default-character-set = utf8

    [mysqld]
    collation-server = utf8_unicode_ci
    character-set-server = utf8
    default-storage-engine = InnoDB

    [mysql]
    default-character-set = utf8
