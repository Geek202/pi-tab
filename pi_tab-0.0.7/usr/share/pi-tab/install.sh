#!/bin/bash
cd ~/Documents/pi-tab
#pwd
python3 /home/pi/Documents/pi-tab/install.py
if [ ! -d "~/.pi-tab" ]; then
 mkdir ~/.pi-tab
fi
if [ ! -d "~/.pi-tab/logs" ]; then
 mkdir ~/.pi-tab/logs
fi
#python wait.py
#clear
