from config import *

class Border(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.surf = pygame.image.load("assets/spritesheets/Border.png")
    self.rect = self.surf.get_rect()
  
  def move(self):
    pass

  def update(self):
    pass