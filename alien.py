import pygame

class Alien(pygame.sprite.Sprite):
	def __init__(self, type, x, y):
		super().__init__()
		path = f"Graphics/alien_{type}.png"
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect(topleft = (x, y))

	def update(self, direction):
		self.rect.x += direction