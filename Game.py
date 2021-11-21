import pygame as pg
import time
pg.init()
pg.display.set_caption("Game")
screen = pg.display.set_mode([1280,720])
clock = pg.time.Clock()


class Enemy_:
      def __init__(self,way,xenemy,yenemy,stepenemy):
            self.enemy=pg.transform.scale(pg.image.load(way),(50,50))
            self.posx=xenemy
            self.posy=yenemy
            self.stepenemy=stepenemy*60
            self.attack_start=False
            self.zdorovie=100
            self.damage=90
            self.attack_timer=500

      def move(self,x,y,delta):
            if abs(self.posx-x)<=300:
                  if self.posx>x+50: self.posx-=self.stepenemy*delta
                  if self.posx<x-50: self.posx+=self.stepenemy*delta
                  if self.posy>y+20: self.posy-=self.stepenemy*delta
                  if self.posy<y-20: self.posy+=self.stepenemy*delta
            if abs(x-self.posx)<=50:
                  self.attack_start=True
            elif abs(self.posx-x)>55:
                  self.attack_start=False
            screen.blit(self.enemy,[self.posx,self.posy])
            

      def attack(self,health,weight):
            self.health_taken = health
            if self.attack_start and self.attack_timer:
                  health-=self.damage
                  self.health_taken = health

                  weight-=weight/100*self.damage
            if health==0:
                  self.posx=0
            self.attack_timer-=1
            if self.attack_timer==0:
                  self.attack_timer=500
            pg.draw.rect(screen, [255,0,0], [0,150, weight, 10], 0)





def game():
      
      x=0
      y=360
      step = 4*60
      xenemy=1128
      yenemy=360
      right,left,up,down=False,False,False,False
      look_right=True
      charge=False
      
      last_time=time.time()

      player = pg.transform.scale(pg.image.load('Textures/Res/Player.png'),(50,50))
      enemy_unknown=Enemy_('Textures/enemy.png',xenemy,yenemy,3.8)



      while True:
            delta=time.time()-last_time
            last_time=time.time()


            if right:                
                  if x>=1228: right=False
                  else: x+=step*delta
            if left:
                  if x<=3: left=False
                  else: x-=step*delta
            if up:
                  if y<=260: up=False
                  else: y-=step*delta
            if down:
                  if y>=668: down=False
                  else: y+=step*delta
     
            if charge: step=6*600
            elif not charge: step=4*60

            for event in pg.event.get():
                  if event.type == pg.KEYDOWN:
                        if event.key == pg.K_d:
                              right=True
                              if look_right==False:
                                    player = pg.transform.flip(player,True,False)
                                    look_right=True
                        
                        elif event.key == pg.K_a:
                              left=True
                              if look_right==True:
                                    player = pg.transform.flip(player,True,False)
                                    look_right=False
                        elif event.key == pg.K_w: 
                              up=True
                        elif event.key == pg.K_s: 
                              down=True
                        if event.key==pg.K_LSHIFT: 
                              charge=True
                  if event.type == pg.KEYUP:
                        if event.key == pg.K_d: right=False
                        elif event.key == pg.K_a: left=False
                        elif event.key == pg.K_w: up=False
                        elif event.key == pg.K_s: down=False
                        if event.key==pg.K_LSHIFT: charge=False
                  if event.type == pg.QUIT: quit()


            screen.fill([255,255,255])
            pg.draw.rect(screen, [150,150,150], [0, 280, 1280, 720], 0)
            screen.blit(player,[x,y])
            enemy_unknown.move(x,y,delta)
            enemy_unknown.attack(100,1280)

            pg.display.flip()
            pg.time.delay(int(1/60*1000))