Title: JS: eval json
Date: 2011-12-09 13:28
Modified: 
Category: Programming
Tags: JS
Slug: js_eval_json
Lang: en
Authors: znotdead
Summary: eval json

### JS: eval json
```js
var jsonEmployee = "{ name: 'Ray', age: 31 }";
var employee = eval(jsonEmployee);
```
`script error: sun.org.mozilla.javascript.internal.EcmaError: SyntaxError: missing ; before statement (<STDIN>#1(eval)#1) in <STDIN>#1(eval) at line number 1`
The problem that `"{ ... }"` is a block of code. So if we wants to have a json we need to add `[]`, i.e. `"[{ ... }]"` or use expressions `"([ ... ])"`

Note that valid JSON need quoted items names.
`{ "name": "Ray", "age": 31 }`

[source](http://rayfd.wordpress.com/2007/03/28/why-wont-eval-eval-my-json-or-json-object-object-literal/)
