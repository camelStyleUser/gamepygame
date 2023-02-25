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
angle=0
winter=True;
flame=False;
freeze=0;
run=True
font=pygame.font.SysFont("Arial",64)
while True:
  for ev in pygame.event.get():
    if ev.type== QUIT:
      pygame.quit()
      run=False
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
  if(freeze>900):
    pygame.quit()
    break
  cold=winter and (not flame)
  freeze+=(cold*2-1)
  if freeze<0:
    freeze=0
  surface.fill((255*winter,255,255*winter))
  rplayer=pygame.transform.rotate(player,angle)
  rrect=rplayer.get_rect(center=playerrect.center)
  surface.blit(rplayer,rrect)
  if winter:
    label=font.render("cold level:"+str(freeze/10),1,(255,0,255))
    surface.blit(label,(0,0))
  x=0
  y=0
  pygame.display.flip()
