Title: MYSQL: InnoDB and Django transactions
Date: 2012-06-07 08:40
Modified: 
Category: Programming
Tags: Mysql,  Django
Slug: mysql_innodb_and_django_transactions
Lang: en
Authors: znotdead
Summary: InnoDB transactions

### InnoDB and Django transactions

1.  Always use InnoDB `my.cnf`:
```
[mysqld]
default-storage-engine = InnoDB
```
2. InnoDB for session:
```
SET storage_engine=INNODB
```
3. InnoDB per table:
```
CREATE TABLE employee (id INT) ENGINE = InnoDB;
ALTER TABLE employee ENGINE = InnoDB;
```

Also it is important to change isolation level. Because with REPEATABLE READ if the first read yield no result, any subsequent read, as it must yield the same result, won't yield anything too.

**my.cnf**:
```
# Set the default transaction isolation level.
transaction-isolation = READ-COMMITTED
```

**Django**:
```
DATABASE_OPTIONS = { "init_command": "SET storage_engine=INNODB, SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED", }
```
