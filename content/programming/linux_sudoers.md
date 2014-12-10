Title: LINUX: sudoers
Date: 2011-12-09 13:27
Modified: 
Category: Programming
Tags: Linux
Slug: linux_sudoers
Lang: en
Authors: znotdead
Summary: 

### LINUX: sudoers

If you want a user have ability to make sudo you should to edit sudoers file.

```
# export EDITOR=vim
# visudo
```

This command edit `/etc/sudoers` file. And it check this file on save. Make your sudoers file looks like:

```
## Allows just user "username" to run all commands as root username ALL=(ALL) ALL username ALL=NOPASSWD: /etc/init.d/apache2 restart
```

Now username can run all commands as root and restart apache2 without password promt. It can be useful on remote deploying for example.
`/etc/sudoers` Syntax

Following is general syntax used by `/etc/sudoers` file:
`USER HOSTNAME=COMMAND`
Where,

`USER`: Name of normal user
`HOSTNAME`: Where command is allowed to run. It is the hostname of the system where this rule applies. sudo is designed so you can use one sudoers file on all of your systems. This space allows you to set per-host rules.
`COMMAND`: A simple filename allows the user to run the command with any arguments he/she wishes. However, you may also specify command line arguments (including wildcards). Alternately, you can specify "" to indicate that the command may only be run without command line arguments.

The sudo command has logged the attempt to the log file `/var/log/secure` or `/var/log/auth.log` file:
```
# tail -f /var/log/auth.log
```
*Examples:*

1. Allow username to run various commands:
    ```
    username ALL=/sbin/halt, /bin/kill
    ```
2. Allow user username to run /sbin/halt without any password i.e. as root without authenticating himself:
    ```
    username ALL= NOPASSWD: /sbin/halt
    ```
3. Allow user username to run any command from /usr/bin directory on the system dev:
    ```
    username dev = /usr/bin/*
    ```
