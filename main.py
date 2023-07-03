import sys, math, random, sys, os
import pip

ose = sys.stderr
oso = sys.stdout

try:
    print("""this is installation of needed packages.\n
shells are run with commands to invoke pip,nothing malicious""")
except:
    pass
sys.stderr = open(os.devnull, "w")
sys.stdout = open(os.devnull, "w")
try:
    os.system("python -m pip install pygame")
except:
    try:
        pip.main(["install", "pygame"])
    except:
        sys.stderr = ose
        sys.stderr.write("couldnt install required packages")
        sys.exit(-1)
import pygame

sys.stdout = oso
sys.stderr = ose
try:
    pygame.mixer.init()
except:
    sys.stderr.write("WARNING!couldnt initialise sounds")
from pygame.locals import *

# libraries
# class for Campfire
FARMSPEED = 1000
SMALLFARMSPEED = 4000
ENEMYSPEED = 5
megaspawndelay = 15000
spawndelay = 10000

map=[[[],[]],[[],[]]]
class Enemy:
    def __init__(this, x, y):
        this.img = pygame.image.load("enemy.png")
        this.imgrect = this.img.get_rect()
        this.imgrect.left = x
        this.imgrect.top = y

    def update(this, plrt):
        global surface
        tox = plrt.centerx
        toy = plrt.centery
        fromx = this.imgrect.centerx
        fromy = this.imgrect.centery
        if math.dist([tox, toy], [fromx, fromy]) < ENEMYSPEED / 10:
            sp = math.dist([tox, toy], [fromx, fromy])
        else:
            sp = ENEMYSPEED
        rendimage = this.img
        angl = math.degrees(math.atan2(toy - fromy, tox - fromx))
        xsp = math.cos(angl) * sp
        ysp = math.sin(angl) * sp
        rendimage = pygame.transform.rotate(rendimage, 180 + math.degrees(math.atan2(xsp, ysp)))
        rendrect = rendimage.get_rect()
        rendrect.center = this.imgrect.center
        this.imgrect.move_ip(xsp, ysp)
        surface.blit(rendimage, rendrect)
        return this.imgrect.colliderect(plrt)


class Megaenemy:
    def __init__(this, x, y):
        this.img = pygame.image.load("megaenemy.png")
        this.imgrect = this.img.get_rect()
        this.imgrect.left = x
        this.imgrect.top = y

    def update(this, plrt):
        global surface
        tox = plrt.centerx
        toy = plrt.centery
        fromx = this.imgrect.centerx
        fromy = this.imgrect.centery
        if math.dist([tox, toy], [fromx, fromy]) < ENEMYSPEED:
            sp = math.dist([tox, toy], [fromx, fromy])
        else:
            sp = ENEMYSPEED
        rendimage = this.img
        angl = math.degrees(math.atan2(toy - fromy, tox - fromx))
        xsp = math.cos(angl) * sp
        ysp = math.sin(angl) * sp
        rendimage = pygame.transform.rotate(rendimage, 180 + math.degrees(math.atan2(xsp, ysp)))
        rendrect = rendimage.get_rect()
        rendrect.center = this.imgrect.center
        this.imgrect.move_ip(xsp, ysp)
        surface.blit(rendimage, rendrect)
        return this.imgrect.colliderect(plrt)


class Campfire:
    def __init__(this, x, y):
        # constructor
        this.img = pygame.image.load("campfire.png")
        this.imgrect = this.img.get_rect()
        this.imgrect.left = x
        this.imgrect.top = y

    def update(this, plrt):
        global surface
        # draw image on rects position
        surface.blit(this.img, this.imgrect)
        return this.imgrect.colliderect(plrt)


class AEStand:
    def __init__(this, x, y):
        this.alive = True
        this.dn = 20
        this.img = pygame.image.load("aestand.png")
        this.imgrect = this.img.get_rect()
        this.imgrect.left = x
        this.imgrect.top = y

    def update(this, plrt):
        global surface, enemies
        # draw image on rects position
        for i in range(len(enemies) - 1, -1, -1):
            if enemies[i].imgrect.colliderect(this.imgrect):
                resources.append(Resource(enemies[i].imgrect.left, enemies[i].imgrect.top, random.choice(spawnin)))
                if type(enemies[i]) == Megaenemy:
                    this.dn -= 1
                enemies.pop(i)
        if this.dn < 1:
            this.alive = False
        surface.blit(this.img, this.imgrect)
        return this.alive


class Home:
    def __init__(this, x, y):
        # constructor
        this.img = pygame.image.load("home.png")
        this.imgrect = this.img.get_rect()
        this.imgrect.left = x
        this.imgrect.top = y

    def update(this, plrt):
        global surface, enemies
        # draw image on rects position
        for i in range(len(enemies) - 1, -1, -1):
            if type(enemies[i]) == Enemy:
                if enemies[i].imgrect.colliderect(this.imgrect):
                    resources.append(Resource(enemies[i].imgrect.left, enemies[i].imgrect.top, random.choice(spawnin)))
                    enemies.pop(i)
        surface.blit(this.img, this.imgrect)
        return this.imgrect.colliderect(plrt)


class Smallfarm:
    def __init__(this, x, y):
        # constructor
        this.img = pygame.image.load("smallfarm.png")
        this.imgrect = this.img.get_rect()
        this.imgrect.left = x
        this.imgrect.top = y
        this.am = 0
        this.lcol = pygame.time.get_ticks()

    def update(this, plrt):
        global surface
        # draw image on rects position
        now = pygame.time.get_ticks()
        if now - this.lcol > SMALLFARMSPEED:
            this.lcol = now
            this.am += 1
        surface.blit(this.img, this.imgrect)
        return this.imgrect.colliderect(plrt)


class Farm:
    def __init__(this, x, y):
        # constructor
        this.img = pygame.image.load("farm.png")
        this.imgrect = this.img.get_rect()
        this.imgrect.left = x
        this.imgrect.top = y
        this.am = 0
        this.lcol = pygame.time.get_ticks()

    def update(this, plrt):
        global surface
        # draw image on rects position
        now = pygame.time.get_ticks()
        if now - this.lcol > FARMSPEED:
            this.lcol = now
            this.am += 1
        surface.blit(this.img, this.imgrect)
        return this.imgrect.colliderect(plrt)

class KillBarrier:
    def __init__(this,x,y):
        this.img=pygame.image.load("apstand.png")
        this.imgrect = this.img.get_rect()
        this.imgrect.left = x
        this.imgrect.top = y
    def update(this,plrt):
        global surface
        # draw image on rects position
        surface.blit(this.img, this.imgrect)
        return this.imgrect.colliderect(plrt)
class Burner:
    def __init__(this, x, y):
        # constructor
        this.img = pygame.image.load("burner.png")
        this.imgrect = this.img.get_rect()
        this.imgrect.left = x
        this.imgrect.top = y

    def update(this, plrt):
        global surface
        # draw image on rects position
        surface.blit(this.img, this.imgrect)
        return this.imgrect.colliderect(plrt)


class Resource:
    def __init__(this, x, y, res):
        this.img = pygame.image.load(res + ".png")
        this.imgrect = this.img.get_rect()
        this.imgrect.left = x
        this.imgrect.top = y
        this.type = res

    def update(this, plrt):
        global surface
        # draw image on rects position
        surface.blit(this.img, this.imgrect)
        return this.imgrect.colliderect(plrt)


# intialise the window to do anything
pygame.init()
# make window
lastresspawn = pygame.time.get_ticks()
surface = pygame.display.set_mode((640, 640))
player = pygame.image.load("player.png")
rot = 0
speed = 4
lprs = pygame.time.get_ticks()
REPCREATE = 350
daycn=0

# get rectangle
playerrect = player.get_rect()
# to set fps etc
clock = pygame.time.Clock()
# some vars
x = 200
y = 200
def maptogame(x,y):
    global enemies,buildings,resources
    enemies=[]
    buildings=[]
    resources=[]
    for i in map[x][y]:
        if type(i)==Resource:
            resources.append(i)
        elif type(i)==Enemy or type(i)==Megaenemy or type(i)==KillBarrier:
            enemies.append(i)
        else:
            buildings.append(i)
def gametomap(x,y):
    global map
    map[x][y]=[]
    map[x][y].extend(enemies)
    map[x][y].extend(buildings)
    map[x][y].extend(resources)
HUNGERDELAY = 20000
spawnin = ['wood', 'stone']
waitdelay = 1000
buildings = []
enemies = []
resources = []
inventory = {'wood': 0, 'stone': 0, 'flammable': 0, 'metal': 0, 'food': 0}
angle = 0
health = 10
qprs = False
winter = True
flame = False
freeze = 0
mapx=0
mapy=0
daydelay=120000
def lightthecampfire():
    global run
    bigwood=pygame.transform.scale(pygame.image.load("wood"),(surface.get_width(),surface.get_height()))
    compl=False
    while True:
        for ev in pygame.event.get():
            # self explanatory
            if ev.type == QUIT:
                pygame.quit()
                run = False
                break
            elif ev.type==KEYDOWN:
                if ev.key==K_ESCAPE:
                    break
        
    return compl
prs = False
run = True
lastenspawn = pygame.time.get_ticks()
lastmegaenspawn = lastenspawn
enemies.append(Enemy(surface.get_width(), surface.get_height()))
# load font
font = pygame.font.SysFont("Arial", 64)
pygame.display.set_caption("gamepygame")
qprt = pygame.time.get_ticks()
hungerlast = pygame.time.get_ticks()
REPEAT = 350
enemies.append(KillBarrier(0,0))
while run:
    # watch for new events
    for ev in pygame.event.get():
        # self explanatory
        if ev.type == QUIT:
            pygame.quit()
            run = False
            break
        # also self-explanatory
        if ev.type == KEYDOWN:
            if ev.key == pygame.K_b:
                keys = pygame.key.get_pressed()
                # if key is pressed
                if keys[pygame.K_c]:
                    if inventory["wood"] > 2:
                        inventory["wood"] -= 3
                        buildings.append(Campfire(playerrect.left, playerrect.top))
                elif keys[pygame.K_h]:
                    if inventory["wood"] > 4 and inventory["stone"] > 3:
                        inventory["wood"] -= 5
                        inventory["stone"] -= 4
                        buildings.append(Home(playerrect.left, playerrect.top))
                elif keys[pygame.K_o]:
                    if inventory["flammable"] > 1 and inventory["stone"] > 3:
                        inventory["flammable"] -= 2
                        inventory["stone"] -= 4
                        buildings.append(Burner(playerrect.left, playerrect.top))
                    elif inventory["wood"] > 4 and inventory["stone"] > 5:
                        inventory["wood"] -= 5
                        inventory["stone"] -= 6
                        buildings.append(Burner(playerrect.left, playerrect.top))
                elif keys[K_f]:
                    if inventory["wood"] > 8 and inventory["stone"] > 8:
                        inventory["wood"] -= 9
                        inventory["stone"] -= 9
                        buildings.append(Farm(playerrect.left, playerrect.top))
                elif keys[K_x]:
                    if inventory["wood"] > 2 and inventory["stone"] > 4:
                        inventory["wood"] -= 3
                        inventory["stone"] -= 5
                        buildings.append(Smallfarm(playerrect.left, playerrect.top))
                elif keys[K_p]:
                    if inventory["metal"] > 1 and inventory["stone"] > 1:
                        inventory["metal"] -= 2
                        inventory["stone"] -= 2
                        buildings.append(AEStand(playerrect.left, playerrect.top))

    # set fps
    if not run:
        continue
    daycn=(pygame.time.get_ticks()-(pygame.time.get_ticks()//daydelay)*daydelay)/daydelay
    if daycn<0.5:
        mult=1-daycn
    elif daycn<1:
        mult=daycn
    clock.tick(60)
    # get pressed keys
    keys = pygame.key.get_pressed()
    x += ((keys[pygame.K_RIGHT] or keys[pygame.K_d]) - (keys[pygame.K_LEFT] or keys[pygame.K_a])) * speed
    y += ((keys[pygame.K_DOWN] or keys[pygame.K_s]) - (keys[pygame.K_UP] or keys[pygame.K_w])) * speed
    playerrect.x += x
    playerrect.y += y
    now = pygame.time.get_ticks()
    delay = now - lastresspawn
    if delay > waitdelay:
        lastresspawn = now
        waitdelay *= 1.05
        resources.append(Resource(random.randint(0, surface.get_width()), random.randint(0, surface.get_height()),
                                  random.choice(spawnin)))
    delay = now - lastenspawn
    if delay > spawndelay:
        lastenspawn = now
        spawndelay *= 0.95
        enemies.append(Enemy(random.randint(0, surface.get_width()), random.randint(0, surface.get_height())))
    if health < 3:
        try:
            warn = pygame.mixer.Sound("warning.wav")
            warn.set_volume(0.3)
            warn.play(0)
        except:
            pass
    gametomap(mapx,mapy)
    if playerrect.right>surface.get_width():
        mapx+=1
        playerrect.centerx=20
    if playerrect.left<0:
        mapx-=1
        playerrect.centerx=surface.get_width()-20
    if playerrect.top<0:
        mapy-=1
        playerrect.centery=surface.get_height()-20
    if playerrect.bottom>surface.get_height():
        mapy+=1
        playerrect.centery=20
    while mapx > len(map)-1:
        mapx-=len(map)
    while mapx<0:
        mapx+=len(map)
    while mapy > len(map[mapx]) - 1:
        mapy-=len(map[mapx])
    while mapy<0:
        mapy+=len(map[mapx])

    maptogame(mapx,mapy)

    flame = False
    home = False
    createrights = [False]
    surface.fill((255 * winter*mult, 255*mult, 255 * winter*mult))
    revbuildings = buildings[::-1]
    for a in range(len(revbuildings) - 1, -1, -1):
        i = revbuildings[a]
        if type(i) == Campfire:
            flame = flame or i.update(playerrect)
            i.update(playerrect)
        if type(i) == Home:
            home = home or i.update(playerrect)
            i.update(playerrect)
        if type(i) == Burner:
            createrights[0] = createrights[0] or i.update(playerrect)
            home = home or i.update(playerrect)
            i.update(playerrect)
        if type(i) == Farm:
            if keys[K_g] and i.update(playerrect):
                inventory["wood"] += i.am
                i.am = 0
            i.update(playerrect)
        if type(i) == Smallfarm:
            if keys[K_g] and i.update(playerrect):
                inventory["wood"] += i.am
                i.am = 0
            i.update(playerrect)
        if type(i) == AEStand:
            if not i.update(playerrect):
                buildings.pop(a)
    buildings = revbuildings[::-1]
    for i in range(len(resources) - 1, -1, -1):
        if resources[i].update(playerrect) and keys[pygame.K_m]:
            inventory[resources[i].type] += 1
            resources.pop(i)
        else:
            resources[i].update(playerrect)
    try:
        if not (x == 0 and y == 0):
            angle = (180 + math.degrees(math.atan2(x, y)))
    except:
        pass
    if (freeze > 800):
        try:
            warn = pygame.mixer.Sound("warning.wav")
            warn.set_volume(0.3)
            warn.play(0)
        except:
            pass
    if (freeze > 1000):
        pygame.quit()
        break
    if (keys[K_k] and (not prs)) and createrights[0]:
        lprs = pygame.time.get_ticks()
        if keys[K_f] and inventory["wood"] > 1:
            inventory["wood"] -= 2
            inventory["flammable"] += 1
        elif keys[K_m] and inventory["stone"] > 1 and inventory["flammable"] > 0:
            inventory["flammable"] -= 1
            inventory["stone"] -= 2
            inventory["metal"] += 2
        elif keys[K_m] and inventory["stone"] > 2 and inventory["wood"] > 0:
            inventory["wood"] -= 1
            inventory["stone"] -= 3
            inventory["metal"] += 1
        elif keys[K_h] and inventory["wood"] > 4:
            inventory["wood"] -= 5
            inventory["stone"] += 1
        elif keys[K_e] and inventory["wood"] > 2 and inventory["stone"] > 0:
            inventory["wood"] -= 3
            inventory["food"] += 1
    if (keys[K_q] and (not qprs)) and inventory["food"] > 0:
        qprt = pygame.time.get_ticks()
        if health < 10:
            inventory["food"] -= 1
            health += 1
        if health > 10:
            health = 10
    if health < 3 and inventory["food"] > 0:
        inventory["food"] -= 1
        health += 1
        if health > 10:
            health = 10
    if health > 10:
        health = 10
    prs = keys[K_k]
    qprs = keys[K_k]
    now = pygame.time.get_ticks()
    for i in range(len(enemies) - 1, -1, -1):
        if enemies[i].update(playerrect):
            if type(enemies[i]) == Enemy:
                health -= 1
            elif type(enemies[i]) == Megaenemy:
                health -= 2
            if type(enemies[i])==KillBarrier:
                health=0
                continue
            resources.append(Resource(enemies[i].imgrect.left, enemies[i].imgrect.top, random.choice(spawnin)))
            enemies.pop(i)

    if now - lprs > REPCREATE:
        prs = False
    if now - qprt > REPEAT:
        qprs = False
    cold = winter and (not flame)
    if now - hungerlast > HUNGERDELAY:
        health -= 1
        hungerlast = now
    if home:
        freeze -= 0.2
    elif cold:
        freeze += 0.5
    elif flame:
        freeze += 0.1
    if freeze < 0:
        freeze = 0
    if health < 1:
        pygame.quit()
        break
    if pygame.time.get_ticks() > 120000:
        if now - lastmegaenspawn > megaspawndelay:
            enemies.append(Megaenemy(random.randint(0, surface.get_width()), random.randint(0, surface.get_height())))
            lastmegaenspawn = now
            megaspawndelay *= 0.95
    rplayer = pygame.transform.rotate(player, angle)
    rrect = rplayer.get_rect(center=playerrect.center)
    surface.blit(rplayer, rrect)
    if winter:
        label = font.render("cold level:" + str(math.floor(freeze / 10)) + "." + str(
            math.floor((freeze / 10 - math.floor(freeze / 10)) * 100)), 1, (255, 0, 255))
        label.set_alpha(127)
        surface.blit(label, (0, 0))
    label1 = font.render("wood:" + str(inventory["wood"]) + " stone:" + str(inventory["stone"]), 1, (255, 0, 255))
    label1.set_alpha(127)
    surface.blit(label1, (0, surface.get_height() - 100))
    label1 = font.render("flammable:" + str(inventory["flammable"]) + " metal:" + str(inventory["metal"]), 1,
                         (255, 0, 255))
    label1.set_alpha(127)
    surface.blit(label1, (0, surface.get_height() - 200))
    label1 = font.render("food:" + str(inventory["food"]) + " health:" + str(health) + "/10", 1, (255, 0, 255))
    label1.set_alpha(127)
    surface.blit(label1, (0, surface.get_height() - 300))
    label1 = font.render(str(int(int(daycn*24*60+0.5)//60)).zfill(2)+":"+str(int(daycn*24*60+0.5)%60).zfill(2), 1, (255, 0, 255))
    label1.set_alpha(127)
    surface.blit(label1, (0, surface.get_height() - 400))
    x = 0
    y = 0
    pygame.display.flip()
