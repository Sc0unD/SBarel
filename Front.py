import pygame as pg
pg.init()
pg.display.set_caption("Front")

def front():

    koef = 0
    shag = 1.5

    font = pg.font.Font(None, 55)
    
    screen = pg.display.set_mode([1280, 720])

    image = pg.image.load('Textures/Front_image.jpg')
    image = pg.transform.scale(image, (1280, 720))


    screen.blit(image,[0,0])

    
    running=True
    while running:
        text = font.render("Press any key",True, [200-koef,200-koef,200-koef])
        if koef>=0:
            koef+=shag
            if koef>=199:
                shag=-shag
            elif koef<=1:
                shag=-shag
        screen.blit(text,[500,650])
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
                running = False
            elif event.type == pg.QUIT:
                pg.quit()
        pg.time.delay(19)
