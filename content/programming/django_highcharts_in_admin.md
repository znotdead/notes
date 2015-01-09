Title: DJANGO: highcharts in admin
Date: 2011-11-22 04:16
Modified: 
Category: Programming
Tags: Django
Slug: django_highcharts_in_admin
Lang: en
Authors: znotdead
Summary: highcharts in admin

### DJANGO: highcharts in admin

Highcharts require jQuery so in your custom template you need 2 lines ( not only charts) because by default in admin there is a jquery by accessible by `django.jQuery` and `var $ = django.jQuery;` won't help you.

```
<script type="text/javascript" src="{{ MEDIA_URL }}site/js/jquery-1.4.4.min.js"></script>
<script type="text/javascript" src="{{ MEDIA_URL }}site/js/highcharts.js"></script>
```
