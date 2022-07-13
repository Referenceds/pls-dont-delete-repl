import random
import time
from config import *

class CombatLog(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    
    self.surf = pygame.Surface((WIDTH,HEIGHT//5))
    self.surf.fill((194,4,4))
    self.rect = self.surf.get_rect()
    self.rect.top = HEIGHT - self.rect.height
    
  
def combatLoop(surf):
  done = False
  f = pygame.font.SysFont("Times",16)
  log = CombatLog()
  menu_sprites = pygame.sprite.Group()
  menu_sprites.add(log)
  while not done:
    for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()
      if event.type == KEYDOWN:
        if event.key == K_a:
          done = True
    f = pygame.font.SysFont("Times",16)
    surf.fill((0,0,0))
    g = f.render("COMBAT",True,(255,255,255)) 
    surf.blit(g,(50,50,50,50))
    for thing in menu_sprites:
      surf.blit(thing.surf,thing.rect)
    pygame.display.update()



      
      
  