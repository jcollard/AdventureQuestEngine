import pygame
from engine import engine
from engine.object import Object
from engine.obstacle import Obstacle
from engine.timer import Timer

def move_left():
  link.set_x(link.x - 2)
  link.set_image("images/link-left.png")
 
def move_right():
  link.set_x (link.x + 2 )
  link.set_image("images/link-right.png")

def move_up():
  link.set_y(link.y - 2)
  link.set_image("images/link-up.png")

def move_down():
  link.set_y(link.y + 2)
  link.set_image("images/link-down.png")

def show_position(x, y):
  print(f"({x}, {y}), ")

engine.on_mouse_click(show_position)

engine.on_key_down(pygame.K_LEFT, move_left)
engine.on_key_down(pygame.K_RIGHT, move_right)
engine.on_key_down(pygame.K_UP, move_up)
engine.on_key_down(pygame.K_DOWN, move_down)

# Sets the background image
engine.set_background("images/bg-down.png")

link = Object("images/link-down.png")
link.set_image("images/link-up.png")
link.set_x(369)
link.set_y(409)
link.set_bbox(35,0,25,3)
link.draw_bbox()
engine.add_object(link)

octorok = Object("images/octorok-down.png")
octorok.facing = "up"
octorok.set_x(360)
octorok.set_y(563)
octorok.draw_bbox()
engine.add_object(octorok)
octorok.hide_bbox()

def octorok_timer(time):
  if octorok.facing == "up":
    octorok.set_image("images/octorok-right.png")
    octorok.facing = "right"
  elif octorok.facing == "right":
    octorok.set_image("images/octorok-down.png")
    octorok.facing = "down"
  elif octorok.facing == "down":
     octorok.set_image("images/octorok-left.png")
     octorok.facing = "left"
  elif octorok.facing == "left":
      octorok.set_image("images/octorok-up.png")
      octorok.facing = "up"

octorok_time_er_ = Timer(250, octorok_timer)
engine.add_timer(octorok_time_er_)

podium = Obstacle([(323,360), (375,362), (375,403),(323,410)])
podium.hide()
engine.add_obstacle(podium)


podium1 = Obstacle([(326, 265), (376, 264), (372, 315), (325, 312)])
podium1.hide()
engine.add_obstacle(podium1)

big_rock = Obstacle([(345,221), (300, 187), (300, 148), (397, 151), (399, 217)])
big_rock.hide()
engine.add_obstacle(big_rock)


engine.start_game()

#can you see me?