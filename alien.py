import pygame, random

class Alien(pygame.sprite.Sprite):
	def __init__(self, type, x, y):
		super().__init__()
		path = f"Graphics/alien_{type}.png"
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect(topleft = (x, y))

	def update(self, direction):
		self.rect.x += direction

class MysteryShip(pygame.sprite.Sprite):
	def __init__(self, screen_width):
		super().__init__()
		self.screen_width = screen_width
		self.image = pygame.image.load("Graphics/mystery.png")
		x = random.choice([0, screen_width - self.image.get_width()])
		if x == 0:
			self.speed = 3
		else:
			self.speed = -3
		self.rect = self.image.get_rect(topleft = (x, 20))

	def update(self):
		self.rect.x += self.speed 
		if self.rect.x > self.screen_width:
			self.kill()
		elif self.rect.x < - 200:
			self.kill()