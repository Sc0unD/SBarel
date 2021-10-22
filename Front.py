import pygame
from pygame.color import THECOLORS
from pygame import font
pygame.init()
pygame.display.set_caption("Front")
def front():
    font = pygame.font.Font(None, 40)
    text = font.render("Press any key",True, THECOLORS ["grey"])
    screen = pygame.display.set_mode([800, 600])

    front = pygame.image.load('front.jpeg')
    front = pygame.transform.scale(front, (800 ,600))
    screen.blit(front,[0,0])
    screen.blit(text,[300,550])
    pygame.display.flip()


    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                running = False
            elif event.type == pygame.QUIT:
                pygame.quit()

