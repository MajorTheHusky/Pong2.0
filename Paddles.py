import pygame
from Config import WIDTH, HEIGHT

class Paddle:
	
	def __init__(self, x, y):
		self.pos = pygame.Vector2 (x, y)
		self.vel = pygame.Vector2 (0, 0)
		self.w = 25
		self.h = 75
		self.color = '#d83dff'
		self.rect = pygame.Rect(self.pos.x, self.pos.y, self.w, self.h)

	def draw (self, surface):
		pygame.draw.rect (surface, self.color, self.rect)

	def setVerticalVelocity (self, vy):
		self.vel.y = vy		

	def move (self, dt):

		adjustedVelocity = self.vel * dt

		# check if at top
		if self.rect.top + adjustedVelocity.y < 0:
			return

		if self.rect.bottom + adjustedVelocity.y > HEIGHT:
			return

		# actually do the move
		self.pos += adjustedVelocity
		self.bindRect()

	def bindRect (self):
		self.rect.x = self.pos.x
		self.rect.y = self.pos.y