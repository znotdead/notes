Title: DJANGO: cycle import debug tip
Date: 2011-12-09 13:31
Modified: 
Category: Programming
Tags: Django
Slug: django_cycle_import_debug_tip
Lang: en
Authors: znotdead
Summary: cycle import

### DJANGO: cycle import debug tip

For better debugging of cycle imports comment following lines:
```python
#except ImportError, e:
#    mod_name, _ = get_mod_func(self._callback_str)
#    raise ViewDoesNotExist("Could not import %s. Error was: %s" % (mod_name, str(e)))
```
in file `{{ DJANGO_PATH }}/core/urlresolvers.py`
