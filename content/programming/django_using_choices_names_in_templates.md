Title: DJANGO: using choices names in templates
Date: 2011-10-09 13:32
Modified: 
Category: Programming
Tags: Django
Slug: django_using_choices_names_in_templates
Lang: en
Authors: znotdead
Summary: use choice name

### DJANGO: using choices names in templates

In `Building` model there are choices for status:
```python
BUILDING_STATUS = (
    ('project', 'Planning'),
    ('inprogress', 'Working'),
    ('ready', 'Ready'),
)
```

Once I found in code smth like this:
```django
{% if building.status == 'project' %}Planning{% endif %}
{% if building.status == 'inprogress' %}Working {% endif %}
{% if building.status == 'ready' %}Ready{% endif %}
```
YOU SHOULD NOT DO THAT. It s ugly! Adding one status is painful as you need to rewrite all templates.

Solution? Django already do useful helper for you:
`{{ building.get_status_display }}`
