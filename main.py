import sys
import pygame
from pygame.locals import *
pygame.init()
surface = pygame.display.set_mode((640,640))
player=pygame.image.load("player.png")
rot=0
speed=1
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
  keys=pygame.key.get_pressed()
  keys = pygame.key.get_pressed()
  playerrect.move([(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed,0])
  playerrect.move([0,(keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed])
  
  
