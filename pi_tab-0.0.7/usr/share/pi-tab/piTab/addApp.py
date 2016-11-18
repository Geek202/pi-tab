#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  addApp.py
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
import csv

def submit():
	f = open("/usr/share/pi-tab/apps","a")
	writer = csv.writer(f)
	writer.writerow([nameIn.get(),commandIn.get()])
	f.close()
	exit()

def main():
	root = Tk()
	nameLabel = Label(root,text="App Name")
	nameLabel.pack()
	nameIn = Entry(root,bd=5)
	nameIn.pack()
	commandLabel = Label(root,text="App command")
	commandLabel.pack()
	commandIn = Entry(root,bd=5)
	commandIn.pack()
	b = Button(root,text="Ok",command=submit)
	b.pack()
	root.mainloop()

if __name__ == '__main__':
	main()

