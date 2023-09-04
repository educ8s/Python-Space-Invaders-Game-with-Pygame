import pygame, sys, random
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
ALIENLASER = pygame.USEREVENT
pygame.time.set_timer(ALIENLASER, 500)

MYSTERYSHIP = pygame.USEREVENT + 1 
pygame.time.set_timer(MYSTERYSHIP, random.randint(5000,10000))

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
 
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == ALIENLASER:
			game.alien_shoot_laser()
		if event.type == MYSTERYSHIP:
			game.create_mystery_ship()

	screen.fill(GREY)
	
	game.alien_lasers.update()
	game.spaceship.update()
	game.mystery_ship.update()
	game.check_for_collisions()

	game.alien_position_checker()
	game.aliens.update(game.alien_direction)
	
	game.spaceship.draw(screen)
	game.spaceship.sprite.lasers.draw(screen)
	game.obstacle_1.blocks.draw(screen)
	game.obstacle_2.blocks.draw(screen)
	game.obstacle_3.blocks.draw(screen)
	game.obstacle_4.blocks.draw(screen)
	game.aliens.draw(screen)
	game.alien_lasers.draw(screen)
	game.mystery_ship.draw(screen)

	#pygame.draw.rect(screen, YELLOW, (10, 10 ,780, 780), 2, 0, 60, 60, 60, 60)
	#pygame.draw.line(screen, YELLOW, (25, 800 - 70), (800 -25, 800 - 70), 3)
	pygame.display.update()
	clock.tick(60)