Title: DJANGO: cycle imports
Date: 2011-12-09 13:36
Modified: 
Category: Programming
Tags: Django
Slug: django_cycle_imports
Lang: en
Authors: znotdead
Summary: cycle import

### DJANGO: cycle imports

to fix cycle imports you should specify `ForeignKeys` as strings
```python
flat = models.ForeignKey('Flat')
```
but if model is placed in other application you should specify it
```python
flat = models.ForeignKey('building.Flat')
```
