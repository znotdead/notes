Title: APACHE: virtual hosts
Date: 2011-12-09 13:34
Modified: 
Category: Programming
Tags: Apache
Slug: apache_virtual_hosts
Lang: en
Authors: znotdead
Summary: virtual hosts

### APACHE: virtual hosts

Very useful [page](http://wiki.apache.org/httpd/CommonMisconfigurations).

On Debian there is `ports.conf` file for apache where `Listen port` and `NameVirtualHost` specified. So there is no need to specify it in `httpd.conf`.

It causes warnings when
```
$ /usr/sbin/apache2ctl configtest

"NameVirtualHost *:80 has no VirtualHosts"
```

as it was in my case. Also I disabled all `./site-enabled` sites and then my sites from httpd start working.

here my `httpd.conf`:
```
<Directory /var/www>
    Order deny,allow
    Allow from all
</Directory>

<VirtualHost *:80>
    DocumentRoot /var/www/site1
    ServerName www.site1.my
    ServerAlias site1.my

    # Other directives here
    WSGIScriptAlias / /var/www/site1/apache/site1.wsgi
    Alias /media /var/www/site1/media/
</VirtualHost>

<VirtualHost *:80>
    DocumentRoot /var/www/site2
    ServerName www.site2.my
    ServerAlias site2.my

    # Other directives here
    WSGIScriptAlias / /var/www/site2/apache/site2.wsgi
    Alias /media /var/www/site2/media/
</VirtualHost>
```
