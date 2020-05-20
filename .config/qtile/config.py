# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

############################
#                          #
#   variables & imports    #
#                          #
############################

import os
import subprocess
from libqtile.config import Key, Screen, Group, Match, Drag, Click,hook
from libqtile.lazy import lazy
from libqtile import layout, bar, widget
from wal_color import colors
from typing import List  # noqa: F401

mod = "mod4"


############################
#                          #
#        keybindings       #
#                          #
############################

keys = [
    # Switch between windows in current stack pane
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

    # Move windows up or down in current stack
    Key([mod, "shift"], "k", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    #brightness control
    Key([], "XF86MonBrightnessUp", lazy.spawn('xbacklight -inc 10')),
    Key([], "XF86MonBrightnessDown", lazy.spawn('xbacklight -dec 10')),
    
   #volume control
    Key([], "XF86AudioRaiseVolume", lazy.spawn('amixer sset Master 20%+')),
    Key([], "XF86AudioLowerVolume", lazy.spawn('amixer sset Master 20%-')),
    Key([], "XF86AudioMute", lazy.spawn('amixer sset Master toggle')),   

   #music
    Key(["mod1"], "s", lazy.spawn('playerctl play-pause')),
    Key(["mod1"], "a", lazy.spawn('playerctl prevoius')),
    Key(["mod1"], "d", lazy.spawn('playerctl next')),   

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn("kitty")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),

    #toggle rofi menus
    Key([mod], "space", lazy.spawn('.config/rofi/scripts/appsmenu.sh')),
    Key([], "Print", lazy.spawn('.config/rofi/scripts/scrotmenu.sh')),
    Key([mod], "p", lazy.spawn('.config/rofi/scripts/powermenu.sh')),
    Key([mod], "n", lazy.spawn('.config/rofi/scripts/networkmenu.py')),

]

############################
#                          #
#        startup           #
#                          #
############################

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

############################
#                          #
#        borders           #
#                          #
############################

layout_theme = {"border_width": 2,
                "margin": 12,
                "border_focus": '#ffffff',
                "border_normal":'#000000'
                }


############################
#                          #
#         groups           #
#                          #
############################

group_names = [("WWW", {'layout': 'max','spawn': 'firefox'}),
              ("DEV", {'layout': 'monadtall','matches':[Match(wm_class=['code-oss','kitty'])],'spawn': ['.config/qtile/dev_layout.sh'] }),
               ("DOC", {'layout': 'max','matches':[Match(wm_class=['ms-office-online'])],'spawn': ['ms-office-online'] }),
               ("CHAT", {'layout': 'monadtall','matches':[Match(wm_class=['TelegramDesktop','whatsapp-nativefier-d52542'])],'spawn': ['telegram-desktop','whatsapp-nativefier-dark']}),
               ("MUS", {'layout': 'max','matches':[Match(wm_class=['spotify'])],'spawn': ['spotify']}),
               ("GAME", {'layout': 'max','matches':[Match(wm_class=['Lutris'])],'spawn': ['lutris']}),
               ("VBOX", {'layout': 'max','matches':[Match(wm_class=['Virt-manager'])],'spawn': ['virt-manager']}),
               ("EXTRA", {'layout': 'monadtall'}),]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group	


layouts = [
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
      layout.Matrix(**layout_theme),
      layout.Floating(**layout_theme),
      layout.MonadTall(cmd_flip=True,**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
      layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


############################
#                          #
#            bar           #
#                          #
############################

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    background=colors[4],
                    foreground=colors[4],
                    highlight_method='block',
                    hide_unused='true',
                    urgent_border='none',
                    this_current_screen_border=colors[2]
                ),
                widget.TextBox(text='',
                    padding=0,
                    fontsize=37,
                    background=colors[15],
                    foreground=colors[4]),
                widget.Prompt(),
                widget.WindowName(
                    background=colors[15],
                    foreground=colors[4]
                ),
                widget.TextBox(text='',
                    padding=0,
                    fontsize=37,
                    background=colors[15],
                    foreground=colors[4]),
                widget.Systray(
                    background=colors[4],
                    foreground=colors[15]
                ),
                widget.TextBox(text='',
                    padding=0,
                    fontsize=37,
                    background=colors[4],
                    foreground=colors[15]),
                widget.TextBox(text='',
                    padding=0,
                    fontsize=20,
                    background=colors[15],
                    foreground=colors[4]),
                widget.Wlan(
                    background=colors[15],
                    foreground=colors[4],
                    interface='wlp3s0',
                    format='{essid}'),
                widget.TextBox(text='',
                    padding=0,
                    fontsize=37,
                    background=colors[15],
                    foreground=colors[4]),
                widget.TextBox(text='',
                    padding=0,
                    fontsize=20,
                    background=colors[4],
                    foreground=colors[15]),
                widget.Backlight(backlight_name="intel_backlight",
                    brightness_file='/sys/class/backlight/intel_backlight/brightness',
                    background=colors[4],
                    foreground=colors[15]),
                                
                widget.TextBox(text='',
                    padding=0,
                    fontsize=37,
                    background=colors[4],
                    foreground=colors[15]),
                widget.TextBox(text='',
                    padding=0,
                    fontsize=20,
                    background=colors[15],
                    foreground=colors[4]),
                widget.Volume(
                    foreground=colors[4],
                    background=colors[15]
                ),
                widget.TextBox(text='',
                    padding=0,
                    fontsize=37,
                    background=colors[15],
                    foreground=colors[4]),
                widget.TextBox(text='',
                    padding=0,
                    fontsize=20,
                    background=colors[4],
                    foreground=colors[15]),
                widget.Clock(format=' %a %d, %H:%M',
                    background=colors[4],
                    foreground=colors[15]),
                widget.TextBox(text='',
                    padding=0,
                    fontsize=37,
                    background=colors[4],
                    foreground=colors[15]),
                widget.CurrentLayout(
                    background=colors[15],
                    foreground=colors[4]
                ),
                widget.TextBox(text='',
                    padding=0,
                    fontsize=37,
                    background=colors[15],
                    foreground=colors[4]),
                widget.BatteryIcon(
                    background=colors[4]
                ),
                widget.Battery(
                    background=colors[4],
                    foreground=colors[15],
                    format='{percent:2.0%}'
                )
            ],
            24,
        ),
    ),
]

############################
#                          #
#     exceptions           #
#                          #
############################

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
    {'wmclass': 'lxpolkit'},  # lxpolkit
    {'wmclass': 'vncviewer'},  # vncviewer
])
auto_fullscreen = True
focus_on_window_activation = "smart"


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"
