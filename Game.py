import pygame as pg
pg.init()
pg.display.set_caption("Game")
screen = pg.display.set_mode([1280,720])

      
def enemyinfo(x,y,xenemy,yenemy):
      stepenemy=0.3
      attack=False
      if 0<xenemy-x+50<=600 and xenemy<=1128: xenemy-=stepenemy
      if 0>xenemy-x-50>=-600 and xenemy>=3: xenemy+=stepenemy
      if 0<y-yenemy<=720: yenemy-=stepenemy
      if 0<y-yenemy>=-720: yenemy+=stepenemy
      if xenemy==x+50 and yenemy==y: attack=True
      if xenemy==x-50 and yenemy==y: attack=True
      return xenemy, yenemy



def game():
      right,left,up,down=False,False,False,False
      x=0
      y=360
      step = 0.5
      xenemy=1128
      yenemy=360
      look_right=True
      charge=False
      attack=False
      health=100
      damage=50
      timer_attack=500
      enemy = pg.transform.scale(pg.image.load('Textures/enemy.png'),(50,50))
      player = pg.transform.scale(pg.image.load('Textures/Res/Player.png'),(50,50))
      while True:
            xenemy,yenemy=enemyinfo(x,y,xenemy,yenemy)
            screen.fill([255,255,255])
            pg.draw.rect(screen, [150,150,150], [0, 280, 1280, 720], 0)
            screen.blit(player,[x,y])
            screen.blit(enemy,[xenemy,yenemy])
            pg.display.flip()


            if right:                
                  if x>=1228: right=False
                  else: x+=step
            if left:
                  if x<=3: left=False
                  else: x-=step
            if up:
                  if y<=260: up=False
                  else: y-=step
            if down:
                  if y>=668: down=False
                  else: y+=step
     
            if charge: step=1
            if not charge: step=0.5
            if attack:
                  if timer_attack==500:
                        health-=damage
                  timer_attack-=1
                  if timer_attack<=0:
                        timer_attack=500
                  

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