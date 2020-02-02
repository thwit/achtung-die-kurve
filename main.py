import pygame
import pygame.gfxdraw
import sys
from model.models import Snake

WINHEIGHT = 500
WINWIDTH = 800
PADDING = 50
FPS = 100
BACKGROUND_COLOR = (95,95,95)
BACKGROUND_COLOR_TRANSPARENT = (95, 95, 95, 0)
TEXT_COLOR = (230,230,230)

COLOR1 = (130,130,130)
COLOR2 = (170,170,170)
COLOR3 = (35,35,35)

LEFT = 0
RIGHT = 1

def main():
	global CLOCK, SCREEN, SURFACE, HEAD_SURFACE, FONT
	pygame.init()
	FONT = pygame.font.SysFont("couriernew", 30)
	CLOCK = pygame.time.Clock()
	SCREEN = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
	SURFACE = pygame.Surface(SCREEN.get_size())
	HEAD_SURFACE = pygame.Surface(SCREEN.get_size(),pygame.SRCALPHA)
	TEXT_SURFACE = pygame.Surface(SCREEN.get_size(),pygame.SRCALPHA)
	run_game()

def run_game():
	players = reset()
	gameover = False
	players_alive = 3
	while True:
		HEAD_SURFACE.fill(BACKGROUND_COLOR_TRANSPARENT)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					gameover = False
					players_alive = 3
					players = reset()		
			
		for player in players:
			if not player.alive:
				continue
			if player.x < 0 or player.x >= WINWIDTH or player.y < 0 or player.y >= WINHEIGHT:
				player.alive = False
				players_alive -= 1
			elif SURFACE.get_at((player.x,player.y)) != BACKGROUND_COLOR:
				player.alive = False
				players_alive -= 1
				continue
			
			player.draw(SURFACE,HEAD_SURFACE)
			
		gameover = players_alive <= 1
		
		if gameover:
			
			text = "GAME OVER"
		
			for i in range(3):
				if players[i].alive:
					text = "PLAYER " + str(i+1) + " WON" 
			
			TEXT_SURFACE = FONT.render(text, False, TEXT_COLOR)
			
			text_rect = TEXT_SURFACE.get_rect(center=(WINWIDTH / 2, WINHEIGHT / 2))
			
			SCREEN.blit(TEXT_SURFACE, text_rect)
			pygame.display.update()
			continue
			
		keys = pygame.key.get_pressed()
		
		
		if keys[pygame.K_LEFT] and players[0].alive:
			players[0].change_angle(LEFT)
		if keys[pygame.K_RIGHT] and players[0].alive:
			players[0].change_angle(RIGHT)
		if keys[pygame.K_a] and players[1].alive:
			players[1].change_angle(LEFT)
		if keys[pygame.K_d] and players[1].alive:
			players[1].change_angle(RIGHT)
		if keys[pygame.K_h] and players[2].alive:
			players[2].change_angle(LEFT)
		if keys[pygame.K_k] and players[2].alive:
			players[2].change_angle(RIGHT)
		
		for player in players:
			player.move()
		
		SCREEN.blit(SURFACE, (0, 0))
		
		SCREEN.blit(HEAD_SURFACE, (0, 0))
		pygame.display.update()
		
		CLOCK.tick(FPS)
		
def reset():
	SURFACE.fill(BACKGROUND_COLOR)
	return [Snake(COLOR1,WINWIDTH,WINHEIGHT), Snake(COLOR2,WINWIDTH,WINHEIGHT), Snake(COLOR3,WINWIDTH,WINHEIGHT)]
		
if __name__ == "__main__":
    main()