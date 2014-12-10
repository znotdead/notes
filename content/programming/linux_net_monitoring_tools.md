Title: LINUX: net monitoring tools
Date: 2011-12-09 13:30
Modified: 
Category: Programming
Tags: Linux
Slug: linux_net_monitoring_tools
Lang: en
Authors: znotdead
Summary: net monitor

### LINUX: net monitoring tools

Sometimes I saw a great network activity but I do not know what happening.
We can investigate who eats our traffic by:
```sh
$ sudo iftop -i wlan0
```
There are many information displayed. In and out rates, graphical view for every connection by in and out.
Here we can see CONNECTION url and rates.
and another way is
```sh
$ sudo nethogs wlan0
```
The output looks much better for eye and all processes are sorted by traffic.
Here we can see PID, PROGRAMM, USER and DEVICE with rates. It allows you to find and quickly kill process.
