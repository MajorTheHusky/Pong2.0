from time import sleep
from pip import main
import pygame
import sys
import pygame.gfxdraw
import random
import Button
from math import sin, cos, atan, pi, floor
from Ball import Ball
from Config import WIDTH, HEIGHT
import Score
from Paddles import Paddle
from GameFonts import show_score, menu_option1, menu_option2, reset_score, end_option1, end_option2, player1_text, AIgame_player_text, player2_text, AI_text, show_score2

# SETUP

pygame.init()
pygame.font.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

paddle_R = Paddle (WIDTH - 25, HEIGHT // 2 - 75 // 2)
paddle_L = Paddle (0, HEIGHT // 2 - 75 // 2)
AIpaddle = Paddle (0, HEIGHT // 2 - 75 // 2)

ball = Ball ()

Games_Font = pygame.font.SysFont("comicsansms", 50)
Menus_Font = pygame.font.SysFont("comicsansms", 25)
Gameover_Font = pygame.font.SysFont("comicsansms", 75)

Lspeed = 200
Rspeed = 200

gameChoice = 1
normalGame = False
AIgame = False
AIgameScore = False
NormalgameScore = False

Button1 = Button.Button("Click Here", (WIDTH - 400, HEIGHT - 465), Menus_Font)
Button2 = Button.Button("Click Here", (WIDTH - 1120, HEIGHT - 465), Menus_Font)

Win = 0

def gameMenu(window):
	choosing = True

	global normalGame
	global NormalgameScore
	global AIgame
	global AIgameScore
	
	while choosing:
		window.fill('#48cce5')

		menu_option1(WIDTH - 450, HEIGHT - 500, Menus_Font)
		menu_option2(WIDTH - 1150, HEIGHT - 500, Menus_Font)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if Button1.click(event):
				choosing = False
				AIgame = False
				normalGame = True
				NormalgameScore = True
				AIgameScore = False

			if Button2.click(event):
				choosing = False
				normalGame = False
				AIgame = True
				AIgameScore = True
				NormalgameScore = False

		Button1.show()
		Button2.show()

		clock.tick(30)

		pygame.display.update()

def AIgameWindow(window):
	reset_score
	global AIgame, choosing, normalGame, choosing2, Win, AIgameScore, NormalgameScore
	while AIgame:
		clock.tick (60)

		#Player Code
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		keys = pygame.key.get_pressed()

		if keys [pygame.K_UP]:
			Rspeed = -300
			paddle_R.setVerticalVelocity (Rspeed)
		if keys [pygame.K_DOWN]:
			Rspeed = 300
			paddle_R.setVerticalVelocity (Rspeed)

		if keys[pygame.K_UP] == 0 and keys[pygame.K_DOWN] == 0:
			Rspeed = 0
			paddle_R.setVerticalVelocity(0)


		#AI Code
		AI_speed = 10
		def Decision(AI_Paddle, Ball_Location):
			if Ball_Location.y < AI_Paddle.pos.y + AI_Paddle.h / 2:
				AIspeed = -250
				AI_Paddle.setVerticalVelocity (AIspeed)
			if Ball_Location.y > AI_Paddle.pos.y + AI_Paddle.h / 2:
				AIspeed = 250
				AI_Paddle.setVerticalVelocity (AIspeed)

		Decision(AIpaddle, ball.pos)

		#Other Code
		dt = clock.get_time() / 1000.0

		ball.collide()
		ball.collidePaddles (AIpaddle, Lspeed)
		ball.collidePaddles (paddle_R, Rspeed)
		Win = ball.reset()
		if Win == 1 or Win == 2:
			window.fill((0, 0, 0))

		ball.move(dt)
		AIpaddle.move (dt)
		paddle_R.move (dt)


		if Win == 0:
			window.fill ('#381f0e')

		ball.draw (window)
		AIpaddle.draw (window)
		paddle_R.draw (window)

		AI_text(WIDTH - 1450, 0, Games_Font)
		AIgame_player_text(WIDTH - 200, 0, Games_Font)
		show_score2(WIDTH // 2 - 150, 0, Gameover_Font, Win)

		pygame.display.update()

		if Win == 1 or Win == 2:
			AIgame = False
			normalGame = False
			NormalgameScore = False
			choosing = False
			choosing2 = True

def gameWindow(window):
	reset_score()
	global normalGame, choosing, AIgame, choosing2, Win, AIgameScore, NormalgameScore
	while normalGame:
		clock.tick (60)

		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		keys = pygame.key.get_pressed()

		# print ('keys', keys[pygame.K_UP], keys[pygame.K_DOWN])

		if keys [pygame.K_UP]:
			Rspeed = -300
			paddle_R.setVerticalVelocity (Rspeed)
		if keys [pygame.K_DOWN]:
			Rspeed = 300
			paddle_R.setVerticalVelocity (Rspeed)

		if keys[pygame.K_UP] == 0 and keys[pygame.K_DOWN] == 0:
			Rspeed = 0
			paddle_R.setVerticalVelocity(0)
		

		if keys [pygame.K_w]:
			Lspeed = -300
			paddle_L.setVerticalVelocity (Lspeed)
		if keys [pygame.K_s]:
			Lspeed = 300
			paddle_L.setVerticalVelocity (Lspeed)

		# if w key and s key aren't pressed 
		if keys[pygame.K_w] == 0 and keys[pygame.K_s] == 0:
			Lspeed = 0
			paddle_L.setVerticalVelocity(0)

		dt = clock.get_time() / 1000.0


		ball.collide()
		ball.collidePaddles (paddle_L, Lspeed)
		ball.collidePaddles (paddle_R, Rspeed)
		Win = ball.reset()
		if Win == 1 or Win == 2:
			window.fill((0, 0, 0))


		ball.move(dt)
		paddle_L.move (dt)
		paddle_R.move (dt)

		if Win == 0:
			window.fill ('#381f0e')

		ball.draw (window)
		paddle_L.draw (window)
		paddle_R.draw (window)

		player1_text(WIDTH - 1480, 0, Games_Font)
		player2_text(WIDTH - 200, 0, Games_Font)
		show_score(WIDTH // 2 - 150, 0, Gameover_Font, Win)

		pygame.display.update()

		if Win == 1 or Win == 2:
			normalGame = False
			AIgame = False
			AIgameScore = False
			choosing = False
			choosing2 = True

def endMenu(window):
	choosing2 = True

	global normalGame
	global AIgame
	global choosing
	global Win
	global AIgameScore
	global NormalgameScore

	while choosing2:
		window.fill('#be040a')

		end_option1(WIDTH - 400, HEIGHT - 500, Menus_Font)
		end_option2(WIDTH - 1175, HEIGHT - 500, Menus_Font)

		if AIgameScore == True:
			show_score2(WIDTH // 2 - 150, 0, Games_Font, Win)	

		if NormalgameScore == True:
			show_score(WIDTH // 2 - 150, 0, Games_Font, Win)		

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if Button1.click(event):
				pygame.quit()
			if Button2.click(event):
				choosing = True
				choosing2 = False
				normalGame = False
				NormalgameScore = False
				AIgame = False
				AIgameScore = False

		Button1.show()
		Button2.show()

		clock.tick(30)

		pygame.display.update()



# RUN
while 1:

	gameMenu(window)

	gameWindow(window)

	AIgameWindow(window)

	endMenu(window)

	

	# To Do:
	# All good here :)