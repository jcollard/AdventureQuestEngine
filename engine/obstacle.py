import pygame
from shapely.geometry import Polygon

class Obstacle(object):

  next_id = 0

  def __init__(self, points, name=None):
    Obstacle.next_id += 1
    if name == None:
      name = f"Obstacle: {Obstacle.next_id}"
    self.name = name
    self.points = points
    self.poly = Polygon(points)
    self.visible = True

  def draw(self, screen):
    if not self.visible:
      return
    pygame.draw.polygon(screen, (255, 0, 0), self.points, 2)

  def show(self):
    self.visible = True

  def hide(self):
    self.visible = False