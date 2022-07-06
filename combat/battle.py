import random
import time
from config import *
def combatLoop(surf):
  done = False
  f = pygame.font.SysFont("Times",16)
  while not done:
     done = False
    f = pygame.font.SysFont("Times",16)
    surf.fill((0,0,0))
    g = f.render("COMBAT",True,(255,255,255)) 
    surf.blit(g,(50,50,50,50))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
          if event.key == K_SPACE:
            done = True


      
      
  