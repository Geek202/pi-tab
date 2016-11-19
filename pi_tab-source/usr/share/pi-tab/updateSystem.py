#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  updateSystem.py
#  
#  Copyright 2016  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



from tkinter import *
from tkinter import ttk
import os,pickle

root = Tk()
def update():
	global label1,yesButton,noButton
	os.system("sudo apt-get update")
	os.system("sudo apt-get dist-upgrade")
	os.system("sudo apt-get install piclone geany usb-modeswitch pi-bluetooth python-pigpio python3-pigpio")
	label1.config(text="Update installed sucsessfully\nDo you want to reboot?")
	updatedFile = open("/usr/share/pi-tab/updated.dat",'wb')
	pickle.dump(True,updatedFile)
	updatedFile.close()
	noButton.config(command=exitZero)
	yesButton.config(command=reboot)
def failExit():
	os._exit(163)
def reboot():
	os.system("sudo reboot")
def exitZero():
	os._exit(0)
label1 = Label(root,text="The system needs an\nupdate; do you want to\ninstall?(Note: Pi Tab will\nnot run if not\nupdateded)")
label1.pack()
yesButton = Button(root,text="Yes",command=update)
yesButton.pack()
noButton=Button(root,text="No",command=failExit)
noButton.pack()
root.mainloop()
