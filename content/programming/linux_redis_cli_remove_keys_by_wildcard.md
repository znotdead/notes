Title: LINUX: redis-cli remove keys by wildcard
Date: 2011-11-10 12:57
Modified: 
Category: Programming
Tags: Linux,  Redis
Slug: linux_redis_cli_remove_keys_by_wildcard
Lang: en
Authors: znotdead
Summary: redis-cli remove keys by wildcard

### LINUX: redis-cli remove keys by wildcard

```
#!/bin/bash
redis-cli keys $1 | awk '{print $1}' | xargs --interactive redis-cli del {} \;
```
How to use:
```
redis-del pattern*
```
[Source](http://www.rustyrazorblade.com/2011/04/redis-wildcard-delete/)
