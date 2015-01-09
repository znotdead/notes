Title: SVN+LINUX: auth on svn and GNOME keyring
Date: 2012-02-06 05:27
Modified: 
Category: Programming
Tags: SVN,  Linux
Slug: svn_linux_auth_on_svn_and_gnome_keyring
Lang: en
Authors: znotdead
Summary: auth on svn and GNOME keyring

### SVN+LINUX: auth on svn and GNOME keyring

when trying to get repository from svn there is error:
Password for '(null)' GNOME keyring:
...

Solution:
```
rm ~/.gnome2/keyrings/login.keyring
```
