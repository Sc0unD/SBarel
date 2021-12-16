import pygame as pg
import game
import json
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

def record():
    with open("records.json", "r") as file:
        rec_l = json.loads(file.readline())
    font = pg.font.Font(None, 50)
    record_image = pg.transform.scale(pg.image.load('Textures/record_im.jpg'),(1280,720))
    run = True
    texts = ["Kills -- ","Shouts -- ","Max level -- "]
    texts_z = [str(rec_l["kills"]),str(rec_l["All_shouts"]),str(rec_l["Max_level"])]
    texts_y = [50,100,150]
    screen.blit(record_image,(0,0))

    while run:
        for i in range(len(texts)):
            text_rec = font.render(texts[i], 1, [255,255,255])
            text_rec1 = font.render(texts_z[i], 1, [255,255,255]) 
            posx = 1280/2 - (text_rec.get_size()[0]/2)
            screen.blit(text_rec,(posx,texts_y[i]))
            screen.blit(text_rec1,(posx + text_rec.get_size()[0],texts_y[i]))
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                run=False
            

def menu():

    run=True

    element_menu=['Start','Story','Control','Records','Exit']
    element_y=[210,310,410,510,610]


 

    

    front = pg.image.load('Textures/menu_image.png')
  
    while run:
        fonts = [None,None,None,None,None]
        fonts_color = ['white','white','white','white','white']
        size = [50,50,50,50,50]

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
        elif 39<=x<=173 and 509<=y<=545:
            fonts[3]='Textures/Res/Burn.otf'
            fonts_color[3]= 'darkorange'
            size[3]=36
        elif 39<=x<=115 and 609<=y<=645:
            fonts[4]='Textures/Res/Burn.otf'
            fonts_color[4]= 'darkorange'
            size[4]=36



        for i in range(len(element_menu)):
            font = pg.font.Font(fonts[i], size[i])
            text = font.render(element_menu[i],1, fonts_color[i])
            screen.blit(text,[40,element_y[i]])


        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                if 39<=x<=291 and 209<=y<=245: 
                    run=False
                    game.game()
                elif 39<=x<=145 and 309<=y<=345: story()
                elif 39<=x<=176 and 409<=y<=445: control()
                elif 39<=x<=119 and 509<=y<=545: record()
                elif 39<=x<=135 and 609<=y<=645: quit() 
                elif event.type == pg.QUIT: quit()   

  
