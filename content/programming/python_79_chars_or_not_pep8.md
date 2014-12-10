Title: PYTHON: 79 chars or not (pep8)
Date: 2011-12-09 13:30
Modified: 
Category: Programming
Tags: Python
Slug: python_79_chars_or_not_pep8
Lang: en
Authors: znotdead
Summary: pep8

### PYTHON: 79 chars or not (pep8)

The most difficult thing in pep8 is 79 chars.
I think that no one project apply this rule.
You can check percentage of not pep-8 strings in your project by two simple commands:

```python
find -name "*.py" | xargs wc -l
```
Lines that have more than 79 characters :
```
find -name "*.py" | xargs awk '{ if (length($0) > 79) printf("%s:%s\n", FILENAME, FNR);}' | wc -l
```
and compare with other projects you use =)
