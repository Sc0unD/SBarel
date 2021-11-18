import pygame as pg
pg.init()
pg.display.set_caption("Menu")

screen = pg.display.set_mode([1280, 720])


def control():
    ypr = pg.image.load('Textures/Control_image.png')

    running=True

    while running:
        screen.blit(ypr,[0,0])
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
                running= False
            elif event.type == pg.QUIT:
                quit()

def story():
    history = pg.image.load('Textures/Story_image.png')
    running = True

    while running:
        screen.blit(history,[0,0])
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
                running= False
            elif event.type == pg.QUIT:
                quit()

def menu():

    running=True

    element_menu=['Start','Story','Control','Exit']
    element_y=[210,310,410,510]
 

    

    front = pg.image.load('Textures/menu_image.png')
  
    while running:
        fonts = [None,None,None,None]
        fonts_color = ['white','white','white','white']
        size = [50,50,50,50]

        (x,y)=pg.mouse.get_pos()

        screen.blit(front,[0,0])

        if 39<=x<=135 and 209<=y<=245:
            fonts[0]= 'Textures/Res/Burn.otf'
            fonts_color[0]= 'darkorange'
            size[0]=36
        elif 39<=x<=135 and 309<=y<=345:
            fonts[1]='Textures/Res/Burn.otf'
            fonts_color[1]= 'darkorange'
            size[1]=36
        elif 39<=x<=173 and 409<=y<=445:
            fonts[2]='Textures/Res/Burn.otf'
            fonts_color[2]= 'darkorange'
            size[2]=36
        elif 39<=x<=115 and 509<=y<=545:
            fonts[3]='Textures/Res/Burn.otf'
            fonts_color[3]= 'darkorange'
            size[3]=36



        for i in range(4):
            font = pg.font.Font(fonts[i], size[i])
            text = font.render(element_menu[i],1, fonts_color[i])
            screen.blit(text,[40,element_y[i]])


        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN and 39<=x<=291 and 209<=y<=245: running=False
            elif 39<=x<=145 and 309<=y<=345 and event.type == pg.MOUSEBUTTONDOWN: story()
            elif 39<=x<=176 and 409<=y<=445 and event.type == pg.MOUSEBUTTONDOWN: control()
            elif 39<=x<=119 and 509<=y<=545 and event.type == pg.MOUSEBUTTONDOWN: quit() 
            elif event.type == pg.QUIT: quit()   

  
