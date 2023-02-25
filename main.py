import sys,math
import pygame
from pygame.locals import *
pygame.init()
surface = pygame.display.set_mode((640,640))
player=pygame.image.load("player.png")
rot=0
speed=4
playerrect=player.get_rect()
clock=pygame.time.Clock()
x=0
y=0
angle=0;
while True:
  for ev in pygame.event.get():
    if ev.type== QUIT:
      pygame.quit()
  clock.tick(60)
  keys = pygame.key.get_pressed()
  x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed
  y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed
  playerrect.x+=x
  playerrect.y+=y
  playerrect.centerx = playerrect.centerx % surface.get_width()
  playerrect.centery = playerrect.centery % surface.get_height()
  try:
    angle=(180+math.degrees(math.atan2(x,y)))
  except:
    pass
  surface.fill((0,0,0))
  rplayer=pygame.transform.rotate(player,angle)
  rrect=rplayer.get_rect(center=playerrect.center)
  surface.blit(rplayer,rrect)
  x=0
  y=0
  pygame.display.flip()

  
  

  
