#from combat.battle import *
from config import *
from objects.player import Player
from objects.tile import Background as Bg 
from objects.tile import load_map
from objects.border import Border
pygame.init()
displaySurface = pygame.display.set_mode((WIDTH, HEIGHT))
FramePerTick = pygame.time.Clock()

P1 = Player()
camera = {
  "x" : 0,
  "y" : 0
}
border = Border()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(border)
all_tiles = {}


# 24 x 24
map = load_map("assets/Maps/TestMap.png")
print("...starting build map...")
for r in map:
  #print(r)
  for c in r:  
   #print(c)
    if not c in all_tiles.keys():
      tile = Bg('grass',c,(0,0))
      all_tiles.update({c:tile})
#print("...finished build map...")

battle = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
          if event.key == K_a:
            battle = not battle
    displaySurface.fill((0, 0, 0))  
    if battle:
      #f = pygame.font.SysFont("Times",16)
      #g = f.render("COMBAT",True,(255,255,255)) 
      #displaySurface.blit(g,(50,50,50,50))
      pass
    else:
      x = camera["x"]
      y = camera["y"]
      for r in map:
        if y < 0 or y > HEIGHT:
          x = camera["x"]
          y += 21
          continue
        else:      
          for p in r:
            if x < 0 or x > WIDTH:
              x += 21
              continue
            else:
              bg = all_tiles[p]
              bg.rect.center = (x,y)
              displaySurface.blit(bg.surf, bg.rect)
              x += 21
          x = camera["x"]
          y += 21
  
      for spr in all_sprites:
          spr.move()
          spr.update()
          displaySurface.blit(spr.surf, spr.rect)
      if P1.pos.x < 120:
        P1.pos.x += abs(P1.vel.x)
        camera["x"] += abs(P1.vel.x)
      if P1.pos.x > WIDTH - 120:
        P1.pos.x -= abs(P1.vel.x)
        camera["x"] -= abs(P1.vel.x)
      if P1.pos.y < 120:
        P1.pos.y += abs(P1.vel.y)
        camera["y"] += abs(P1.vel.y)
      if P1.pos.y > HEIGHT - 120:
        P1.pos.y -= abs(P1.vel.y)
        camera["y"] -= abs(P1.vel.y)
      pygame.display.update()
      FramePerTick.tick(FPS)
    print(f"battle:{battle}")