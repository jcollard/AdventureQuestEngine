import pygame
from engine import engine
from engine.object import Object
from engine.obstacle import Obstacle

# Sets the background image
engine.set_background("images/bg-start.png")

player = Object("images/octorok-down.png")
player.draw_bbox()
engine.add_object(player)

player = Object("images/link-right.png", x=50, y=50)
player.draw_bbox()
engine.add_object(player)

def move_left():
  player.set_image('images/link-left.png')
  result = player.set_x(player.x - 5)

def move_right():
  player.set_image('images/link-right.png')
  result = player.set_x(player.x + 5)

def move_up():
  player.set_image('images/link-up.png')
  result = player.set_y(player.y - 5)

def move_down():
  player.set_image('images/link-down.png')
  result = player.set_y(player.y + 5)

engine.on_key_down(pygame.K_LEFT, move_left)
engine.on_key_down(pygame.K_RIGHT, move_right)
engine.on_key_down(pygame.K_UP, move_up)
engine.on_key_down(pygame.K_DOWN, move_down)

engine.start_game()