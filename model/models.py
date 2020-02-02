import pygame
import pygame.gfxdraw
import random
import math

PADDING = 50

LEFT = 0
RIGHT = 1
HITBOX_PADDING = 7.5

class Snake:
	def __init__(self,color,WINWIDTH,WINHEIGHT, random_color=False):
		self.ix = random.randrange(PADDING,WINWIDTH-PADDING)
		self.iy = random.randrange(PADDING,WINHEIGHT-PADDING)
		self.fx = float(self.ix)
		self.fy = float(self.iy)
		
		self.angle = random.randrange(0,360)
		self.speed = 0.75
		self.radius = 4
		
		self.gap_counter = 0
		self.gap_timer = 0
	
		self.x = int(self.fx + self.speed * HITBOX_PADDING * math.cos(math.radians(self.angle)))
		self.y = int(self.fy + self.speed * HITBOX_PADDING * math.sin(math.radians(self.angle)))
		
		self.alive = True
		
		self.px = self.ix
		self.py = self.iy
		self.random_color = random_color
		if self.random_color:
			self.color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
		else:
			self.color = color
		
	def move(self):
		self.px = self.ix
		self.py = self.iy
		self.fx += self.speed * math.cos(math.radians(self.angle))
		self.fy += self.speed * math.sin(math.radians(self.angle))
		self.ix = int(self.fx)
		self.iy = int(self.fy)
		
		self.x = int(self.fx + self.speed * HITBOX_PADDING * math.cos(math.radians(self.angle)))
		self.y = int(self.fy + self.speed * HITBOX_PADDING * math.sin(math.radians(self.angle)))
	
	def draw(self, SURFACE, HEAD_SURFACE):
		
		self.gap_counter += 1
		
		if self.random_color and self.gap_counter % 7 == 0:
			self.color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
			
		if self.gap_counter >= 350 and self.gap_timer <= 35:
			pygame.gfxdraw.aacircle(HEAD_SURFACE, self.ix, self.iy, self.radius, self.color)
			pygame.gfxdraw.filled_circle(HEAD_SURFACE, self.ix, self.iy, self.radius, self.color)
			self.gap_timer += 1
		elif self.gap_counter >= 350:
			self.gap_counter = 0
			self.gap_timer = 0
		else:
			pygame.gfxdraw.aacircle(SURFACE, self.ix, self.iy, self.radius, self.color)
			pygame.gfxdraw.filled_circle(SURFACE, self.ix, self.iy, self.radius, self.color)

	def change_angle(self, dir):
		if dir == LEFT:
			self.angle -= 2
		if dir == RIGHT:
			self.angle += 2