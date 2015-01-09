Title: DJANGO: remove empty value in select
Date: 2011-11-11 02:15
Modified: 
Category: Programming
Tags: Django
Slug: django_remove_empty_value_in_select
Lang: en
Authors: znotdead
Summary: remove empty value in select

### DJANGO: remove empty value in select

If you have choices field and in admin you don't want to show empty (field always is required) than in your model you should specify `blank=False` and `default=<value>`. In this case in admin you get choice field without empty value.
