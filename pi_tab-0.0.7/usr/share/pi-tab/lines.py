#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lines.py
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

import pygame
from random import randint

class line():
	def __init__(self,screen,width,height,pos,length):
		self.random_colour()
		self.draw(screen,width,height,pos,length)
	def random_colour():
		self._colour = [randint(100,255),randint(100,255),randint(100,255)]
	def draw(screen,width,height,pos,length):
		pygame.draw.line(screen,self._colour,pos,(pos[0],pos[1]+length

if __name__ == '__main__':
	main()

