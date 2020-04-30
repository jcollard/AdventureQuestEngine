import pygame
from engine import engine
from engine.player import Player
from engine.obstacle import Obstacle

backgrounds = ['images/bg-start.png', 
  'images/bg-right.png', 
  'images/bg-left.png',
  'images/bg-up.png',
  'images/bg-down.png']

background = 1

o1 = Obstacle([(225, 310), (223, 209), (371, 208), (374, 313)])
o2 = Obstacle([(198, 161), (382, 165), (429, 207), (473, 203), (394, 140), (187, 141), (130, 180), (164, 192)])
o3 = Obstacle([(326, 377), (401, 375), (401, 392), (327, 393)])

engine.add_obstacle(o1)
engine.add_obstacle(o2)
engine.add_obstacle(o3)

def change_background():
  global background
  background += 1

  if background > 4:
    background = 0
  
  engine.set_background(backgrounds[background])

def move_left():
  player.set_image('images/link_left.png')
  result = player.set_x(player.x - 5)
  if result == "LEFT":
    engine.set_background('images/bg-left.png')
    player.set_x(engine.width-player.width)

def move_right():
  player.set_image('images/link_right.png')
  result = player.set_x(player.x + 5)
  if result == "RIGHT":
    engine.set_background('images/bg-right.png')
    player.set_x(0)

def move_up():
  player.set_image('images/link_up.png')
  result = player.set_y(player.y - 5)
  if result == "TOP":
    engine.set_background('images/bg-up.png')
    player.set_y(engine.height-player.height)

def move_down():
  player.set_image('images/link_down.png')
  result = player.set_y(player.y + 5)
  if result == "BOTTOM":
    engine.set_background('images/bg-down.png')
    player.set_y(0)

def mouse_click(x, y):
  print(x, y)

player = Player('images/link_down.png')
player.draw_bbox()
player.set_bbox(20, 0, 28, 10)
engine.add_player(player)
engine.on_mouse_click(mouse_click)
engine.set_background('images/bg-start.png')
engine.on_key_down(pygame.K_LEFT, move_left)
engine.on_key_down(pygame.K_RIGHT, move_right)
engine.on_key_down(pygame.K_UP, move_up)
engine.on_key_down(pygame.K_DOWN, move_down)
engine.start_game()