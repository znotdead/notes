Title: LINUX: ext4 fs
Date: 2014-11-24 12:09
Modified: 
Category: Programming
Tags: Linux
Slug: ext4_fs
Lang: en
Authors: znotdead
Summary: big HDD load on big MySQL update

### ext4 fs
posted Apr 4, 2012, 4:18 AM by Mila Rahalevich

I was updating many millions rows in MySQL and there was a very big HDD load. I decided to decrease journaling by next options in fstab:
```
UUID  /               ext4    errors=remount-ro,commit=60 0       1
```

Bute after reboot I noticed than mount shows:
```
errors=remount-ro,commit=60,commit=0
```

So I need to remount manually by
```
mount -o remount /
```
Or I have changes in `/usr/lib/pm-utils/power.d/journal-commit`
```
JOURNAL_COMMIT_TIME_AC=${JOURNAL_COMMIT_TIME_AC:-120}
```
