from config import *
from objects.player import Player
from objects.tile import Background as Bg

pygame.init()
displaySurface = pygame.display.set_mode((WIDTH, HEIGHT))
FramePerTick = pygame.time.Clock()

P1 = Player()


all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_tiles = pygame.sprite.Group()

map = [
  
  ['OR','OR','OR','OR','OR'],
  ['OR','OR','OR','OR','OR'],
  ['OR','OR','OR','OR','OR'],
  ['OR','OR','OR','OR','OR'],
  ['OR','TL','TM','TR','OR'],
  ['OR','ML','MM','MR','OR'],
  ['OR','ML','MM','MR','OR'],
  ['OR','BL','BM','BR','OR'],
  ['OR','OR','OR','OR','OR'],
  ['OR','OR','OR','OR','OR'],

]
x = 200
y = 0
for r in map:
  for c in r:  
    tile = Bg('grassy',c,(x,y))
    all_tiles.add(tile)
    x += 22
  y += 22
  x = 200



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    displaySurface.fill((0, 0, 0))

    for tile in all_tiles:
        tile.update()
        displaySurface.blit(tile.surf, tile.rect)

    for spr in all_sprites:
        spr.move()
        spr.update()
        displaySurface.blit(spr.surf, spr.rect)
    if P1.pos.x < 120:
      P1.pos.x += abs(P1.vel.x)
    if P1.pos.x > WIDTH - 120:
      P1.pos.x -= abs(P1.vel.x)
    if P1.pos.y < 120:
      P1.pos.y += abs(P1.vel.y)
    if P1.pos.y > HEIGHT - 120:
      P1.pos.y -= abs(P1.vel.y)
    pygame.display.update()
    FramePerTick.tick(FPS)
