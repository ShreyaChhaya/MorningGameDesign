# #Maria Suarez
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


from subprocess import HIGH_PRIORITY_CLASS
import sys
import pygame, time,os,random, math, datetime
date=datetime.datetime.now()
pygame.init()#initialize the pygame package

os.system('cls')

WIDTH=700 #like constant
HEIGHT=700

TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//30)
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51), 'red':(255, 0, 0), 'purple': (138,43,226), 'yellow':(255,215,0), 'black':(0,0,0), 'lblue':(0,206,209)}
clr=colors.get("limeGreen")
message=['Instructions', 'Settings', 'Game 1', 'Game 2', 'Scoreboard', 'Exit']
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game")  #change the title of my window

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
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_settings)
    Title = TITLE_FONT.render("Circle eats Square Menu", 1, colors.get("blue"))
    screen.fill(colors.get('white'))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    yMenu=150
    
    for item in message:
        Button_menu=pygame.Rect(WIDTH/2.5, yMenu, WIDTH/4, 40)
        text=MENU_FONT.render(item, 1, colors.get('blue'))
        pygame.draw.rect(screen, colors.get('limeGreen'), Button_menu)
        screen.blit(text, (Bx, yMenu))
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
    screen.fill(colors.get("white"))

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
                pygame.display.quit()
                print("You quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint((mx, my)):
                    mainMenu() 

def settings():
    global screen 
    WIDTH=700
    HEIGHT=700
    title=TITLE_FONT.render('Settings', 1, colors.get('blue'))
    text=MENU_FONT.render('Return to Menu', 1, colors.get('blue'))

    screen.fill(colors.get('white'))

    Button_3 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    #buttons for size changing 
    Button_4=pygame.Rect(WIDTH/20, HEIGHT/1.8, WIDTH//7, 40)
    Button_5=pygame.Rect(WIDTH/4, HEIGHT/1.8, WIDTH//5, 40)
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_4)
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_5)

    #buttons for color changing 
    Button_6=pygame.Rect(WIDTH/21, HEIGHT/3, WIDTH//3.8, 40)
    Button_7=pygame.Rect(WIDTH/2.9, HEIGHT/3, WIDTH//3.5, 40)
    Button_8=pygame.Rect(WIDTH/1.5, HEIGHT/3, WIDTH//3.5, 40)
    pygame.draw.rect(screen, colors.get('pink'), Button_6)
    pygame.draw.rect(screen, colors.get('black'), Button_7)
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_8)
    #buttons for sound
    Button_9=pygame.Rect(WIDTH/20, HEIGHT/1.3, WIDTH//6, 40)
    Button_10=pygame.Rect(WIDTH/3, HEIGHT/1.3, WIDTH//6, 40)
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_9)
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_10)

    #text for buttons/screen
    screen.blit(title, (WIDTH/2.5,50))
    screen.blit(text, (WIDTH//18, HEIGHT/1.1))
    text5=MENU_FONT.render('UP 100', 1, colors.get('blue'))
    text6=MENU_FONT.render('DOWN 100', 1, colors.get('blue'))
    screen.blit(text5, (WIDTH/18, HEIGHT/1.8))
    screen.blit(text6, (WIDTH/4, HEIGHT/1.8))
    text2=MENU_FONT.render('Pink/Purple/Blue', 1, colors.get('purple'))
    text3=MENU_FONT.render('Yellow/Red/Black', 1, colors.get('yellow'))
    text4=MENU_FONT.render('Green/Blue/White', 1, colors.get('blue'))
    screen.blit(text2, (WIDTH/20, HEIGHT/3))
    screen.blit(text3, (WIDTH/2.8, HEIGHT/3))
    screen.blit(text4, (WIDTH/1.5, HEIGHT/3))
    text7=MENU_FONT.render('Sound On', 1, colors.get('blue'))
    text8=MENU_FONT.render('Sound Off', 1, colors.get('blue'))
    screen.blit(text7, (WIDTH/18, HEIGHT/1.3))
    screen.blit(text8, (WIDTH/3, HEIGHT/1.3))
    text9=MENU_FONT.render('Change color scheme:', 1, colors.get('blue'))
    text10=MENU_FONT.render('Change screen size:', 1, colors.get('blue'))
    text11=MENU_FONT.render('Change sound settings:', 1, colors.get('blue'))
    screen.blit(text9, (WIDTH/18, HEIGHT/4))
    screen.blit(text10, (WIDTH/18, HEIGHT/2.1))
    screen.blit(text11, (WIDTH/18, HEIGHT/1.5))
    pygame.display.update()

    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.display.quit()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_3.collidepoint((mx, my)):
                    mainMenu()
                if Button_4.collidepoint((mx, my)):
                    WIDTH+=100
                    HEIGHT+=100 
                    screen=pygame.display.set_mode((WIDTH,HEIGHT))
                if Button_5.collidepoint((mx, my)):
                    WIDTH-=100
                    HEIGHT-=100 
                    screen=pygame.display.set_mode((WIDTH,HEIGHT))




def scoreboard():
    high=0
    title=TITLE_FONT.render('Scoreboard', 1, colors.get('blue'))
    text3 = MENU_FONT.render("Return to Menu", 1, colors.get("blue"))

    screen.fill(colors.get('white'))
    Button_3 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    
    screen.blit(title, (WIDTH//3,50))
    screen.blit(text3, (WIDTH//17, HEIGHT/1.1))
    pygame.display.update()
    
    
    print(score)
    # if score>high:
    #     high=score
    # scrLine=str(high)+"\t " (':')+ "\t" +date.strftime('%m/%d/%Y')+ "\n"
    scrLine=str(score)+(': ')+ "\t"+date.strftime("%m-%d-%Y")+ "\n"
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
                pygame.display.quit()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_3.collidepoint((mx, my)):
                    mainMenu()

def exit():
    title=TITLE_FONT.render('Bye-Bye!', 1, colors.get('blue'))
    screen.fill(colors.get('white'))

    screen.blit(title, (WIDTH/2.5, HEIGHT/2.5))
    pygame.display.update()

    pygame.time.delay(1000)
    pygame.display.quit()
    



def Game_1():
    global score 
    score=0
    hb=50
    wb=50
    xb=100
    rad=25
    yb=300
    high=0

    charx = xb
    chary = yb

    cx=350
    cy=350
    speed=2
    ibox = rad*math.sqrt(2)
    xig = cx-(ibox/2)
    yig = cy-(ibox/2)

    #mouse varuables
    global mx
    global my


    #bg=pygame.image.load('PygameFiles\images\\bgSmaller.jpg')
    #char = pygame.image.load('PygameFiles\images\PixelArtTutorial.png')
    #char = pygame.transform.scale(char, (50, 50))

    square=pygame.Rect(xb,yb,wb,hb)# create the object to draw
    insSquare=pygame.Rect(xig,yig,ibox,ibox)
    squareClr=colors.get("pink")
    #keep running create a lp
    mountainSquare=pygame.Rect(250,320,180,250)
    circleClr=colors.get("blue")
    backgrnd=colors.get("pink")
    run = True
    while run:
        pygame.draw.rect(screen, colors.get("white"), mountainSquare)
        #screen.blit(bg, (0,0))
        screen.fill(backgrnd)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                print("you quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                # print(mousePos)
        keys = pygame.key.get_pressed() #allow us to see what key was pressed

        #square movement
        if keys[pygame.K_d] and square.x < WIDTH-wb:
            square.x += speed
            #charx += speed
        if keys[pygame.K_a] and square.x > 0:
            square.x -= speed
            #charx -= speed
        if keys[pygame.K_s] and square.y < HEIGHT-hb:
            square.y += speed
            #chary += speed
        if keys[pygame.K_w] and square.y > 0:
            square.y -= speed
            #chary -= speed

        #circle and inscribed square movement
        if keys[pygame.K_RIGHT] and cx < WIDTH-rad:
            cx += speed
            insSquare.x += speed
        if keys[pygame.K_LEFT] and cx > 0+rad:
            cx -= speed
            insSquare.x -= speed
        if keys[pygame.K_DOWN] and cy < HEIGHT-rad:
            cy += speed
            insSquare.y += speed
        if keys[pygame.K_UP] and cy > 0+rad:
            cy -= speed
            insSquare.y -= speed
        
        #circle square collide
        if square.colliderect(insSquare): 
            print("BOOM")
            cx = random.randint(rad, WIDTH-rad)
            cy = random.randint(rad, HEIGHT-rad)
            rad += 5
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            score+=1
            insSquare=pygame.Rect(xig,yig,ibox,ibox)
        
        #mountain collide square
        if square.colliderect(mountainSquare):
            square.x = 10
            square.y = 10
            #charx = 10
            #chary = 10
        
        #mountain collide circle
        if insSquare.colliderect(mountainSquare):
            cx = rad + 10
            cy = rad + 10
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)

        #rect(surface, color, object)
        pygame.draw.rect(screen, colors.get("blue"), square)
        pygame.draw.rect(screen, colors.get("blue"), insSquare)
        #screen.blit(char, (charx, chary))

        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, colors.get("red"), (cx, cy), rad)
        
        pygame.display.update()

    print(score)

    text=MENU_FONT.render('Return to Menu', 1, colors.get('blue'))
    Button_3 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    screen.blit(text, (WIDTH//18, HEIGHT/1.1))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.display.quit()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_3.collidepoint((mx, my)):
                    mainMenu()

    

def Game_2():
    global score 
    score=0
    hb=50
    wb=50
    xb=100
    rad=25
    yb=300
    high=0

    charx = xb
    chary = yb

    cx=350
    cy=350
    speed=2
    ibox = rad*math.sqrt(2)
    xig = cx-(ibox/2)
    yig = cy-(ibox/2)

    #mouse varuables
    global mx
    global my

    bg=pygame.image.load('PygameFiles\images\\bgSmaller.jpg')
    char=pygame.image.load('pygameFiles\images\\ufo.png')
    char=pygame.transform.scale(char, (WIDTH//7, WIDTH//7))

    char2=pygame.image.load('pygameFiles\images\\alien.jpg')
    char2=pygame.transform.scale(char2, (WIDTH//10,WIDTH//10 ))


    square=pygame.Rect(xb,yb,wb,hb)# create the object to draw
    insSquare=pygame.Rect(xig,yig,ibox,ibox)
    squareClr=colors.get("pink")
    #keep running create a lp
    mountainSquare=pygame.Rect(250,320,180,250)
    circleClr=colors.get("blue")
    backgrnd=colors.get("limeGreen")
    run = True
    while run:
        #pygame.draw.rect(screen, colors.get("white"), mountainSquare)
        screen.blit(bg, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                print("you quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                # print(mousePos)
        keys = pygame.key.get_pressed() #allow us to see what key was pressed

        #square movement
        if keys[pygame.K_d] and square.x < WIDTH-wb:
            square.x += speed
            charx += speed
        if keys[pygame.K_a] and square.x > 0:
            square.x -= speed
            charx -= speed
        if keys[pygame.K_s] and square.y < HEIGHT-hb:
            square.y += speed
            chary += speed
        if keys[pygame.K_w] and square.y > 0:
            square.y -= speed
            chary -= speed

        #circle and inscribed square movement
        if keys[pygame.K_RIGHT] and cx < WIDTH-rad:
            cx += speed
            insSquare.x += speed
        if keys[pygame.K_LEFT] and cx > 0+rad:
            cx -= speed
            insSquare.x -= speed
        if keys[pygame.K_DOWN] and cy < HEIGHT-rad:
            cy += speed
            insSquare.y += speed
        if keys[pygame.K_UP] and cy > 0+rad:
            cy -= speed
            insSquare.y -= speed
        
        #circle square collide
        if square.colliderect(insSquare): 
            print("BOOM")
            cx = random.randint(rad, WIDTH-rad)
            cy = random.randint(rad, HEIGHT-rad)
            rad += 5
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            score+=1
            insSquare=pygame.Rect(xig,yig,ibox,ibox)
        
        #mountain collide square
        if square.colliderect(mountainSquare):
            square.x = 10
            square.y = 10
            charx = 10
            chary = 10
        
        #mountain collide circle
        if insSquare.colliderect(mountainSquare):
            cx = rad + 10
            cy = rad + 10
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)

        #rect(surface, color, object)
        #pygame.draw.rect(screen, colors.get("pink"), square)
        #pygame.draw.rect(screen, colors.get("pink"), insSquare)
        screen.blit(char, (charx, chary))

        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, colors.get("limeGreen"), (cx, cy), rad)

        
        pygame.display.update()

    text=MENU_FONT.render('Return to Menu', 1, colors.get('blue'))
    Button_3 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    screen.blit(text, (WIDTH//18, HEIGHT/1.1))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.display.quit()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_3.collidepoint((mx, my)):
                    mainMenu()

    
        
mainMenu()
Instructions() 
exit()

        

            