import pygame
from laser import Laser 

class Spaceship(pygame.sprite.Sprite):

	def __init__(self, screen_width, screen_height, offset):
		super().__init__()
		self.offset = offset
		self.image = pygame.image.load("Graphics/ship.png")
		self.rect = self.image.get_rect(midbottom = ((screen_width+offset)/2, screen_height))
		self.speed = 5
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.offset = offset
		self.laser_ready = True
		self.laser_time = 0
		self.laser_cooldown = 300
		self.lasers = pygame.sprite.Group()

	def player_input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			self.rect.x += self.speed

		elif keys[pygame.K_LEFT]:
			self.rect.x -= self.speed

		elif keys[pygame.K_SPACE] and self.laser_ready:
			self.lasers.add(Laser(self.rect.center, 5, self.screen_height))
			self.laser_ready = False
			self.laser_time = pygame.time.get_ticks()

	def recharge(self):
		if not self.laser_ready:
			current_time = pygame.time.get_ticks()
			if current_time - self.laser_time >= self.laser_cooldown:
				self.laser_ready = True

	def constrain_position(self):
		if self.rect.left < self.offset:
			self.rect.x = self.offset
		if self.rect.right > self.screen_width:
			self.rect.right = self.screen_width

	def update(self):
		self.player_input()
		self.constrain_position()
		self.recharge()
		self.lasers.update()

	def reset(self):
		self.rect = self.image.get_rect(midbottom = ((self.screen_width + self.offset)/2, self.screen_height))
