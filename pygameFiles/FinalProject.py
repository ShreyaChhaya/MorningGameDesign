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
    global WIDTH, score, tomato_y, tomato_x, char
    global HEIGHT
    speed=5
    toppingSpeed=3
    tomato_y=100
    tomato_x = 100
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
    imgInf=[topBun, tomato, pickles, patty, onion, mustard, lettuce, ketchup, cheese]
    row_count = 0
    # for img in imgInf:
    #     imgRect=img.get_rect()
    #     imgRect.x=0
    #     imgRect.y=-10
    #     tile = (img, imgRect)
    #     imgInf.append(tile)


    bg=pygame.image.load('pygameFiles\Images\\backgroundlevel1.jpg')
    bg=pygame.transform.scale(bg, (WIDTH, HEIGHT))
    char = pygame.image.load('pygameFiles\Images\\burger toppings\\bottom bun cropped (2).png')
    char = pygame.transform.scale(char, (100, 50))
    rect= char.get_rect()
    rect.center = WIDTH//2, HEIGHT/1.05
    screen.blit(char, rect)
    pygame.draw.rect(screen, colors.get('white'), rect, 1)
    screen.blit(char, (WIDTH/2.5,HEIGHT/1.1))
    pygame.display.update()
    tomato = pygame.transform.scale(tomato, (100,50))
    Trect= tomato.get_rect()
    Trect.center = WIDTH//2, HEIGHT//2
    screen.blit(tomato, rect)
    game1=True
    while game1:
        #move character
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
        if not rect.colliderect(Trect):
            tomato_y = tomato_y+toppingSpeed
            Trect.y= Trect.y+toppingSpeed
        if tomato_y > HEIGHT:
            tomato_x=random.randrange(0, WIDTH-50)
            tomato_y=-100 
        Trect.x= tomato_x
        Trect.y=tomato_y
        if rect.colliderect(Trect):
            tomato_x=charx
            tomato_y=chary-20
        #pygame.draw.rect(screen, colors.get('white'), rect)
        #pygame.draw.rect(screen, colors.get('white'), Trect)
        pygame.display.update()

    # #have end of game to to game over function and make this into function after game completed
    # screen.fill(colors.get('black'))

    # #button to return to menu
    # title=TITLE_FONT.render('GAME OVER', 1, colors.get('blue'))
    # screen.blit(title, (WIDTH/3, HEIGHT/3))
    # #text for score - add sore inwhen game complete
    # scoretext=MENU_FONT.render('Your score is ', 1, colors.get('blue'))
    # screen.blit(scoretext, (WIDTH/3, HEIGHT/2))
    # ButtonBack1 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
    # pygame.draw.rect(screen, colors.get("limeGreen"), ButtonBack1)
    # #return to menu text 
    # text=MENU_FONT.render('Return to Menu', 1, colors.get('blue'))
    # screen.blit(text, (WIDTH/18, HEIGHT/1.1))
    # pygame.display.update()
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

        

            