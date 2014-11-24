Title: LINUX: ssh config
Date: 2011-10-12 05:46
Modified: 
Category: Programming
Tags: Linux
Slug: linux_ssh_config
Lang: en
Authors: znotdead
Summary: ssh config

### ssh config

You can make alias for ssh access to your repository for example. Place this line in `~/.bash_aliases`

```
alias ssh_repo='ssh -2 username@192.168.1.10 -i /home/znotdead/.ssh/repo.username.id_rsa'
```

But if you would like to make hg push you can't do it beautifully. For that all you need that is make config file in `~/.ssh`
```
$ touch ~/.ssh/config
$ vim ~/.ssh/config
```
Place next lines in your file:
```
Host hg
     IdentityFile ~/.ssh/repo.username.id_rsa
     HostName 192.168.1.10
     User username
```

Here you are =). Now you can access to you repo by:
```
$ ssh hg
```
and from mercurial by URL:
```
ssh://username@hg/~/repo_folder
```
