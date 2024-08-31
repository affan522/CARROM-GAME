import pygame, sys                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
from pygame.locals import *
pygame.init()
FPS=30# frames per second setting
fpsClock=pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((500, 500),0,32)
pygame.display.set_caption('Carrom!')
clock = pygame.time.Clock()
BLACK = (  0,   0,   0)
LIGHTBROWN = ( 255, 255, 153)
WHITE = (255, 255, 255)
BROWN = (102,51,0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0) 
BLUE  = (  0,   0, 255)

class coin(pygame.sprite.Sprite):
    def __init__(self,flag):
        pygame.sprite.Sprite.__init__(self)
        if flag==1:
            self.image=pygame.image.load("striker.png")
        elif flag==2:
            self.image=pygame.image.load("queen.png")
        elif flag==3:
            self.image=pygame.image.load("wcoin.png")
        elif flag==4:
            self.image=pygame.image.load("bcoin.png")
        elif flag==5:
            self.image=pygame.image.load("center.png")
        elif flag==6:
            self.image=pygame.image.load("pocket.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)
         
def skeleton():
    pygame.draw.polygon(DISPLAYSURF, LIGHTBROWN, ((50,50),(50,400),(400,400),(400,50))) 
    pygame.draw.rect(DISPLAYSURF, BLACK,(116,95,220,12),1)
    pygame.draw.rect(DISPLAYSURF, BLACK,(95,117,12,220),1)
    pygame.draw.rect(DISPLAYSURF, BLACK,(116,345,220,12),1)
    pygame.draw.rect(DISPLAYSURF, BLACK,(345,117,12,220),1)
    pygame.draw.line(DISPLAYSURF, BLACK,(82,82),(172,172))
    pygame.draw.line(DISPLAYSURF, BLACK,(82,368),(172,278))
    pygame.draw.line(DISPLAYSURF, BLACK,(368,82),(278,172))
    pygame.draw.line(DISPLAYSURF, BLACK,(278,278),(368,368))
    pygame.draw.rect(DISPLAYSURF, BROWN,(42,42,350,12))
    pygame.draw.rect(DISPLAYSURF, BROWN,(42,392,362,12))
    pygame.draw.rect(DISPLAYSURF, BROWN,(42,42,12,350))
    pygame.draw.rect(DISPLAYSURF, BROWN,(392,42,12,350))
    pocket_list.draw(DISPLAYSURF)
    striker_list.draw(DISPLAYSURF)
    return

def boundary(tempx,tempy):
    for i in all_sprites_list:
        if i.rect.x<=62:
            tempx=-tempx
            i.rect.x=62
        elif i.rect.x>=376:
            tempx=-tempx
            i.rect.x=376
        if i.rect.y<=62:
            tempy=-tempy
            i.rect.y=62
        elif i.rect.y>=376:
            tempy=-tempy
            i.rect.y=376
            
    if striker.rect.x<=62:
        tempx=-tempx
        striker.rect.x=62
    if striker.rect.x>=376:
        tempx=-tempx
        striker.rect.x=376
    if striker.rect.y<=62:
        tempy=-tempy
        striker.rect.y=62
    if striker.rect.y>=376:
        tempy=-tempy
        striker.rect.y=376

    return

def coinpocket():
    global score
    global success
    for i in all_sprites_list:
        for j in pocket_list:
            if i.rect.colliderect(j):
                score=score+5
                success=success+1
                all_sprites_list.remove(i)
                striker_list.draw(DISPLAYSURF)
                all_sprites_list.draw(DISPLAYSURF)
                pygame.display.update()
                clock.tick(70)
                DISPLAYSURF.fill(WHITE)
                skeleton()
                pygame.display.flip()
            
    for i in pocket_list:
        if striker.rect.colliderect(i):
            striker.rect.x=127
            striker.rect.y=345
        if score>=1:
            score=score-1
        striker_list.draw(DISPLAYSURF)
        all_sprites_list.draw(DISPLAYSURF)
        pygame.display.update()
        clock.tick(70)
        DISPLAYSURF.fill(WHITE)
        skeleton()
        pygame.display.flip()
    return
    
def handlecollision():
    coinpocket()
    c=1
    for i in all_sprites_list:
        if striker.rect.colliderect(i):
            dx=i.rect.x-striker.rect.x
            dy=i.rect.y-striker.rect.y
            if dx==0:
                dx=0.1
            m=(dy)/(dx) 
            ctr=0
            if abs(m)<=1:
                b=(2*abs(dy))
                a=(b-(2*abs(dx)))
                p0=(b-abs(dx))
                if m>0:
                    tempx=30
                    tempy=30
                else:
                    tempx=-30
                    tempy=30
                while (ctr*15)<=abs(dx):
                    if (p0<0):
                        i.rect.x=i.rect.x-tempx
                        boundary(tempx,tempy)
                        p0=p0+b
                        coincollision(i,c)
                        striker_list.draw(DISPLAYSURF)
                        all_sprites_list.draw(DISPLAYSURF)
                        pygame.display.update()
                        clock.tick(70)
                        DISPLAYSURF.fill(WHITE)
                        skeleton()
                        ctr=ctr+1
                        pygame.display.flip()
                    else:
                        i.rect.x=i.rect.x-tempx
                        i.rect.y=i.rect.y-tempy
                        boundary(tempx,tempy)
                        p0=p0+a
                        coincollision(i,c)
                        striker_list.draw(DISPLAYSURF)
                        all_sprites_list.draw(DISPLAYSURF)
                        pygame.display.update()
                        clock.tick(70)
                        DISPLAYSURF.fill(WHITE)
                        skeleton()
                        pygame.display.flip()
                        ctr=ctr+1
            else:
                b=(2*abs(dx))
                a=(b-(2*abs(dy)))
                p0=((2*abs(dx))-abs(dy))
                tempy=30
                if m>0:
                    tempx=30
                else:
                    tempx=-30
                while (ctr*15)<=abs(dy):
                    if (p0<0):
                        i.rect.y=i.rect.y-tempy
                        boundary(tempx,tempy)
                        p0=p0+b
                        coincollision(i,c)
                        striker_list.draw(DISPLAYSURF)
                        all_sprites_list.draw(DISPLAYSURF)
                        pygame.display.update()
                        clock.tick(70)
                        DISPLAYSURF.fill(WHITE)
                        skeleton()
                        ctr=ctr+1
                        pygame.display.flip()
                    else:
                        i.rect.x=i.rect.x-tempx
                        i.rect.y=i.rect.y-tempy
                        boundary(tempx,tempy)
                        pygame.display.update()
                        p0=p0+a
                        coincollision(i,c)
                        striker_list.draw(DISPLAYSURF)
                        all_sprites_list.draw(DISPLAYSURF)
                        pygame.display.update()
                        clock.tick(70)
                        DISPLAYSURF.fill(WHITE)
                        skeleton()
                        ctr=ctr+1
                        pygame.display.flip()
    return

def coincollision(i,c):
    coinpocket()
    c=c+1
    if c<10:
        for j in all_sprites_list:
            if i.rect.colliderect(j) and i!=j:#collisions among the coins
                dx=j.rect.x-i.rect.x
                dy=j.rect.y-i.rect.y
                if dx==0:
                    dx=0.1
                m=(dy)/(dx) 
                ctr=0
                if abs(m)<=1:
                    b=(2*abs(dy))
                    a=(b-(2*abs(dx)))
                    p0=(b-abs(dx))
                    tempy=30
                    if m>0:
                        tempx=30
                    else:
                        tempx=-30
                    while (ctr*15)<=abs(dx):
                        if (p0<0):
                            j.rect.x=j.rect.x-tempx
                            boundary(tempx,tempy)
                            p0=p0+b
                            coincollision(j,c)
                            striker_list.draw(DISPLAYSURF)
                            all_sprites_list.draw(DISPLAYSURF)
                            pygame.display.update()
                            clock.tick(70)
                            DISPLAYSURF.fill(WHITE)
                            skeleton()
                            ctr=ctr+1
                            pygame.display.flip()
                        else:
                            j.rect.x=j.rect.x-tempx
                            j.rect.y=j.rect.y-tempy
                            boundary(tempx,tempy)
                            p0=p0+a
                            coincollision(j,c)
                            striker_list.draw(DISPLAYSURF)
                            all_sprites_list.draw(DISPLAYSURF)
                            pygame.display.update()
                            clock.tick(70)
                            DISPLAYSURF.fill(WHITE)
                            skeleton()
                            pygame.display.flip()
                            ctr=ctr+1
                else:
                    b=(2*abs(dx))
                    a=(b-(2*abs(dy)))
                    p0=((2*abs(dx))-abs(dy))
                    tempy=30
                    if m>0:
                        tempx=30
                    else:
                        tempx=-30
                    while (ctr*15)<=abs(dy):
                        if (p0<0):
                            j.rect.y=j.rect.y-tempy
                            boundary(tempx,tempy)
                            p0=p0+b
                            coincollision(j,c)
                            striker_list.draw(DISPLAYSURF)
                            all_sprites_list.draw(DISPLAYSURF)
                            pygame.display.update()
                            clock.tick(70)
                            DISPLAYSURF.fill(WHITE)
                            skeleton()
                            ctr=ctr+1
                            pygame.display.flip()
                        else:
                            j.rect.x=j.rect.x-tempx
                            j.rect.y=j.rect.y-tempy
                            boundary(tempx,tempy)
                            pygame.display.update()
                            p0=p0+a
                            coincollision(j,c)
                            striker_list.draw(DISPLAYSURF)
                            all_sprites_list.draw(DISPLAYSURF)
                            pygame.display.update()
                            clock.tick(70)
                            DISPLAYSURF.fill(WHITE)
                            skeleton()
                            ctr=ctr+1
                            pygame.display.flip()
            
    return


     
def linedrawing(pos):
    cor=pygame.mouse.get_pos()
    x=cor[0]
    y=cor[1]
    striker.rect.x=pos[0]
    striker.rect.y=pos[1]
    dy=(y-striker.rect.y)
    dx=(x-striker.rect.x)
    if dx==0:
        dx=0.1
    m =(dy/dx)
    tempx=0
    tempy=0
    ctr=0
    if abs(m)<1:
        b=(2*abs(dy))
        a=(b-(2*abs(dx)))
        p0=(b-abs(dx))
        tempy=15
        if m>0:
            tempx=15
        else:
            tempx=-15
        while (ctr*15)<=abs(dx):
            if (p0<0):
                striker.rect.x=striker.rect.x-tempx
                boundary(tempx,tempy)
                p0=p0+b
                handlecollision()
                striker_list.draw(DISPLAYSURF)
                all_sprites_list.draw(DISPLAYSURF)
                pygame.display.update()
                clock.tick(70)
                DISPLAYSURF.fill(WHITE)
                skeleton()
                pygame.display.flip()
                ctr=ctr+1
            else:
                striker.rect.x=striker.rect.x-tempx
                striker.rect.y=striker.rect.y-tempy
                boundary(tempx,tempy)
                p0=p0+a
                handlecollision()
                striker_list.draw(DISPLAYSURF)
                all_sprites_list.draw(DISPLAYSURF)
                pygame.display.update()
                clock.tick(70)
                DISPLAYSURF.fill(WHITE)
                skeleton()
                pygame.display.flip()
                ctr=ctr+1
    else:
        b=(2*abs(dx))
        a=(b-(2*abs(dy)))
        p0=((2*abs(dx))-abs(dy))
        c=0
        tempy=15
        if m>0:
            tempx=15
        else:
            tempx=-15
        while (ctr*15)<=abs(dy):
            if (p0<0):
                striker.rect.y=striker.rect.y-tempy
                boundary(tempx,tempy)
                p0=p0+b
                handlecollision()
                striker_list.draw(DISPLAYSURF)
                all_sprites_list.draw(DISPLAYSURF)
                pygame.display.update()
                clock.tick(70)
                DISPLAYSURF.fill(WHITE)
                skeleton()
                pygame.display.flip()
                ctr=ctr+1
            else:
                striker.rect.x=striker.rect.x-tempx
                striker.rect.y=striker.rect.y-tempy
                boundary(tempx,tempy)
                pygame.display.update()
                p0=p0+a
                handlecollision()
                striker_list.draw(DISPLAYSURF)
                all_sprites_list.draw(DISPLAYSURF)
                pygame.display.update()
                clock.tick(70)
                DISPLAYSURF.fill(WHITE)
                skeleton()
                pygame.display.flip()
                ctr=ctr+1
    return

def texts(score):
   font=pygame.font.Font(None,30)
   scoretext=font.render("Score:"+str(score)+"   Trials left:"+str(trials), False,(255,25,0))
   DISPLAYSURF.blit(scoretext, (50, 10))
   return
    
score=0
trials=120
success=0
q_coin_list=pygame.sprite.Group()
striker_list=pygame.sprite.Group()
center_list=pygame.sprite.Group()
w_coin_list=pygame.sprite.Group()
b_coin_list=pygame.sprite.Group()
pocket_list=pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
#initializing objects and adding them to the sprites array
#Striker
striker=coin(1)
striker.rect.x=127
striker.rect.y=345
striker.f=1
striker_list.add(striker)
#Center
center=coin(5)
center.rect.x=210
center.rect.y=210
center_list.add(center)
#pockets
p1=coin(6)
p1.rect.x=42
p1.rect.y=42
pocket_list.add(p1)
p2=coin(6)
p2.rect.x=42
p2.rect.y=380
pocket_list.add(p2)
p3=coin(6)
p3.rect.x=380
p3.rect.y=42
pocket_list.add(p3)
p4=coin(6)
p4.rect.x=380
p4.rect.y=380
pocket_list.add(p4)
#Queen
q_coin=coin(2)
q_coin.f=2
q_coin.rect.x=225
q_coin.rect.y=225
q_coin_list.add(q_coin)
all_sprites_list.add(q_coin)
#White coin
w_coin=coin(3)
w_coin.f=3
w_coin.rect.x=225
w_coin.rect.y=235
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)
w_coin=coin(3)
w_coin.f=3
w_coin.rect.x=225
w_coin.rect.y=245
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)
w_coin=coin(3)
w_coin.f=3
w_coin.rect.x=225
w_coin.rect.y=205
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)
w_coin=coin(3)
w_coin.f=3
w_coin.rect.x=216
w_coin.rect.y=220
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)
w_coin=coin(3)
w_coin.f=3
w_coin.rect.x=207
w_coin.rect.y=215
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)
w_coin=coin(3)
w_coin.f=3
w_coin.rect.x=233
w_coin.rect.y=220
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)
w_coin=coin(3)
w_coin.rect.x=242
w_coin.rect.y=215
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)
w_coin=coin(3)
w_coin.f=3
w_coin.rect.x=207
w_coin.rect.y=235
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)
w_coin=coin(3)
w_coin.f=3
w_coin.rect.x=242
w_coin.rect.y=235
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)

#Black coin
b_coin=coin(4)
b_coin.rect.x=225
b_coin.rect.y=215
b_coin_list.add(b_coin)
all_sprites_list.add(b_coin)
b_coin=coin(4)
b_coin.rect.x=216
b_coin.rect.y=210
b_coin_list.add(b_coin)
all_sprites_list.add(b_coin)
b_coin=coin(4)
b_coin.rect.x=216
b_coin.rect.y=230
b_coin_list.add(b_coin)
all_sprites_list.add(b_coin)
b_coin=coin(4)
b_coin.rect.x=216
b_coin.rect.y=240
b_coin_list.add(b_coin)
all_sprites_list.add(b_coin)
b_coin=coin(4)
b_coin.rect.x=233
b_coin.rect.y=210
b_coin_list.add(b_coin)
all_sprites_list.add(b_coin)
b_coin=coin(4)
b_coin.rect.x=233
b_coin.rect.y=230
b_coin_list.add(b_coin)
all_sprites_list.add(b_coin)
b_coin=coin(4)
b_coin.rect.x=233
b_coin.rect.y=240
b_coin_list.add(b_coin)
all_sprites_list.add(b_coin)
b_coin=coin(4)
b_coin.rect.x=243
b_coin.rect.y=225
b_coin_list.add(b_coin)
all_sprites_list.add(b_coin)
b_coin=coin(4)
b_coin.rect.x=207
b_coin.rect.y=225
b_coin_list.add(b_coin)
all_sprites_list.add(b_coin)

all_sprites_list.draw(DISPLAYSURF)
select=0

ctr=0
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if select==0:
        image=pygame.image.load('carrom.png')
        DISPLAYSURF.blit(image,(0,0))
        font=pygame.font.Font(None,25)
        text=font.render("Right Click to Start", False,(185,185,185))
        DISPLAYSURF.blit(text, (150, 470))
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==3:
                select=1
                pygame.time.delay(20)
                
    if select==1:    
        DISPLAYSURF.fill(WHITE)
        skeleton()
        center_list.draw(DISPLAYSURF)
        striker_list.draw(DISPLAYSURF)
        #pocket_list.draw(DISPLAYSURF)
        all_sprites_list.draw(DISPLAYSURF)
        texts(score)
        if event.type==pygame.MOUSEBUTTONDOWN:
            if(trials<0):
                font=pygame.font.Font(None,30)
                scoretext=font.render("U Lost", False,(255,25,0))
                DISPLAYSURF.blit(scoretext, (50, 10))
                pygame.quit()
                sys.exit()
            if(success==19):
                font=pygame.font.Font(None,30)
                scoretext=font.render("U Win", False,(255,25,0))
                DISPLAYSURF.blit(scoretext, (50, 10))
                pygame.quit()
                sys.exit()
            if event.button==3:
                pos=pygame.mouse.get_pos()
                if pos[0]>116 and pos[0]<336 and pos[1]>345 and pos[1]<357:
                    striker.rect.x=pos[0]
                    striker.rect.y=345
                    striker_list.draw(DISPLAYSURF)
                    pocket_list.draw(DISPLAYSURF)
                    all_sprites_list.draw(DISPLAYSURF)
            elif event.button==1:
                trials=trials-1
                linedrawing(pos)
    pygame.display.flip()

