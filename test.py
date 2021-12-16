import pygame, sys
from pygame.color import THECOLORS
from pygame import font
pygame.init()
pygame.display.set_caption("Крутая игра")
def direction():
    # global name
     screen = pygame.display.set_mode([300, 200])
     background = pygame.Surface([300,160])
     info_w = pygame.Surface([300,40])
     info_w.fill([255,255,255])
     color = THECOLORS["blue"]
     font = pygame.font.SysFont("Arial", 24)
     color = THECOLORS["blue"]
     myfont = pygame.font.SysFont("Arial", 16)
     info_text=font.render("Введите ваше имя",1, THECOLORS ["red"])
     info_w.blit(info_text,[50,10])
     screen.blit(info_w, (0, 0))
     text = font.render("",1, THECOLORS ["blue"])
     my_text = myfont.render("Press Enter",1, THECOLORS ["black"])
     k=0; h=12; hor=80;  s=""; name="popov"
     running=True
#background.fill([255,200,0])
     
     while running:
          background.fill([255,200,0])
          background.blit(my_text, [hor+20,120] )
          background.blit(text, [hor,50] )
          for event in pygame.event.get():
             if event.type == pygame.KEYDOWN:
                 if event.key==pygame.K_ESCAPE:
                     running = False
                 else:
                     st=pygame.key.name(event.key)
                     if k==0 and not st=="return":
                          st=st.title()
                          k=1
                     if st=="space":
                          st=" "
                          k=0
                     if st=="backspace":
                          st=""
                          a=len(s)-1
                          s=s[0:a]
                     if  not(st=="return"):
                         s=s+st
                     if st =="return":
                          name=s
                          running=False
                     text = font.render(s,0, THECOLORS ["blue"])
          screen.blit(background, (0, 40))
          pygame.display.flip()
     return name
#direction()
#pygame.quit()


print(direction())
