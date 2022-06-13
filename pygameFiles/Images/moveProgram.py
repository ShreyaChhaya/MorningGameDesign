#shreya chhaya
#6/9/2022
#we are learning pygame basic function
#creating screens, colors, shapes
#moving shapes
#K_UP 
#K_DOWN
#K_RIGHT
#K_LEFT
import random
from turtle import circle
import pygame, time, os
os.system('cls')
pygame.init() #must start with this every time for pygame to work

WIDTH=700 #size of screen - 700 pixels, like a constant - can still be modified later
HEIGHT=700
#create display window with any name you want
screen=pygame.display.set_mode((WIDTH,HEIGHT)) #creates screen

pygame.display.set_caption('My First Game') #changes title
pygame.time.delay(2000) #putting in delay for the pop up screen in milliseconds
colors={'yellow': (255,255,0), 'green':(0,255,0), 'red':(255,0,0), 'purple':(125,0,125), 'green2':(0, 125, 125), 'limegreen' : (153,255,51), 'white':(255,255,255), 'black':(0,0,0), 'lightPur':(204,204,205)} #dictionary for colors
clr=colors.get('limegreen')

hb=50 #height
wb=50 #width
xb=100 #varaible 
yb=300 #variable
squareClr=colors.get('red')
circleclr=colors.get('purple')
square=pygame.Rect(xb,yb,wb,hb) #create the object to draw
cx=350
cy=350
rad=50
#keep running create a loop 
background=clr #now that background is green, no delay needed - will stay green 
run=True
#create a variable to move
speed=1
while run:
    screen.fill(background)
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            run=False
            print('You quit')
    keys=pygame.key.get_pressed() #give key that has been pressed - this is a list
    if keys[pygame.K_RIGHT] and square.x < WIDTH -(wb):
        square.x += speed
    if keys[pygame.K_LEFT] and square.x > speed:
        square.x -= speed #subtract to go left
    if keys[pygame.K_UP] and square.y > speed:
        square.y -= speed
    if keys[pygame.K_DOWN] and square.y < HEIGHT -(hb): 
        square.y += speed
    #make circle
    if keys[pygame.K_d] and cx < WIDTH -(rad):
        cx += speed
    if keys[pygame.K_a] and cx > (speed+rad):
        cx -= speed
    if keys[pygame.K_w] and cy > (speed+rad):
        cy -= speed
    if keys[pygame.K_s] and cy < HEIGHT -(rad):
        cy += speed
    if square.collidepoint(cx,cy):
        print('boom!')
        cx=random.randint(rad, WIDTH-rad)
        cy=random.randint(rad, HEIGHT-rad)
    pygame.draw.rect(screen, squareClr, square)
    #to draw circle - (surface, color, center, radius)  
    pygame.draw.circle(screen, circleclr, (350,350), rad)
    
    pygame.display.update()

