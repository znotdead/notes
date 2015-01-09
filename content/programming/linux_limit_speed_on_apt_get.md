Title: LINUX: limit speed on apt-get
Date: 2013-02-08 13:23
Modified: 
Category: Programming
Tags: Linux
Slug: linux_limit_speed_on_apt_get
Lang: en
Authors: znotdead
Summary: limit speed of apt-get

### LINUX: limit speed on apt-get

Limiting speed to near 200 kB/s. Note that not exactly.
```
sudo apt-get -o  Acquire::http::Dl-Limit=200 -y dist-upgrade
```
