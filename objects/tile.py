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

"""
COLOR CODES FOR MAP

TL : FF 00 00

TM: FF 54 00

TR: FF 6B 00

LM: FF 98 00

TM: FF F2 00

MR: A7 FF 00

BL: 20 FF 00

BM: 00 FF 5C

BR: 00 FF CC

"""



def load_map(filename):
  surf = pygame.image.load(filename)
  rCount = surf.get_height()
  cCount = surf.get_width()
  map = []
  for row in range(rCount):
    crow = []
    for col in range(cCount):
      color = surf.get_at((row,col)) 
      r = hex(color[0])[2:]
      if len(r) == 1:
        r = "0"+r
      g = hex(color[1])[2:]
      if len(g) == 1:
        g = "0"+g
      b = hex(color[2])[2:]
      if len(b) == 1:
        b = "0"+b
      crow.append(r+g+b) 
    map.append(crow)
  return map