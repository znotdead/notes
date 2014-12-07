Title: JS: check if flash plugin installed
Date: 2011-07-29 23:06
Modified: 
Category: Programming
Tags: JS
Slug: js_check_if_flash_plugin_installed
Lang: en
Authors: znotdead
Summary: flash check

### JS: check if flash plugin installed

We can determine if flash installed in browser.

**Pure JS:**

```
var hasFlash = false;
try {
  var fo = new ActiveXObject('ShockwaveFlash.ShockwaveFlash');
  if(fo) hasFlash = true;
}catch(e){
  if(navigator.mimeTypes ["application/x-shockwave-flash"] != undefined) hasFlash = true;
}
```

With help of `SWFOBJECT` we can determine version of flash player if exists.

```
swfobject.getFlashPlayerVersion()
```

But we should check diffrenet versions of ShockwaveFlash as all true libraries do =). So my recent version is:
```
var flash = 0;
var pluginList = ["", ".3", ".4", ".5", ".6", ".7"]
if (window.ActiveXObject) {
    for (i = 0; i < pluginList.length; i++) {
        try {
            new ActiveXObject("ShockwaveFlash.ShockwaveFlash" + pluginList[i]);
            flash = 1;
        } catch (e) {}
    }
} else {
    if (navigator.mimeTypes && navigator.mimeTypes["application/x-shockwave-flash"] ) {
        var plugin = navigator.mimeTypes["application/x-shockwave-flash"].enabledPlugin;
        if (plugin && parseInt(plugin.description.match(/\d+/)[0]))
            flash = 1;
    }
}
```
