#Shreya Chhaya 
#tic tac toe 
#functions: 
# grid(), 
#zeroGrid()
#drawMarkers()
#checkWinner()
#gameOver()

import pygame, time, random, math, sys, os
os.system('cls')
pygame.init()
player= 1
WIDTH=700 
HEIGHT=700

TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//30)
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51), 'red':(255, 0, 0), 'purple': (138,43,226), 'yellow':(255,215,0), 'black':(0,0,0), 'lblue':(0,206,209)}

screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption('Tic Tac Toe')
global count
count=0

player=1
markers=[]
lineWidth=10
Game=True
MxMy=(0,0)
print(markers)  
cirClr=colors.get("lblue")
xClr=colors.get("lblue")
def zero_Array(): 
    for x in range(3):
        row= [0] *3
        markers.append(row)
backgrnd=colors.get('black')


def grid():
    lineClr=colors.get("purple")
    for x in range(1,3):
        pygame.draw.line(screen,lineClr,(0,HEIGHT//3*x),(WIDTH,HEIGHT//3*x),lineWidth)  #Hztal line
        pygame.draw.line(screen,lineClr,(WIDTH//3*x, 0),(WIDTH//3*x,HEIGHT),lineWidth)  #Vert line
    pygame.time.delay(100)

def draw_Markers():
    global count
    count=0
    xValue=0
    for x in markers:   # getting a rw
        yValue=0
        for y in x:  #each elem fthe rw
            if y ==1:
                print ("x")
                count+=1
                pygame.draw.line(screen,xClr,(xValue * WIDTH//3 + 15, yValue * HEIGHT//3 + 15), (xValue * WIDTH//3 + WIDTH//3-15, yValue * WIDTH//3 + WIDTH//3-15),lineWidth)
                pygame.draw.line(screen, xClr,(xValue*WIDTH//3 +WIDTH//3-15, yValue*HEIGHT//3+15),(xValue *WIDTH//3+15,yValue*HEIGHT//3+HEIGHT//3-15),lineWidth)
            if y==-1:
                print("O")
                count+=1
                pygame.draw.circle(screen,cirClr,(xValue*WIDTH//3+WIDTH//6,yValue*HEIGHT//3 +HEIGHT//6),WIDTH//6-15, lineWidth)
            yValue +=1
        xValue +=1
    pygame.display.update()

def x_winner():
    screen.fill(backgrnd)
    text=MENU_FONT.render('Player X won!', 1, (cirClr))
    screen.blit(text, (WIDTH/2.5, HEIGHT/2.5))
    pygame.display.update()
    pygame.time.delay(3000)
    gameEnd()
def o_winner():
    screen.fill(backgrnd)
    texto=MENU_FONT.render('Player O won!', 1, (cirClr))
    screen.blit(texto, (WIDTH/2.5, HEIGHT/2.5))
    pygame.display.update()
    pygame.time.delay(3000)
    gameEnd() 

def checkWinner():
    if markers[0][0] + markers[0][1] + markers[0][2] == 3:
        x_winner()
    elif markers[0][0] + markers[0][1] + markers[0][2] == -3:
        o_winner()
    elif markers[1][0] + markers[1][1] + markers[1][2] == 3:
        x_winner()
    elif markers[1][0] + markers[1][1] + markers[1][2] == -3:
        o_winner()
    elif markers[2][0] + markers[2][1] + markers[2][2] == 3:
        x_winner()
    elif markers[2][0] + markers[2][1] + markers[2][2] == -3:
        o_winner()
    elif markers[0][0] + markers[1][0] + markers[2][0] == 3:
        x_winner()
    elif markers[0][0] + markers[1][0] + markers[2][0] == -3:
        o_winner()
    elif markers[0][1] + markers[1][1] + markers[2][1] == 3:
        x_winner()
    elif markers[0][1] + markers[1][1] + markers[2][1] == -3:
        o_winner()
    elif markers[0][2] + markers[1][2] + markers[2][2] == 3:
        x_winner()
    elif markers[0][2] + markers[1][2] + markers[2][2] == -3:
        o_winner()
    elif markers[0][0] + markers[1][1] + markers[2][2] == 3:
        x_winner()
    elif markers[0][0] + markers[1][1] + markers[2][2] == -3:
        o_winner()
    elif markers[2][0] + markers[1][1] + markers[0][2] == 3:
        x_winner()
    elif markers[2][0] + markers[1][1] + markers[0][2] == -3:
        o_winner()
    else:
        Game = True

    
def gameEnd():
    global count
    global Game
    Game = False
    screen.fill(backgrnd)
    textagn=MENU_FONT.render('Do you want to play again', 1, (cirClr))
    screen.blit(textagn,(WIDTH/2.8, HEIGHT/2.8))
    Button_yes=pygame.Rect(WIDTH/4, HEIGHT//2, 100, 50)
    Button_no=pygame.Rect(3*WIDTH/4, HEIGHT//2, 100, 50)
    pygame.draw.rect(screen, colors.get('pink'), Button_yes)
    pygame.draw.rect(screen, colors.get('pink'), Button_no)
    textYes=MENU_FONT.render('Yes', 1, (cirClr))
    textNo=MENU_FONT.render('No', 1, (cirClr))
    screen.blit(textYes, (WIDTH//4, HEIGHT//2))
    screen.blit(textNo, (3*WIDTH//4, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(10000)
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            mousePos=pygame.mouse.get_pos()
            mx=mousePos[0]
            my=mousePos[1]
            if Button_yes.collidepoint((mx, my)):
                count=0
                grid()
                draw_Markers()
                Game = True
            if Button_no.collidepoint((mx, my)):
                text=MENU_FONT.render('Bye!', 1, (cirClr))
                screen.fill(backgrnd)
                screen.blit(text, (WIDTH/2.5, HEIGHT/2.5))
                pygame.display.update()
                pygame.time.delay(1000)
                pygame.display.quit()
                

zero_Array()
count=0
while Game and count<9:
    screen.fill(backgrnd)
    grid()
    draw_Markers()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #Menu(mainTitle,messageMenu)
            pygame.quit()
            sys.exit()
            print("You quit")
        if event.type == pygame.MOUSEBUTTONDOWN:
            count+=1
            MxMy = pygame.mouse.get_pos()
            cellx=MxMy[0]//(WIDTH//3)
            celly=MxMy[1]//(HEIGHT//3)
            print(cellx, celly)
            if markers[cellx][celly]==0:
                markers[cellx][celly]=player
                player *=-1
                checkWinner()
    if count==9:
        text=MENU_FONT.render('Tie.', 1, cirClr)
        screen.fill(backgrnd)
        screen.blit(text, (WIDTH/3, HEIGHT/3))
        gameEnd()

        pygame.display.update() 
        pygame.time.delay(100)
