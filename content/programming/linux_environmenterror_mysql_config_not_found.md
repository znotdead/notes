Title: LINUX: EnvironmentError: mysql_config not found
Date: 2012-02-06 05:34
Modified: 
Category: Programming
Tags: Linux
Slug: linux_environmenterror_mysql_config_not_found
Lang: en
Authors: znotdead
Summary: EnvironmentError: mysql_config not found

### EnvironmentError: mysql_config not found

when trying to install MySQL-python there is error:
```
# pip install MySQL-python
```
```
EnvironmentError: mysql_config not found
```
To fix it you need to install libmysqlclient15-dev:
```
# apt-get install libmysqlclient15-dev
# pip install MySQL-python
```
