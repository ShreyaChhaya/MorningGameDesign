#shreya Chhaya
#final project code - sky burger adaptation
#functions
#Game1()
#game2()

# #shreyaChhaya
# #6/9/2022
# #We are learning pygame basic functins, 
# # creating screens, clrs, shape ,move 
# # move  the square
# # K_UP                  up arrow
# # K_DOWN                down arrow
# # K_RIGHT               right arrow
# # K_LEFT                left arrow
# #picture = pygame. image. load(filename)
# #picture = pygame. transform. scale(picture, (1280, 720))
# #bg=pygame.image.load('ClassStuff\CircleEatsSquare\Images\\bgSmaller.jpg')


from operator import truediv
from subprocess import HIGH_PRIORITY_CLASS
import sys
import pygame, time, os,random, math, datetime
date=datetime.datetime.now()
from pygame import mixer
from pygame.locals import*
pygame.init()#initialize the pygame package

os.system('cls')
WIDTH=700 #like constant
HEIGHT=600
clock=pygame.time.Clock()

menuColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//30)
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51), 'red':(255, 0, 0), 'purple': (138,43,226), 'yellow':(255,215,0), 'black':(0,0,0), 'lblue':(0,206,209)}

message=['Instructions', 'Settings', 'Game 1', 'Game 2', 'Scoreboard', 'Exit']
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game")  #change the title of my window


#background music
# mixer.music.load('background (1).wav')
# mixer.music.play(-1)

#boxes for menu
Bx=WIDTH/2.5
Button_menu=pygame.Rect(Bx, 125, WIDTH/4, 40)
Button_instruct=pygame.Rect(Bx, 150, WIDTH//4, 40)
Button_settings=pygame.Rect(Bx, 200, WIDTH/4, 40)
Button_Game1=pygame.Rect(Bx, 250, WIDTH/4, 40)
Button_Game2=pygame.Rect(Bx, 300, WIDTH/4, 40)
Button_score=pygame.Rect(Bx, 350, WIDTH/4, 40)
Button_exit=pygame.Rect(Bx, 400, WIDTH/4, 40)
#images
bg=pygame.image.load('PygameFiles\images\\bgSmaller.jpg')
char = pygame.image.load('PygameFiles\images\PixelArtTutorial.png')
char = pygame.transform.scale(char, (50, 50))
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)

mx = 0
my = 0


def mainMenu():
    global menuColor
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_settings)
    Title = TITLE_FONT.render("Circle eats Square Menu", 1, colors.get("blue"))
    screen.fill(menuColor)
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    yMenu=150
    
    for item in message:
        Button_menu=pygame.Rect(WIDTH/2.5, yMenu, WIDTH/4, 40)
        text=MENU_FONT.render(item, 1, colors.get('blue'))
        pygame.draw.rect(screen, colors.get('limeGreen'), Button_menu)
        screen.blit(text, (WIDTH/2.5, yMenu))
        pygame.display.update()
        pygame.time.delay(50)
        yMenu += 50
    MENU=True
    while MENU:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                print("You quit")
                pygame.display.quit()
                MENU=False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_instruct.collidepoint((mx, my)):
                    Instructions()
                if Button_settings.collidepoint((mx, my)):
                    settings()
                if Button_Game1.collidepoint((mx, my)):
                    Game_1()
                if Button_score.collidepoint((mx, my)):
                    scoreboard()
                if Button_exit.collidepoint((mx, my)):
                    exit()
                if Button_Game2.collidepoint((mx, my)):
                    Game_2()


    
def Instructions():
    #rendering text objects
    Title = TITLE_FONT.render("Instructions", 1, colors.get("blue"))
    text = MENU_FONT.render('Return to Menu', 1, colors.get('blue'))

    #fills screen with white
    screen.fill(menuColor)

    #creating button options
    Button_1 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_1)

    #Instructions
    myFile = open("PygameFiles\instructions.txt", "r")
    content = myFile.readlines()

    #var to controll change of line
    yinstructions = 150
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yinstructions))
        pygame.display.update()
        pygame.time.delay(50)
        yinstructions += 40

    myFile.close()

    #renderig fonts to the screen
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    screen.blit(text, (WIDTH//17,HEIGHT/1.1))

    pygame.display.update()
    Instructions = True
    while Instructions:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Instructions=False
                mainMenu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint((mx, my)):
                    mainMenu() 


def settings():
    global menuColor
    global screen 
    global WIDTH
    global HEIGHT
    title=TITLE_FONT.render('Settings', 1, colors.get('blue'))
    text=MENU_FONT.render('Return to Menu', 1, colors.get('blue'))

    screen.fill(menuColor)

    color=MENU_FONT.render('Change Background Color:', 1, colors.get('blue'))
    screen.blit(color, (WIDTH/18, HEIGHT/4))
    pygame.display.update()
    pygame.time.delay(50)
    
    
#changing color random
    Button_color = pygame.Rect(WIDTH/21, HEIGHT/3, WIDTH//3.8, 40)
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_color)

    textcolor = MENU_FONT.render('Random', 1, colors.get('blue'))
    screen.blit(textcolor, (WIDTH/20, HEIGHT/3))
#back to menu
    Button_3 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)

    #buttons for size changing 
    Button_4=pygame.Rect(WIDTH/20, HEIGHT/1.8, WIDTH//7, 40)
    Button_5=pygame.Rect(WIDTH/4, HEIGHT/1.8, WIDTH//5, 40)
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_4)
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_5)

    #buttons for sound
    Button_on=pygame.Rect(WIDTH/20, HEIGHT/1.3, WIDTH//6, 40)
    Button_off=pygame.Rect(WIDTH/3, HEIGHT/1.3, WIDTH//6, 40)
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_on)
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_off)

    #text for buttons/screen
    screen.blit(title, (WIDTH/2.5,50))
    screen.blit(text, (WIDTH//18, HEIGHT/1.1))
    text5=MENU_FONT.render('UP 100', 1, colors.get('blue'))
    text6=MENU_FONT.render('DOWN 100', 1, colors.get('blue'))
    screen.blit(text5, (WIDTH/18, HEIGHT/1.8))
    screen.blit(text6, (WIDTH/4, HEIGHT/1.8))
    
    text7=MENU_FONT.render('Sound On', 1, colors.get('blue'))
    text8=MENU_FONT.render('Sound Off', 1, colors.get('blue'))
    screen.blit(text7, (WIDTH/18, HEIGHT/1.3))
    screen.blit(text8, (WIDTH/3, HEIGHT/1.3))
    text10=MENU_FONT.render('Change screen size:', 1, colors.get('blue'))
    text11=MENU_FONT.render('Change sound settings:', 1, colors.get('blue'))
    screen.blit(text10, (WIDTH/18, HEIGHT/2.1))
    screen.blit(text11, (WIDTH/18, HEIGHT/1.5))
    pygame.display.update()

    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                mainMenu()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                #button for menu
                if Button_3.collidepoint((mx, my)):
                    mainMenu()
                    #button for color
                if Button_color.collidepoint((mx, my)):
                    menuColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                    print("change color")
                    pygame.display.update()
                    settings()
                    #buttons for sound
                if Button_on.collidepoint((mx,my)):
                    mixer.music.play(-1)
                    print("music on")
                if Button_off.collidepoint((mx,my)):
                    mixer.music.stop()
                    print("music off")
                    #buttons for sizing
                if Button_4.collidepoint((mx,my)) and WIDTH <1000 and HEIGHT<1000:
                    WIDTH +=100
                    HEIGHT +=100
                    screen=pygame.display.set_mode((WIDTH, HEIGHT))
                    settings()
                if Button_5.collidepoint((mx,my)) and WIDTH>600 and HEIGHT>600:
                    WIDTH -=100
                    HEIGHT -=100
                    screen=pygame.display.set_mode((WIDTH, HEIGHT))
                    settings()
            pygame.display.update()


def scoreboard():
    high=0
    title=TITLE_FONT.render('Scoreboard', 1, colors.get('blue'))
    text3 = MENU_FONT.render("Return to Menu", 1, colors.get("blue"))

    screen.fill(menuColor)
    Button_3 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    
    screen.blit(title, (WIDTH//3,50))
    screen.blit(text3, (WIDTH//17, HEIGHT/1.1))
    pygame.display.update()
    
    
    print(score)
    # if score>high:
    #     high=score
    # scrLine=str(high)+"\t " (':')+ "\t" +date.strftime('%m/%d/%Y')+ "\n"
    scrLine=str(score)+(': ')+ '\t'+ userName+ "\t"+date.strftime("%m-%d-%Y")+ "\n"
    myFile = open("PygameFiles\scoreboard.txt", "a")
    myFile.write(str(scrLine))
    myFile.close()

    myFile=open('pygameFiles\scoreboard.txt', 'r')
    content = myFile.readlines()

    #var to controll change of line
    yscore = 150
    for lines in content:
        Instruc = MENU_FONT.render(lines[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yscore))
        pygame.display.update()
        pygame.time.delay(50)
        yscore += 40

    myFile.close()

    scoreboard=True
    while scoreboard:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                mainMenu()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_3.collidepoint((mx, my)):
                    mainMenu()

def exit():
    title=TITLE_FONT.render('Bye-Bye!', 1, colors.get('blue'))
    screen.fill(menuColor)

    screen.blit(title, (WIDTH/2.5, HEIGHT/2.5))
    pygame.display.update()

    pygame.time.delay(1000)
    pygame.display.quit()


def Game_1():
    #game over after top bun caught
    def gameOver():
        screen.fill(colors.get('black'))

        #button to return to menu
        title=TITLE_FONT.render('GAME OVER', 1, colors.get('blue'))
        screen.blit(title, (WIDTH/3, HEIGHT/3))
        #text for score - add sore inwhen game complete
        scoretext=MENU_FONT.render('Your score is '+str(score), 1, colors.get('blue'))
        screen.blit(scoretext, (WIDTH/3, HEIGHT/2))
        ButtonBack1 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
        pygame.draw.rect(screen, colors.get("limeGreen"), ButtonBack1)
        #return to menu text 
        text=MENU_FONT.render('Return to Menu', 1, colors.get('blue'))
        screen.blit(text, (WIDTH/18, HEIGHT/1.1))
        pygame.display.update()

        over=True
        while over:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    over=False
                    mainMenu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    mx = mousePos[0]
                    my = mousePos[1]
                    if ButtonBack1.collidepoint((mx, my)):
                        mainMenu() 

    #define/globalize variables
    global WIDTH, score, tomato_y, tomato_x, char, bunx, buny, pickle_x, pickle_y, patty_y, patty_x, onion_x, onion_y, mustard_x, mustard_y, lettuce_x, lettuce_y, ketchup_x, ketchup_y, cheese_x, cheese_y
    global HEIGHT
    speed=5
    toppingSpeed=3
    tomato_y=360
    tomato_x = 360
    patty_x=436
    patty_y=200
    onion_x=564
    onion_y=0
    mustard_x=125
    mustard_y=-50
    lettuce_x=330
    lettuce_y=26
    ketchup_x=520
    ketchup_y=660
    cheese_x=260
    cheese_y=144
    bunx=0
    buny=0
    img_y=0
    img_x=0
    pickle_y=50
    pickle_x=50
    chary=HEIGHT/1.1
    screen= pygame.display.set_mode((WIDTH,HEIGHT))
    charx=100
    wb=100
    score = 0 

    #get all images for toppings
    topBun=pygame.image.load('pygameFiles\Images\\burger toppings\\top bun.png')

    tomato=pygame.image.load('pygameFiles\Images\\burger toppings\\tomato.png')
    pickles=pygame.image.load('pygameFiles\Images\\burger toppings\pickles.png')
    patty=pygame.image.load('pygameFiles\Images\\burger toppings\patty.png')
    onion=pygame.image.load('pygameFiles\Images\\burger toppings\onion.png')
    mustard=pygame.image.load('pygameFiles\Images\\burger toppings\mustard.png')
    lettuce=pygame.image.load('pygameFiles\Images\\burger toppings\lettuce.png')
    ketchup=pygame.image.load('pygameFiles\Images\\burger toppings\ketchup.png')
    cheese=pygame.image.load('pygameFiles\Images\\burger toppings\cheese.png')

    #list of toppings
    imgInf=[tomato, pickles, patty, onion, mustard, lettuce, ketchup, cheese]
    row_count = 0
    # for img in imgInf:
    #     imgRect=img.get_rect()
    #     imgRect.x=0
    #     imgRect.y=-10
    #     tile = (img, imgRect)
    #     imgInf.append(tile)

    #separate rectangle for top bun
    topBun=pygame.transform.scale(topBun, (100,50))
    rectBun=topBun.get_rect()
    rectBun.center=WIDTH//2,HEIGHT//2
    screen.blit(topBun, rectBun)
    screen.blit(topBun, (WIDTH//2, HEIGHT//2))

    #rect and character tomato
    tomato = pygame.transform.scale(tomato, (100,50)) #tomato
    Trect= tomato.get_rect() #tomato
    Trect.center = WIDTH//2, HEIGHT//2 #tomao
    screen.blit(tomato, Trect) #tomato

    #pickles rectangle
    pickles=pygame.transform.scale(pickles, (100,50))
    rectPic=pickles.get_rect()
    rectPic.center=WIDTH//2,HEIGHT//2
    screen.blit(pickles, rectPic)
    screen.blit(pickles, (WIDTH//2, HEIGHT//2))

    #patty rectangle
    patty=pygame.transform.scale(patty, (100,50))
    rectPat=patty.get_rect()
    rectPat.center=WIDTH//2,HEIGHT//2
    screen.blit(patty, rectPat)
    screen.blit(patty, (WIDTH//2, HEIGHT//2))

    #onion rect
    onion=pygame.transform.scale(onion, (100,50))
    rectOn=topBun.get_rect()
    rectOn.center=WIDTH//2,HEIGHT//2
    screen.blit(onion, rectOn)
    screen.blit(onion, (WIDTH//2, HEIGHT//2))

    #mustard 
    mustard = pygame.transform.scale(mustard, (100,50)) 
    rectMus= mustard.get_rect() 
    rectMus.center = WIDTH//2, HEIGHT//2
    screen.blit(mustard, rectMus) 
    screen.blit(mustard, (WIDTH//2, HEIGHT//2))

    #lettuce
    lettuce = pygame.transform.scale(lettuce, (100,50)) 
    rectLet= lettuce.get_rect() 
    rectLet.center = WIDTH//2, HEIGHT//2
    screen.blit(lettuce, rectLet) 
    screen.blit(lettuce, (WIDTH//2, HEIGHT//2))

    #ketchup 
    ketchup = pygame.transform.scale(ketchup, (100,50)) 
    rectKet= ketchup.get_rect() 
    rectKet.center = WIDTH//2, HEIGHT//2
    screen.blit(ketchup, rectKet) 
    screen.blit(ketchup, (WIDTH//2, HEIGHT//2))

    #cheese
    cheese = pygame.transform.scale(cheese, (100,50)) 
    rectCh= cheese.get_rect() 
    rectCh.center = WIDTH//2, HEIGHT//2
    screen.blit(cheese, rectCh) 
    screen.blit(cheese, (WIDTH//2, HEIGHT//2))

    rectList=[Trect, rectPic, rectPat, rectOn, rectMus, rectLet, rectKet, rectCh]

    #background
    bg=pygame.image.load('pygameFiles\Images\\backgroundlevel1.jpg')
    bg=pygame.transform.scale(bg, (WIDTH, HEIGHT))

    #character bottom bun/rect for it
    char = pygame.image.load('pygameFiles\Images\\burger toppings\\bottom bun cropped (2).png')
    char = pygame.transform.scale(char, (100, 50))
    rect= char.get_rect()
    rect.center = WIDTH//2, HEIGHT/1.05
    screen.blit(char, rect)
    pygame.draw.rect(screen, colors.get('white'), rect, 1)
    screen.blit(char, (WIDTH/2.5,HEIGHT/1.1))
    pygame.display.update()



    #game loop
    game1=True
    while game1:
        #quit
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game1=False
                mainMenu()

        #move character
        keys = pygame.key.get_pressed() #allow us to see what key was pressed
        if keys[pygame.K_RIGHT] and charx < WIDTH-wb:
            charx += speed
        if keys[pygame.K_LEFT] and charx > 0:
            charx -= speed
        rect.x=charx
        screen.blit(bg, (0,0))
        screen.blit(char, (charx,HEIGHT/1.1))
        screen.blit(tomato, (tomato_x,tomato_y))
        screen.blit(topBun, (bunx, buny))
        screen.blit(pickles, (pickle_x, pickle_y))
        screen.blit(patty, (patty_x, patty_y))
        screen.blit(onion, (onion_x, onion_y))
        screen.blit(mustard, (mustard_x, mustard_y))
        screen.blit(lettuce, (lettuce_x, lettuce_y))
        screen.blit(ketchup, (ketchup_x, ketchup_y))
        screen.blit(cheese, (cheese_x, cheese_y))
        

        #if bun collides with tomato
        if not rect.colliderect(Trect):
            tomato_y = tomato_y+toppingSpeed
            Trect.y= Trect.y+toppingSpeed
        if tomato_y > HEIGHT:
            tomato_x=random.randrange(0, WIDTH-50)
            tomato_y=-100 
        Trect.x= tomato_x
        Trect.y=tomato_y
        rect.y=chary
        if rect.colliderect(Trect):
            tomato_x=charx
            tomato_y=chary-20
            score+=1

        #pickles collidepoint
        if not rect.colliderect(rectPic):
            pickle_y = pickle_y+toppingSpeed
            rectPic.y= rectPic.y+toppingSpeed
        if pickle_y > HEIGHT:
            pickle_x=random.randrange(0, WIDTH-50)
            pickle_y=-100 
        rectPic.x= pickle_x
        rectPic.y=pickle_y
        if rect.colliderect(rectPic):
            pickle_x=charx
            pickle_y=chary-20
            score+=1

        #patty
        if not rect.colliderect(rectPat):
            patty_y = patty_y+toppingSpeed
            rectPat.y= rectPat.y+toppingSpeed
        if patty_y > HEIGHT:
            patty_x=random.randrange(0, WIDTH-50)
            patty_y=-100 
        rectPat.x= patty_x
        rectPat.y=patty_y
        if rect.colliderect(rectPat):
            patty_x=charx
            patty_y=chary-20
            score+=1
        #onion
        if not rect.colliderect(rectOn):
            onion_y = onion_y+toppingSpeed
            rectOn.y= rectOn.y+toppingSpeed
        if onion_y > HEIGHT:
            onion_x=random.randrange(0, WIDTH-50)
            onion_y=-100 
        rectOn.x= onion_x
        rectOn.y=onion_y
        if rect.colliderect(rectOn):
            onion_x=charx
            onion_y=chary-20
            score+=1
        #mustard
        if not rect.colliderect(rectMus):
            mustard_y = mustard_y+toppingSpeed
            rectMus.y= rectMus.y+toppingSpeed
        if pickle_y > HEIGHT:
            mustard_x=random.randrange(0, WIDTH-50)
            mustard_y=-100 
        rectMus.x= patty_x
        rectMus.y=patty_y
        if rect.colliderect(rectMus):
            mustard_x=charx
            mustard_y=chary-20
            score+=1
        #lettuce
        if not rect.colliderect(rectLet):
            lettuce_y = lettuce_y+toppingSpeed
            rectLet.y= rectLet.y+toppingSpeed
        if lettuce_y > HEIGHT:
            lettuce_x=random.randrange(0, WIDTH-50)
            lettuce_y=-100 
        rectLet.x= lettuce_x
        rectLet.y=lettuce_y
        if rect.colliderect(rectLet):
            lettuce_x=charx
            lettuce_y=chary-20
            score+=1
        #ketchup
        if not rect.colliderect(rectKet):
            ketchup_y = ketchup_y+toppingSpeed
            rectKet.y= rectKet.y+toppingSpeed
        if ketchup_y > HEIGHT:
            ketchup_x=random.randrange(0, WIDTH-50)
            ketchup_y=-100 
        rectKet.x= ketchup_x
        rectKet.y=ketchup_y
        if rect.colliderect(rectKet):
            ketchup_x=charx
            ketchup_y=chary-20
            score+=1
        #cheese
        if not rect.colliderect(rectCh):
            cheese_y = cheese_y+toppingSpeed
            rectCh.y= rectCh.y+toppingSpeed
        if cheese_y > HEIGHT:
            cheese_x=random.randrange(0, WIDTH-50)
            cheese_y=-100 
        rectCh.x= cheese_x
        rectCh.y=cheese_y
        if rect.colliderect(rectCh):
            cheese_x=charx
            cheese_y=chary-20
            score+=1

        

        # for item in rectList:
        #     if not rect.colliderect(item):
        #         img_y = img_y+toppingSpeed
        #         item.y= item.y+toppingSpeed
        #     if img_y > HEIGHT:
        #         img_x=random.randrange(0, WIDTH-50)
        #         img_y=-100 
        #     item.x= img_x
        #     item.y=img_y
        #     if rect.colliderect(Trect):
        #         img_x=charx
        #         img_y=chary-20
        #         score+=1

        #for game over- make more random with collidepoints - so far if top collides with tomato, game over
        if not rect.colliderect(rectBun):
            buny = buny+toppingSpeed
            rectBun.y= rectBun.y+toppingSpeed
        if buny > HEIGHT:
            bunx=random.randrange(0, WIDTH-50)
            buny=-100 
        rectBun.x= bunx
        rectBun.y=buny
        if Trect.colliderect(rectBun):
            gameOver()


        # pygame.draw.rect(screen, colors.get('white'), rect)
        # pygame.draw.rect(screen, colors.get('white'), Trect)
        # pygame.draw.rect(screen, colors.get('white'), rectBun)
        pygame.display.update()

def Game_2():
    global score, WIDTH, HEIGHT
    speed = 10
    wb=100
    charx=100
    score = 0
    bg=pygame.image.load('pygameFiles\Images\\backgroundlevel2.jpg')
    bg=pygame.transform.scale(bg, (WIDTH, HEIGHT))
    char = pygame.image.load('pygameFiles\Images\\burger toppings\\bottom bun cropped (2).png')
    char = pygame.transform.scale(char, (100,50))
    screen.blit(bg, (0,0))
    screen.blit(char, (WIDTH/2.5,HEIGHT/1.1))
    pygame.display.update()
    game2=True
    while game2:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game2=False
                mainMenu()
        keys = pygame.key.get_pressed() #allow us to see what key was pressed
        if keys[pygame.K_RIGHT] and charx < WIDTH-wb:
            charx += speed
        if keys[pygame.K_LEFT] and charx > 0:
            charx -= speed
        screen.blit(bg, (0,0))
        screen.blit(char, (charx,HEIGHT/1.1))
        pygame.display.update()



 
run = True 
screen.fill(menuColor)
userName=''
nameClr=(colors.get('blue')) #for text for name
bxClr=(200, 200, 200) #text box 

title=TITLE_FONT.render('Enter Name', 1, bxClr)
screen.blit(title, (WIDTH/2.5, HEIGHT//7))
pygame.display.update()


nameBox=pygame.Rect(WIDTH//4, HEIGHT//3, WIDTH//2, HEIGHT//10)
pygame.draw.rect(screen, bxClr, nameBox)
pygame.display.update()
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #Menu(mainTitle,messageMenu)
            mainMenu()
            print("You quit")
        if event.type == pygame.MOUSEBUTTONDOWN:
            print()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(userName)
                #run main menu - if in main program
                mainMenu()
            if event.key ==pygame.K_BACKSPACE: 
                userName=userName[:-1]
                print('back')
            else:
                userName += event.unicode
        pygame.draw.rect(screen, bxClr, nameBox)
        textSurface=MENU_FONT.render(userName, True, nameClr)
        #use rect x and y to  allign the text 
        screen.blit(textSurface, (nameBox.x+5, nameBox.y+5))
        pygame.display.update()
        
        
mainMenu()
Instructions() 
exit()

        

            