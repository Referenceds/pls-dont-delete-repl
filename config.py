import pygame, sys
from pygame.locals import * 
from random import randint
from utils.spritesheet import SpriteSheet
vec = pygame.math.Vector2
WIDTH = 500
HEIGHT = 500
ACC = 0.5
FRIC = -0.5
FPS = 60