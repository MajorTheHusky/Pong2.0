from math import atan, floor, pi, cos, sin
import pygame
import random
from Config import WIDTH, HEIGHT
from Score import Lscore, Rscore


class Ball:

	def __init__(self):
		self.rad = 15
		self.pos = pygame.Vector2 (1500 // 2, 750 // 2)
		self.vel = pygame.Vector2 (0, 0)
		self.color = pygame.Color ('#FAEBD7')
		self.speed = 500
		self.angle = 0
		self.setAngle()
		self.hitbox = pygame.Rect(0, 0, self.rad * 2, self.rad * 2)
		self.hitbox.center = (self.pos.x, self.pos.y)

	def setAngle (self):
		theta = atan( (HEIGHT/2) / (WIDTH/2) )
		
		tr = floor(theta * 180 / pi)		# top-right angle
		br = floor(-theta * 180 / pi	)	# bottom-right angle
		tl = floor((pi - theta) * 180 / pi) # top-left angle
		bl = floor((pi + theta) * 180 / pi) # bot-left angle

		direction = random.choice(['left', 'right'])

		if direction == 'left': 
			self.angle = random.randrange(tl, bl)
		else:
			self.angle = random.randrange(br, tr)

		self.angle = self.angle * pi / 180


	def draw (self, surface):
		pygame.gfxdraw.aacircle (surface, int(self.pos.x), int(self.pos.y), self.rad, self.color)
		pygame.gfxdraw.filled_circle(surface, int(self.pos.x), int(self.pos.y), self.rad, self.color)

	def move (self, dt):

		self.vel.x = self.speed * cos (self.angle)
		self.vel.y = self.speed * sin (self.angle)
		self.pos += self.vel * dt

		self.hitbox.center = (self.pos.x, self.pos.y)
		
	def collide (self):
		top = self.pos.y - self.rad
		bottom = self.pos.y + self.rad

		zeroVector = pygame.Vector2(0, 0)
		
		# collide with top
		if top < 0 or bottom > HEIGHT:
			self.vel.y = -self.vel.y
			self.angle = zeroVector.angle_to(self.vel) * pi / 180.0

		# collide right

		# collide left

	def collidePaddles (self, paddle):
		zeroVector = pygame.Vector2(0, 0)
		if self.hitbox.colliderect (paddle.rect):
			self.vel.x = -self.vel.x
			self.angle = zeroVector.angle_to(self.vel) * pi / 180.0

	def movetoCenter (self):
		self.pos = pygame.Vector2(WIDTH // 2, HEIGHT //2)
		self.hitbox.center = (self.pos.x, self.pos.y)
		self.setAngle()

	def reset (self):
		global Lscore, Rscore

		if self.pos.x >= WIDTH:
			Lscore += 1
			self.movetoCenter()
			print (Lscore, "-", Rscore)
		
		if self.pos.x <= 0:
			Rscore += 1
			self.movetoCenter()
			print (Lscore, "-", Rscore)