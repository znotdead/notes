Title: PYTHON: mimetypes
Date: 2012-07-04 07:14
Modified: 
Category: Programming
Tags: Python
Slug: mimetypes
Lang: en
Authors: znotdead
Summary: set correct header to response for browser

### mimetypes

If your linux setup in files `python -c 'import mimetypes; print mimetypes.knownfiles'` doesn't have xlsx, for example, than on download of file in opera it will change it to zip or anything else.

So if browser doesn't recognize file extension, than mimetype and encoding are `None`

```python
>>> import mimetypes
>>> mimetypes.guess_type('filename.xlsx')
(None, None)
```

Mimetype looks for type in files:

```python
>>> mimetypes.knownfiles
['/etc/mime.types', '/etc/httpd/mime.types', '/etc/httpd/conf/mime.types', '/etc/apache/mime.types', '/etc/apache2/mime.types', '/usr/local/etc/httpd/conf/mime.types', '/usr/local/lib/netscape/mime.types', '/usr/local/etc/httpd/conf/mime.types', '/usr/local/etc/mime.types']
```

If we add `'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet xlsx'`  in one of this files than

```python
>>> mimetypes.guess_type('filename.xlsx')
('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', None)
```

and we can set correct header to response to browser understand.
