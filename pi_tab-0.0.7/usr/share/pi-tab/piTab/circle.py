import pygame, random

class Circle:
	_minimum=100; _maximum=255
	_colour=None
	_properties=[]
	
	def __init__(self,screen,width,height):
		self.random_colour()
		self.draw_circle(screen,width,height)

	def draw_circle(self, screen, width, height):
		x=random.randint(1,width)
		y=random.randint(1,height)
		size=random.randint(1,5)
		self._properties=[x,y,size]
		pygame.draw.circle(screen,self._colour,(x,y),size)

	def random_colour(self):
		red=random.randint(self._minimum,self._maximum)
		green=random.randint(self._minimum,self._maximum)
		blue=random.randint(self._minimum,self._maximum)
		self._colour=[red,green,blue]

	def clear_circle(self,screen):
		pygame.draw.circle(screen,(0,0,0),(self._properties[0],self._properties[1]),self._properties[2])
