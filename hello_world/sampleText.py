import pygame, sys
from pygame.locals import *

pygame.init()

# setup window
SURFACE = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Sample Text')

# setup colors
WHITE = (200, 200 , 200)
GREEN = (41, 171, 104)
BLUE = (135, 202, 250)

fontOjb = pygame.font.Font('freesansbold.ttf', 32)    # create a font obj
surfObj = fontOjb.render('Sample Text heheh ulol', True, GREEN, BLUE) # create surface obj to call render() method
rectObj = surfObj.get_rect()  # create a rect obj  
rectObj.center = (200, 150)   # set the center of the rect obj         

while True:   # main game loop
  SURFACE.fill(WHITE)       # fill color to window  
  SURFACE.blit(surfObj, rectObj)  # blit the surface obj with the text to rect obj 
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  pygame.display.update() # make the display surface appear on screen


