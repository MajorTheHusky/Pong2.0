import pygame
from Score import Lscore, Rscore

def reset_score():
  global Lscore, Rscore
  Lscore = 0
  Rscore = 0

def show_score(x, y, ScoreFont):
  from Main import window
  global Lscore, Rscore
  scoreBoard = ScoreFont.render("Score: " + str(Lscore) + " - " + str(Rscore), True, (255, 255, 255))
  window.blit(scoreBoard,(x, y))
  print(Lscore, Rscore)

