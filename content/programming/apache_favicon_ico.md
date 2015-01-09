Title: APACHE: favicon.ico
Date: 2012-01-26 06:57
Modified: 
Category: Programming
Tags: Apache
Slug: apache_favicon_ico
Lang: en
Authors: znotdead
Summary: apache favicon.ico

### APACHE: favicon.ico

In some cases there is request to http://hostname/favicon.ico
but django project doesn't have url to this, so on deployment it will be better to make an alias in apache config:

```
Alias /favicon.ico /var/www/project/media/site/img/favicon.ico
```
