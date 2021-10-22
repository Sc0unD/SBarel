import pygame
from pygame.color import THECOLORS
from pygame import font
pygame.init()
pygame.display.set_caption("Menu")

def draw_text(font, text, pos, screen):
    for l in text.split('\n'):
        t = font.render(l,True, 'white')
        screen.blit(t, pos)
        pos[1] += t.get_size()[1]

def menu():
    element_menu=['Start','Story','Control','Exit']
    element_y=[210,310,410,510]
    font = pygame.font.Font(None, 50)

    screen = pygame.display.set_mode([800, 600])

    front = pygame.image.load('menu_kart.jpg')
    front = pygame.transform.scale(front,(800,600))

    running=True
    while running:
        screen.blit(front,[0,0])

        for i in range(0,4):
            text = font.render(element_menu[i],1, [255,255,255])
            screen.blit(text,[40,element_y[i]])
        pygame.display.flip()

        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x,y)=pygame.mouse.get_pos()
                    for i in range (0,4):
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if 39<=x<=291 and 209<=y<=260: 
                                running=False
                elif event.type == pygame.QUIT:
                    pygame.quit()
#                                while True:  
 #                                   draw_text(pygame.font.Font(None, 50), res.story, [100,100], screen)
       
                    
            
