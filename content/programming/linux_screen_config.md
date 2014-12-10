Title: LINUX: screen config
Date: 2011-12-09 13:29
Modified: 
Category: Programming
Tags: Linux
Slug: linux_screen_config
Lang: en
Authors: znotdead
Summary: screen

### LINUX: screen config

Now screen config allows to scroll =)
```
## general tweaks
vbell off
autodetach on
startup_message off
defscrollback 1000
attrcolor b ".I"
termcap xterm 'Co#256:AB=\E[48;5;%dm:AF=\E[38;5;%dm'
defbce "on"
#term screen-256color
 
## apps I want to auto-launch
screen -t 'bash'
screen -t 'root'
stuff "cd /var/www/^M"
stuff "sudo su"
screen -t 'mysql'
screen -t 'bash'
 
## scrolling
termcapinfo xterm ti@:te@
 
## statusline, customized. (should be one-line)
hardstatus alwayslastline '%{gk}[ %{G}%H %{g}][%= %{wk}%?%-Lw%?%{=b kR}[%{W}%n%f %t%?(%u)%?%{=b kR}]%{= kw}%?%+Lw%?%?%= %{g}][%{Y}%l%{g}]%{=b C}[ %D %m/%d %C%a ]%{W}'
```

[gist](https://gist.github.com/721598)

To activate scrolling press `Ctrl+a` and `Esc`.
Than `mouse scroll`, `arrows` or `PgUp/PgDn`
