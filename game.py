import pygame
from spaceship import Spaceship
from alien import Alien
from obstacle import Obstacle

class Game():
	def __init__(self, screen_width, screen_height):
		self.spaceship = pygame.sprite.GroupSingle()
		self.spaceship.add(Spaceship(screen_width, screen_height))
		self.obstacle_1 = Obstacle(screen_width/4 - 128,screen_height - 100)
		self.obstacle_2 = Obstacle((screen_width/4)*2 - 128,screen_height - 100)
		self.obstacle_3 = Obstacle((screen_width/4)*3 - 128,screen_height - 100)
		self.obstacle_4 = Obstacle((screen_width/4)*4 - 128,screen_height - 100)
		self.aliens = pygame.sprite.Group()
		self.create_aliens()

	def create_aliens(self):
		for row in range(5):
			for column in range(11):
				x = column * 55
				y = row * 55
				if row == 0:
					alien_sprite = Alien(3, 75 + x, 80 + y)
				elif row == 1 or row == 2:
					alien_sprite = Alien(2, 75 + x, 80 + y)
				else:
					alien_sprite = Alien(1, 75 + x, 80 + y)
				self.aliens.add(alien_sprite)
