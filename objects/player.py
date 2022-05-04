from config import *
from assets.entities import *

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()

    self.animation_state = 'walk_down'
    self.animations = {}
    self.animation_timer = 0
    
    self.sheet = SpriteSheet(ENTITIES['player']['sheetname'])
    for state in ['walk_up','walk_down','walk_left','walk_right']:
      left    = ENTITIES['player'][state]['left']
      top     = ENTITIES['player'][state]['top']
      width   = ENTITIES['player'][state]['width']
      height  = ENTITIES['player'][state]['height']
      spacing = ENTITIES['player'][state]['spacing']
      length  = ENTITIES['player'][state]['length']
      timer   = ENTITIES['player'][state]['timer']
      animation_rects = [(left+(frame*width)+(frame*spacing),top,width,height) for frame in range(length)]
      animation = self.sheet.images_at(animation_rects, length, -1)
      self.animations.update({state:{"frames":animation,"timer":timer}})
   # frame = 0
    self.surf = self.animations[self.animation_state]["frames"][0]
    self.rect = self.surf.get_rect()

    self.acc = vec(0,0)
    self.vel = vec(0,0)
    self.pos = vec(WIDTH/2,HEIGHT/2)


  def move(self):
    self.moving = False
    self.acc = vec(0,0)
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_LEFT]:
      self.acc.x = -ACC
      self.animation_state = 'walk_left'
      self.moving = True
    if pressed_keys[K_RIGHT]:
      self.acc.x = ACC
      self.animation_state = 'walk_right'
      self.moving = True
    if pressed_keys[K_UP]:
      self.acc.y = -ACC
      self.animation_state = 'walk_up'
      self.moving = True
    if pressed_keys[K_DOWN]:
      self.acc.y = ACC
      self.animation_state = 'walk_down'
      self.moving = True
    
    self.acc.x += self.vel.x * FRIC
    self.acc.y += self.vel.y * FRIC
    self.vel += self.acc
    self.pos += self.vel + 0.5 * self.acc

    if self.pos.x < 0:
      self.pos.x = WIDTH
    if self.pos.x > WIDTH:
      self.pos.x = 0

    self.rect.midbottom = self.pos

  def update(self):
    self.check_animations()

  def check_animations(self):
    if self.surf in self.animations[self.animation_state]["frames"] and self.moving:
      if self.animation_timer >= self.animations[self.animation_state]["timer"]:
        new_index = self.animations[self.animation_state]["frames"].index(self.surf)+1
        anim_len = len(self.animations[self.animation_state]["frames"])
        self.surf = self.animations[self.animation_state]["frames"][new_index%anim_len]
        self.animation_timer = 0
      else:
        self.animation_timer += 1
    else: 
      self.surf = self.animations[self.animation_state]["frames"][0]
      self.animation_timer = 0
      
