Title: LINUX: exim4 paniclog
Date: 2011-11-05 02:39
Modified: 
Category: Programming
Tags: Linux
Slug: linux_exim4_paniclog
Lang: en
Authors: znotdead
Summary: exim4 paniclog

### LINUX: exim4 paniclog

After reconfiguration exim there is error:
```bash
# dpkg-reconfigure exim4-config
Stopping MTA for restart: exim4_listener.
Restarting MTA: exim4.
ALERT: exim paniclog /var/log/exim4/paniclog has non-zero size, mail system possibly broken ... failed!
```
On ports in seems to me nothing strage using 25
```
# netstat -napt|grep 25
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      14886/exim4
tcp6       0      0 ::1:25                  :::*                    LISTEN      14886/exim4
```
So solution (may be temporary):
```
# rm /var/log/exim4/paniclog
```
