import pygame, random, sys
from pygame.locals import *


def collide(x1, x2, y1, y2, w1, w2, h1, h2):
	if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:
		return True
	else:
		return False
	
	
def die(screen, score):
	font=pygame.font.SysFont('Arial', 30)
	text=font.render('Your score was: '+str(score), True, (0, 0, 0))
	screen.blit(text, (10, 270))
	pygame.display.update()
	pygame.time.wait(2000)
	sys.exit(0)
	
xs = [290, 290, 290, 290, 290]  #These seem to be the different cooridinates of each snake segment
ys = [290, 270, 250, 230, 210]

direction, score = 0, 0
fruit_pos = (random.randint(0, 590), random.randint(0, 590))
fruit_image = pygame.Surface((10, 10))
fruit_image.fill((255, 0, 0))
seg = pygame.Surface((20, 20))  #Snake segment
seg.fill((0, 255, 50))

pygame.init()
font = pygame.font.SysFont('Arial', 20)
clock = pygame.time.Clock()

display=pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

while True:
	clock.tick(10)
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit(0)
		elif event.type == KEYDOWN:
			if event.key == K_UP and direction != 3: direction = 1
			elif event.key == K_DOWN and direction != 1: direction = 3
			elif event.key == K_LEFT and direction != 0: direction = 2
			elif event.key == K_RIGHT and direction != 2: direction = 0
	i = len(xs)-1
	
	
	while i >= 2:
		
		#Check if the snake collides with itself 
		if collide(xs[0], xs[i], ys[0], ys[i], 20, 20, 20, 20):
			die(s, score)
		i-= 1
	
	#If Snake collides with the fruit, add a segment
	if collide(xs[0], fruit_pos[0], ys[0], fruit_pos[1], 20, 10, 20, 10):
		score+=1
		xs.append(700)
		ys.append(700)
		fruit_pos=(random.randint(0,590),random.randint(0,590))
	
	#If snake hits the borders
	if xs[0] < 0 or xs[0] > 580 or ys[0] < 0 or ys[0] > 580:
		die(display, score)
		
	i = len(xs)-1
	while i >= 1:			#Shift the segments position
		xs[i] = xs[i-1]
		ys[i] = ys[i-1]
		i -= 1
	if direction==0: xs[0] += 20	#move the first segment in the direction chosen
	elif direction==1: ys[0] -= 20
	elif direction==2: xs[0] -= 20
	elif direction==3: ys[0] += 20	
	display.fill((255, 255, 255))	 #background
	for i in range(0, len(xs)): #print segments to screen
		display.blit(seg, (xs[i], ys[i]))
	display.blit(fruit_image, fruit_pos)
	text=font.render(str(score), True, (0, 0, 0))
	display.blit(text, (10, 10))
	pygame.display.update()
