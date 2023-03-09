import sys,math
import pygame
from pygame.locals import *
#libraries
#class for Campfire
class Campfire:
    def __init__(this,x,y):
        #constructor
        this.img=pygame.image.load("campfire.png")
        this.imgrect=this.img.get_rect()
        this.imgrect.left=x
        this.imgrect.top=y
    def update(this,plrt):
        global surface
        #draw image on rects position
        surface.blit(this.img,this.imgrect)
        return this.imgrect.colliderect(plrt)
#intialise the window to do anything
pygame.init()
#make window
surface = pygame.display.set_mode((640,640))
player=pygame.image.load("player.png")
rot=0
speed=4
#get rectangle
playerrect=player.get_rect()
#to set fps etc
clock=pygame.time.Clock()
#some vars
x=0
y=0
campfires=[]
angle=0
winter=True;
flame=False;
freeze=0;
run=True
#load font
font=pygame.font.SysFont("Arial",64)
while run:
  #watch for new events
  for ev in pygame.event.get():
    #self explanatory
    if ev.type== QUIT:
      pygame.quit()
      run=False
    #also self explanatory
    if ev.type== KEYDOWN:
      if ev.key==pygame.K_b and winter:
          keys = pygame.key.get_pressed()
          #if key is pressed
          if keys[pygame.K_c]:
            campfires.append(Campfire(playerrect.left,playerrect.top))
  #set fps
  clock.tick(60)
  #get pressed keys
  keys = pygame.key.get_pressed()
  x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed
  y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed
  playerrect.x+=x
  playerrect.y+=y
  playerrect.centerx = playerrect.centerx % surface.get_width()
  playerrect.centery = playerrect.centery % surface.get_height()
  flame=False;
  surface.fill((255*winter,255,255*winter))
  for i in campfires:
      flame=flame or i.update(playerrect)
      i.update(playerrect)
  
  try:
    if x==0 and y==0:
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
  rplayer=pygame.transform.rotate(player,angle)
  rrect=rplayer.get_rect(center=playerrect.center)
  surface.blit(rplayer,rrect)
  if winter:
    label=font.render("cold level:"+str(freeze/10),1,(255,0,255))
    surface.blit(label,(0,0))
  x=0
  y=0
  pygame.display.flip()
