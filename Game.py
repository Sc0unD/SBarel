import pygame
pygame.init()
def game():
      screen = pygame.display.set_mode([1920,1080])
      pygame.display.flip()
      running=True
      while running:
            for event in pygame.event.get():
                  if event.type == pygame.KEYDOWN:
                        running = False
                  elif event.type == pygame.QUIT:
                        pygame.quit()
