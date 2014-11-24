Title: DJANGO: dump and load data
Date: 2011-12-16 07:02
Modified: 
Category: Programming
Tags: Django
Slug: django_dump_and_load_data
Lang: en
Authors: znotdead
Summary: dump and load data

### dump and load data

If you want to get json from DB for certain model there are 2 usefull commands:
Example is better to show.
To get data from db:

```bash
./manage.py dumpdata global_settings.AutoLetter >  ./tools/initial_data/autoletter.json
```

To load data to db:

```bash
./manage.py loaddata ./tools/initial_data/autoletter.json
```
