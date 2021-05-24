#!/bin/bash

vscodium
sleep 3
kitty &
sleep 1 
kitty sh -c "unset LINES; unset COLUMNS; ranger" &
