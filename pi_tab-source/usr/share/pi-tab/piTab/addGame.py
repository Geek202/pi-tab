#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  addGame.py
#  
#  Copyright 2016  <pi@raspberrypi>
#  
#  This application is free software; you can redistribute it and/or modify
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



from Tkinter import *
from tkFileDialog import askopenfilename
from os import system
from time import sleep

def callback():
    name= askopenfilename(title = "Choose a game.",
                          filetypes=[('zip','.zip'),('zip','.egg')]
                           ) 
    copy = system("unzip {0}".format(name))
    if copy == 2304:
        text = Text(width=12,height=1)
        text.delete(0.0,END)
        text.insert(END,"Invalid file")
        b = Button(text="Ok",command=exit)
        b.pack(fill=X)
        text.pack(fill=X)
        mainoop()
        exit()
    del copy
    sleep(1)
    copy = system("mv {0} {1}".format("*.app", "/usr/share/pi-tab/games/"))
    if copy == 256:
        text = Text(width=12,height=1)
        text.delete(0.0,END)
        text.insert(END,"No app found")
        b = Button(text="Ok",command=exit)
        b.pack(fill=X)
        text.pack(fill=X)
        mainloop()
        exit()
    exit()
    
errmsg = 'Error!'
Button(text='Choose', command=callback).pack(fill=X)
Button(text="Cancel",command=exit).pack(fill=X)
mainloop()
