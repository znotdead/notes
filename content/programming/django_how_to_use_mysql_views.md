Title: DJANGO: how to use mysql views
Date: 2011-12-09 13:35
Modified: 
Category: Programming
Tags: Django
Slug: django_how_to_use_mysql_views
Lang: en
Authors: znotdead
Summary: MySQL views
Status: draft

### DJANGO: how to use mysql views

You have a statistics. Lets see this on bug tracker example statistics, i.e. you wish statistics looks like:
```python
class Stat(models.Model):
    date = ...
    bugs_open = IntegerField(...)
    bugs_closed = ...
    bugs_inprogress = ...
    bugs_invalid = ...
```
app_label = stattracker.
And you need to make filters and so on by sum of all active bugs. So you can add column as bugs_active and fill it by trigger. But it is not what we want.
We can make Stat as abstract class, i.e.
```python
class Stat(modes.Model):
    ...

    class Meta:
        abstract = True
```
and than create 2 models.
First model will be a copy of abstract. i.e.
```python
class StatTracker(Stat):
    pass
```
Notice that we inherit from abstract class `Stat`

and another model will be for view. i.e.
```python
class StatTrackerView(Stat):
    bugs_sum = ...
    bugs_active_sum = ...

    class Meta:
        managed = False
```
and now create MysqlView
```sql
CREATE OR REPLACE VIEW trackerstat_stattrackerview AS
SELECT *,(bugs_open+bugs_inprogress) as bugs_active_sum,
(bugs_open+bugs_inprogress+bugs_invalid) as bugs_sum
FROM trackerstat_stattracker;
```
Adventages:
- You do not need triggers to update sum fields
- simple adding new sum fields. Only change view and add field to model.
- ...


Disadventages:
- You should remember that you have 2 models. I for get data and there is OperationalError when trying to save View model. And 2 model is for put data.
- ...
