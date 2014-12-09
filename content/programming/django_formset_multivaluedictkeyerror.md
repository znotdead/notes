Title: DJANGO: formset MultiValueDictKeyError
Date: 2011-12-09 13:28
Modified: 
Category: Programming
Tags: Django
Slug: django_formset_multivaluedictkeyerror
Lang: en
Authors: znotdead
Summary: formset MultiValueDictKeyError

### DJANGO: formset MultiValueDictKeyError

Exception Type: 	MultiValueDictKeyError
Exception Value:

Key `form-0-id` not found in <QueryDict: ...


You forgot to add `{{ form.id }}` when iterating though forms of formset in template. i.e.
```
    {{ formset.management_form }}
    {% for form in formset.forms %}
        {{ form.id }}
        <p><b>{{ form.instance.field_1 }}</b></p>
        <dl>
                <dt>{{ form.image.label }}</dt><dd>{{ form.image }}</dd>
                <dt>{{ form.banner_link.label }}</dt><dd>{{ form.banner_link }}</dd>
        </dl>
    {% endfor %}
```
