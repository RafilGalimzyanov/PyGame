import pygame
import time

pygame.init()
экрана_ширина = 1280
экрана_высота = 720
экранаРазмер = pygame.display.set_mode((экрана_ширина,экрана_высота))#
pygame.display.set_caption("KUZ")
clock = pygame.time.Clock()
### PLATFORM ###
platform1_ширина=128
platform1_высота=93
platform1_левый = pygame.image.load(r"Texture_Paketi\Tiles\13.png")
platform1_orta = pygame.image.load(r"Texture_Paketi\Tiles\14.png")
platform1_правый = pygame.image.load(r"Texture_Paketi\Tiles\15.png")
####################################################

### ОБЪЕКТЫ ###



enemy1_1=pygame.image.load(r"Texture_Paketi_3\PNG\Enemies\enemyFlying_1.png")
enemy1_3=pygame.image.load(r"Texture_Paketi_3\PNG\Enemies\enemyFlying_3.png")
enemy1_max_sprite =2
enemy1_current_sprite=0


персонаж_current_sprite = 0
персонаж_перв = pygame.image.load(r"объекты\minus.png")
персонаж_перв=pygame.transform.smoothscale(персонаж_перв,(50,50))
персонаж_второй = pygame.image.load(r"объекты\второй.png")
персонаж_второй=pygame.transform.smoothscale(персонаж_второй,(50,50))

шапка = pygame.image.load(r"объекты\witcher_hat.png")
шапка=pygame.transform.smoothscale(шапка,(64,64))


сердце = pygame.image.load(r"объекты\сердце.png")
сердце=pygame.transform.smoothscale(сердце,(64,64))
котел = pygame.image.load(r"Texture_Paketi\Object\котел.png")
котел=pygame.transform.smoothscale(котел,(100,100))
ot = pygame.image.load(r"Texture_Paketi\Object\Bush (3).png")
ot=pygame.transform.smoothscale(ot,(120,70))
срез_дерево = pygame.image.load(r"Texture_Paketi\Object\Tree_1.png")



ev = pygame.image.load(r"объекты\ev.png")
ev=pygame.transform.smoothscale(ev,(300,300))

взрыв = pygame.image.load(r"объекты\взрыв.png")
взрыв=pygame.transform.smoothscale(взрыв,(210,270))

portal = pygame.image.load(r"объекты\Portal.png")
tas1 = pygame.image.load(r"Ground&Stone\Stone\tas1.png")
####################################################################
platform1_правый=pygame.transform.scale(platform1_правый,(int(platform1_ширина/1.2),int(platform1_высота/1.2)))
platform1_orta=pygame.transform.scale(platform1_orta,(int(platform1_ширина/1.2),int(platform1_высота/1.2)))
platform1_левый=pygame.transform.scale(platform1_левый,(int(platform1_ширина/1.2),int(platform1_высота/1.2)))

tas=pygame.image.load(r"фон\background5.jpg")
заднийфон = pygame.image.load(r"фон\background4.jpg")
заднийфон_gece = pygame.image.load(r"фон\background2.png")
заднийфон_gece=pygame.transform.scale(заднийфон_gece,(1280,800))

ведьма = pygame.image.load(r"объекты\witch.png")
ведьма=pygame.transform.smoothscale(ведьма,(134,140))
ведьма = pygame.transform.flip(ведьма, True, False)

персонаж_sprite = pygame.image.load("персонаж\ghost.png")
персонаж_sprite_left = pygame.image.load("персонаж\ghost_left.png")

персонаж_sprite_left_fairy = pygame.image.load("персонаж\ghost_left.png")
персонаж_sprite_left_fairy=pygame.transform.smoothscale(персонаж_sprite_left_fairy,(50,50))
персонаж_sprite_number = 29
персонаж_current_sprite = 0

обратная_анимация=False
pygame.display.set_icon(персонаж_перв)
правый=True
левый=False

раздел=1


персонаж_ширина=105      #319
персонаж_высота= 107    #306

death_number=0

время_полета=0

статус_записи=0

can=3

action_скольжение_x = 0

mod='Ходьба (Примечание: вы можете проходить сквозь объекты в режиме призрака)'


def персонаж(x,y,правый_yon):
    if правый_yon==True:
        экранаРазмер.blit(персонаж_sprite,(x,y),(персонаж_current_sprite*персонаж_ширина,0,персонаж_ширина,персонаж_высота))
    else:
        экранаРазмер.blit(персонаж_sprite_left, (x, y),(персонаж_current_sprite * персонаж_ширина, 0, персонаж_ширина, персонаж_высота))

def rectangle(rectangle_x,rectangle_y,rectangle_width,rectangle_height,rectangle_color):
    экранаРазмер.blit(platform1_левый,(rectangle_x,rectangle_y))
    экранаРазмер.blit(platform1_orta, (rectangle_x+platform1_ширина-27, rectangle_y))
    экранаРазмер.blit(platform1_правый, (rectangle_x+platform1_ширина*2-54, rectangle_y))

def обьект(обьект_x,раздел_sec):
    global can
    if раздел_sec==1:
        экранаРазмер.blit(шапка, (1400+обьект_x, 95))
    elif раздел_sec==2:
        экранаРазмер.blit(portal, (2100 + обьект_x, 0))
        экранаРазмер.blit(шапка, (2200 + обьект_x, 100))


    if can==3:
        экранаРазмер.blit(сердце, (экрана_ширина-64, 0))
        экранаРазмер.blit(сердце, (экрана_ширина-128, 0))
        экранаРазмер.blit(сердце, (экрана_ширина - 192, 0))
    elif can==2:
        экранаРазмер.blit(сердце, (экрана_ширина - 64, 0))
        экранаРазмер.blit(сердце, (экрана_ширина - 128, 0))
    elif can==1:
        экранаРазмер.blit(сердце, (экрана_ширина - 64, 0))
    elif can==0:
        can=3
        death()

white=(255, 255, 255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
sky_blue=(67,190,215)
pink=(255,20,147)

def death():
    pygame.mixer.music.load('Musics\Just Go(12).mp3')
    pygame.mixer.music.play(-1)
    global death_number
    death_number+=1
    объявление("вы переигрываете"+str(death_number)+"раз")



def прыжок_fonk():
    global время_полета
    время_полета+=1/30


def game_loop():

    kontrol=False

    global enemy1_max_sprite
    global enemy1_current_sprite

    global раздел
    global action_скольжение_x
    global обьект_action_скольжение_x
    global can
    global mod
    global время_полета
    global персонаж_current_sprite
    global обратная_анимация

    global правый
    global левый
    обратная_анимация=False

    подъем_y=0

    прыжок=False

    персонаж_yon=1


    монстр_x=0
    монстр_x_изменение = 0
    монстр_kontrol=False

    x_изменение = 0
    y_изменение=0
    сила_тяжести=0
    x = 0
    y = 0
    speed=6
    gameExit = False

    заднийфон_x=0

    rectangle_width = 310
    rectangle_height = 10
    rectangle1_x=0
    rectangle1_y =300

    обьект_x=0

    while gameExit == False:  #Пока это ложь :

        ### ВОПРОСЫ ДВИЖЕНИЯ  ###

       if x < персонаж_ширина/2:
           action_скольжение_x=0
           x=персонаж_ширина/2

       if y <= 10 and раздел==2:
           y = 20


       if x > экрана_ширина-персонаж_ширина / 1.5:
           action_скольжение_x = 0
           x = экрана_ширина-персонаж_ширина / 1.5

       if монстр_kontrol==False:
           монстр_x_изменение=8

       if монстр_x >= 250:
           монстр_kontrol=True
       if монстр_x <= -50:
           монстр_kontrol = False

       if монстр_kontrol==True:
           монстр_x_изменение = -8
#очередь событий
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()

           if event.type == pygame.KEYDOWN: #проверить, является ли полученное событие нажатием клавиши со стрелками, если да-получить код нажатой клавиш  и сформировать новые координаты

               if event.key == pygame.K_UP :
                   прыжок=True

               if event.key == pygame.K_RIGHT :
                   if левый==True:
                       x += персонаж_ширина / 2

                   if x < экрана_ширина - персонаж_ширина / 1.5:
                       action_скольжение_x = -speed

                   x_изменение = speed

               if event.key == pygame.K_LEFT:
                   if правый == True:
                       x -= персонаж_ширина/2

                   if x > персонаж_ширина / 2:

                       action_скольжение_x = speed


                   x_изменение = -speed

           if event.type == pygame.KEYUP:

               if event.key == pygame.K_UP :
                   action_скольжение_x=0
                   время_полета=0
                   прыжок=False


               if event.key == pygame.K_RIGHT:
                   action_скольжение_x = 0
                   x_изменение = 0
                   персонаж_yon=1
               if event.key == pygame.K_LEFT:
                   action_скольжение_x = 0
                   x_изменение = 0
                   персонаж_yon=0
        ################################






       if прыжок==True:
           статус_записи=21
           mod='Режим призрака (Примечание: в режиме призрака вы можете перемещаться по объектам)'
           прыжок_fonk()
           y-=10
       elif прыжок==False:
           статус_записи = 0
           mod = 'Ходьба (Примечание: вы можете перемещаться по объектам в режиме призрака)'

       if время_полета>=0.5:
           прыжок=False
       if раздел!=3:
           if правый==True and прыжок==False and раздел==1:
               if y + персонаж_высота + 18 >= rectangle1_y and y + персонаж_высота < rectangle1_y and (
                       x  <= rectangle1_x + rectangle_width and x + (
                       персонаж_ширина / 4) > rectangle1_x):
                   y_изменение = 0

               elif y + персонаж_высота + 18 >= rectangle1_y + 80 and y + персонаж_высота < rectangle1_y + 80 and (
                       x  <= rectangle1_x + 350 + rectangle_width and x + (
                       персонаж_ширина / 4) > rectangle1_x + 350):
                   y_изменение = 0

               elif y + персонаж_высота + 18 >= rectangle1_y + 240 and y + персонаж_высота < rectangle1_y + 240 and (
                       x  <= rectangle1_x + 800 + rectangle_width and x + (
                       персонаж_ширина / 4) > rectangle1_x + 800):
                   y_изменение = 0

               elif y + персонаж_высота + 18 >= rectangle1_y + 240 and y + персонаж_высота < rectangle1_y + 240 and (
                       x  <= rectangle1_x + 1500 + rectangle_width and x + (
                       персонаж_ширина / 4) > rectangle1_x + 1500):
                   y_изменение = 0

               elif y + персонаж_высота + 18 >= rectangle1_y + 80 and y + персонаж_высота < rectangle1_y + 80 and (
                       x  <= rectangle1_x + 1600 + rectangle_width and x + (
                       персонаж_ширина / 4) > rectangle1_x + 1600):
                   y_изменение = 0

               elif y + персонаж_высота + 18 >= rectangle1_y + 80-монстр_x/2 and y + персонаж_высота < rectangle1_y + 80-монстр_x/2 and (
                       x <= rectangle1_x + 1900 + rectangle_width and x + (
                       персонаж_ширина / 4) > rectangle1_x + 1900):
                   подъем_y=8
                   y_изменение = 0

               elif y + персонаж_высота + 18 >= rectangle1_y -150 and y + персонаж_высота < rectangle1_y -150 and (
                       x  <= rectangle1_x + 1400 + rectangle_width and x + (
                       персонаж_ширина / 4) > rectangle1_x + 1400):
                   y_изменение = 0

               else:
                   y_изменение += сила_тяжести
                   подъем_y = 0

           if левый==True and прыжок==False and раздел==1:
               if y + персонаж_высота + 18 >= rectangle1_y and y + персонаж_высота < rectangle1_y and (
                       x + (персонаж_ширина ) <= rectangle1_x + rectangle_width and x + (
                       персонаж_ширина ) > rectangle1_x):
                   y_изменение = 0

               elif y + персонаж_высота + 18 >= rectangle1_y + 80 and y + персонаж_высота < rectangle1_y + 80 and (
                       x + (персонаж_ширина ) <= rectangle1_x + 350 + rectangle_width and x + (
                       персонаж_ширина ) > rectangle1_x + 350):
                   y_изменение = 0

               elif y + персонаж_высота + 18 >= rectangle1_y + 240 and y + персонаж_высота < rectangle1_y + 240 and (
                       x + (персонаж_ширина ) <= rectangle1_x + 800 + rectangle_width and x + (
                       персонаж_ширина ) > rectangle1_x + 800):
                   y_изменение = 0

               elif y + персонаж_высота + 18 >= rectangle1_y + 240 and y + персонаж_высота < rectangle1_y + 240 and (
                       x + (персонаж_ширина ) <= rectangle1_x + 1500 + rectangle_width and x + (
                       персонаж_ширина ) > rectangle1_x + 1500):
                   y_изменение = 0

               elif y + персонаж_высота + 18 >= rectangle1_y + 80 and y + персонаж_высота < rectangle1_y + 80 and (
                       x + (персонаж_ширина ) <= rectangle1_x + 1600 + rectangle_width and x + (
                       персонаж_ширина ) > rectangle1_x + 1600):
                   y_изменение = 0

               elif y + персонаж_высота + 18 >= rectangle1_y + 80-монстр_x/2 and y + персонаж_высота < rectangle1_y + 80-монстр_x/2 and (
                       x + (персонаж_ширина ) <= rectangle1_x + 1900 + rectangle_width and x + (
                       персонаж_ширина ) > rectangle1_x + 1900):
                   подъем_y = 8
                   y_изменение = 0

               elif y + персонаж_высота + 18 >= rectangle1_y -150 and y + персонаж_высота < rectangle1_y -150 and (
                       x + (персонаж_ширина ) <= rectangle1_x + 1400 + rectangle_width and x + (
                       персонаж_ширина ) > rectangle1_x + 1400):
                   y_изменение = 0


               else:
                   y_изменение += сила_тяжести
                   подъем_y=0

           if правый == True and прыжок == False and раздел == 2:
                if y + персонаж_высота + 18 >= rectangle1_y  and y + персонаж_высота < rectangle1_y  and (
                        x <= rectangle1_x + rectangle_width and x + (
                        персонаж_ширина / 4) > rectangle1_x):
                    y_изменение = 0

                elif y + персонаж_высота + 18 >= rectangle1_y - 80 and y + персонаж_высота < rectangle1_y - 80 and (
                        x <= rectangle1_x + 350 + rectangle_width and x + (
                        персонаж_ширина / 4) > rectangle1_x + 350):
                    y_изменение = 0

                elif y + персонаж_высота + 18 >= rectangle1_y + 140 and y + персонаж_высота < rectangle1_y + 140 and (
                        x <= rectangle1_x + 600 + rectangle_width and x + (
                        персонаж_ширина / 4) > rectangle1_x + 600):
                    y_изменение = 0

                elif y + персонаж_высота + 18 >= rectangle1_y  and y + персонаж_высота < rectangle1_y  and (
                        x <= rectangle1_x + 900 + rectangle_width and x + (
                        персонаж_ширина / 4) > rectangle1_x + 900):
                    y_изменение = 0

                elif y + персонаж_высота + 18 >= rectangle1_y + 150 and y + персонаж_высота < rectangle1_y + 150 and (
                        x <= rectangle1_x + 1400 + rectangle_width and x + (
                        персонаж_ширина / 4) > rectangle1_x + 1400):
                    y_изменение = 0

                elif y + персонаж_высота + 18 >= rectangle1_y  -20 - монстр_x / 2 and y + персонаж_высота < rectangle1_y -20 - монстр_x / 2 and (
                        x <= rectangle1_x + 1900 + rectangle_width and x + (
                        персонаж_ширина / 4) > rectangle1_x + 1900):
                    подъем_y = 8
                    y_изменение = 0

                elif y + персонаж_высота + 18 >= rectangle1_y  and y + персонаж_высота < rectangle1_y  and (
                        x <= rectangle1_x + 1600 + rectangle_width and x + (
                        персонаж_ширина / 4) > rectangle1_x + 1600):
                    y_изменение = 0

                else:
                    y_изменение += сила_тяжести
                    подъем_y = 0

           if левый == True and прыжок == False and раздел == 2:
                if y + персонаж_высота + 18 >= rectangle1_y  and y + персонаж_высота < rectangle1_y  and (
                        x + (персонаж_ширина) <= rectangle1_x + rectangle_width and x + (
                        персонаж_ширина) > rectangle1_x):
                    y_изменение = 0

                elif y + персонаж_высота + 18 >= rectangle1_y - 80 and y + персонаж_высота < rectangle1_y - 80 and (
                        x + (персонаж_ширина) <= rectangle1_x + 350 + rectangle_width and x + (
                        персонаж_ширина) > rectangle1_x + 350):
                    y_изменение = 0

                elif y + персонаж_высота + 18 >= rectangle1_y + 140 and y + персонаж_высота < rectangle1_y + 440 and (
                        x + (персонаж_ширина) <= rectangle1_x + 600 + rectangle_width and x + (
                        персонаж_ширина) > rectangle1_x + 600):
                    y_изменение = 0

                elif y + персонаж_высота + 18 >= rectangle1_y  and y + персонаж_высота < rectangle1_y  and (
                        x + (персонаж_ширина) <= rectangle1_x + 900 + rectangle_width and x + (
                        персонаж_ширина) > rectangle1_x + 900):
                    y_изменение = 0

                elif y + персонаж_высота + 18 >= rectangle1_y + 150 and y + персонаж_высота < rectangle1_y + 150 and (
                        x + (персонаж_ширина) <= rectangle1_x + 1400 + rectangle_width and x + (
                        персонаж_ширина) > rectangle1_x + 1400):
                    y_изменение = 0

                elif y + персонаж_высота + 18 >= rectangle1_y  -20 - монстр_x / 2 and y + персонаж_высота < rectangle1_y -20 - монстр_x / 2 and (
                        x + (персонаж_ширина) <= rectangle1_x + 1900 + rectangle_width and x + (
                        персонаж_ширина) > rectangle1_x + 1900):
                    подъем_y = 8
                    y_изменение = 0

                elif y + персонаж_высота + 18 >= rectangle1_y  and y + персонаж_высота < rectangle1_y  and (
                        x + (персонаж_ширина) <= rectangle1_x + 1600 + rectangle_width and x + (
                        персонаж_ширина) > rectangle1_x + 1600):
                    y_изменение = 0


                else:
                    y_изменение += сила_тяжести
                    подъем_y = 0
            #############################
       rectangle1_x+=action_скольжение_x
       обьект_x+=action_скольжение_x
       y+= y_изменение-подъем_y
       x += x_изменение
       print(x,",",y)

       заднийфон_x+=action_скольжение_x
       монстр_x+=монстр_x_изменение





    ############################
       if раздел == 1:
           сила_тяжести=1
           экранаРазмер.blit(заднийфон, (заднийфон_x + action_скольжение_x, 0))
           if y <= 50 and round(x, -1) == 730:
               раздел = 2

               объявление("Глава 1 Завершена ! ")

           if enemy1_current_sprite < enemy1_max_sprite and kontrol==False:
               enemy1_current_sprite = enemy1_current_sprite+1

           if enemy1_current_sprite == enemy1_max_sprite:
               kontrol = True

           if kontrol==True:
               enemy1_current_sprite = enemy1_current_sprite - 1

           if enemy1_current_sprite == 0:
               kontrol = False



           rectangle(rectangle1_x, rectangle1_y, rectangle_width, rectangle_height, blue)
           rectangle(rectangle1_x+350, rectangle1_y+80, rectangle_width, rectangle_height, blue)
           rectangle(rectangle1_x + 800, rectangle1_y + 240, rectangle_width, rectangle_height, blue)
           rectangle(rectangle1_x + 1500, rectangle1_y + 240, rectangle_width, rectangle_height, blue)
           rectangle(rectangle1_x + 1600, rectangle1_y +80, rectangle_width, rectangle_height, blue)
           rectangle(rectangle1_x + 1900, rectangle1_y + 80-монстр_x/2, rectangle_width, rectangle_height, blue)
           rectangle(rectangle1_x + 1400, rectangle1_y -150 , rectangle_width, rectangle_height, blue)
           обьект(обьект_x,1)

           if  enemy1_current_sprite==0:
               экранаРазмер.blit(enemy1_1, (rectangle1_x + 830 + action_скольжение_x + монстр_x, rectangle1_y + 160))
           elif enemy1_current_sprite==1 :
               экранаРазмер.blit(enemy1_3, (rectangle1_x + 830 + action_скольжение_x + монстр_x, rectangle1_y + 160))



           if round(int(x), -2) == round(rectangle1_x + 830 + action_скольжение_x + монстр_x, -2) and round(int(y),-2) == round(rectangle1_y + 100, -2):
               can -= 1
               объявление('СМЕРТЬ')
               time.sleep(1)
               game_loop()


           сообщение("Mod : "+mod,280+статус_записи,20,black,16)

        ###ЛИЦО ПЕРСОНАЖА  ###
           if 0 < x_изменение:
               правый=True
               левый=False
               персонаж(x, y,True)
           elif  0 > x_изменение:
               левый=True
               правый=False
               персонаж(x, y, False)
           elif персонаж_yon==1:
               правый = True
               левый = False
               персонаж(x, y, True)
           elif персонаж_yon == 0:
               левый = True
               правый = False
               персонаж(x, y, False)
    ############################
       if раздел == 2:
           сила_тяжести=1
           экранаРазмер.blit(tas, (заднийфон_x + action_скольжение_x, 0))
           обьект(обьект_x, 2)
           if  y>=70 and round(x, -1) >= 1100:
               раздел = 3
               разделКонец()

               #########################################################


               fairy1("И старый волшебник остался проживать своей век с призраками ", экрана_ширина / 2, 200,white, 22)
               экранаРазмер.blit(ev, (экрана_ширина / 2 - 500, экрана_высота / 2 - 65))

           if enemy1_current_sprite < enemy1_max_sprite and kontrol == False:
               enemy1_current_sprite = enemy1_current_sprite + 1

           if enemy1_current_sprite == enemy1_max_sprite:
               kontrol = True

           if kontrol == True:
               enemy1_current_sprite = enemy1_current_sprite - 1

           if enemy1_current_sprite == 0:
               kontrol = False

           if раздел!=3:
               rectangle(rectangle1_x, rectangle1_y, rectangle_width, rectangle_height, blue)
               rectangle(rectangle1_x + 350, rectangle1_y + -80, rectangle_width, rectangle_height, blue)
               rectangle(rectangle1_x + 600, rectangle1_y + 140, rectangle_width, rectangle_height, blue)
               rectangle(rectangle1_x + 900, rectangle1_y , rectangle_width, rectangle_height, blue)
               rectangle(rectangle1_x + 1400, rectangle1_y + 150, rectangle_width, rectangle_height, blue)
               rectangle(rectangle1_x + 1900, rectangle1_y - 20 - монстр_x / 2, rectangle_width, rectangle_height,blue)
               rectangle(rectangle1_x + 1600, rectangle1_y , rectangle_width, rectangle_height, blue)




               if enemy1_current_sprite == 0:
                   экранаРазмер.blit(enemy1_1, (rectangle1_x + 1400 + action_скольжение_x + монстр_x, rectangle1_y + 55))
               elif enemy1_current_sprite == 1:
                   экранаРазмер.blit(enemy1_3, (rectangle1_x + 1400 + action_скольжение_x + монстр_x, rectangle1_y + 55))


               if enemy1_current_sprite == 0:
                   экранаРазмер.blit(enemy1_1, (rectangle1_x + 1130 + action_скольжение_x - монстр_x, rectangle1_y -100))
               elif enemy1_current_sprite == 1:
                   экранаРазмер.blit(enemy1_3, (rectangle1_x + 1130 + action_скольжение_x - монстр_x, rectangle1_y -100))

               сообщение("Mod : " + mod, 280 + статус_записи, 20, black, 16)

               ### персонаж ###
               if 0 < x_изменение:
                   правый = True
                   левый = False
                   персонаж(x, y, True)
               elif 0 > x_изменение:
                   левый = True
                   правый = False
                   персонаж(x, y, False)
               elif персонаж_yon == 1:
                   правый = True
                   левый = False
                   персонаж(x, y, True)
               elif персонаж_yon == 0:
                   левый = True
                   правый = False
                   персонаж(x, y, False)
               if round(int(x), -2) == round(rectangle1_x + 1404 + action_скольжение_x + монстр_x, -2) and round(int(y),
                                                                                                            -2) == round(
                       rectangle1_y + 20, -2):
                   can -= 1
                   объявление('смерть')
                   time.sleep(1)
                   game_loop()

               if round(int(x), -2) == round(rectangle1_x + 1134 + action_скольжение_x - монстр_x, -2) and round(int(y),
                                                                                                            -2) == round(
                       178, -2):
                   can -= 1
                   объявление('смерть')
                   time.sleep(1)
                   game_loop()


       if персонаж_sprite_number == персонаж_current_sprite:

           обратная_анимация=True

       if обратная_анимация==True and персонаж_current_sprite !=0:
           персонаж_current_sprite -=1
       else:
           персонаж_current_sprite+=1
           обратная_анимация=False

           ### Столкновение ###
       if y > экрана_высота:

           can -= 1
           объявление('ты ушел в пустоту')
           clock.sleep(1)
           game_loop()



           ###############################




       pygame.display.update()  # Если внутри ничего не написано, обновится вся поверхность 
       clock.tick(30)  # FPS


def объявление(text):
    font = pygame.font.Font('freesansbold.ttf', 96)
    fontRender = font.render( text, True, red)
    font_rect=fontRender.get_rect()
    font_rect.center=(экрана_ширина/2,экрана_высота/2)
    экранаРазмер.blit(fontRender,(font_rect))
    pygame.display.update()
    time.sleep(1)
    game_loop()

def сообщение(text,x,y,цвет,измерение):
    font = pygame.font.Font('freesansbold.ttf', измерение)
    fontRender = font.render( text, True, цвет)
    font_rect=fontRender.get_rect()
    font_rect.center=(x,y)
    экранаРазмер.blit(fontRender,(font_rect))

def fairy1(text,x,y,цвет,измерение):
    font = pygame.font.Font('freesansbold.ttf', измерение)
    fontRender = font.render( text, True, цвет)
    font_rect=fontRender.get_rect()
    font_rect.center=(x,y)
    экранаРазмер.blit(fontRender,(font_rect))

def раздел1():

    fairy1("Эндердаст : Начало", экрана_ширина / 2, экрана_высота / 2, red, 64)

    pygame.mixer.music.load('Musics\Deniz.mp3')
    pygame.display.update()  
    clock.tick(30)  # FPS
    time.sleep(0.5)
    text_counter = 0
    pygame.mixer.music.play(-1)

    while 1:

        экранаРазмер.blit(заднийфон_gece, (0, -50))


        экранаРазмер.blit(ot, (-20, экрана_высота - 200))
        экранаРазмер.blit(ot, (экрана_ширина - 50, экрана_высота - 200))

        ########################################################

        

        экранаРазмер.blit(ot, (-20, экрана_высота - 200))
        экранаРазмер.blit(ot, (экрана_ширина - 50, экрана_высота - 200))

        ########################################################

        ## ZEMlY DIZAYN ##
        экранаРазмер.blit(platform1_orta, (0, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (105, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (210, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (315, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (420, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (525, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (630, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (735, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (840, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (945, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (1050, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (1100, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (1175, экрана_высота - 130))

        экранаРазмер.blit(tas1, (-5, экрана_высота - 111))
        экранаРазмер.blit(tas1, (210, экрана_высота - 111))
        экранаРазмер.blit(tas1, (418, экрана_высота - 111))
        экранаРазмер.blit(tas1, (622, экрана_высота - 111))
        экранаРазмер.blit(tas1, (824, экрана_высота - 111))
        экранаРазмер.blit(tas1, (1026, экрана_высота - 111))
        экранаРазмер.blit(tas1, (1218, экрана_высота - 111))

        экранаРазмер.blit(срез_дерево, (150, экрана_высота - 172))
        #########################################################
        ## fairy ##
        if text_counter == 0:
            экранаРазмер.blit(котел, (экрана_ширина / 2 - 100, экрана_высота - 210))
            экранаРазмер.blit(ведьма, (экрана_ширина / 2 - 200, экрана_высота / 2 + 100))
            fairy1("Когда мир только начал знакомиться с волшебством(нажмите пробел)", экрана_ширина / 2, 200, white, 22)

        elif text_counter == 1:
            экранаРазмер.blit(ведьма, (экрана_ширина / 2 - 200, экрана_высота / 2 + 100))
            экранаРазмер.blit(котел, (экрана_ширина / 2 - 100, экрана_высота - 210))
            fairy1("Волшебник попытался взять сил у самого древнего древа", экрана_ширина / 2,200, white, 22)

        elif text_counter == 2:
            экранаРазмер.blit(ведьма, (экрана_ширина / 2 - 200, экрана_высота / 2 + 100))
            экранаРазмер.blit(котел, (экрана_ширина / 2 - 100, экрана_высота - 210))
            fairy1("Но ничего не вышло...", экрана_ширина / 2, 200, white, 22)
            экранаРазмер.blit(взрыв, (экрана_ширина / 2 - 150, экрана_высота/2))

        elif text_counter == 3:
            экранаРазмер.blit(ведьма, (экрана_ширина / 2 - 200, экрана_высота / 2 + 100))
            fairy1("И неожиданно открылся портал", экрана_ширина / 2, 200, white, 22)
            экранаРазмер.blit(portal, (экрана_ширина / 2 +300, экрана_высота / 2))

        elif text_counter == 4:
            экранаРазмер.blit(ведьма, (экрана_ширина / 2 - 200, экрана_высота / 2 + 100))
            fairy1("Волшебник осознал, что что-то пошло не так, но было уже поздно...", экрана_ширина / 2, 200, white, 22)
            экранаРазмер.blit(portal, (экрана_ширина / 2 + 300, экрана_высота / 2))
            экранаРазмер.blit(персонаж_перв, (экрана_ширина / 2 + 250, экрана_высота / 2+170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина/ 2 + 280, экрана_высота / 2 + 165))
            экранаРазмер.blit(персонаж_перв, (экрана_ширина / 2 + 180, экрана_высота / 2 + 170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 210, экрана_высота / 2 + 165))
            экранаРазмер.blit(персонаж_перв, (экрана_ширина / 2 + 320, экрана_высота / 2 + 170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 350, экрана_высота / 2 + 165))

        elif text_counter == 5:
            экранаРазмер.blit(ведьма, (экрана_ширина / 2 - 200, экрана_высота / 2 + 100))
            fairy1("И из портала вышли маленькие магические призраки", экрана_ширина/ 2, 200, white,22)
            экранаРазмер.blit(portal, (экрана_ширина / 2 + 300, экрана_высота / 2))
            экранаРазмер.blit(персонаж_перв, (экрана_ширина / 2 + 250, экрана_высота / 2 + 170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 280, экрана_высота / 2 + 165))
            экранаРазмер.blit(персонаж_перв, (экрана_ширина / 2 + 180, экрана_высота / 2 + 170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 210, экрана_высота / 2 + 165))
            экранаРазмер.blit(персонаж_перв, (экрана_ширина / 2 + 320, экрана_высота / 2 + 170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 350, экрана_высота / 2 + 165))

        elif text_counter == 6:

            fairy1("Колдун открыл призракам свое дом и приютил их",экрана_ширина / 2, 200, white, 22)
            экранаРазмер.blit(ev, (экрана_ширина / 2-500 , экрана_высота / 2-65))

        elif text_counter == 7:
            экранаРазмер.blit(ведьма, (экрана_ширина / 2 , экрана_высота / 2 + 100))
            экранаРазмер.blit(ev, (экрана_ширина / 2 - 500, экрана_высота / 2 - 65))
            экранаРазмер.blit(котел, (экрана_ширина / 2 + 100, экрана_высота - 210))
            fairy1("Вошлебник, который хотел возрадить силу волшебного леса, провел эксперимент", экрана_ширина / 2, 200, white,22)
            экранаРазмер.blit(персонаж_перв, (экрана_ширина / 2 + 250, экрана_высота / 2 + 170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 280, экрана_высота / 2 + 165))
            экранаРазмер.blit(персонаж_перв, (экрана_ширина / 2 + 180, экрана_высота / 2 + 170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 210, экрана_высота / 2 + 165))
            экранаРазмер.blit(персонаж_перв, (экрана_ширина / 2 + 320, экрана_высота / 2 + 170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 350, экрана_высота / 2 + 165))

        elif text_counter == 8:
            экранаРазмер.blit(ведьма, (экрана_ширина / 2 , экрана_высота / 2 + 100))
            экранаРазмер.blit(ev, (экрана_ширина/ 2 - 500, экрана_высота / 2 - 65))
            экранаРазмер.blit(котел, (экрана_ширина / 2 + 100, экрана_высота - 210))
            fairy1("Но один из призраков помешал эксперименту", экрана_ширина / 2, 200, white,22)
            экранаРазмер.blit(персонаж_перв, (экрана_ширина / 2 + 250, экрана_высота / 2 + 170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 280, экрана_высота / 2 + 165))
            экранаРазмер.blit(персонаж_перв, (экрана_ширина/ 2 + 180, экрана_высота / 2 + 170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 210, экрана_высота / 2 + 165))
            экранаРазмер.blit(персонаж_перв, (экрана_ширина / 2 + 320, экрана_высота / 2 + 170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 350, экрана_высота / 2 + 165))
            экранаРазмер.blit(взрыв, (экрана_ширина / 2 + 50, экрана_высота / 2))

        elif text_counter == 9:
            экранаРазмер.blit(ведьма, (экрана_ширина / 2 , экрана_высота / 2 + 100))
            экранаРазмер.blit(ev, (экрана_ширина / 2 - 500, экрана_высота / 2 - 65))
            экранаРазмер.blit(котел, (экрана_ширина / 2 + 100, экрана_высота - 210))
            fairy1("И это порадило стаю крылатых демонов", экрана_ширина / 2, 200, white,22)
            экранаРазмер.blit(персонаж_перв, (экрана_ширина / 2 + 250, экрана_высота / 2 + 170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 280, экрана_высота / 2 + 165))
            экранаРазмер.blit(персонаж_перв, (экрана_ширина / 2 + 180, экрана_высота / 2 + 170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 210, экрана_высота / 2 + 165))
            экранаРазмер.blit(персонаж_перв, (экрана_ширина / 2 + 320, экрана_высота / 2 + 170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 350, экрана_высота / 2 + 165))
            экранаРазмер.blit(взрыв, (экрана_ширина / 2 + 50, экрана_высота / 2))
            экранаРазмер.blit(portal, (экрана_ширина / 2 + 400, экрана_высота / 2))
            экранаРазмер.blit(enemy1_1, (экрана_ширина / 2 + 300, экрана_высота / 2))
            экранаРазмер.blit(enemy1_3, (экрана_ширина / 2 + 420, экрана_высота / 2+50))

        elif text_counter == 10:
            экранаРазмер.blit(ведьма, (экрана_ширина / 2 , экрана_высота / 2 + 100))
            экранаРазмер.blit(ev, (экрана_ширина/ 2 - 500, экрана_высота / 2 - 65))
            экранаРазмер.blit(котел, (экрана_ширина / 2 + 100, экрана_высота - 210))
            fairy1("У волшебника не было выбора и отправил остальных призраков исправлять свои ошибки", экрана_ширина / 2, 200, white,22)
            экранаРазмер.blit(персонаж_перв, (экрана_ширина / 2 + 350, экрана_высота / 2 + 170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 380, экрана_высота / 2 + 165))
            экранаРазмер.blit(персонаж_перв, (экрана_ширина / 2 + 280, экрана_высота / 2 + 170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 310, экрана_высота / 2 + 165))
            экранаРазмер.blit(персонаж_перв, (экрана_ширина / 2 + 420, экрана_высота / 2 + 170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 450, экрана_высота / 2 + 165))
            экранаРазмер.blit(portal, (экрана_ширина / 2 + 400, экрана_высота / 2))
            экранаРазмер.blit(enemy1_3, (экрана_ширина / 2 + 330, экрана_высота / 2+20))
            экранаРазмер.blit(enemy1_1, (экрана_ширина / 2 + 450, экрана_высота / 2+30))

        elif text_counter == 11:
            экранаРазмер.blit(ведьма, (экрана_ширина / 2 , экрана_высота / 2 + 100))
            экранаРазмер.blit(ev, (экрана_ширина / 2 - 500, экрана_высота / 2 - 65))
            экранаРазмер.blit(котел, (экрана_ширина / 2 + 100, экрана_высота - 210))
            fairy1("призраки остались предоставлены своей судьбе", экрана_ширина / 2, 200, white,22)
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 450, экрана_высота / 2 +200))


        elif text_counter == 12:
            game_loop()
        ###############################################################

        pygame.display.update()  # Если в нем ничего не будет написано, он обновит всю поверхность
        clock.tick(30)  # FPS




        ### ПРОБЛЕМА ДВИЖЕНИЯ ###

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    экранаРазмер.blit(заднийфон_gece, (0, -50))



                    ## ПОЛ ТАКОЙ ЖЕ ##
                    экранаРазмер.blit(platform1_orta, (0, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (105, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (210, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (315, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (420, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (525, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (630, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (735, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (840, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (945, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (1050, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (1100, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (1175, экрана_высота - 130))

                    экранаРазмер.blit(tas1, (-5, экрана_высота - 111))
                    экранаРазмер.blit(tas1, (210, экрана_высота - 111))
                    экранаРазмер.blit(tas1, (418, экрана_высота - 111))
                    экранаРазмер.blit(tas1, (622, экрана_высота - 111))
                    экранаРазмер.blit(tas1, (824, экрана_высота - 111))
                    экранаРазмер.blit(tas1, (1026, экрана_высота - 111))
                    экранаРазмер.blit(tas1, (1218, экрана_высота - 111))

                    экранаРазмер.blit(срез_дерево, (150, экрана_высота - 172))
                    #########################################################

                    экранаРазмер.blit(ведьма, (экрана_ширина / 2 - 200, экрана_высота / 2 + 100))

                    text_counter+=1


                if event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_LEFT:
                    pass

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_UP:
                    pass

                if event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_LEFT:
                    pass

        ################################


def разделКонец():
    pygame.mixer.music.load(r'Musics\twist.mp3')
    pygame.mixer.music.play(-1)
    text_counter = 0

    while 1:

        экранаРазмер.blit(заднийфон_gece, (0, -50))

        экранаРазмер.blit(ot, (-20, экрана_высота - 200))
        экранаРазмер.blit(ot, (экрана_ширина - 50, экрана_высота - 200))

        ########################################################

        ## zemlya##
        экранаРазмер.blit(platform1_orta, (0, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (105, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (210, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (315, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (420, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (525, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (630, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (735, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (840, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (945, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (1050, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (1100, экрана_высота - 130))
        экранаРазмер.blit(platform1_orta, (1175, экрана_высота - 130))

        экранаРазмер.blit(tas1, (-5, экрана_высота - 111))
        экранаРазмер.blit(tas1, (210, экрана_высота - 111))
        экранаРазмер.blit(tas1, (418, экрана_высота - 111))
        экранаРазмер.blit(tas1, (622, экрана_высота - 111))
        экранаРазмер.blit(tas1, (824, экрана_высота - 111))
        экранаРазмер.blit(tas1, (1026, экрана_высота - 111))
        экранаРазмер.blit(tas1, (1218, экрана_высота - 111))

        экранаРазмер.blit(срез_дерево, (150, экрана_высота - 172))


        экранаРазмер.blit(ev, (экрана_ширина / 2 - 500, экрана_высота / 2 - 65))






        #########################################################
        ## СКАЗКА  ##
        if text_counter == 0:
            экранаРазмер.blit(ведьма, (экрана_ширина / 2 -100, экрана_высота / 2 + 100))
            экранаРазмер.blit(portal, (экрана_ширина / 2 + 300, экрана_высота / 2))
            экранаРазмер.blit(персонаж_перв, (экрана_ширина / 2 + 250, экрана_высота / 2 + 170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 280, экрана_высота / 2 + 165))
            экранаРазмер.blit(персонаж_перв, (экрана_ширина / 2 + 200, экрана_высота / 2 + 170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 230, экрана_высота / 2 + 165))

            fairy1("Старый волшебник был очень рад видеть призраков, своих бесплотных помошников, которым удалось выбраться из портала", экрана_ширина / 2, 200, white, 22)

        elif text_counter == 1:
            экранаРазмер.blit(ведьма, (экрана_ширина / 2 + 100, экрана_высота / 2 + 100))
            экранаРазмер.blit(персонаж_перв, (экрана_ширина / 2 + 150, экрана_высота / 2 + 170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 180, экрана_высота / 2 + 165))
            экранаРазмер.blit(персонаж_перв, (экрана_ширина / 2 + 80, экрана_высота / 2 + 170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 110, экрана_высота / 2 + 165))
            экранаРазмер.blit(персонаж_перв, (экрана_ширина / 2 + 220, экрана_высота / 2 + 170))
            экранаРазмер.blit(персонаж_второй, (экрана_ширина / 2 + 250, экрана_высота / 2 + 165))
            fairy1("И жили они долго и счастливо ...", экрана_ширина / 2,200, white, 22)

        elif text_counter == 2:

            fairy1("", экрана_ширина / 2, 200, white, 22)


        elif text_counter == 3:
            fairy1("Игру написал: Кузьменок Вячеслав 09-02",экрана_ширина / 2, 200, white, 22)

        elif text_counter == 4:
            fairy1("", экрана_ширина / 2, 200,white, 22)

        elif text_counter == 5:
            quit()
            exit()

        pygame.display.update()  #Если внутри ничего не написано, обновится вся поверхность 
        clock.tick(30)  # FPS

        ###ПРОБЛЕМЫ ДВИЖЕНИЯ  ###

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    экранаРазмер.blit(заднийфон_gece, (0, -50))

                    ## ДИЗАЙН ЗЕМЛИ  ##
                    экранаРазмер.blit(platform1_orta, (0, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (105, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (210, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (315, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (420, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (525, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (630, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (735, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (840, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (945, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (1050, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (1100, экрана_высота - 130))
                    экранаРазмер.blit(platform1_orta, (1175, экрана_высота - 130))

                    экранаРазмер.blit(tas1, (-5, экрана_высота - 111))
                    экранаРазмер.blit(tas1, (210, экрана_высота - 111))
                    экранаРазмер.blit(tas1, (418, экрана_высота - 111))
                    экранаРазмер.blit(tas1, (622, экрана_высота - 111))
                    экранаРазмер.blit(tas1, (824, экрана_высота - 111))
                    экранаРазмер.blit(tas1, (1026, экрана_высота - 111))
                    экранаРазмер.blit(tas1, (1218, экрана_высота - 111))

                    экранаРазмер.blit(срез_дерево, (150, экрана_высота - 172))
                    #########################################################

                    экранаРазмер.blit(ведьма, (экрана_ширина / 2 - 200, экрана_высота / 2 + 100))

                    text_counter+=1

раздел1()
pygame.quit()
quit()
