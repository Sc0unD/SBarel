import pygame as pg
import time, importlib

pg.init()
pg.display.set_caption("Game")
screen = pg.display.set_mode([1280,720])


class Enemy_:
      def __init__(self,way,xenemy,yenemy,stepenemy,health_player,attack_delay):
            self.enemy=pg.transform.scale(pg.image.load(way),(50,50))
            self.posx=xenemy
            self.posy=yenemy
            self.stepenemy=stepenemy*60
            self.attack_start=False
            self.zdorovie=100
            self.damage=60
            self.attack_timer=117
            self.attack_delay = attack_delay
            self.weight=1280
            self.weight_max=self.weight
            self.health_player = health_player
            self.otnoshenie=(self.health_player-self.damage)/self.health_player
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
            

      def attack(self):

            if self.attack_start and self.attack_timer==self.attack_delay:
                  self.health_player-=self.damage
                  self.attack_timer-=1           
                  self.weight-=self.weight_max*(1-self.otnoshenie)
            if self.attack_timer<self.attack_delay: 
                  self.attack_timer-=1 
                  if self.attack_timer==0:
                        self.attack_timer=self.attack_delay
            pg.draw.rect(screen, [255,0,0], [0,150, self.weight, 10], 0)
            pg.display.flip()
            if self.health_player<=0:
                  run=True
                  while run:
                        screen.fill([255,255,255])
                        pg.display.flip()
                        for event in pg.event.get():
                              if event.type == pg.KEYDOWN:
                                    if event.key == pg.K_SPACE:
                                          run=False
                                          game()

           





def game():
      
      x=0
      y=360
      step = 4
      xenemy=1128
      yenemy=360
      right,left,up,down=False,False,False,False
      look_right=True
      charge=False
      
      last_time=time.time()

      player = pg.transform.scale(pg.image.load('Textures/Res/Player.png'),(50,50))
      enemy_unknown=Enemy_('Textures/enemy.png',xenemy,yenemy,3.8,100,117)



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
     
            if charge: step=7*60
            elif not charge: step=4*60

            for event in pg.event.get():
                  if event.type == pg.KEYDOWN:
                        if event.key == pg.K_d:
                              right=True
                              if look_right==False:
                                    player = pg.transform.flip(player,True,False)
                                    look_right=True
                        
                        if event.key == pg.K_a:
                              left=True
                              if look_right==True:
                                    player = pg.transform.flip(player,True,False)
                                    look_right=False
                        if event.key == pg.K_w: 
                              up=True
                        if event.key == pg.K_s: 
                              down=True
                        if event.key==pg.K_LSHIFT: 
                              charge=True
                  if event.type == pg.KEYUP:
                        if event.key == pg.K_d: right=False
                        if event.key == pg.K_a: left=False
                        if event.key == pg.K_w: up=False
                        if event.key == pg.K_s: down=False
                        if event.key==pg.K_LSHIFT: charge=False
                  if event.type == pg.QUIT: quit()


            screen.fill([255,255,255])
            pg.draw.rect(screen, [150,150,150], [0, 280, 1280, 720], 0)
            screen.blit(player,[x,y])
            enemy_unknown.move(x,y,delta)
            enemy_unknown.attack()

            pg.display.flip()
            pg.time.delay(int(1/60*1000))
