#
# These things are run when an Openbox X Session is started.
# You may place a similar script in $HOME/.config/openbox/autostart
# to run user-specific things.
#

# If you want to use GNOME config tools...
#
#if test -x /usr/lib/x86_64-linux-gnu/gnome-settings-daemon >/dev/null; then
#  /usr/lib/x86_64-linux-gnu/gnome-settings-daemon &
#elif which gnome-settings-daemon >/dev/null 2>&1; then
#  gnome-settings-daemon &
#fi

xrandr --size 1920x1080 &
feh --bg-scale ~/.config/wallpaper/debian.png &
bash $HOME/.config/polybar/launch.sh --hack
