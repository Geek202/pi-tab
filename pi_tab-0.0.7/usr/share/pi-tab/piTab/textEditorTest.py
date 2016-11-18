#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  textEditor.py
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
from tkinter import filedialog,scrolledtext

#saved = False

def save():
	file = filedialog.asksaveasfilename(title='Save As',
										filetypes=[('text','*.txt'),('python','.py'),('c', '.c'),('c','.h')])
	f = open(file,'w')
	f.write(fileEdit.get())
	f.close()


def loadFile():
	save()
	

def exitEditor():
	save()
	exit()

def main():
	global root,fileEdit
	root = Tk()
	exitButton = Button(root,text='Exit',command=exitEditor)
	exitButton.pack(side='left')
	saveButton = Button(root,text='Save As',command=save)
	saveButton.pack(side='right')
	openButton = Button(root, text='Open',command=loadFile)
	openButton.pack(side='right')
	fileEdit = scrolledtext.__init__(master=root,name='Editor')
	fileEdit.pack(side='bottom')
	root.mainloop()

if __name__ == '__main__':
	main()

