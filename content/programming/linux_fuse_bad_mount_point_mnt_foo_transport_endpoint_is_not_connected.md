Title: LINUX: fuse: bad mount point /mnt/foo: Transport endpoint is not connected
Date: 2011-11-05 09:05
Modified: 2011-11-05 09:05
Category: Programming
Tags: Linux
Slug: linux_fuse_bad_mount_point_mnt_foo_transport_endpoint_is_not_connected
Lang: en
Authors: znotdead
Summary: fuse: bad mount point /mnt/foo

### fuse: bad mount point /mnt/foo: Transport endpoint is not connected

1. kill sshfs
2. kill all that uses /mnt/foo (`lsof | grep foo`)
3. umount -l /mnt/foo
4. mount sshfs again
