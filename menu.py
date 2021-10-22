import pygame
from pygame.color import THECOLORS
from pygame import font
pygame.init()
pygame.display.set_caption("Menu")
element_menu=['Start','Story','Control','Exit']
element_xy=[210,310,410,510]
def menu(element_menu,element_xy):
      font = pygame.font.Font(None, 55)
      screen = pygame.display.set_mode([800, 600])
      front = pygame.image.load('menu_kart.jpg')
      front = pygame.transform.scale(front,(800,600))
      screen.blit(front,[0,0])
      for i in range(0,4):
            text = font.render(element_menu[i],1, [255,255,255])
            screen.blit(text,[40,element_xy[i]])
      pygame.display.flip()
      running=True
      while running:
            for event in pygame.event.get():
                  if event.type == pygame.KEYDOWN:
                        running = False
                  elif event.type == pygame.QUIT:
                        pygame.quit()
