Title: LINUX: fstab mount samba
Date: 2011-07-29 23:09
Modified: 
Category: Programming
Tags: Linux
Slug: linux_fstab_mount_samba
Lang: en
Authors: znotdead
Summary: fstab

### LINUX: fstab mount samba

There can be a problem with mounting samba on boot.
In dmesg I found next error on mounting:
`CIFS VFS: cifs_mount failed w/return code = -113`


To prevent mounting when network is down you should use fstab option `_netdev`.
I.e. your fstab entry can looks like:
```
//192.168.1.3/media   /media cifs         rw,async,nodev,noexec,nosuid,rw,user=username,password=userpasswd,noperm,users,gid=12,_netdev 0 0
```
