import sys
import pygame
from pygame.locals import *
pygame.init()
surface = pygame.display.set_mode((640,640))
player=pygame.image.load("player.png")
playerrect=player.get_rect()
clock=pygame.time.Clock()
playerrect.move((298,298))
while True:
  for ev in pygame.event.get():
    if ev.type== QUIT:
      pygame.quit()
  clock.tick(60)
  surface.fill((0,0,0))
  surface.blit(player,playerrect)
  pygame.display.flip()
  
  
