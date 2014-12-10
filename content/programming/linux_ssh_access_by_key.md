Title: LINUX: ssh access by key
Date: 2011-12-09 13:27
Modified: 
Category: Programming
Tags: Linux
Slug: linux_ssh_access_by_key
Lang: en
Authors: znotdead
Summary: 

### LINUX: ssh access by key

From local computer A as user a generate a pair of authentication keys. Do not enter a passphrase:

```sh
a@A:~$ ssh-keygen -t rsa Generating public/private rsa key pair. Enter file in which to save the key (/home/a/.ssh/id_rsa): Created directory '/home/a/.ssh'. Enter passphrase (empty for no passphrase): Enter same passphrase again: Your identification has been saved in /home/a/.ssh/id_rsa. Your public key has been saved in /home/a/.ssh/id_rsa.pub. The key fingerprint is: 3e:4f:05:79:3a:9f:96:7c:3b:ad:e9:58:37:bc:37:e4 a@A
```

Create a directory `~/.ssh` as user b on B.:
```sh
a@A:~$ ssh b@B mkdir -p .ssh
```

Finally append a's new public key to `b@B:.ssh/authorized_keys`:
```sh
a@A:~$ cat .ssh/id_rsa.pub | ssh b@B 'cat >> .ssh/authorized_keys'
```
That is all.

**Notes:**
- Put the public key in .ssh/authorized_keys2
- Change the permissions of .ssh to 700
- Change the permissions of .ssh/authorized_keys2 to 640
