#!/bin/bash

if [ "$1" == "inc" ]; then
    xbacklight -inc 10 -steps 5 
fi

if [ "$1" == "dec" ]; then
    xbacklight -dec 10 -steps 5
fi

BRIGHTNESS=$(xbacklight -get)
NOTI_ID=$(notify-send.py "Brightness" "$BRIGHTNESS/100" \
                         --hint string:image-path:video-display boolean:transient:true \
                                int:has-percentage:$BRIGHTNESS)

