#!/usr/bin/env python

import math,random,pygame,sys,pickle,os
from fruit import *
from game import *
from turret import *
from bullet import *

##TOP LEVEL CONSTANTS
FPS = 30
WINDOWWIDTH=480; WINDOWHEIGHT=640
GAMETITLE="Pi Splat"
WHITE=[255,255,255]; RED=[255,0,0]; GREEN=[0,255,0]; BLUE=[0,0,255]; BLACK=[0,0,0]
NUMBER_OF_LEVELS=5

def main():
	game=Game()
	
	#INITIAL SETUP
	pygame.init()
	pygame.key.set_repeat(1, 75)
	pygame.mouse.set_visible(False)
	displayFont=pygame.font.Font("/usr/share/pi-tab/256BYTES.TTF",28)
	clock=pygame.time.Clock()
	surface=pygame.display.set_mode([WINDOWWIDTH,WINDOWHEIGHT])
	pygame.display.set_caption(GAMETITLE)
	
	#SPLASH SCREEN
	splash=pygame.image.load("/usr/share/pi-tab/images/splash.png")
	surface.blit(splash,(0,0))
	pygame.display.update()
	game_over=False
	start_game=False
	
	while start_game==False:
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					game_over=True
				elif event.key==pygame.K_RETURN or event.key==pygame.K_KP_ENTER:
					resume=False
					start_game=True
				elif event.key==pygame.K_LSHIFT or event.key==pygame.K_RSHIFT:
					resume=True
					start_game=True

	if resume==True: #if they want to pick up a saved game
		if os.path.exists("savedata.dat")==True:
			game.load_game()
	
	#MAIN GAME LOOP
	while game.get_level()<=NUMBER_OF_LEVELS and game_over==False:
		
		#SHOW LEVEL NUMBER
		surface.fill(BLACK)
		levelText=displayFont.render('Level: '+str(game.get_level()),True,GREEN)
		surface.blit(levelText,(150,300))
		pygame.display.update()
		pygame.time.wait(1500)
		
		#SET UP VARIABLES FOR LEVEL
		game.save_game()
		live_fruit_sprites=pygame.sprite.Group()
		game._raspberries_saved=0
		bullet_sprites=pygame.sprite.Group()
		other_sprites=pygame.sprite.Group()
		turret=Turret(WINDOWWIDTH,WINDOWHEIGHT)
		other_sprites.add(turret)
		ticktock=1
		level_over=False
		
		#PLAY INDIVIDUAL LEVEL
		while level_over==False and game_over==False:
			for event in pygame.event.get():
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_ESCAPE:
						game_over=True
					elif event.key==pygame.K_LEFT:
						turret.update_position("left",WINDOWWIDTH,game.get_level())
					elif event.key==pygame.K_RIGHT:
						turret.update_position("right",WINDOWWIDTH,game.get_level())
					elif event.key==pygame.K_SPACE:
						bullet=Bullet(turret.get_gun_position())
						bullet_sprites.add(bullet)
			
			if ticktock >=120:
				ticktock=0
				if len(live_fruit_sprites)<10:
					live_fruit_sprites.add((Fruit(WINDOWWIDTH)))
					
			for sprite in bullet_sprites:
				sprite.update_position()
			
			collisions=pygame.sprite.groupcollide(live_fruit_sprites,bullet_sprites,False,True) 
			
			if collisions: #if there are any
				for fruit in collisions: #go through all collisions and check
					fruit.shot(game)
				
			background=pygame.image.load("/usr/share/pi-tab/images/gameBoard.png")
			surface.blit(background,(0,0))
			bullet_sprites.draw(surface)
			other_sprites.draw(surface)
			
			for sprite in live_fruit_sprites:
				sprite.update_position(game.get_level(),WINDOWHEIGHT,game)
			live_fruit_sprites.draw(surface)
			
			scoreText=displayFont.render('Score: '+str(game.get_score()),True,GREEN)
			levelText=displayFont.render('Level: '+str(game.get_level()),True, WHITE)
			raspberriesText=displayFont.render('Raspberries: '+str(game.get_raspberries_saved()),True,RED)
			surface.blit(scoreText,(10,10))
			surface.blit(levelText,(10,50))
			surface.blit(raspberriesText,(10,90))
			pygame.display.update()
			ticktock+=game.get_level()
			
			if game.get_raspberries_saved()>=10:
				game.update_level(1)
				level_over=True
			clock.tick(FPS)

	#handle end of game
	
	surface.fill(BLACK)
	scoreText=displayFont.render('Game over. Score: '+str(game.get_score()),True,GREEN)
	surface.blit(scoreText,(10,200))
	pygame.display.update()
	
if __name__ == '__main__':
    main()
