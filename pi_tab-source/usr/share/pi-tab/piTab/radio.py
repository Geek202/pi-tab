#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  radio.py
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

import os
from tkinter import *

Radio1 = '"http://www.listenlive.eu/bbcradio1.m3u"'
Radio2 = '"http://www.listenlive.eu/bbcradio2.m3u"'
Radio3 = '"http://www.listenlive.eu/bbcradio3.m3u"'
Radio4 = '"http://www.listenlive.eu/bbcradio4.m3u"'
Radio5 = '"http://www.listenlive.eu/bbc5live.m3u"'
Radio6 = "'http://www.listenlive.eu/bbc6music.m3u'"
Absolute80s = "'http://network.absoluteradio.co.uk/core/audio/mp3/live.pls?service=a8bb'"
Gem106 = "'http://webradio.radiomonitor.com/m3u/Gem-128.m3u'"
Capital = "'http://media-ice.musicradio.com/CapitalMP3.m3u'"
UncleWilliamsHeartFM = "'http://media-ice.musicradio.com/HeartWatfordMP3.m3u'"

def radio1():
	change_chanel(Radio1)
	stateText.delete(0.0,END)
	stateText.insert(END, "BBC Radio 1")
def radio2():
	change_chanel(Radio2)
	stateText.delete(0.0,END)
	stateText.insert(END, "BBC Radio 2")
def radio3():
	change_chanel(Radio3)
	stateText.delete(0.0,END)
	stateText.insert(END,"BBC Radio 3")
def radio4():
	change_chanel(Radio4)
	stateText.delete(0.0,END)
	stateText.insert(END, "BBC Radio 4")
def radio5():
	change_chanel(Radio5)
	stateText.delete(0.0,END)
	stateText.insert(END, "BBC Radio 5 live")
def radio6():
	change_chanel(Radio6)
	stateText.delete(0.0,END)
	stateText.insert(END, "BBC Radio 6 Music") # display the text
def absolute80s():
	change_chanel(Absolute80s) # set the chanel
	stateText.delete(0.0,END)
	stateText.insert(END, "Absolute 80s") # display the text
def gem106():
	change_chanel(Gem106)
	stateText.delete(0.0,END)
	stateText.insert(END, "Gem 106") # display the text
def capital():
	change_chanel(Capital)
	stateText.delete(0.0,END)
	stateText.insert(END, "Capital FM") # display the text
def Heart():
	change_chanel(UncleWilliamsHeartFM)
	stateText.delete(0.0,END)
	stateText.insert(END, "Heart(Hertfordshire)") # display the text
def stop():
	os.system("killall mplayer")
	stateText.delete(0.0,END)
	stateText.insert(END, "Ready")

def change_chanel(url):
	os.system("killall mplayer")
	os.system("mplayer -playlist {0} &".format(url))
def exitRadio():
	os.system("killall mplayer")
	os._exit(0)

os.system("python3 /usr/share/pi-tab/apt-fix.py") # check if mplayer is installed - if not: install it

root = Tk() # create a window
root.title("Radio")
#############################
#                           #
#      Button Creation      #
#                           #
#############################
bs = list()
stateText = Text(root,width=17,height=1)
bs.append(stateText)
r1Button = Button(root,text="Radio1 - BBC Radio one", command=radio1)
bs.append(r1Button)
r2Button = Button(root,text="Radio2 - BBC Radio two", command=radio2)
bs.append(r2Button)
r3Button = Button(root,text="Radio3 - BBC Radio three", command=radio3)
bs.append(r3Button)
r4Button = Button(root,text="Radio4 - BBC Radio four", command=radio4)
bs.append(r4Button)
r5Button = Button(root,text="Radio5 live - BBC radio five live", command=radio5)
bs.append(r5Button)
r6Button = Button(root,text="Radio6 - BBC Radio 6 Music",command=radio6)
bs.append(r6Button)
a80sButton = Button(root,text="Absolute 80s",command=absolute80s)
bs.append(a80sButton)
gemButton = Button(root,text="Gem 106",command=gem106)
bs.append(gemButton)
capitalButton = Button(root,text="Capital FM",command=capital)
bs.append(capitalButton)
stopButton = Button(root,text="Stop playing",command=stop)
bs.append(stopButton)
exitButton = Button(root,text="Exit",command=exitRadio)
bs.append(exitButton)
for b in bs:
	b.pack()
stateText.delete(0.0,END)
stateText.insert(END,"Ready")
root.mainloop() # display the window
