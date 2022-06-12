#shreya chhaya
#6/9/2022
#we are learning pygame basic function
#creating screens, colors, shapes

import pygame, time, os
os.system('cls')
pygame.init() #must start with this every time for pygame to work

WIDTH=700 #size of screen - 700 pixels, like a constant - can still be modified later
HEIGHT=700
#create display window with any name you want
screen=pygame.display.set_mode((WIDTH,HEIGHT)) #creates screen

pygame.display.set_caption('My First Game') #changes title
pygame.time.delay(2000) #putting in delay for the pop up screen in milliseconds
greenClr=(0, 255, 0) #green
screen.fill(greenClr)
#pygame.display.update()
#pygame.time.delay(2000)
redClr=(255,0,0) #making screen red - RGB - all power for red, nothing for green, nothing for blue
#screen.fill(redClr) #fill background with red
#pygame.display.update()
#pygame.time.delay(2000)
purpleClr=(125, 0, 125)
green2=(0, 125, 125)
yellClr=(255,255,0)
blackClr=(0,0,0)
white=(255,255,255)
colors={'purple':(125,0,125), 'green2':(0, 125, 125), 'limegreen' : (153,255,51) } #dictionary for colors
clr=colors.get('limegreen')
hb=50 #height
wb=50 #width
xb=100 #varaible 
yb=300 #variable
square=(xb,yb,wb,hb) #create the object to draw
#keep running create a loop 
background=clr #now that background is green, no delay needed - will stay green 
run=True
while run:
    screen.fill(background)
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            run=False
            print('You quit')
    pygame.draw.rect(screen, redClr, square) #draw square- on screen, red color, shape square 
    #to draw circle - (surface, color, center, radius)  
    pygame.draw.circle(screen, purpleClr, (350,350), 25)
    pygame.draw.circle(screen, green2, (150, 150), 75)
    pygame.draw.circle(screen, purpleClr, (150,150), 25)
    #smileyface: figure out mouth with arc or semi-circle
    pygame.draw.circle(screen, yellClr, (350,350), 100)
    pygame.draw.circle(screen, white, (310,325), 25)
    pygame.draw.circle(screen, white, (390,325), 25)
    pygame.draw.circle(screen, blackClr, (310,325), 10)
    pygame.draw.circle(screen, blackClr, (390,325), 10)
    pygame.draw.circle(screen, blackClr, (350,390), 25)
    pygame.draw.circle(screen, yellClr, (350, 375), 30)
    pygame.display.update()

