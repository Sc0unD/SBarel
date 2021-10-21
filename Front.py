import pygame, sys
from pygame.color import THECOLORS
from pygame import font
import interface
pygame.init()
pygame.display.set_caption("AAA")
ui = interface.Interface()
def joke():
    ui.set_ui([
        interface.Button((300,200),'grey','Ti pidor',pygame.font.Font(None, 100),bg='green')
    ])
def splash_screen():
    font = pygame.font.Font(None, 45)
    text = font.render("Welcome to Tamriel",True, THECOLORS ["grey"])
    screen = pygame.display.set_mode([800, 600])

    front = pygame.image.load('front.jpeg')
    front = pygame.transform.scale(front, (800 ,600))
    screen.blit(front,[0,0])
    screen.blit(text,[250,550])
    ui.set_ui([
        interface.Button((700,400),'grey','najmi',pygame.font.Font(None, 30), joke  ,bg='green')
    ])


    running=True
    while running:
        for event in pygame.event.get():
            ui.update_buttons(event)
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                running = False
        ui.draw(screen)
        pygame.display.flip()
splash_screen()
pygame.quit()