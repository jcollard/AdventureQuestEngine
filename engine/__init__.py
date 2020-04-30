import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

resolution = (800, 600)

class Engine(object):

  def __init__(self):
    self.set_background('images/bg-start.png')
    self.key_handlers = {}
    self.mouse_handlers = {}
    self.player = None
    self.keys = set()
    self.obstacles = set()
    self.width = resolution[0]
    self.height = resolution[1]

  def add_obstacle(self, obstacle):
    self.obstacles.add(obstacle)

  def set_background(self, img):
    background = pygame.image.load(img)
    self.background = pygame.transform.scale(background, resolution)

  def on_key_down(self, key, handler):
    self.key_handlers[key] = handler

  def on_mouse_move(self, handler):
    self.mouse_handlers[pygame.MOUSEMOTION] = handler

  def on_mouse_click(self, handler):
    self.mouse_handlers[pygame.MOUSEBUTTONDOWN] = handler

  def add_player(self, player):
    self.player = player


  def start_game(self) :
    pygame.init()
    
    # Set the width and height of the screen [width, height]
    screen = pygame.display.set_mode(resolution, flags=pygame.FULLSCREEN)

    # Loop until the user clicks the close button.
    done = False
    
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    while not done:
        # --- Main event loop
        for event in pygame.event.get():

            if event.type in self.mouse_handlers:
              pos = pygame.mouse.get_pos()
              self.mouse_handlers[event.type](pos[0],pos[1])

            if event.type == pygame.KEYDOWN:
              self.keys.add(event.key)

            if event.type == pygame.KEYUP:
              if event.key in self.keys:
                self.keys.remove(event.key)

        for key in self.keys:
          if key in self.key_handlers:
            self.key_handlers[key]()
    

        screen.fill(BLACK)
        
    
        # --- Drawing code should go here
        screen.blit(self.background, (0,0))
        if self.player:
          self.player.draw(screen)
    
        for obstacle in self.obstacles:
          obstacle.draw(screen)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    
        clock.tick(60)
    
    # Close the window and quit.
    pygame.quit()

engine = Engine()