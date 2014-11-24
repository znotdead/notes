Title: PYTHON: csv with Cyrillic
Date: 2011-12-23 02:39
Modified: 
Category: Programming
Tags: Python
Slug: python_csv_with_cyrillic
Lang: ru
Authors: znotdead
Summary: csv with Cyrillic

### csv with Cyrillic

When I need to generate a csv with Russian comments for correct display in Excel (OpenOffice suggest you encoding) you need to convert all to cp1251 =(

Also You need to remember that first field should NOT to be ID because of [MS Office bug](http://support.microsoft.com/kb/323626/)
So in Django whet I return a csv file:

```python
response = HttpResponse(mimetype='text/csv')
response['Content-Disposition'] = 'attachment; filename=filename.csv'
w = csv.writer(response, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# first field should NOT to be ID because of [MS Office bug](http://support.microsoft.com/kb/323626/)
# MS Excel doesn't understand UTF-8 for csv. So... cp1251 =(

w.writerow(map(lambda x: unicode(x).encode('cp1251'),
                         [u'Номер', u'Примечание']))
for item in queryset:
    row = [item.number, unicode(item.comment)]
    w.writerow(map(lambda x: unicode(x).encode('cp1251'), row))
return response
```
