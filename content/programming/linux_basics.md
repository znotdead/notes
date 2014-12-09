Title: LINUX: basics
Date: 2011-12-09 13:34
Modified: 
Category: Programming
Tags: Linux
Slug: linux_basics
Lang: en
Authors: znotdead
Summary: basics

### LINUX: basics

One day I was needed to write list of the most usable commands for those who knows nothing about linux. To not to loose this list I post it here

Suppose main programs I mentioned below, may be something I missed. You can add other commands to this list.
I recommend to try each command and read man's to remember it :)
MUST KNOW check list ( without options ):
for all commands to see more complete information use: `man <command>` or `info <command>`

`ls` - list directory contents ( `ls -lah`  for me it is the most usable combination )
*Examples:*
```sh
$ ls -lah  # shows current dir contents
$ ls -lah /  # shows contens of root derictory (if you has permissions)
```

`cd` - change directory (built-in in Bash)
*Examples:*
```sh
$ cd # move to directory in $HOME env. variable, i.e. you home directory
$ cd /srv/ # moving to srv directory from root, i.e. you are now in /srv
$ cd ./srv/ #moving to srv from current dir, i.e. you are now in $OLDPWD/srv
$ cd - # go to $OLDPWD dir
```

`less` - viewer of files
*Examples:*
less <path_to_file> # shows file conents
if ypu press h You will see many available commands for less. most useful can be:
q - quit
F - Forward forever; like "tail -f".
/pattern  - Search forward for (N-th) matching line.
?pattern - Search backward for (N-th) matching line.
n -  Repeat previous search (for N-th occurrence).
N -  Repeat previous search in reverse direction.
g - Go to first line in file (or line N).
G  -  Go to last line in file (or line N).
:n  -  Examine the (N-th) next file from the command line.
:p - Examine the (N-th) previous file from the command line.
v - Edit the current file with $VISUAL or $EDITOR.

`vim` - file editor and very powerful IDE ( To begin using it pass through small tutorial for 15 minutes `vimtutor` )

`ps`  - processes snapshot (the most usable are `ps axf`, ` ps -eo euser,ruser,suser,fuser,f,comm` )

`grep` - print lines matching a pattern ( the most usable `grep -irn` (ignore case, recursive, line number)
*Examples:*
```sh
$ ps axf | grep mongo
17422 pts/0    S+     0:00  |           \_ grep mongo
22581 ?        S      0:00 /bin/bash /opt/sbin/daemonizer.sh --working-dir /opt/var/mongo --name mongo --pid /opt/var/run/mongo.pid --log /opt/var/log/mongo.log -- /opt/mongodb-linux-x86_64-1.6.2/bin/mongod --dbpath=/srv/Mongo-Data
22582 ?        S      0:00  \_ /bin/bash /opt/sbin/daemonizer.sh --working-dir /opt/var/mongo --name mongo --pid /opt/var/run/mongo.pid --log /opt/var/log/mongo.log -- /opt/mongodb-linux-x86_64-1.6.2/bin/mongod --dbpath=/srv/Mongo-Data
22583 ?        Sl    74:28  |   \_ /opt/mongodb-linux-x86_64-1.6.2/bin/mongod --dbpath=/srv/Mongo-Data
22584 ?        S      0:49  \_ /bin/bash /opt/sbin/daemonizer.sh --working-dir /opt/var/mongo --name mongo --pid /opt/var/run/mongo.pid --log /opt/var/log/mongo.log -- /opt/mongodb-linux-x86_64-1.6.2/bin/mongod --dbpath=/srv/Mongo-Data

$ ps axf | grep MONGO
17432 pts/0    S+     0:00  |           \_ grep MONGO

$ ps axf | grep -irn MONGO
73:17434 pts/0    S+     0:00  |           \_ grep -irn mongo
103:22581 ?        S      0:00 /bin/bash /opt/sbin/daemonizer.sh --working-dir /opt/var/mongo --name mongo --pid /opt/var/run/mongo.pid --log /opt/var/log/mongo.log -- /opt/mongodb-linux-x86_64-1.6.2/bin/mongod --dbpath=/srv/Mongo-Data
104:22582 ?        S      0:00  \_ /bin/bash /opt/sbin/daemonizer.sh --working-dir /opt/var/mongo --name mongo --pid /opt/var/run/mongo.pid --log /opt/var/log/mongo.log -- /opt/mongodb-linux-x86_64-1.6.2/bin/mongod --dbpath=/srv/Mongo-Data
105:22583 ?        Sl    74:28  |   \_ /opt/mongodb-linux-x86_64-1.6.2/bin/mongod --dbpath=/srv/Mongo-Data
106:22584 ?        S      0:49  \_ /bin/bash /opt/sbin/daemonizer.sh --working-dir /opt/var/mongo --name mongo --pid /opt/var/run/mongo.pid --log /opt/var/log/mongo.log -- /opt/mongodb-linux-x86_64-1.6.2/bin/mongod --dbpath=/srv/Mongo-Data
```

`man` ( `man -k` )
*Examples:*
```sh
$ man man
$ man 5 config # open man specifying section (man for one command can be placed in 2 or more sections )
```

`info`
*Examples:*
```sh
$ info info
```

`rpm` - RPM Package Manager
*Examples:*
```sh
$ rpm -q memcached -i  # info about a package
Name        : memcached                    Relocations: (not relocatable)
Version     : 1.4.5                             Vendor: Fedora Project
Release     : 1.el5                         Build Date: Tue 06 Apr 2010 09:27:51 PM EEST
Install Date: Mon 27 Sep 2010 01:42:44 PM EEST      Build Host: x86-03.phx2.fedoraproject.org
Group       : System Environment/Daemons    Source RPM: memcached-1.4.5-1.el5.src.rpm
Size        : 147753                           License: BSD
Signature   : DSA/SHA1, Wed 07 Apr 2010 08:25:46 PM EEST, Key ID 119cc036217521f6
Packager    : Fedora Project
URL         : http://www.memcached.org/
Summary     : High Performance, Distributed Memory Object Cache
Description :
memcached is a high-performance, distributed memory object caching
system, generic in nature, but intended for use in speeding up dynamic
web applications by alleviating database load.

$ rpm -q memcached  # query package installed

$ rpm -qa | grep vim

$ rpm -qf /etc/profile
setup-2.5.25-1

$ rpm -q memcached -l  # show package list
/etc/rc.d/init.d/memcached
/etc/sysconfig/memcached
/usr/bin/memcached
/usr/bin/memcached-tool
/usr/share/doc/memcached-1.4.5
/usr/share/doc/memcached-1.4.5/AUTHORS
/usr/share/doc/memcached-1.4.5/CONTRIBUTORS
/usr/share/doc/memcached-1.4.5/COPYING
/usr/share/doc/memcached-1.4.5/ChangeLog
/usr/share/doc/memcached-1.4.5/NEWS
/usr/share/doc/memcached-1.4.5/README
/usr/share/doc/memcached-1.4.5/protocol.txt
/usr/share/doc/memcached-1.4.5/readme.txt
/usr/share/doc/memcached-1.4.5/threads.txt
/usr/share/man/man1/memcached.1.gz
/var/run/memcached

$ rpm -iv --test MySQL-client-community-5.1.48-1.rhel5.x86_64.rpm # test installation verbosly
Preparing packages for installation...
        package MySQL-client-community-5.1.48-1.rhel5.x86_64 is already installed

$ rpm -Uvh totem-0.99.5-1.fr.i386.rpm # install package
```

`ssh` - OpenSSH SSH client (remote login program)
*Examples:*
```sh
$ ssh user@10.10.0.221 "ps axf | grep mono" > /tmp/1.txt  # execute command "ps axf | grep mono" on 221 comp under user user and write output to file /tmp/1.txt
Attention: file will be overwritten
$ ssh user@10.10.0.232 # login to 232 as user
```

`scp` - secure copy (remote file copy program)
*Examples:*
```sh
$ scp user@host1:file1 user@host2:file2
$ scp -r /tmp/*.log host:/tmp/logs_from_host1 #copy all files ends 'log' to host
```

`screen`
*Examples:*
```sh
$ screen -r [[pid.]tty[.host]] #connect to previous session
```
there are too many commands. All of them you can see on man pages

`cp` - copy files and directories
*Examples:*
```sh
$ cp file1 file2
$ cp -r /tmp/*.lock /tmp/z/ # copy all lock files from /tmp to /tmp/z
```

`mv` - move (rename) files

`rm` - remove files or directories
*Examples:*
```sh
$ rm /tmp/z/1/*.lock #rm all lockfiles from /tmp/z/1/
$ rm -r /tmp/z/1/ # rm dir 1 with all it's content
```

`yum` - Yellowdog Updater Modified ( is  an interactive, rpm based, package manager)
( `yum search`, `yum install`, `yum update`, `yum remove`, `yum info` )
*Examples:*
```sh
$ sudo yum search memcached # search package
============================== Matched: memcached ==============================
libmemcache.x86_64 : A client library for memcached
memcached.x86_64 : Distributed memory object caching system
memcached-devel.x86_64 : Header files for memcached
memcached-devel.i386 : Files needed for development using memcached protocol
perl-Apache-Session-Memcached.noarch : Perl module to store persistent data
                                     : using memcached
perl-Cache-Memcached.noarch : Perl module implements a client library for
                            : memcached
perl-Memcached-libmemcached.x86_64 : Thin fast full interface to the
                                   : libmemcached client API
php-pecl-memcache.x86_64 : PECL package to use the memcached distributed caching
                         : system
python-memcached.noarch : Python interface to the memcached memory cache daemon
python-openid.noarch : Python OpenID libraries
python-shove.noarch : Common object storage frontend

$  sudo yum install memcached  # install founded package
```

`tar` - The GNU version of the tar archiving utility
*Examples:*
```sh
$ tar -xvvzf tarfile.tar.gz # extract tar file to currnet dir
$ tar -cvvzf   bar/ # create gzipped tar archive of bar directory called foo.tar.gz
$ tar -cjf foo.tar.bz2 bar/  # create bzipped tar archive of the directory bar called foo.tar.bz2
$ tar -xzf foo.tar.gz blah.txt # extract the file blah.txt from foo.tar.gz
```

`who` - show who is logged on
*Examples:*
```sh
$ who -u
```

`whoami` - print effective userid (alias for  id -un )
*Examples:*
```sh
$ whoami
user
```

`touch` - change file timestamps (Update the access and modification times of each FILE to the current time.)
*Examples:*
```sh
$ ls -lah # change timestamp. if file not exists create it (if no option -c )
total 64K
drwxrwxr-x 2 user user 4.0K Sep 27 15:29 .
drwxrwxrwt 9 root  root   52K Sep 27 15:41 ..
$ touch 1.tzt
$ ls -lah
total 64K
drwxrwxr-x 2 user user 4.0K Sep 27 15:43 .
drwxrwxrwt 9 root  root   52K Sep 27 15:41 ..
-rw-rw-r-- 1 user user    0 Sep 27 15:43 1.tzt
$ date
Mon Sep 27 15:43:28 EEST 2010
$ touch 1.tzt
$ ls -lah
total 68K
drwxrwxr-x 2 user user 4.0K Sep 27 15:43 .
drwxrwxrwt 9 root  root   52K Sep 27 15:41 ..
-rw-rw-r-- 1 user user   13 Sep 27 15:46 1.tzt
$ date
Mon Sep 27 15:46:21 EEST 2010
```

`tail` - output the last part of files
*Examples:*
```sh
$ tail  /var/log/yum.log
$ tail -f /var/log/yum.log # output  appended  data  as  the  file  grows
```

`head` - output the first part of files
*Examples:*
```sh
$ head -n 15 /var/log/yum.log # prints first 15 lines
$ head /var/log/yum.log # prints first 10 lines
```

`cat` - concatenate files and print on the standard output
*Examples:*
```sh
$ echo 'file1' > 1.txt
$ echo 'file2' > 2.txt
$ cat *.txt > 12.txt # concatenate 2 files in one
$ cat 12.txt # if 1 file is given then prints to stdout.
file1
file2
```

`/dev/null` or the null device is a special file that discards all data written to it (but reports that the write operation succeeded) and provides no data to any process that reads from it (yielding EOF immediately)
`/dev/zero` is a special file that provides as many null characters (ASCII NUL, 0x00) as are read from it
`/der/random` is a special file that serves as a random number generator or as a pseudorandom number generator

`dd` - convert and copy a file (data duplicate )
*Examples:*
```sh
$ dd if=/dev/zero of=/dev/null count=10MB & pid=$! # `dd' is run in the background to copy 10 million blocks.
$ kill -s INFO $pid; wait $pid
3385223+0 records in
3385223+0 records out
1733234176 bytes (1.7 GB) copied, 6.42173 seconds, 270 MB/s
10000000+0 records in
10000000+0 records out
5120000000 bytes (5.1 GB) copied, 18.913 seconds, 271 MB/s
$ dd if=/dev/fd0H1440 of=/var/tmp/images.tar.gz # make backup
$ dd if=images-without-dir.tar.gz of=/dev/fd0H1440 # restore from backup
```

`find` - search for files in a directory hierarchy
*Examples:*
find [path...] [expression]
```sh
$ find /tmp/ -type f -name *.lock # find files with name lock in the end
$ find /tmp/ -type f # find dirs
```

`svn` -Subversion command line client tool
*Examples:*
```sh
$ svn update
```
and many others . see svn help and google

`du` - estimate file space usage
*Examples:*
```sh
$ du -hs /tmp/
du: cannot read directory `/tmp/mc-root': Permission denied
44M     /tmp/
```

`which` - shows the full path of (shell) commands.
*Examples:*
```sh
$ which my_command.sh
/opt/my_command.sh
```

`echo` - display a line of text
*Examples:*
```sh
$ echo -e "ksjdfhjksdhf\nasdhfjkhsdfjkh\tsdkjf\tskldf\nlasjkdjfh"
ksjdfhjksdhf
asdhfjkhsdfjkh  sdkjf   skldf
lasjkdjfh
$ echo "ksjdfhjksdhf\nasdhfjkhsdfjkh\tsdkjf\tskldf\nlasjkdjfh"
ksjdfhjksdhf\nasdhfjkhsdfjkh\tsdkjf\tskldf\nlasjkdjfh
```

`vimdiff` - edit two or three versions of a file with Vim and show differences
  do – Get changes from other window into the current window.
  dp – Put the changes from current window into the other window.
  ]c – Jump to the next change.
  [c – Jump to the previous change.
  Ctrl W + Ctrl W – Switch to the other split window.
  :diffupdate – diff update
  :syntax off – syntax off
  zo – open folded text
  zc – close folded text

`pwd` - print working directory ( alias for echo $PWD )

`date` -print or set the system date and time

`uname` -print system information ( uname -a )

`ping` - send ICMP ECHO_REQUEST to network hosts. To quit press ctrl+C
*Examples:*
```sh
$ ping 10.10.0.221
PING 10.10.0.221 (10.10.0.221) 56(84) bytes of data.
64 bytes from 10.10.0.221: icmp_seq=1 ttl=64 time=0.589 ms
64 bytes from 10.10.0.221: icmp_seq=2 ttl=64 time=0.249 ms

--- 10.10.0.221 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 999ms
rtt min/avg/max/mdev = 0.249/0.419/0.589/0.170 ms
```

`ifconfig` - configure a network interface
*Examples:*
```sh
$ ifconfig eth0 10.10.0.221 #setup interface eth0 to 10.10.0.221 ip
```

`wc` - print the number of newlines, words, and bytes in files
*Examples:*
```sh
$ ls -lah /var/log/ | wc -l
80
```

`watch` - execute a program periodically, showing output fullscreen
*Examples:*
```sh
$ watch -n 20  "ps axf | grep mono | sort "
```

`sudo` -  execute a command as another user
*Examples:*
```sh
$ sudo -u www vi ~www/htdocs/index.html #
```
To edit the index.html file as user www:
```sh
$ sudo shutdown -r +15 "quick reboot" #
```
To shutdown a machine

`top` -display Linux tasks

`mc` - Visual shell for Unix-like systems.

`chmod` - change file access permissions (change mode)
*Examples:*
```sh
$ chmod 664 myfile
$ ls -l myfile -rw-rw-r-- 1 57 Jul 3 10:13 myfile
$ chmod a+r file # read is added for all$ chmod -R u+w,go-w docs  # change the permissions of the directory docs and all its contents to add write access for the user, and deny write access for everybody else.
$ chmod 755 file  #  is equivalent to u=rwx (4+2+1),go=rx (4+1 & 4+1). (user, group, others )
4 = read
2 = write
1 = execute
$ chmod 666 ./dir1
$ ls ./dir1
1.txt
$ cd ./dir1
-bash: cd: ./1: Permission denied #if folder has no execute permission you can't enter to it but can read it
```

`chown` -  change file owner and group
*Examples:*
```sh
$ sudo chown user2.wheel ./1/1.txt
$ sudo ls -lah ./1
total 8.0K
drw-rw-rw- 2 user user 4.0K Sep 27 16:33 .
drwxrwxr-x 3 user user 4.0K Sep 27 16:32 ..
-rw-rw-r-- 1 user2  wheel    0 Sep 27 16:33 1.txt
```

`wget` - The non-interactive network downloader
*Examples:*
```sh
$ wget -c http://sourceforge.net/projects/pam-mysql/files/pam-mysql/0.7RC1/pam_mysql-0.7RC1.tar.gz/download #download file in current dir
```

`lynx` - is a text-based web browser for use on cursor-addressable character cell terminals and is very configurable.

`ntpdate` - set the date and time via NTP
`rdate`  - get the time via the network
*Examples:*
```sh
$ /usr/sbin/ntpdate ntp.apple.com
$ rdate -s rdate.cpanel.net
```

`kill` -  terminate a process
*Examples:*
```sh
# send SIGTERM (1234 - pid of process )
$ kill 1234
$ kill -s TERM 1234
# send SIGKILL
$ kill -9 1234
```

`cal` -  displays a calendar
*Examples:*
```sh
$ cal -my
```

`awk` - pattern scanning and processing language
*Examples:*
```sh
$cat /etc/group | awk  'BEGIN     { FS = ":" } {print $1 | "sort -r"}' # prints all users in system in reverse order
```

`sed` - stream editor for filtering and transforming text
*Examples:*
```sh
$ sed -e 's/oldstuff/newstuff/g' inputFileName > outputFileName
```

`netstat` - Print  network  connections, routing tables, interface statistics,
       masquerade connections, and multicast memberships
*Examples:*
```sh
$netstat -sp tcp
```

`.` -current dir
`.filename` - hidden file
`..` - parent dir

`mkdir` - make directories
*Examples:*
```sh
$ mkdir ./z/1 # if there is no z folder in current dir
mkdir: cannot create directory `./z/1': No such file or directory
$ mkdir -p ./z/1 # no error if existing, make parent directories as needed
$ mkdir /tmp/zz
```

`|` - pipe, sends stdout of one program to stdin of other,
*Examples:*
```sh
$ cat 1. txt | grep 'hi'
```
`>`, `<`
*Examples:*
```sh
$ cat 1.txt > 11.txt
$ cat 11.txt
file1
$ mysql < file1.sql
```

`>>`
*Examples:*
```sh
$ cat 11.txt
file1
[user@machine z]$ echo "sdkjfhsdjkfhjkh" >> 11.txt
[user@machine z] DEV $ cat 11.txt
file1
sdkjfhsdjkfhjkh
```

`shutdown` -  bring the system down
`halt`, `reboot`, `poweroff` - stop the system.
`fsck` - check and repair a Linux file system
`alias` - define or print aliases
`set` - prints all variables
`sort` - sort lines of text files
`uniq` - report or omit repeated lines
`history` -prints commands history
`file`  - determine file type
`vmstat` - Report virtual memory statistics
`strace` - trace system calls and signals (If you can't understand why program falling use it for DEBUG purposes )
`useradd`, `adduser`, `userdel`, `groupadd`, `groupdel` - managing accounts
`mount` - mount a file system
`passwd` - change the password for the current user
`df` - report file system disk space usage
`export` - set env. variable
`locate` - find files by name
`ln` - make links between files
`sleep` - Delay for a specified time.
`lsof` - Identify processes.
`tree` - list contents of directories in a tree-like format.
*Examples:*
```sh
$ file /usr/bin/mysql
/usr/bin/mysql: ELF 64-bit LSB executable, AMD x86-64, version 1 (SYSV), for GNU/Linux 2.6.9, dynamically linked (uses shared libs), for GNU/Linux 2.6.9, stripped
$ mount -t iso9660 -o ro /dev/cdrom /mnt/cdrom
$ alias
alias l='ls -lah'
alias l.='ls -d .* --color=tty'
alias ll='ls -l --color=tty'
alias ls='ls --color=tty'
alias mc='. /usr/share/mc/bin/mc-wrapper.sh'
alias vi='vim'
alias which='alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde'
$ export PATH=$PATH:/opt/acroread/bin
$ ln -s targetfile linkname #symbolic link
```

`jobs`  - prints all jobs
Ctrl+Z- Suspend (stop, but not quit) a process running in the foreground (suspend).Ctrl+C - Interrupt (terminate and quit) a process running in the foreground.
fg - move job to foreground
bg - move job to background

`killall` - kill processes by name
*Examples:*
```sh
$ killall gdm
```

`bash`
```sh
$ man bash
```
[VERY COOL BASH BOOK](http://tldp.org/LDP/abs/html/) to become PRO. VERY MUST READ for BASH scripting!!!
