#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pi-tab.py
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
from datetime import datetime
from subprocess import call
import os
import glob
import logging
import getpass

logging.basicConfig(filename="/home/"+getpass.getuser()+"/.pi-tab/logs/" + datetime.now().isoformat() + ".log",
                    level=logging.INFO,format="%(asctime)s : %(message)s")

def exitPiTab():
	logging.info("Exiting...")
	os._exit(0)
	
def idle():
	os.system('python /usr/share/pi-tab/piTab/idleEditor.py')

def games():
	logging.info("Games menu entered")
	os.system("python3 '/usr/share/pi-tab/piTab/gamesMenu.py' &")
def terminate():
	logging.info("Shutdown menu")
	os.system("python3 {0}".format("/usr/share/pi-tab/piTab/exit.py &"))
def radio():
	logging.info("Radio mode")
	os.system("python3 /usr/share/pi-tab/piTab/radio.py &")
def turtle():
	logging.info("Turtle")
	os.system("python3 /usr/share/pi-tab/turtleController.py &")

def backupUSBdevice():
	logging.info("Backup Device")
	os.system("python3 /usr/share/pi-tab/piTab/backup.py &")

def __main__(args):
	logging.info("Started with args: {0}".format(str(args)))
	if args.addGame:
		logging.info("App game requested")
		call(["python","/usr/share/pi-tab/addGame.py"])
		os._exit(0)
	if args.addApp:
		logging.info("App add requested")
		call(["python3","/usr/share/pi-tab/addApp.py"])
		os._exit(0)
	'''if args.update:
		logging.info("Update requested")
		updated = False
		cDir = glob.glob("~/*.zip")
		for item in cDir:
			if item.find("pi-tab"):
					if item.find(""+open("/usr/shre/pi-tab/version.txt","r").read()):
						call(["unzip", str(update)])
						logging.info("Updating...")
						call(["python3", "pi-tab/seup.py install"])
						updated = True
		if updated:
			logging.info("Update installed")
		else:
			logging.info("No update found")
		os._exit(0)
	'''
	logging.info("Initiated - no flags suplied")
	window = Tk()
	window.attributes("-topmost", 1)
	window.title("Pi Tab Main Menu")
	exitButton = Button(window,text="Exit",command=exitPiTab)
	buttons = list()
	buttons.append(exitButton)
	gamesButton = Button(window,text="Games",command=games)
	buttons.append(gamesButton)
	shutdownButton = Button(window,text='Shutdown',command=terminate)
	buttons.append(shutdownButton)
	radioButton = Button(window,text="Radio menu",command=radio)
	buttons.append(radioButton)
	turtleButton = Button(window,text="Turtle Controller!",command=turtle)
	buttons.append(turtleButton)
	idleButton = Button(window,text='IDLE 3',command=idle)
	buttons.append(idleButton)
	buttons.append(Button(window, text='Backup tool', command=backupUSBdevice))
	
	for button in buttons:
		button.pack()
	window.mainloop()

'''
if __name__ == '__main__':
	main()
'''
