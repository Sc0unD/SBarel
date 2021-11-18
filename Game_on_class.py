import pygame as pg
pg.init()
pg.display.set_caption("Game")
screen = pg.display.set_mode([1280,720])
def game():
      right,left,up,down=False,False,False,False
      x=0
      y=0
      step = 1
      running=True
      look_right=True
      player = pg.image.load('Textures/Res/Player.png')
      player = pg.transform.scale(player,(150,150))
      while running:
            screen.fill([255,255,255])
            screen.blit(player,[x,y])
            screen.blit(axe,[xAxe,yAxe])
            pg.display.flip()
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
                        if event.key==pg.K_f:
                              metanie=True
                              if look_right:
                                    xAxe=x+150
                                    storona_axe=1
                              elif not look_right:
                                    xAxe=x-5
                                    storona_axe=2
                              yAxe=y+75
                  if event.type == pg.KEYUP:
                        if event.key == pg.K_d:
                              right=False
                        if event.key == pg.K_a:
                              left=False
                        elif event.key == pg.K_w:
                              up=False
                        elif event.key == pg.K_s:
                              down=False
                  if event.type == pg.QUIT:
                        exit()
            if right:
                  if x>=1128:
                        right=False
                  else:
                        x+=step
            if left:
                  if x<=3:
                        left=False
                  else:
                        x-=step
            if up:
                  if y<=0:
                        up=False
                  else:
                        y-=step
            if down:
                  if y>=568:
                        down=False
                  else:
                        y+=step            
