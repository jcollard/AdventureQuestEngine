import pygame

class ImageCache(object):

  def __init__(self):
    self.cache = {}

  def get_image(self, path):
    if path not in self.cache:
      self.cache[path] = pygame.image.load(path)
    return self.cache[path]

image_cache = ImageCache()