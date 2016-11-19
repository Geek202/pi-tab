#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gamesMenu.py
#  
#  Copyright 2016  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This application/library is distributed in the hope that it will be useful,
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
from subprocess import call
from os import _exit

def pi_splat():
	call(["python","/usr/share/pi-tab/games/pi-splat/main.py"])
def exitGames():
	_exit(0)

def main():
	window = Tk()
	window.attributes("-topmost",1)
	piSplatButton = Button(window,text="Pi Splat",command=pi_splat)
	buttons = list()
	buttons.append(piSplatButton)
	exitButton = Button(window,text="Exit",command=exitGames)
	buttons.append(exitButton)
	for button in buttons:
		button.pack()
	window.mainloop()

if __name__ == '__main__':
	main()

