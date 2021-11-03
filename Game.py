import pygame as pg
pg.init()
pg.display.set_caption("Game")
x=0
y=0
def game():
      screen = pg.display.set_mode([1280,720])
      screen.fill([255,255,255])
      pg.display.flip()
      running=True
      player = pg.image.load('Textures/Front_image.jpg')
      player = pg.transform.scale(player,(50,50))
      while running:
            screen.blit(player,[x,y])
            for event in pg.event.get():
                  if event.type == pg.QUIT:
                        pg.quit()
