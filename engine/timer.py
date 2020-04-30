import time

class Timer(object):

  def __init__(self, delay, handler):
    self.delay = delay
    self.handler = handler
    self.running = False
    self.last_tick = 0
    self.start()
  
  def start(self):
    self.running = True
    self.last_tick = int(round(time.time() * 1000))

  def tick(self):
    if not self.running:
      return
    delta = int(round(time.time() * 1000))
    if delta >= (self.last_tick + self.delay):
      self.handler(delta - self.last_tick)
      self.last_tick = delta

  def stop(self):
    self.running = False