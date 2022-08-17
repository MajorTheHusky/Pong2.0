import pygame
import Score

def reset_score():
  Score.Lscore = 0
  Score.Rscore = 0

def show_score(x, y, ScoreFont, Wins):
  from Main import window

  if Wins == 1:
    scoreBoard = ScoreFont.render("Player 1 WINS!!!", True, (255, 255, 255))
  elif Wins == 2:
    scoreBoard = ScoreFont.render("Player 2 WINS!!!", True, (255, 255, 255))
  else:
    scoreBoard = ScoreFont.render("Score: " + str(Score.Lscore) + " - " + str(Score.Rscore), True, (255, 255, 255))

  window.blit(scoreBoard,(x, y))
  print(Score.Lscore, Score.Rscore)

def show_score2(x, y, ScoreFont, Wins):
  from Main import window

  if Wins == 1:
    scoreBoard = ScoreFont.render("AI WINS!!!", True, (255, 255, 255))
  elif Wins == 2:
    scoreBoard = ScoreFont.render("Player WINS!!!", True, (255, 255, 255))
  else:
    scoreBoard = ScoreFont.render("Score: " + str(Score.Lscore) + " - " + str(Score.Rscore), True, (255, 255, 255))

  window.blit(scoreBoard,(x, y))
  print(Score.Lscore, Score.Rscore)

def menu_option1(x, y, MenuFont):
  from Main import window

  choice1 = MenuFont.render("Play Against Someone", True, (0, 0, 0))

  window.blit(choice1, (x, y))

def menu_option2(x, y, MenuFont):
  from Main import window

  choice2 = MenuFont.render("Play Against A.I.", True, (0, 0, 0))

  window.blit(choice2, (x, y))

def end_option1(x, y, MenuFont):
  from Main import window

  choice11 = MenuFont.render("Quit Game", True, (0, 0, 0))

  window.blit(choice11, (x, y))

def end_option2(x, y, MenuFont):
  from Main import window

  choice22 = MenuFont.render("Go Back To Main Menu", True, (0, 0, 0))

  window.blit(choice22, (x, y))

def player1_text(x, y, MenuFont):
  from Main import window

  player1_text = MenuFont.render("Player 1", True, (255, 255, 255))

  window.blit(player1_text, (x, y))

def player2_text(x, y, MenuFont):
  from Main import window

  player2_text = MenuFont.render("Player 2", True, (255, 255, 255))

  window.blit(player2_text, (x, y))

def AI_text(x, y, MenuFont):
  from Main import window

  AI_text = MenuFont.render("AI", True, (255, 255, 255))

  window.blit(AI_text, (x, y))

def AIgame_player_text(x, y, MenuFont):
  from Main import window

  AIgame_player_text = MenuFont.render("Player", True, (255, 255, 255))

  window.blit(AIgame_player_text, (x, y))