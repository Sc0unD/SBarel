import pygame as pg
import time
from random import randint as rd

pg.init()
pg.display.set_caption("Game")

screen = pg.display.set_mode([1280,720])
images=['Textures/enemy.png','Textures/enemy.png','Textures/enemy.png']

max_health=100
health_player=max_health


class Enemy:
      def __init__(self,attack_timer=111,damage=rd(30,80)):
            self.posx=rd(700,1200)
            self.posy=rd(320,650)
            self.modify=rd(45,60)
            self.size=self.modify
            self.enemy=pg.transform.scale(pg.image.load(images[rd(0,2)]),(self.size,self.size))
            self.stepenemy=rd(20,39)*60/10
            self.attack_start=False
            self.health_enemy_max=100
            self.health_enemy=self.health_enemy_max
            self.hp_bar_max=self.modify+20
            self.hp_bar_cur=self.hp_bar_max
            self.damage=damage
            self.attack_timer=attack_timer
            self.attack_delay = attack_timer
            self.distanciaX=rd(40,60)
            self.distanciaY=rd(15,35)
            self.stay_timer=150
            self.s=[1,-1]
            self.ss=self.s[rd(0,1)]
            
      def move(self,x,y,delta):
            if abs(self.posx-x)<=300:
                  if self.posx>x+self.distanciaX: self.posx-=self.stepenemy*delta
                  if self.posx<x-self.distanciaX: self.posx+=self.stepenemy*delta
                  if self.posy>y+self.distanciaY: self.posy-=self.stepenemy*delta
                  if self.posy<y-self.distanciaY: self.posy+=self.stepenemy*delta
                  self.presledovanie=True
                  self.ss=self.s[rd(0,1)]
                  self.stay_timer=150
            else: 
                  self.presledovanie=False
                  
            if not self.presledovanie:
                  if self.stay_timer>0:
                        self.stay_timer-=1
                  if self.stay_timer<=0 and 10<self.posx<1200 and 280<self.posy<1200:
                        if self.ss==1:
                              self.posx+=self.stepenemy*delta
                        elif self.ss==-1:
                              self.posx-=self.stepenemy*delta
                  if self.posx<=10 or self.posx>=1200:
                        # self.stay_timer=150
                        self.ss=self.ss*-1
                  
                  
            if abs(x-self.posx)<=50 and abs(y-self.posy)<=40:
                  self.attack_start=True
            elif abs(self.posx-x)>50 or abs(y-self.posy)>=40:
                  self.attack_start=False
            screen.blit(self.enemy,[self.posx,self.posy])
            

      def attack(self):

            global health_player

            if self.attack_start and self.attack_timer==self.attack_delay:
                  health_player-=self.damage
                  self.attack_timer-=1           
                  
            if self.attack_timer<self.attack_delay: 
                  self.attack_timer-=1 
                  if self.attack_timer<=0:
                        self.attack_timer=self.attack_delay
      
      def damage_taken(self,attack_player,damage_player):
            if attack_player:
                  self.health_enemy-=damage_player
            self.hp_bar_cur=self.hp_bar_max*(self.health_enemy/self.health_enemy_max)
            pg.draw.rect(screen, [255,0,0],[(self.posx+(self.size/2))-self.hp_bar_cur/2 ,self.posy-8,self.hp_bar_cur,5],0)


                        

def death():
      size = 40   
      run=True
      image_death=pg.transform.scale(pg.image.load('Textures/3.jpg'),(1280,720))
      
                 
      while run:
            font  = pg.font.Font('Textures/Res/Chronicle.ttf', int(size))
            text = font.render("GAME OVER",True, [255,0,0])
            pg.display.flip()
            pg.time.delay(12)
         


            death_picX=(1280-text.get_size()[0])//2
            

            screen.blit(image_death,(0,0))
            screen.blit(text,(death_picX,310))
            if size<=100:
                  size+=1.4
            elif size>100:
                  run=False
                  pg.time.delay(500)
                  run1=True
                  
                  text = font.render("Press SPACE",True, [255,0,0,255]) 
                  text1 = font.render(" to restart",True, [255,0,0,255])
                  death_picX=0-text.get_size()[0]
                  death_picX1=1280
                  all_lenth = text.get_size()[0] + text1.get_size()[0]
                  posx=(1280-all_lenth)//2

                  while run1:
            
                        if death_picX<posx:
                              death_picX+=14
                        if death_picX1>posx+all_lenth-text1.get_size()[0]:
                              death_picX1-=14

                        screen.blit(image_death,(0,0))
                        screen.blit(text,(death_picX ,310))
                        screen.blit(text1,(death_picX1 ,310))
                        pg.display.flip()
                        pg.time.delay(30)

                        
                        for event in pg.event.get():
                              if event.type == pg.KEYDOWN:
                                    if event.key == pg.K_SPACE:
                                          run1=False
                                          game()
                                    if event.type == pg.QUIT: quit()

            pg.display.flip()

            pg.time.delay(35)

            
def game():
      global health_player,max_health
      
      x=0
      y=360
      step = 4

      right,left,up,down=False,False,False,False
      look_right=True
      charge=False
      attack=False
      damage=90
      weigth_health_bar=200
      

      player = pg.transform.scale(pg.image.load('Textures/Res/Player.png'),(50,50))



      kolvo=rd(1,5)
      enemyes=[0]*kolvo
      for i in range(kolvo):
            enemyes[i]=Enemy()


      last_time=time.time()

      while True:

            # health=enemyes[0].attack(health)

            delta=time.time()-last_time
            last_time=time.time()

#Move            
            
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




#Draw
            screen.fill([255,255,255])
            pg.draw.rect(screen, [150,150,150], [0, 280, 1280, 720], 0)
            screen.blit(player,[x,y])
            for i in range(kolvo):
                  enemyes[i].move(x,y,delta)
                  enemyes[i].attack()
                  enemyes[i].damage_taken(attack,damage)
            # enemy1.move(x,y,delta)
            # enemy2.move(x,y,delta)
            weigth = weigth_health_bar*(health_player/max_health)
            pg.draw.rect(screen, [255,0,0], [30,30,weigth,13], 0)
            pg.display.flip()
#Health
            
            if health_player<=0:
                  health_player=max_health
                  pg.time.wait(300)
                  death()


#Delay            
            pg.time.wait(int(1/60*1000))







