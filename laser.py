import pygame

class Laser(pygame.sprite  .Sprite):
	def __init__(self, pos, speed, screen_height):
		super().__init__()
		self.image = pygame.Surface((4,15))
		self.image.fill((243, 216, 63))
		self.rect = self.image.get_rect(center = pos)
		self.speed = speed
		self.screen_height = screen_height

	def destroy(self):
		if self.rect.y <= 0 or self.rect.y >= self.screen_height + 50:
			self.kill()

	def update(self):
		self.rect.y -= self.speed
		self.destroy()