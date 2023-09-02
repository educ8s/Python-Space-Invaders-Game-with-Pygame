import pygame, sys, shelve
from spaceship import Spaceship
from obstacle import *
from alien import Alien
from game import Game

pygame.init()

GREY = (29, 29, 27)
YELLOW = (243, 216, 63)
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
 
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill(GREY)
	game.spaceship.update()
	game.aliens.update(1)
	game.spaceship.draw(screen)
	
	game.spaceship.sprite.lasers.draw(screen)
	game.obstacle_1.blocks.draw(screen)
	game.obstacle_2.blocks.draw(screen)
	game.obstacle_3.blocks.draw(screen)
	game.obstacle_4.blocks.draw(screen)
	game.aliens.draw(screen)

	#pygame.draw.rect(screen, YELLOW, (10, 10 ,780, 780), 2, 0, 60, 60, 60, 60)
	#pygame.draw.line(screen, YELLOW, (25, 800 - 70), (800 -25, 800 - 70), 3)
	pygame.display.update()
	clock.tick(60)