#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  exit.py
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
from os import system,_exit

def halt():
	system("sudo shutdown -h now")
	_exit(0)

def cancel():
	_exit(0)

def reboot():
	system("sudo reboot")
	_exit(0)

def main():
	window = Tk()
	window.attributes("-topmost",1)
	shutdown = Button(window,text="Shutdown",command=halt)
	buttons = list()
	buttons.append(shutdown)
	cancelButton = Button(window,text="Cancel",command=cancel)
	rebootButton = Button(window,text="Reboot",command=reboot)
	buttons.append(rebootButton)
	buttons.append(cancelButton)
	for b in buttons:
		b.pack()
	window.mainloop()
	

if __name__ == '__main__':
	main()

