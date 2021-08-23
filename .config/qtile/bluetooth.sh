#!/bin/bash

state=$(bluetoothctl show | grep Powered | cut -d " "  -f2)

if [ $state == "yes" ];
then
    notify-send "System" "Bluetooth Off"
    bluetoothctl power off
    notify-send.py a --hint boolean:deadd-notification-center:true \
               int:id:1 boolean:state:false type:string:buttons
else
    notify-send "System" "Bluetooth On"
    bluetoothctl power on
    notify-send.py a --hint boolean:deadd-notification-center:true \
               int:id:1 boolean:state:true type:string:buttons 
fi
