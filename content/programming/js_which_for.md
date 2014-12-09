Title: JS: which for
Date: 2011-12-09 13:32
Modified: 
Category: Programming
Tags: JS
Slug: js_which_for
Lang: ru
Authors: znotdead
Summary: for (var i in data) or for (var i=0;i<data.length;i++)?

### JS: which for

If you want to iterate by array than use
```js
for (var i=0;i<data.length;i++) {
    do_smth_with(data[i])
}
```
NOT
```js
for (var i in data) {
   do_smth_with(data[i])
}
```
Use this to iterate by objects only.
