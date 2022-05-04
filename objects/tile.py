from config import *
from assets.Backgrounds import *
class Tile(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.surf = pygame.Surface((58,58))
    self.rect = self.surf.get_rect()
    self.surf.fill((208,0,255))
    
  def update(self):
    pass 

class Background(Tile):
  def __init__(self, type, position, coords):
    super().__init__()
    self.tileset = SpriteSheet(BACKGROUNDS[type]['tileset'])
    
    left    = BACKGROUNDS[type][position]['left']
    top     = BACKGROUNDS[type][position]['top']
    width   = BACKGROUNDS[type][position]['width']
    height  = BACKGROUNDS[type][position]['height']
    self.surf = self.tileset.image_at((left,top,width,height))
    self.rect = self.surf.get_rect()
    self.rect.topleft = coords
    
  