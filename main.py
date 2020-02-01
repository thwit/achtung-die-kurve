import pygame
import pygame.gfxdraw
import sys
import random
import math

WINHEIGHT = 500
WINWIDTH = 800
PADDING = 50
FPS = 100
BACKGROUND_COLOR = (95,95,95)
BACKGROUND_COLOR_TRANSPARENT = (95, 95, 95, 0)
PLAYER_COLOR = (0,0,0)

LEFT = 0
RIGHT = 1
HITBOX_PADDING = 5.5


class Snake:
	def __init__(self):
		self.ix = random.randrange(PADDING,WINWIDTH-PADDING)
		self.iy = random.randrange(PADDING,WINHEIGHT-PADDING)
		self.fx = float(self.ix)
		self.fy = float(self.iy)
		
		self.angle = random.randrange(0,360)
		self.speed = 0.75
		self.radius = 3
		
		self.gap_counter = 0
		self.gap_timer = 0
	
		self.x = int(self.fx + self.speed * HITBOX_PADDING * math.cos(math.radians(self.angle)))
		self.y = int(self.fy + self.speed * HITBOX_PADDING * math.sin(math.radians(self.angle)))
		
		self.px = self.ix
		self.py = self.iy
		
	def move(self):
		self.px = self.ix
		self.py = self.iy
		self.fx += self.speed * math.cos(math.radians(self.angle))
		self.fy += self.speed * math.sin(math.radians(self.angle))
		self.ix = int(self.fx)
		self.iy = int(self.fy)
		
		self.x = int(self.fx + self.speed * HITBOX_PADDING * math.cos(math.radians(self.angle)))
		self.y = int(self.fy + self.speed * HITBOX_PADDING * math.sin(math.radians(self.angle)))
	
	def draw(self):
		
		HEAD_SURFACE.fill(BACKGROUND_COLOR_TRANSPARENT)
		if self.gap_counter >= 350 and self.gap_timer <= 35:
			pygame.gfxdraw.aacircle(HEAD_SURFACE, self.ix, self.iy, self.radius, PLAYER_COLOR)
			pygame.gfxdraw.filled_circle(HEAD_SURFACE, self.ix, self.iy, self.radius, PLAYER_COLOR)
			
			#pygame.gfxdraw.aacircle(SURFACE, self.px, self.py, self.radius, BACKGROUND_COLOR)
			#pygame.gfxdraw.filled_circle(SURFACE, self.px, self.py, self.radius+1, BACKGROUND_COLOR)
			self.gap_timer += 1
		elif self.gap_counter >= 350:
			self.gap_counter = 0
			self.gap_timer = 0
		else:
			self.gap_counter += 1
			pygame.gfxdraw.aacircle(SURFACE, self.ix, self.iy, self.radius, PLAYER_COLOR)
			pygame.gfxdraw.filled_circle(SURFACE, self.ix, self.iy, self.radius, PLAYER_COLOR)

	def change_angle(self, dir):
		if dir == LEFT:
			self.angle -= 2
		if dir == RIGHT:
			self.angle += 2
			
def main():
	global CLOCK, SCREEN, SURFACE, HEAD_SURFACE
	pygame.init()
	CLOCK = pygame.time.Clock()
	SCREEN = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
	SURFACE = pygame.Surface(SCREEN.get_size())
	HEAD_SURFACE = pygame.Surface(SCREEN.get_size(),pygame.SRCALPHA)
	run_game()

def run_game():
	player = reset()
	gameover = False
	while True:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					gameover = False
					player = reset()
		

		if gameover or SURFACE.get_at((player.x,player.y)) != BACKGROUND_COLOR:
			gameover = True
			continue		
					
		player.draw()
		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_LEFT]:
			player.change_angle(LEFT)
		if keys[pygame.K_RIGHT]:
			player.change_angle(RIGHT)
		
		player.move()
		
		SCREEN.blit(SURFACE, (0, 0))
		
		SCREEN.blit(HEAD_SURFACE, (0, 0))
		pygame.display.update()
		
		CLOCK.tick(FPS)
		
def reset():
	SURFACE.fill(BACKGROUND_COLOR)
	return Snake()
		
if __name__ == "__main__":
    main()