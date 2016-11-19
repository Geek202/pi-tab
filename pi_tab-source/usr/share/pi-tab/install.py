#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  install.py
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
import pickle
from tkinter import messagebox
import os ; from time import sleep

update = False

def slide2():
	global root,entry1,entry2
	root.destroy()
	root = Tk()
	root.title("Pi Tab Setup Wizzard")
	label = Label(root, text = "Step 1\nCreate a\nusername and\npassword", font=("American Typewriter", 16))
	label.pack()
	label2 = Label(root, text = "Username:")
	label2.pack()
	entry1 = Entry(root, bd=5)
	entry1.pack()
	entry2 = Entry(root, bd=5)
	label3 = Label(root, text="Password:")
	label3.pack()
	entry2.pack()
	backButton = Button(root, text = "<<back", command = slide1)
	backButton.pack()
	nextButton = Button(root, text = "next>>", command = slide3)
	nextButton.pack()

def main():
	global root
	root = Tk()
	slide1()
	root.title("Pi Tab Setup Wizzard")
	root.mainloop()

def slide3():
	global root,username,password
	username = entry1.get()
	password = entry2.get()
	datafile = open("/home/pi/Documents/pi-tab/passwords.dat", 'wb')
	data = [username, password]
	pickle.dump(data,datafile)
	datafile.close()
	root.destroy()
	root = Tk()
	root.title("Pi Tab Setup Wizzard")
	label1 = Label(root, text = "Step 2 - Installation",font=("American Typewriter", 16))
	label1.pack()
	backButton = Button(root, text = "<<back")
	backButton.pack()
	okButton = Button(root, text = "Lets Go", command = install)
	okButton.pack()
	

def install():
	global root
	if update:
		if not os.path.exists("~/Desktop/pi-tab/Documents/pi-tab/updated.dat"):
			print("System update")
			result = os.system("python3 ~/Documents/pi-tab/updateSystem.py")
			if not result == 0:
				print("Install failed")
				root.destroy()
				root = Tk()
				root.withdraw()
				messagebox.showerror("Install Failed","Install Failed")
				os._exit(163)
	os.system("sudo python3 ~/Documents/pi-tab/setup.py install")
	os._exit(0)

def slide1():
	global root
	root.destroy()
	root = Tk()
	label = Label(root, text ="Hello!\nAnd welcome\nto the Pi Tab\nSetup Wizzard!\nLet's get started!",font=("American Typewriter", 16))
	label.pack()
	
	#Menu Bar
	
	menu = Menu(root)
	root.config(menu=menu)
	
	file = Menu(menu)
	
	#file.add_command(label = 'Open', command = OpenFile)
	file.add_command(label = 'Exit', command = exit)
	menu.add_cascade(label = 'File', menu = file)
	nextButton = Button(root,text="Next>>",command=slide2)
	bs = [nextButton]
	for b in bs:
		b.pack()

if __name__ == '__main__':
	main()

