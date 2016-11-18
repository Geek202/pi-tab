import pygame
class Turret(pygame.sprite.Sprite):
	def __init__(self,WINDOWWIDTH,WINDOWHEIGHT):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("/usr/share/pi-tab/images/turret.png")
		self.rect = self.image.get_rect()
		self.rect.x = (WINDOWWIDTH-self.rect.width)/2
		self.rect.y =WINDOWHEIGHT-self.rect.height
	
	def update_position(self,direction,WINDOWWIDTH,level):
		if direction=="left" and self.rect.x>10:
			self.rect.x-=10+level
		elif direction=="right" and self.rect.x<(WINDOWWIDTH-10):
			self.rect.x+=10+level
	
	def get_gun_position(self):
		position={}
		position["x"]=self.rect.x+(self.rect.width/2)
		position["y"]=self.rect.y-(self.rect.height/2)
		return position

