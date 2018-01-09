import pygame
import time
from random import*
 
pygame.init()
 
display_width = 800
display_height = 600
 
black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)
 
block_color = (53,115,255)
 
car_width = 73
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
Back = pygame.image.load('b.png')
carImg = pygame.image.load('racecar.png')
car2Img = pygame.image.load('racecar2.png')
gameIcon = pygame.image.load('gameIcon.png')

pygame.display.set_icon(gameIcon)
y1 = (display_height * 0.8)

pause = False
#crash = True
 
def things_dodged(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))
 
def back():
    gameDisplay.blit(Back,(0,0))

def car(x,y1):
    gameDisplay.blit(carImg,(x,y1))
def car2(x1,cspd):
    gameDisplay.blit(car2Img,(x1,cspd)) 
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
##def message_display(text):
##    largeText = pygame.font.SysFont("comicsansms",115)
##    TextSurf, TextRect = text_objects(text, largeText)
##    TextRect.center = ((display_width/2),(display_height/2))
##    gameDisplay.blit(TextSurf, TextRect)
## 
##    pygame.display.update()
## 
##    time.sleep(2)
## 
##    game_loop()
    
    
 
def crash():
    
    
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        

        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15) 

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False
    

def paused():

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        

        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)   


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
        
        
    
    

    
def game_loop():
    global pause

    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x1 = (display_width * 0.70)
    y1 = (display_height * 0.8)

 
    x_change = 0
    y1_change = 0
    spd = 0
    sppd = 0
    cspd = 0
    csppd = 0
    cr = 0
    dirt = 0
    dirt2 = 0
    sspd = 0
    sspd2 = 0
    sspd3 = 0
 
 
    dodged = 0
 
    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                    
 
            if event.type == pygame.KEYUP:
                sspd = randint(1,9)
                sspd2 = sspd
                sspd = randint(10,11)
                sspd3 = (sspd + sspd2)
                spd = sspd3
                sppd = randint(1,5)
                csppd = randint(0,1)
                dirt = csppd
                csppd = randint(0,1)
                dirt2 = (dirt + csppd)
                y1_change = sspd
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            

        if sppd == 1:
            spd += 1
            sppd = 0
        if csppd == 1:
            cspd += 1
            csppd == 0
        if spd > cspd:
            cr = 0
        if cr == 1:
            cspd -= 1
            cr = 0
 
        x += x_change
        y += y1_change
        gameDisplay.fill(white)
 
        back()
        car(x,y1)
        car2(x1,dirt2)
        things_dodged(spd)
 
        if x == 300 or x == 420:
            crash() 
        
        pygame.display.update()
        clock.tick(60)
y1 = (display_height * 0.8)
game_intro()
game_loop()
pygame.quit()
quit()
