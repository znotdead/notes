Title: JS: checkbox state with JQuery
Date: 2011-12-09 13:31
Modified: 
Category: Programming
Tags: JS
Slug: js_checkbox_state_with_jquery
Lang: en
Authors: znotdead
Summary: checkbox state

### JS: checkbox state with JQuery

Check if the checkbox is checked =)
```js
$('input').is(':checked')
$('input').attr('checked')
```
Changing the state of the checkbox:
```js
$('input').attr('checked', true); // or false to uncheck
```
