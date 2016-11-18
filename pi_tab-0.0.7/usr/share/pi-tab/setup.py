#!/usr/bin/env python3

from setuptools import setup
from os import system,path
setup ( name = 'Pi-Tab',
        version = '0.0.6',
        author = 'Thomas George Bryan',
        packages = ['piTab'],
)
'''
system("sudo cp pi-tab.desktop pi\ tab\ game\ adder.desktop pi\ tab\ app\ adder.desktop 'pi tab updater.desktop' /usr/share/applications")
system("sudo cp pi_tab pi_tab_add_game pi_tab_add_app pi_tab_update /usr/bin")
system("sudo apt-get install python-pygame")
if not path.exists("/usr/share/pi-tab"):
    system("sudo mkdir /usr/share/pi-tab")
if not path.exists("/usr/share/pi-tab/games") and not path.exists("/usr/share/pi-tab/images"):
    system("sudo mkdir /usr/share/pi-tab/images && sudo mkdir /usr/share/pi-tab/games")
system("sudo rm /usr/share/pi-tab/*")
system("sudo rm /usr/share/pi-tab/games/* && sudo rm /usr/share/pi-tab/images/*")
system("sudo cp piTab/images/* /usr/share/pi-tab/images/")
system("echo '0.0.4' > verson.txt")
system("sudo cp * /usr/share/pi-tab")
system("sudo cp piTab/* /usr/share/pi-tab/")
system("sudo cp -r piTab/games /usr/share/pi-tab")
system("mkdir /home/pi/.pi-tab")
system("mkdir /home/pi/.pi-tab/logs")
'''
