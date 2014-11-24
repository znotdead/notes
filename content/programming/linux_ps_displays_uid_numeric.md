Title: LINUX: ps displays UID numeric
Date: 2012-06-25 04:24
Modified: 
Category: Programming
Tags: Linux
Slug: linux_ps_displays_uid_numeric
Lang: en
Authors: znotdead
Summary: ps UID numeric

### ps displays UID numeric

By default ps displays `$UID` `$GUID` as names (words) but when you wants to select process by user with certain `$UID` you should use n option i.e. `ps auxww`

Output:
```
daemon    1048  0.0  0.0  16784   376 ?        Ss   10:56   0:00 atd
root      1049  0.0  0.0  18984  1028 ?        Ss   10:56   0:00 cron
114       1253  0.0  0.0  48784  1124 ?        Ss   10:56   0:00 /usr/sbin/exim4 -bd -q30m
1000      2206  0.0  0.6 630752 26416 ?        Sl   10:56   0:01 nautilus -n
```

With `n` option `ps auxwwn`

Output:
```
      1  1048  0.0  0.0  16784   376 ?        Ss   10:56   0:00 atd
       0  1049  0.0  0.0  18984  1028 ?        Ss   10:56   0:00 cron
     114  1253  0.0  0.0  48784  1124 ?        Ss   10:56   0:00 /usr/sbin/exim4 -bd -q30m
    1000  2206  0.0  0.6 630752 26416 ?        Sl   10:56   0:01 nautilus -n
```
