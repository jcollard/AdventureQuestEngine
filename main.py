import pygame
from engine import engine
from engine.object import Object
from engine.obstacle import Obstacle

def move_left():
  link.set_x(link.x - 2)
  
def move_right():
  link.set_x (link.x + 2 )

def move_up():
  link.set_y(link.y - 2)

def move_down():
  link.set_y(link.y + 2)

def show_position(x, y):
  print(x, y)

engine.on_mouse_click(show_position)

engine.on_key_down(pygame.K_LEFT, move_left)
engine.on_key_down(pygame.K_RIGHT, move_right)
engine.on_key_down(pygame.K_UP, move_up)
engine.on_key_down(pygame.K_DOWN, move_down)

# Sets the background image
engine.set_background("images/bg-down.png")

link = Object("images/link-down.png")
link.set_x(369)
link.set_y(409)
link.set_bbox(35,0,25,3)
link.draw_bbox()
engine.add_object(link)

podium = Obstacle([(323,360), (375,362), (375,403),(323,410)])
podium.hide()
engine.add_obstacle(podium)

big_rock = Obstacle([(345,221), (300, 187), (300, 148), (397, 151), (399, 217)])
big_rock.hide()
engine.add_obstacle(big_rock)


# can you see me type

engine.start_game()