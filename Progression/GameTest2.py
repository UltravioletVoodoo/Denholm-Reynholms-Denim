import sys
import pygame
pygame.init()


size = width, height = 1280, 800
speed = [1,0]
black = 0,0,0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("Denholm.jpg").convert()
ballrect = ball.get_rect()

while 1:
	for event in pygame.event.get():
		#handle a clean quit
		if event.type == pygame.QUIT: sys.exit()
		
		
		#move the object with the arrow keys
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			speed[1] = -1
			speed[0] = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			speed[1] = 1
			speed[0] = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			speed[0] = -1
			speed[1] = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			speed[0] = 1
			speed[1] = 0
		
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
	
	screen.fill(black)
	screen.blit(ball, ballrect)
	pygame.display.flip()




#print "This program is currently undergoing maintenance. Sorry for any inconvenience"