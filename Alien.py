import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""docstring for Alien"""
	def __init__(self, ai_settings,screen):
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		#load alien image
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		#start new alien from top left corner
		self.rect.x = self.rect.width
		self.rect.y =self.rect.height

		#store the exact position of alien
		self.x = float(self.rect.x)

	def blitme(self):
		self.screen.blit(self.image,self.rect)		

	def check_edges(self):
		"""Return True if alien is at edge of screen."""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0 :
			return True

	def update(self):
		'''Move the alien right or left'''
		self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x