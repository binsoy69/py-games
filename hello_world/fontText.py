import pygame, sys
from pygame.locals import *

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World v2')

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (0, 0, 100)

fontObj = pygame.font.Font('freesansbold.ttf', 64)
textSurfaceObj = fontObj.render('Hello World', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

while True:   # main game loop
  SURFACE.fill(WHITE)
  SURFACE.blit(textSurfaceObj, textRectObj)
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()