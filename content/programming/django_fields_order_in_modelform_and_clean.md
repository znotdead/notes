Title: DJANGO: fields order in ModelForm and clean
Date: 2011-04-20 23:14
Modified: 2011-07-29 3:33
Category: Programming
Tags: Django
Slug: django_fields_order_in_modelform_and_clean
Lang: en
Authors: znotdead
Summary: fields order

### DJANGO: fields order in ModelForm and clean

Imagine that we wants to clean field image differently in dependence of value of type.
```python
class MyImageForm(forms.ModelForm):
    class Meta:
        model = MyImage
        fields = ('image', 'type', 'image_url')
```

in this case from `clean_image` method we can't get `self.cleaned_data['type']`. But if we change order :
```python
fields = ( 'type', 'image', 'image_url')
```
In this case type will be available in `self.cleaned_data['type']` and we can validate in dependence of it's value.
So in my case it works. (django 1.2)
But in docs I can't found any information about it only by sources. Fields order influence not only render order but and clean.
