Title: DJANGO: do not dissplay any links in admin change_list
Date: 2011-12-23 12:29
Modified: 
Category: Programming
Tags: Django
Slug: django_do_not_dissplay_any_links_in_admin_change_list
Lang: en
Authors: znotdead
Summary: do not dissplay any links in admin change_list

### do not dissplay any links in admin change_list

There is example where in change list I want to display coutry and city for example but do not show links to edit it.
This will not work:
```python
class GeoAdmin(admin.ModelAdmin):
    list_display = ('country', 'city',)
    list_display_links = []
```
because there is check on empty list in django.
And this will work:
```python
class GeoAdmin(admin.ModelAdmin):
    list_display = ('country', 'city',)

    def __init__(self, *args, **kwargs):
        super(GeoAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = (None,)
```
