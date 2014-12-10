Title: PYTHON: base64 multiple lines
Date: 2011-12-09 13:28
Modified: 
Category: Programming
Tags: Python
Slug: python_base64_multiple_lines
Lang: en
Authors: znotdead
Summary: base64

### PYTHON: base64 multiple lines

Here's how to use it.
```python
>>> import base64
>>> base64.encodestring('hello world') 'aGVsbG8gd29ybGQ=\n'
>>> base64.decodestring(_) 'hello world'
>>>
```

If the text is long, the base64 module will split the encoded data into multiple lines. And thus we need to replace '\n' in results.
