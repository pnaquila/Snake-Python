import pygame, random, sys
from pygame.locals import *

class snake():
	def collide(self,x1, x2, y1, y2, w1, w2, h1, h2):                    #Collision function
		if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:     #x1 is position of snake, w1 is width of snake? h1 is the height? maybe h1 is height up, h2 height down? same for width? Just guesses here...
			return True
		else:
			return False
		
		
	def die(self,screen, score):
		font=pygame.font.SysFont('Arial', 30)
		text=font.render('Your score was: '+str(score), True, (0, 0, 0))
		screen.blit(text, (10, 270))
		pygame.display.update()
		pygame.time.wait(2000)
		
		text = font.render('Press Space to Replay',True, (0,0,0))
		screen.blit(text,(10, 400))
		pygame.display.update()
		
		self.clock.tick(30)					##Check this please
		for event in pygame.event.get():
				if  event.key == K_SPACE:
					self.setup()
						
		sys.exit(0)
		
	def __init(self):
		pygame.init()
		self.font = pygame.font.SysFont('Arial', 20)
		self.clock = pygame.time.Clock()

		self.display=pygame.display.set_mode((600, 600))
		pygame.display.set_caption('Snake')
		
		self.setup()
	
	def setup(self):
		self.xs = [290, 290, 290, 290, 290]                                  #These seem to be the different cooridinates of each snake segment
		self.ys = [290, 270, 250, 230, 210]

		self.direction, score = 0, 0
		self.fruit_pos = (random.randint(0, 590), random.randint(0, 590))
		self.fruit_image = pygame.Surface((10, 10))
		self.fruit_image.fill((255, 0, 0))
		self.seg = pygame.Surface((20, 20))                                  #Snake segment
		self.seg.fill((0, 255, 50))
		
		self.game()

	def game():

		while True:
			self.clock.tick(10)
			for event in pygame.event.get():
				if event.type == QUIT:
					sys.exit(0)
				elif event.type == KEYDOWN:
					if event.key == K_UP and self.direction != 3: self.direction = 1
					elif event.key == K_DOWN and self.direction != 1: self.direction = 3
					elif event.key == K_LEFT and self.direction != 0: self.direction = 2
					elif event.key == K_RIGHT and self.direction != 2: self.direction = 0
			i = len(self.xs)-1
			
			
			while i >= 2:
				
																		#Check if the snake collides with itself 
				if self.collide(self.xs[0], self.xs[i], self.ys[0], self.ys[i], 20, 20, 20, 20):
					self.die(self.display, self.score)
				i-= 1
			
																		#If Snake collides with the fruit, add a segment
			if self.collide(self.xs[0], self.fruit_pos[0], self.ys[0], self.fruit_pos[1], 20, 10, 20, 10):
				self.score+=1
				self.xs.append(700)    #Why 700?#
				self.ys.append(700)
				self.fruit_pos=(random.randint(0,590),random.randint(0,590))
			
																		#If snake hits the borders
			if self.xs[0] < 0 or self.xs[0] > 580 or self.ys[0] < 0 or self.ys[0] > 580:
				self.die(self.display, self.score)
				
			i = len(self.xs)-1
			while i >= 1:			                        #Shift the segments position
				self.xs[i] = self.xs[i-1]
				self.ys[i] = self.ys[i-1]
				i -= 1
			if self.direction==0: self.xs[0] += 20	                        #move the first segment in the direction chosen
			elif self.direction==1: self.ys[0] -= 20
			elif self.direction==2: self.xs[0] -= 20
			elif self.direction==3: self.ys[0] += 20	
			self.display.fill((255, 255, 255))	                        #background
			for i in range(0, len(self.xs)):                             #print segments to screen
				self.display.blit(self.seg, (self.xs[i], self.ys[i]))
			self.display.blit(self.fruit_image, self.fruit_pos)
			text=self.font.render(str(self.score), True, (0, 0, 0))
			self.display.blit(text, (10, 10))
			pygame.display.update()


if __name__ == '__main__':
	snakey = snake()
