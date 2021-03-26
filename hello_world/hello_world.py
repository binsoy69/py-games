import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAY = pygame.display.set_mode((600, 500))
pygame.display.set_caption('Hello World Using Pygame!')
while True: # game loop
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
