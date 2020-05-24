import pygame
from shapely.geometry import Polygon
from engine import engine

class Object(object):

  next_id = 0

  def __init__(self, img, name=None, x=None, y=None):
    Object.next_id += 1
    self.id = Object.next_id
    if name is None:
      name = "Object: {self.id}"
    if x is None:
      x = engine.width/2
    if y is None:
      y = engine.height/2
    self.name = name
    self.sprite = pygame.image.load(img)
    self.x = x
    self.y = y
    self.width = self.sprite.get_width()
    self.height = self.sprite.get_height()

    self.top = 0
    self.left = 0
    self.bottom = self.height
    self.right = self.width
    self.show_bbox = False

  def draw(self, screen):
    screen.blit(self.sprite, (self.x,self.y))
    if self.show_bbox:
      pygame.draw.polygon(screen, (255, 0, 0), self.get_bbox(), 2)

  def draw_bbox(self):
    self.show_bbox = True

  def hide_bbox(self):
    self.show_bbox = False

  def set_image(self, img):
    self.sprite = pygame.image.load(img)
    self.width = self.sprite.get_width()
    self.height = self.sprite.get_height()

  def set_bbox(self, top, left, width, height):
    self.top = top
    self.left = left
    self.right = width
    self.bottom = height

  def get_bbox(self, x=None, y=None):
    if x is None:
      x = self.x
    if y is None:
      y = self.y
    return [
      (x + self.left, y + self.top), 
      (x + self.left + self.right, y + self.top), 
      (x + self.left + self.right, y + self.top + self.bottom), 
      (x + self.left, y + self.top + self.bottom)]

  def check_obstacle(self, x, y):
    if self not in engine.objects:
      return False
    poly = Polygon(self.get_bbox(x,y))
    for o in engine.obstacles:
      if(poly.intersects(o.poly)):
        return o
    for o in engine.objects:
      if o == self:
        continue
      if poly.intersects(Polygon(o.get_bbox())):
        return o
    return False

  def set_x(self, x):
    o = self.check_obstacle(x, self.y)
    if o:
      return o

    if x < 0:
      self.x = 0
      return "LEFT"

    if x + self.width > engine.width:
      self.x = engine.width - self.width
      return "RIGHT"

    self.x = x
    return None
  
  def set_y(self, y):
    o = self.check_obstacle(self.x, y)
    if o:
      return o

    if y < 0:
      self.y = 0
      return "TOP"
    if y + self.height > engine.height:
      self.y = engine.height - self.height
      return "BOTTOM"

    self.y = y
    return None