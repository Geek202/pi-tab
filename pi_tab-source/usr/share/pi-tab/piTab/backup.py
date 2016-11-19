#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  backup.py
#  
#  Copyright 2016 Unknown <pi@pi>
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
from tkinter import filedialog
import os, glob
import shutil
files = glob.glob(os.path.join(filedialog.askdirectory(title='Import folder'),'*.*'))
dest = filedialog.askdirectory(title='Destination Folder')

def go():
	for file_name in files:
		if (os.path.isfile(file_name)):
			shutil.copy(file_name, dest)
	os._exit(0)

root = Tk()
Button(root, text='Backup', command=go).pack(fill=X)
root.mainloop()
