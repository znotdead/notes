Title: PYTHON: _imagingft C module is not installed
Date: 2011-12-13 05:18
Modified: 
Category: Programming
Tags: Python
Slug: python_imagingft_c_module_is_not_installed
Lang: en
Authors: znotdead
Summary: _imagingft C module is not installed

### PYTHON: _imagingft C module is not installed

after installing PIL 1.1.7 and using django-simple-captha there is error:
```
ImportError: The _imagingft C module is not installed
```

The problem was that you need to install dev package for FreeType
```
apt-get install libfreetype6-dev
```
After that re-install PIL:
```
pip install --upgrade pil
```
