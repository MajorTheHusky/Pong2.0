import pygame
import sys
import pygame.gfxdraw
import random
from math import sin, cos, atan, pi, floor
from Ball import Ball
from Config import WIDTH, HEIGHT
from Score import Lscore, Rscore
from Paddles import Paddle
from GameFonts import show_score

# SETUP
pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

paddle_R = Paddle (WIDTH - 25, HEIGHT // 2 - 75 // 2)
paddle_L = Paddle (0, HEIGHT // 2 - 75 // 2)

ball = Ball ()

Score_Font = pygame.font.SysFont("comicsansms", 25)

speed = 300

# RUN
while 1:

	clock.tick (60)

	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	keys = pygame.key.get_pressed()

	# print ('keys', keys[pygame.K_UP], keys[pygame.K_DOWN])

	if keys [pygame.K_UP]:
		paddle_R.setVerticalVelocity (-speed)
	if keys [pygame.K_DOWN]:
		paddle_R.setVerticalVelocity (speed)

	if keys[pygame.K_UP] == 0 and keys[pygame.K_DOWN] == 0:
		paddle_R.setVerticalVelocity(0)
	

	if keys [pygame.K_w]:
		paddle_L.setVerticalVelocity (-speed)
	if keys [pygame.K_s]:
		paddle_L.setVerticalVelocity (speed)

	# if w key and s key aren't pressed 
	if keys[pygame.K_w] == 0 and keys[pygame.K_s] == 0:
		paddle_L.setVerticalVelocity(0)

	dt = clock.get_time() / 1000.0

	ball.collide()
	ball.collidePaddles (paddle_L)
	ball.collidePaddles (paddle_R)
	ball.reset()

	ball.move(dt)
	paddle_L.move (dt)
	paddle_R.move (dt)

	window.fill ('#381f0e')

	ball.draw (window)
	paddle_L.draw (window)
	paddle_R.draw (window)

	show_score(WIDTH // 2 - 50, 0, Score_Font)

	pygame.display.update()