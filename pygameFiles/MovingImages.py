
import pygame
pygame.init()

win=pygame.display.set_mode((500,480))

pygame.display.set_caption('First Game')

#put pictures onto code
walkRight = [pygame.image.load('pygameFiles\Images\\R1.png'), pygame.image.load('pygameFiles\Images\\R2.png'), pygame.image.load('pygameFiles\Images\\R3.png'), pygame.image.load('pygameFiles\Images\\R4.png'), pygame.image.load('pygameFiles\Images\\R5.png'), pygame.image.load('pygameFiles\Images\\R6.png'), pygame.image.load('pygameFiles\Images\\R7.png'), pygame.image.load('pygameFiles\Images\\R8.png'), pygame.image.load('pygameFiles\Images\\R9.png')]
walkLeft = [pygame.image.load('pygameFiles\Images\\L1.png'), pygame.image.load('pygameFiles\Images\\L2.png'), pygame.image.load('pygameFiles\Images\\L3.png'), pygame.image.load('pygameFiles\Images\\L4.png'), pygame.image.load('pygameFiles\Images\\L5.png'), pygame.image.load('pygameFiles\Images\\L6.png'), pygame.image.load('pygameFiles\Images\\L7.png'), pygame.image.load('pygameFiles\Images\\L8.png'), pygame.image.load('pygameFiles\Images\\L9.png')]
bg = pygame.image.load('pygameFiles\Images\\bg.jpg')
char = pygame.image.load('pygameFiles\Images\\standing.png')

clock=pygame.time.Clock() #allows changing fps
#define variables for character movement
x=50
y=400
width=64
height=64
vel=5
isJump=False
jumpCount=10
left=False
right=False
walkCount=0


#drawing objets- outside of main loop
def redrawGameWindow():
    global walkCount #so that you can change variable
    win.blit(bg, (0,0)) #place background picture at 0,0
    if walkCount+1>=27:
        walkCount=0 #walkcount cant go more than 27 because nine sprites for three frames each and frame rate is 27
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount+=1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount+=1
    else:
        win.blit(char, (x,y))
    pygame.display.update()

#mainloop
run=True
while run:
    clock.tick(27)
    pygame.time.delay(50) 

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    #move left
    if keys[pygame.K_LEFT] and x>vel:
        x-=vel
        left=True
        right=False #moves left not right
    #move right
    elif keys[pygame.K_RIGHT] and x<500-width-vel:
        x+=vel
        right=True
        left=False
    else:
        right = False
        left=False
        walkCount=0
    #jump 
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump=True
            right=False
            left=False
            walkCount=0
    else:
        if jumpCount>= -10:
            neg=1
            if jumpCount<0:
                neg=-1
            y-= (jumpCount ** 2) * 0.5 * neg
            jumpCount-=1
        else:
            isJump=False
            jumpCount=10
    redrawGameWindow() #whenever change anything in terms of drawing, do it upthere but affects it here
    

