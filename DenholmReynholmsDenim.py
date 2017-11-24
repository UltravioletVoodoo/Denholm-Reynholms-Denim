import sys
import pygame
import random
import time

#Initialize global variables
DenholmScore = 0
DouglasScore = 0



def ENDGAME():
	time.sleep(5)
	sys.exit()
			
def STARTGAME():
	
	#Set up globals
	global DenholmScore
	global DouglasScore

	#Initialize the game screen
	pygame.init()
	size = width, height = 1200, 600
	white = 255,255,255
	screen = pygame.display.set_mode(size)
	started = False
	
	#Check for win condition
	if DenholmScore == 3: 
		DenholmWins = pygame.image.load("DenholmWins.png").convert()
		DenholmWinsRect = DenholmWins.get_rect()
		screen.blit(DenholmWins, DenholmWinsRect)
		pygame.display.flip()
		ENDGAME()
	if DouglasScore == 3:
		DouglasWins = pygame.image.load("DouglasWins.png").convert()
		DouglasWinsRect = DouglasWins.get_rect()
		screen.blit(DouglasWins, DouglasWinsRect)
		pygame.display.flip()
		ENDGAME()

	#Initialize the player avatars
	Denholm = pygame.image.load("Denholm.jpg").convert()
	Douglas = pygame.image.load("Douglas.jpg").convert()
	DenholmRect = Denholm.get_rect()
	DouglasRect = Douglas.get_rect()
	
	#Initialize player positions
	DouglasRect[0] = width - DouglasRect[2]
	DenholmRect[1] = height/2 - DenholmRect[3]/2
	DouglasRect[1] = height/2 - DouglasRect[3]/2
	DenholmSpeed = [0,0]
	DouglasSpeed = [0,0]

	#Initialize the game ball
	Denim = pygame.image.load("Denim.jpg").convert()
	DenimRect = Denim.get_rect()
	DenimRect[0] = width/2 - DenimRect[2]/2
	DenimRect[1] = height/2 - DenimRect[3]/2
	DenimSpeed = [0,0]





	#Game Loop
	while 1:
		
		#event handler
		for event in pygame.event.get():
			#handle a clean quit
			if event.type == pygame.QUIT: sys.exit()
			
			#Scan for key presses
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP and DouglasRect.top > 0:
					DouglasSpeed[1] = -1
				if event.key == pygame.K_DOWN and DouglasRect.bottom < height:
					DouglasSpeed[1] = 1
				if event.key == pygame.K_w and DenholmRect.top > 0:
					DenholmSpeed[1] = -1
				if event.key == pygame.K_s and DenholmRect.bottom < height:
					DenholmSpeed[1] = 1
				if event.key == pygame.K_SPACE and started == False:
					#Start the game
					started = True
					
					#Set the ball speed and direction
					choice = random.randrange(0,2)
					if choice == 0: DenimSpeed[0] = 2
					if choice == 1: DenimSpeed[0] = -2
					choice = random.randrange(0,8)
					if choice == 0: DenimSpeed[1] = 1
					if choice == 1: DenimSpeed[1] = 2
					if choice == 2: DenimSpeed[1] = 3
					if choice == 3: DenimSpeed[1] = 4
					if choice == 4: DenimSpeed[1] = -1
					if choice == 5: DenimSpeed[1] = -2
					if choice == 6: DenimSpeed[1] = -3
					if choice == 7: DenimSpeed[1] = -4
					
			
			#Scan for key releases
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					DouglasSpeed[1] = 0
				if event.key == pygame.K_DOWN:
					DouglasSpeed[1] = 0
				if event.key == pygame.K_w:
					DenholmSpeed[1] = 0
				if event.key == pygame.K_s:
					DenholmSpeed[1] = 0
				
		#Move the rects
		DenholmRect = DenholmRect.move(DenholmSpeed)
		DouglasRect = DouglasRect.move(DouglasSpeed)
		DenimRect = DenimRect.move(DenimSpeed)
		
		#Ensure that neither Reynholm leaves the playing area
		if DenholmRect.top < 0: DenholmSpeed[1] = 0
		if DenholmRect.bottom > height: DenholmSpeed[1] = 0
		if DouglasRect.top < 0: DouglasSpeed[1] = 0
		if DouglasRect.bottom > height: DouglasSpeed[1] = 0
		
		#Ensure that the ball does not leave the playing area unless it is scoring
		#THIS AREA NEEDS MODIFICATION AS IT CONTAINS BUGS
		if DenimRect.top <= 0 or DenimRect.bottom >= height: DenimSpeed[1] = -DenimSpeed[1]
		if DenimRect.right >= DouglasRect.left:
			if ((DenimRect.top <= DouglasRect.top) and (DenimRect.bottom >= DouglasRect.top)): DenimSpeed[1] = -DenimSpeed[1]
			if ((DenimRect.top <= DouglasRect.bottom) and (DenimRect.bottom >= DouglasRect.bottom)): DenimSpeed[1] = -DenimSpeed[1]
			if ((DouglasRect.bottom >= DenimRect.top >= DouglasRect.top) or (DouglasRect.bottom >= DenimRect.bottom >= DouglasRect.top)): DenimSpeed[0] = -2
		if DenimRect.left <= DenholmRect.right:
			if ((DenimRect.top <= DenholmRect.bottom) and (DenimRect.bottom >= DenholmRect.bottom)): DenimSpeed[1] = -DenimSpeed[1]
			if ((DenimRect.top <= DenholmRect.top) and (DenimRect.bottom >= DenholmRect.top)): DenimSpeed[1] = -DenimSpeed[1]
			if ((DenholmRect.bottom >= DenimRect.top >= DenholmRect.top) or (DenholmRect.bottom >= DenimRect.bottom >= DenholmRect.top)): DenimSpeed[0] = 2

		
		#Stop the ball to end the match if someone scores
		#Increment the player scores
		#Then wait 5 seconds, and reset the game
		if DenimRect.right >= width:
			DenimSpeed = [0,0]
			DenholmScore = DenholmScore + 1
			time.sleep(1.5)
			STARTGAME()
		if DenimRect.left <= 0:
			DenimSpeed = [0,0]
			DouglasScore = DouglasScore + 1
			time.sleep(1.5)
			STARTGAME()
		
		#Draw the changes
		screen.fill(white)
		screen.blit(Denholm, DenholmRect)
		screen.blit(Douglas, DouglasRect)
		screen.blit(Denim, DenimRect)
		pygame.display.flip()
		
		
		
STARTGAME()	