import pygame, sys
from pygame.locals import *

pygame.init()
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
    pygame.draw.circle(DISPLAYSURF, BLACK,(60,60),14)
    pygame.draw.circle(DISPLAYSURF, BLACK,(389,60),14)
    pygame.draw.circle(DISPLAYSURF, BLACK,(389,389),14)
    pygame.draw.circle(DISPLAYSURF, BLACK,(60,389),14)
    pygame.draw.rect(DISPLAYSURF, BROWN,(42,42,350,12))
    pygame.draw.rect(DISPLAYSURF, BROWN,(42,392,362,12))
    pygame.draw.rect(DISPLAYSURF, BROWN,(42,42,12,350))
    pygame.draw.rect(DISPLAYSURF, BROWN,(392,42,12,350))
    return

def linedrawing(pos):
    cor=pygame.mouse.get_pos()
    x=cor[0]
    y=cor[1]
    striker.rect.x=pos[0]
    striker.rect.y=pos[1]
    dy=(y-striker.rect.y)
    dx=(x-striker.rect.x)
    m =(dy/dx)
    tempx=0
    tempy=0
    ctr=0
    if abs(m)<1:
        b=(2*abs(dy))
        a=(b-(2*abs(dx)))
        p0=(b-abs(dx))
        if m>0:
            tempx=10
        else:
            tempx=-10
        while (ctr*10)<=abs(dx):
            if (p0<0):
                striker.rect.x=striker.rect.x-tempx
                p0=p0+b
                print (p0)
                all_sprites_list.draw(DISPLAYSURF)
                pygame.display.update()
                clock.tick(30)
                DISPLAYSURF.fill(WHITE)
                skeleton()
                pygame.display.flip()
                ctr=ctr+1
            else:
                striker.rect.x=striker.rect.x-tempx
                striker.rect.y=striker.rect.y-10
                p0=p0+a
                print (p0)
                all_sprites_list.draw(DISPLAYSURF)
                pygame.display.update()
                clock.tick(30)
                DISPLAYSURF.fill(WHITE)
                skeleton()
                pygame.display.flip()
                ctr=ctr+1
    else:
        b=(2*abs(dx))
        a=(b-(2*abs(dy)))
        p0=((2*abs(dx))-abs(dy))
        if m>0:
            tempx=10
        else:
            tempx=-10
        while (ctr*10)<=abs(dy):
            if (p0<0):
                striker.rect.y=striker.rect.y-10
                p0=p0+b
                
                print (p0)
                all_sprites_list.draw(DISPLAYSURF)
                pygame.display.update()
                clock.tick(30)
                DISPLAYSURF.fill(WHITE)
                skeleton()
                pygame.display.flip()
                ctr=ctr+1
            else:
                striker.rect.x=striker.rect.x-tempx
                striker.rect.y=striker.rect.y-10
                pygame.display.update()
                p0=p0+a
                print (p0)
                all_sprites_list.draw(DISPLAYSURF)
                pygame.display.update()
                clock.tick(30)
                DISPLAYSURF.fill(WHITE)
                skeleton()
                pygame.display.flip()
                ctr=ctr+1
    return
    

q_coin_list=pygame.sprite.Group()
striker_list=pygame.sprite.Group()
center_list=pygame.sprite.Group()
w_coin_list=pygame.sprite.Group()
b_coin_list=pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
#initializing objects and adding them to the sprites array
#Striker
striker=coin(1)
striker.rect.x=127
striker.rect.y=345
striker_list.add(striker)
all_sprites_list.add(striker)
#Center
center=coin(5)
center.rect.x=210
center.rect.y=210
center_list.add(center)
#Queen
q_coin=coin(2)
q_coin.rect.x=225
q_coin.rect.y=225
q_coin_list.add(q_coin)
all_sprites_list.add(q_coin)
#White coin
w_coin=coin(3)
w_coin.rect.x=225
w_coin.rect.y=235
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)
w_coin=coin(3)
w_coin.rect.x=225
w_coin.rect.y=245
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)
w_coin=coin(3)
w_coin.rect.x=225
w_coin.rect.y=205
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)
w_coin=coin(3)
w_coin.rect.x=216
w_coin.rect.y=220
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)
w_coin=coin(3)
w_coin.rect.x=207
w_coin.rect.y=215
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)
w_coin=coin(3)
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
w_coin.rect.x=207
w_coin.rect.y=235
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)
w_coin=coin(3)
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
#DISPLAYSURF.blit(pygame.image.load("center.png"),(210,210))
ctr=0
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(WHITE)
    skeleton()
    center_list.draw(DISPLAYSURF)
    all_sprites_list.draw(DISPLAYSURF)
    if event.type==pygame.MOUSEBUTTONDOWN:
        if event.button==3:
            pos=pygame.mouse.get_pos()
            if pos[0]>116 and pos[0]<336 and pos[1]>345 and pos[1]<357:
                striker.rect.x=pos[0]
                striker.rect.y=pos[1]
                all_sprites_list.draw(DISPLAYSURF)
        elif event.button==1:
            linedrawing(pos)

            

    
            
            
    pygame.display.flip()

