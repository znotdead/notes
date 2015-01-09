Title: RABBITMQ: simple create user commands
Date: 2012-02-09 04:27
Modified: 
Category: Programming
Tags: RabbitMQ
Slug: rabbitmq_simple_create_user_commands
Lang: en
Authors: znotdead
Summary: simple create user commands

### RABBITMQ: simple create user commands

to add host and user with all permissions:
```bash
rabbitmqctl add_vhost /host
rabbitmqctl add_user username password
rabbitmqctl set_permissions -p /host username ".*" ".*" ".*"
```
