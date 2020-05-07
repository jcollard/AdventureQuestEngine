from engine.image_cache import image_cache
import pygame

class Sprite(object):

  NEXT_ID = 0

  def __init__(self, path, top=0, left=0, width=None, height=None):
    Sprite.NEXT_ID += 1
    self.id = Sprite.NEXT_ID
    sheet = image_cache.get_image(path)
    if width is None:
      width = sheet.get_width()
    if height is None:
      height = sheet.get_height()
    self.img = pygame.Surface((width, height))

    self.img.blit(sheet, (0,0), pygame.Rect(top, left, width, height))
    self.x = 0
    self.y = 0

  def set_x(self, x):
    self.x = x

  def set_y(self, y):
    self.y = y