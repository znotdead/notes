Title: LINUX: make deb from tarball
Date: 2012-12-10 21:09
Modified: 
Category: Programming
Tags: Linux
Slug: linux_make_deb_from_tarball
Lang: en
Authors: znotdead
Summary: make deb from tarball

### LINUX: make deb from tarball
`dh-make` - tool that converts source archives into Debian package source

*Example:*
```sh
tar -xvvf vim-7.1.tar.bz2
cd vim71/
dh_make -p vim_7.1 -f ../vim-7.1.tar.bz2 -e emailk@gmail.com
dpkg-buildpackage -rfakeroot
```
