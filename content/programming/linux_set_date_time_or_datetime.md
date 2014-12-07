Title: LINUX: set date, time or datetime
Date: 2011-04-28 23:01
Modified: 
Category: Programming
Tags: Linux
Slug: linux_set_date_time_or_datetime
Lang: en
Authors: znotdead
Summary: set date

### LINUX: set date, time or datetime

Set datetime:
```bash
$ sudo date -s "28 APR 2011 10:00:00"
```

Set only date:
```bash
$ sudo date +%Y%m%d -s "20110428"
```

Set only time:
```bash
$ sudo date +%T -s "10:00:00"
```
