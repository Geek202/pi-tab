import pygame, circle
pygame.init()
clock = pygame.time.Clock() # Clock to limit speed
WIDTH=600; HEIGHT=600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
BLACK=(0,0,0)
screen.fill(BLACK)
circles=[]

for n in range(100):
	clock.tick(45)
	circles.append(circle.Circle(screen,WIDTH,HEIGHT))
	pygame.display.update()

clock.tick(1)

for c in circles:
	clock.tick(45)
	c.clear_circle(screen)
	pygame.display.update()

raw_input("Press a key")
