Title: MERCURIAL: fncache error
Date: 2011-12-09 13:33
Modified: 
Category: Programming
Tags: Mercurial
Slug: mercurial_fncache_error
Lang: en
Authors: znotdead
Summary: fncache error

### MERCURIAL: fncache error

Existing non-fncache repositories, that is, repositories created with Mercurial 1.0 (or older), will remain as they are, as Mercurial will still be able to read and write non-fncache repositories.

The fncache repo format can be disabled with
```
[format]
usefncache = False
```
in the `hgrc` [see](http://www.selenic.com/mercurial/hgrc.5.html#format) or with `--config format.usefncache=0` on the command line. For example, the command
```
$ hg --config format.usefncache=0 clone --pull A B
```

converts the local fncache repo A to non-fncache repo B.

If you need to use mercurial repository which was created with fncache than you need in `.hg/requires` delete `fncache` row.

If you have `tar.gz`, for example, with broken repo than you should extract it in REPO folder and than convert it to fix by:
```
hg convert --config convert.hg.ignoreerrors=True ./REPO/ ./FIXED_REPO/
```
In my case there was one deleted file and it was displayed as not commited changes. I was needed to commit fixing repo and now I can use it. This solution can be applied if you have only one initial commit in broken repo. So cases with rolling back can't be used.
