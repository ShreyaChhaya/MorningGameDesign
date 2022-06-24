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
from ssl import OP_ENABLE_MIDDLEBOX_COMPAT
from subprocess import ABOVE_NORMAL_PRIORITY_CLASS, HIGH_PRIORITY_CLASS
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

#random menu color each time game is opened, can change to new random color in settings
menuColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

#getting fonts 
TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//30)

#color dictionary
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51), 'red':(255, 0, 0), 'purple': (138,43,226), 'yellow':(255,215,0), 'black':(0,0,0), 'lblue':(0,206,209)}

#message - each option in menu
message=['Instructions', 'Settings', 'Level 1', 'Level 2', 'Scoreboard', 'Exit']

screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Burger Stack")  #change the title of my window


#background music
mixer.music.load('background (1).wav')
mixer.music.play(-1)

#buttons for menu
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
    #blit title
    global menuColor
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_settings)
    Title = TITLE_FONT.render("Burger Stack!", 1, colors.get("blue"))
    screen.fill(menuColor)
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    yMenu=150
    
    for item in message:
        #button for each section of menu
        Button_menu=pygame.Rect(WIDTH/2.5, yMenu, WIDTH/4, 40)
        text=MENU_FONT.render(item, 1, colors.get('blue'))
        pygame.draw.rect(screen, colors.get('limeGreen'), Button_menu)
        screen.blit(text, (WIDTH/2.5, yMenu))
        pygame.display.update()
        pygame.time.delay(50)
        yMenu += 50
    MENU=True
    while MENU:
        #to quit
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                print("You quit")
                pygame.display.quit()
                MENU=False

            #if certian button, go to certain place
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

    #fills screen with random menu color
    screen.fill(menuColor)

    #creating button options
    Button_1 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_1)

    #Instructions
    myFile = open("PygameFiles\instructions.txt", "r")
    content = myFile.readlines()

    #variable to control change of line
    yinstructions = 150
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yinstructions))
        pygame.display.update()
        pygame.time.delay(50)
        yinstructions += 40

    myFile.close()

    #print text
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
    #title text
    title=TITLE_FONT.render('Settings', 1, colors.get('blue'))
    text=MENU_FONT.render('Return to Menu', 1, colors.get('blue'))

    screen.fill(menuColor)
    #text
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

    #loop for each button
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
                    #button for color - changes color randomly
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
    #text for scoreboard

    title=TITLE_FONT.render('Scoreboard', 1, colors.get('blue'))
    text3 = MENU_FONT.render("Return to Menu", 1, colors.get("blue"))

    screen.fill(menuColor)
    Button_3 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    
    screen.blit(title, (WIDTH//3,50))
    screen.blit(text3, (WIDTH//17, HEIGHT/1.1))
    pygame.display.update()
    
    #open score file and write the score line in it
    print(score)
    scrLine=str(score)+(': ')+ ' '+ userName+ " "+date.strftime("%m-%d-%Y")+ "\n"
    myFile = open("PygameFiles\scoreboard.txt", "a")
    myFile.write(str(scrLine))
    myFile.close()

    #read scor file
    myFile=open('pygameFiles\scoreboard.txt', 'r')
    content = myFile.readlines()

    #variable to control change of line
    yscore = 150
    for lines in content:
        Instruc = MENU_FONT.render(lines[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yscore))
        pygame.display.update()
        pygame.time.delay(50)
        yscore += 40

    myFile.close()

    #back to menu if quit
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
    #text 
    title=TITLE_FONT.render('Bye-Bye!', 1, colors.get('blue'))
    screen.fill(menuColor)

    screen.blit(title, (WIDTH/2.5, HEIGHT/2.5))
    pygame.display.update()

    #delay and then leave window
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
    global WIDTH, score, tomato_y, tomato_x, char, bunx, buny, pickle_x, pickle_y, patty_y, patty_x, onion_x, onion_y, mustard_x, mustard_y, lettuce_x, lettuce_y, ketchup_x, ketchup_y, cheese_x, cheese_y, rect
    global HEIGHT
    speed=5
    topping1Speed=8
    topping2Speed=5
    topping3Speed=12
    tomato_y=222
    tomato_x = 360
    patty_x=436
    patty_y=-700
    onion_x=564
    onion_y=500
    mustard_x=125
    mustard_y=-200
    lettuce_x=330
    lettuce_y=350
    ketchup_x=520
    ketchup_y=660
    cheese_x=260
    cheese_y=144
    bunx=0
    buny=0
    bun2x=500
    bun2y=333
    pickle_y=-600
    pickle_x=50
    chary=HEIGHT/1.1
    screen= pygame.display.set_mode((WIDTH,HEIGHT))
    charx=100
    wb=100
    score = 0 

    #get all images for toppings
    topBun=pygame.image.load('pygameFiles\Images\\burger toppings\\top bun.png')
    topBun2=pygame.image.load('pygameFiles\Images\\burger toppings\\top bun.png')

    tomato=pygame.image.load('pygameFiles\Images\\burger toppings\\tomato.png')
    pickles=pygame.image.load('pygameFiles\Images\\burger toppings\pickles.png')
    patty=pygame.image.load('pygameFiles\Images\\burger toppings\patty.png')
    onion=pygame.image.load('pygameFiles\Images\\burger toppings\onion.png')
    mustard=pygame.image.load('pygameFiles\Images\\burger toppings\mustard.png')
    lettuce=pygame.image.load('pygameFiles\Images\\burger toppings\lettuce.png')
    ketchup=pygame.image.load('pygameFiles\Images\\burger toppings\ketchup.png')
    cheese=pygame.image.load('pygameFiles\Images\\burger toppings\cheese.png')

    toppingList=[topBun, topBun2, tomato, pickles, patty, onion, mustard, lettuce, ketchup, cheese]

#rectangles 
    #separate rectangle for top bun
    topBun=pygame.transform.scale(topBun, (100,50))
    rectBun=topBun.get_rect()
    rectBun.center=WIDTH//2,HEIGHT//2
    screen.blit(topBun, rectBun)
    screen.blit(topBun, (WIDTH//2, HEIGHT//2))

    topBun2=pygame.transform.scale(topBun2, (100,50))
    rectBun2=topBun2.get_rect()
    rectBun2.center=WIDTH//2,HEIGHT//2
    screen.blit(topBun2, rectBun2)
    screen.blit(topBun2, (WIDTH//2, HEIGHT//2))

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

    rectList=[rectBun, Trect, rectPic, rectPat, rectOn, rectMus, rectLet, rectKet, rectCh]

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

        #blit all the new toppings after moving position
        screen.blit(bg, (0,0))
        screen.blit(char, (charx,HEIGHT/1.1))
        screen.blit(tomato, (tomato_x,tomato_y))
        screen.blit(topBun, (bunx, buny))
        screen.blit(topBun2, (bun2x, bun2y))
        screen.blit(pickles, (pickle_x, pickle_y))
        screen.blit(patty, (patty_x, patty_y))
        screen.blit(onion, (onion_x, onion_y))
        screen.blit(mustard, (mustard_x, mustard_y))
        screen.blit(lettuce, (lettuce_x, lettuce_y))
        screen.blit(ketchup, (ketchup_x, ketchup_y))
        screen.blit(cheese, (cheese_x, cheese_y))
        
#collisions 

        #if bun collides with tomato
        if not rect.colliderect(Trect):
            tomato_y = tomato_y+topping1Speed
            Trect.y= Trect.y+topping1Speed
            score+=0
        if tomato_y > HEIGHT:
            tomato_x=random.randrange(0, WIDTH-50)
            tomato_y=-100 
        Trect.x= tomato_x
        Trect.y=tomato_y
        if rect.colliderect(Trect):
            tomato_x=charx
            tomato_y=chary-20
            score+=1
            

        #pickles collidepoint
        if not rect.colliderect(rectPic):
            pickle_y = pickle_y+topping2Speed
            rectPic.y= rectPic.y+topping2Speed
            score+=0
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
            patty_y = patty_y+topping2Speed
            rectPat.y= rectPat.y+topping2Speed
            score+=0
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
            onion_y = onion_y+topping3Speed
            rectOn.y= rectOn.y+topping3Speed
            score+=0
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
            mustard_y = mustard_y+topping3Speed
            rectMus.y= rectMus.y+topping3Speed
            score+=0
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
            lettuce_y = lettuce_y+topping2Speed
            rectLet.y= rectLet.y+topping2Speed
            score+=0
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
            ketchup_y = ketchup_y+topping2Speed
            rectKet.y= rectKet.y+topping2Speed
            score+=0
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
            cheese_y = cheese_y+topping1Speed
            rectCh.y= rectCh.y+topping1Speed
            score+=0
        if cheese_y > HEIGHT:
            cheese_x=random.randrange(0, WIDTH-50)
            cheese_y=-100 
        rectCh.x= cheese_x
        rectCh.y=cheese_y
        if rect.colliderect(rectCh):
            cheese_x=charx
            cheese_y=chary-20
            score+=1


        #for game over- make more random with collidepoints - so far if top collides with tomato, game over
        if not rect.colliderect(rectBun):
            buny = buny+topping1Speed
            rectBun.y= rectBun.y+topping1Speed
        if buny > HEIGHT:
            bunx=random.randrange(0, WIDTH-50)
            buny=-100 
        rectBun.x= bunx
        rectBun.y=buny
        if rect.colliderect(rectBun):
            gameOver()
        if not rect.colliderect(rectBun2):
            bun2y = bun2y+topping1Speed
            rectBun2.y= rectBun2.y+topping1Speed
        if bun2y > HEIGHT:
            bun2x=random.randrange(0, WIDTH-50)
            bun2y=-100 
        rectBun2.x= bun2x
        rectBun2.y=bun2y
        if rect.colliderect(rectBun2):
            gameOver()

        # pygame.draw.rect(screen, colors.get('white'), rect)
        # pygame.draw.rect(screen, colors.get('white'), Trect)
        # pygame.draw.rect(screen, colors.get('white'), rectBun)
        pygame.display.update()

def Game_2():
#faster speed, more topping variety, different background
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
    global avo_x, avo_y, bacon_x, bacon_y, eg_x, eg_y, oli_x, oli_y, pep_x, pep_y, mush_x, mush_y
    global WIDTH, score, tomato_y, tomato_x, char, bunx, buny, pickle_x, pickle_y, patty_y, patty_x, onion_x, onion_y, mustard_x, mustard_y, lettuce_x, lettuce_y, ketchup_x, ketchup_y, cheese_x, cheese_y
    global HEIGHT
    speed=7
    topping1Speed=11
    topping2Speed=9
    topping3Speed=14
    topping4Speed=3
    tomato_y=222
    tomato_x = 360
    patty_x=436
    patty_y=-700
    onion_x=564
    onion_y=500
    mustard_x=125
    mustard_y=-200
    lettuce_x=330
    lettuce_y=350
    ketchup_x=520
    ketchup_y=660
    cheese_x=260
    cheese_y=144
    bunx=0
    buny=0
    bun2x=500
    bun2y=333
    pickle_y=-600
    pickle_x=50
    chary=HEIGHT/1.1
    screen= pygame.display.set_mode((WIDTH,HEIGHT))
    charx=100
    wb=100
    avo_x=590
    avo_y=345
    bacon_x=19
    bacon_y=-900
    eg_x=279
    eg_y=0
    oli_x=357
    oli_y=543
    pep_x=690
    pep_y=480
    mush_x=40
    mush_y=200
    
    score = 0 

    #get all images for toppings
    topBun=pygame.image.load('pygameFiles\Images\\burger toppings\\top bun.png')
    topBun2=pygame.image.load('pygameFiles\Images\\burger toppings\\top bun.png')

    tomato=pygame.image.load('pygameFiles\Images\\burger toppings\\tomato.png')
    pickles=pygame.image.load('pygameFiles\Images\\burger toppings\pickles.png')
    patty=pygame.image.load('pygameFiles\Images\\burger toppings\patty.png')
    onion=pygame.image.load('pygameFiles\Images\\burger toppings\onion.png')
    mustard=pygame.image.load('pygameFiles\Images\\burger toppings\mustard.png')
    lettuce=pygame.image.load('pygameFiles\Images\\burger toppings\lettuce.png')
    ketchup=pygame.image.load('pygameFiles\Images\\burger toppings\ketchup.png')
    cheese=pygame.image.load('pygameFiles\Images\\burger toppings\cheese.png')

    #level 2 toppings only
    avocado=pygame.image.load('pygameFiles\Images\\burger toppings\\avocado.png')
    bacon= pygame.image.load('pygameFiles\Images\\burger toppings\\bacon.png')
    eg= pygame.image.load('pygameFiles\Images\\burger toppings\eggs.png')
    olive=pygame.image.load('pygameFiles\Images\\burger toppings\olives.png')
    pep=pygame.image.load('pygameFiles\Images\\burger toppings\peppers.png')
    mush=pygame.image.load('pygameFiles\Images\\burger toppings\mushrooms.png')

#rectangles for each topping
    toppingList=[topBun, topBun2, tomato, pickles, patty, onion, mustard, lettuce, ketchup, cheese, avocado, bacon, eg, olive, pep, mush]
    #separate rectangle for top bun
    topBun=pygame.transform.scale(topBun, (100,50))
    rectBun=topBun.get_rect()
    rectBun.center=WIDTH//2,HEIGHT//2
    screen.blit(topBun, rectBun)
    screen.blit(topBun, (WIDTH//2, HEIGHT//2))

    topBun2=pygame.transform.scale(topBun2, (100,50))
    rectBun2=topBun2.get_rect()
    rectBun2.center=WIDTH//2,HEIGHT//2
    screen.blit(topBun2, rectBun2)
    screen.blit(topBun2, (WIDTH//2, HEIGHT//2))

    #avocado
    avocado=pygame.transform.scale(avocado, (100,50))
    rectAvo=avocado.get_rect()
    rectAvo.center=WIDTH//2,HEIGHT//2
    screen.blit(avocado, rectAvo)
    screen.blit(avocado, (WIDTH//2, HEIGHT//2))

    #bacon
    bacon=pygame.transform.scale(bacon, (100,50))
    rectBac=bacon.get_rect()
    rectBac.center=WIDTH//2,HEIGHT//2
    screen.blit(bacon, rectBac)
    screen.blit(bacon, (WIDTH//2, HEIGHT//2))
    #eggs
    eg=pygame.transform.scale(eg, (100,50))
    rectEg=eg.get_rect()
    rectEg.center=WIDTH//2,HEIGHT//2
    screen.blit(eg, rectEg)
    screen.blit(eg, (WIDTH//2, HEIGHT//2))
    #olives
    olive=pygame.transform.scale(olive, (100,50))
    rectOl=olive.get_rect()
    rectOl.center=WIDTH//2,HEIGHT//2
    screen.blit(olive, rectOl)
    screen.blit(olive, (WIDTH//2, HEIGHT//2))
    #pepper
    pep=pygame.transform.scale(topBun, (100,50))
    rectPep=pep.get_rect()
    rectPep.center=WIDTH//2,HEIGHT//2
    screen.blit(pep, rectPep)
    screen.blit(pep, (WIDTH//2, HEIGHT//2))
    #mushrooms
    mush=pygame.transform.scale(mush, (100,50))
    rectMush=mush.get_rect()
    rectMush.center=WIDTH//2,HEIGHT//2
    screen.blit(mush, rectMush)
    screen.blit(mush, (WIDTH//2, HEIGHT//2))

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

    #background
    bg=pygame.image.load('pygameFiles\Images\\backgroundlevel2.jpg')
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

        #blit all the new toppings after moving position
        screen.blit(bg, (0,0))
        screen.blit(char, (charx,HEIGHT/1.1))
        screen.blit(tomato, (tomato_x,tomato_y))
        screen.blit(topBun, (bunx, buny))
        screen.blit(topBun2, (bun2x, bun2y))
        screen.blit(pickles, (pickle_x, pickle_y))
        screen.blit(patty, (patty_x, patty_y))
        screen.blit(onion, (onion_x, onion_y))
        screen.blit(mustard, (mustard_x, mustard_y))
        screen.blit(lettuce, (lettuce_x, lettuce_y))
        screen.blit(ketchup, (ketchup_x, ketchup_y))
        screen.blit(cheese, (cheese_x, cheese_y))
        screen.blit(mush, (mush_x, mush_y))
        screen.blit(pep, (pep_x, pep_y))
        screen.blit(olive, (oli_x, oli_y))
        screen.blit(eg, (eg_x, eg_y))
        screen.blit(bacon, (bacon_x, bacon_y))
        screen.blit(avocado, (avo_x, avo_y))

#collisions
        #if bun collides with tomato
        if not rect.colliderect(Trect):
            tomato_y = tomato_y+topping1Speed
            Trect.y= Trect.y+topping1Speed
            score+=0
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
            
        #avocado collide
        if not rect.colliderect(rectAvo):
            avo_y = avo_y+topping4Speed
            rectAvo.y= rectAvo.y+topping4Speed
            score+=0
        if avo_y > HEIGHT:
            avo_x=random.randrange(0, WIDTH-50)
            avo_y=-100 
        rectAvo.x= avo_x
        rectAvo.y=avo_y
        rect.y=chary
        if rect.colliderect(rectAvo):
            avo_x=charx
            avo_y=chary-20
            score+=1
            
        #bacon
        if not rect.colliderect(rectBac):
            bacon_y = bacon_y+topping4Speed
            rectBac.y= rectBac.y+topping4Speed
            score+=0
        if bacon_y > HEIGHT:
            bacon_x=random.randrange(0, WIDTH-50)
            bacon_y=-100 
        rectBac.x= bacon_x
        rectBac.y=bacon_y
        rect.y=chary
        if rect.colliderect(rectBac):
            bacon_x=charx
            bacon_y=chary-20
            score+=1
        #eggs
        if not rect.colliderect(rectEg):
            eg_y = eg_y+topping3Speed
            rectEg.y= rectEg.y+topping3Speed
            score+=0
        if eg_y > HEIGHT:
            eg_x=random.randrange(0, WIDTH-50)
            eg_y=-100 
        rectEg.x= eg_x
        rectEg.y=eg_y
        rect.y=chary
        if rect.colliderect(rectEg):
            eg_x=charx
            eg_y=chary-20
            score+=1
        #olives
        if not rect.colliderect(rectOl):
            oli_y = oli_y+topping4Speed
            rectOl.y= rectOl.y+topping4Speed
            score+=0
        if oli_y > HEIGHT:
            oli_x=random.randrange(0, WIDTH-50)
            oli_y=-100 
        rectOl.x= oli_x
        rectOl.y=oli_y
        rect.y=chary
        if rect.colliderect(rectOl):
            oli_x=charx
            oli_y=chary-20
            score+=1
        #peppers
        if not rect.colliderect(rectPep):
            pep_y = pep_y+topping3Speed
            rectPep.y= rectPep.y+topping3Speed
            score+=0
        if pep_y > HEIGHT:
            pep_x=random.randrange(0, WIDTH-50)
            pep_y=-100 
        rectPep.x= pep_x
        rectPep.y=pep_y
        rect.y=chary
        if rect.colliderect(rectPep):
            pep_x=charx
            pep_y=chary-20
            score+=1
        #mushrooms
        if not rect.colliderect(rectMush):
            mush_y = mush_y+topping2Speed
            rectBac.y= rectBac.y+topping2Speed
            score+=0
        if mush_y > HEIGHT:
            mush_x=random.randrange(0, WIDTH-50)
            mush_y=-100 
        rectMush.x= mush_x
        rectMush.y=mush_y
        rect.y=chary
        if rect.colliderect(rectMush):
            mush_x=charx
            mush_y=chary-20
            score+=1
        #pickles collidepoint
        if not rect.colliderect(rectPic):
            pickle_y = pickle_y+topping2Speed
            rectPic.y= rectPic.y+topping2Speed
            score+=0
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
            patty_y = patty_y+topping2Speed
            rectPat.y= rectPat.y+topping2Speed
            score+=0
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
            onion_y = onion_y+topping3Speed
            rectOn.y= rectOn.y+topping3Speed
            score+=0
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
            mustard_y = mustard_y+topping3Speed
            rectMus.y= rectMus.y+topping3Speed
            score+=0
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
            lettuce_y = lettuce_y+topping2Speed
            rectLet.y= rectLet.y+topping2Speed
            score+=0
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
            ketchup_y = ketchup_y+topping2Speed
            rectKet.y= rectKet.y+topping2Speed
            score+=0
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
            cheese_y = cheese_y+topping1Speed
            rectCh.y= rectCh.y+topping1Speed
            score+=0
        if cheese_y > HEIGHT:
            cheese_x=random.randrange(0, WIDTH-50)
            cheese_y=-100 
        rectCh.x= cheese_x
        rectCh.y=cheese_y
        if rect.colliderect(rectCh):
            cheese_x=charx
            cheese_y=chary-20
            score+=1

        #for game over- make more random with collidepoints - so far if top collides with tomato, game over
        if not rect.colliderect(rectBun):
            buny = buny+topping1Speed
            rectBun.y= rectBun.y+topping1Speed
        if buny > HEIGHT:
            bunx=random.randrange(0, WIDTH-50)
            buny=-100 
        rectBun.x= bunx
        rectBun.y=buny
        if rect.colliderect(rectBun):
            gameOver()
        if not rect.colliderect(rectBun2):
            bun2y = bun2y+topping1Speed
            rectBun2.y= rectBun2.y+topping1Speed
        if bun2y > HEIGHT:
            bun2x=random.randrange(0, WIDTH-50)
            bun2y=-100 
        rectBun2.x= bun2x
        rectBun2.y=bun2y
        if rect.colliderect(rectBun2):
            gameOver()

        # pygame.draw.rect(screen, colors.get('white'), rect)
        # pygame.draw.rect(screen, colors.get('white'), Trect)
        # pygame.draw.rect(screen, colors.get('white'), rectBun)
        pygame.display.update()


#get username
run = True 
screen.fill(menuColor)
userName=''
nameClr=(colors.get('blue')) #for text for name
bxClr=(200, 200, 200) #text box 

title=TITLE_FONT.render('Enter Name', 1, bxClr)
screen.blit(title, (WIDTH/2.5, HEIGHT//7))
pygame.display.update()

#loop- have user type in name, return goes to menu, backspace deletes letter
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

        

            