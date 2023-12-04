
# Import and initialize the pygame library
import pygame
import math
import random
import playsound
import time
import threading
nosie = playsound.playsound("./noise2.mp3")
def playNoise():
    playsound.playsound("./noise2.mp3")


time.sleep(1)
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1000, 1000])

# Run until the user asks to quit
running = True

Ppos = []
va22 = 40
ballSize = 25
boxLen = 9*va22
boxHig = 9*va22
initHig = 100
initWid = 50

x = (boxLen+initWid)/2
y = (initHig+boxHig)/2
speed = 3.5
xVel = 1
yVel = 1
angle = math.pi/3.5
drawLoop = 0
drawLoopInc = 5
col = 0
col2 = 0
random.seed(5)
angleRand = False
colMul = 1
ranvalangle= random.random()*3/30

white = (255, 255, 255)
black = (0, 0, 0)

# assigning values to X and Y variable
X = 400
Y = 400



font = pygame.font.Font('freesansbold.ttf', 64)

# create a text surface object,
# on which text is drawn on it.
word = '0'
text = font.render(word, True, white, black)

# create a rectangular object for the
# text surface object
textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = ((boxLen+initWid)/2, 50)


def gameLoop():
    global text
    global word
    global textRect
    global ranvalangle
    global angle
    global Ppos
    global x
    global y
    global speed
    global xVel
    global yVel
    global ballSize
    global colMul

    global boxLen
    global boxHig
    global initWid
    global initHig
    global col
    global col2

    global drawLoopInc
    global drawLoop
    if drawLoop == drawLoopInc:
        if len(Ppos) == 400:
            Ppos.pop(0)

        Ppos.append((x,y, ballSize, col, col2))
        drawLoop = 0
        print("sdfasf")
        if col >= 255:
            colMul = -1
            col =  col + 2*colMul
            col2+=10
        elif col <= 0:
            colMul = 1
            col = col + 2*colMul
            col2 +=10
        else:
            col = col+ 1*colMul

    else: drawLoop += 1

    rx = x+ballSize
    lx = x-ballSize-5

    uy = y-ballSize-5
    dy = y+ballSize+5
#TODO redo all of this with phys calculations with trig so i can do angle stuff
    Ximpact = False
    Yimpact = False
    if xVel ==1:
        if rx >= boxLen+5:
            xVel = -1
            x = x-speed*math.cos(angle)
            Ximpact = True
        elif rx <= boxLen+5:
            x = x + speed*math.cos(angle)
    elif xVel == -1:
        if lx<=initWid:
            xVel = 1
            x = x + speed*math.cos(angle)
            Ximpact = True
        elif lx >= initWid:
            x = x-speed*math.cos(angle)


    if yVel == 1:
        if uy <= initHig:
            yVel = -1
            y = y + speed*math.sin(angle)
            Yimpact = True
        elif uy > initHig:
            y = y-speed*math.sin(angle)
    elif yVel == -1:
        if dy >= initHig+boxHig:
            yVel = 1
            y = y- speed*math.sin(angle)
            Yimpact = True
        elif dy < initHig+boxHig:
            y = y+speed*math.sin(angle)



    if Ximpact == True or Yimpact == True:
        word = str(int(word) +1)
        text = font.render(word, True, white, black)
        textRect = text.get_rect()
        textRect.center = ((boxLen+initWid)/2, 50)
        #x2 = threading.Thread(target=playNoise)
        #x2.start()
        playsound.playsound("./noise2.mp3", False)
        ballSize *= 1.0
        speed *= 1.01
        if angleRand == True:
            yon = random.randint(0,1)
            if yon ==0:
                angle -=ranvalangle
            else: angle +=ranvalangle
init = 0
gameRate = 5

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    color = (0,0,0)
    screen.fill(color)
    p = pygame.time.get_ticks()
    if p > init:
        init = pygame.time.get_ticks() +  gameRate

        gameLoop()


    for i in Ppos:
        #print(i)
    #    print(Ppos)
    #    exit()
        val = abs((i[3]%510)-255)
        #pygame.draw.circle(screen, (abs(i[3]/(i[4]+1)), i[3], i[3]), (i[0], i[1]), i[2])
        pygame.draw.circle(screen, (val, val, val), (i[0], i[1]), i[2])

    screen.blit(text, textRect)
    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (x, y), ballSize)
    pygame.draw.rect(screen, (44,44,255),pygame.Rect(boxLen, initHig, 5, boxHig))
    pygame.draw.rect(screen, (44, 255, 44), pygame.Rect(initWid, initHig, 5, boxHig))

    pygame.draw.rect(screen, (255, 44, 44), pygame.Rect(initWid, initHig, boxLen-initWid, 5))
    pygame.draw.rect(screen, (44, 44, 44), pygame.Rect(initWid, initHig+boxHig-5, boxLen-initWid, 5))
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()