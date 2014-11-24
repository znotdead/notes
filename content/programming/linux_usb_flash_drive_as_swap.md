Title: LINUX: usb flash drive as swap
Date: 2014-03-10 10:25
Modified: 
Category: Programming
Tags: Linux
Slug: linux_usb_flash_drive_as_swap
Lang: en
Authors: znotdead
Summary: flash drive as swap

### usb flash drive as swap

Change usb flash to another better label. A have had ADATA UFD, but I doesn't like spaces, so I'd like to change it to SWAP_USB

to skip test before all we need change config to avoid error:

Total number of sectors (30869504) not a multiple of sectors per track (63)!
Add `mtools_skip_check=1` to your `.mtoolsrc` file to skip this test

```
echo mtools_skip_check=1 >> ~/.mtoolsrc
```
and then change label:
```
$ sudo mlabel -i /dev/sdb ::swap_usb
```

Make swap file

```
dd if=/dev/zero of=/media/znotdead/SWAP_USB/swap bs=4096 count=524288
```
we will get 2Gb file (2 * 1024 * 1024^2 / 4096 = 524288)

Make swap:

```
sudo mkswap /media/znotdead/SWAP_USB/swap
```

Turn swap on:

```
sudo swapon -p 1000 /media/znotdead/SWAP_USB/swap
```
