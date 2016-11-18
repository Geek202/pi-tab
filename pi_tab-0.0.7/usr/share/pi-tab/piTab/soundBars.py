#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  soundBars.py
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

def main():
	root = Tk()
	c = Canvas(root,width=500,height=500)
	c.pack()
	line1 = c.create_polygon(0,500,50,500,50,250,0,250,fill="red")
	line2 = c.create_polygon(50,500,100,500,100,250,100,250,fill="blue")
	line3 = c.create_polygon(100,500,150,500,150,250,150,250,fill="green")
	root.update()
	root.mainloop()

if __name__ == '__main__':
	main()

