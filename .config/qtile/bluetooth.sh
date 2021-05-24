#!/bin/bash

state=$(bluetoothctl show | grep Powered | cut -d " "  -f2)

if [ $state == "yes" ];
then
    notify-send "System" "Bluetooth Off"
    bluetoothctl power off
else
    notify-send "System" "Bluetooth On"
    bluetoothctl power on 
fi
