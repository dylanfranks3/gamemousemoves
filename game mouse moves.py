import tkinter as tk
import pygame
import time
import os
from random import randint
import datetime
import threading
pygame.init()

root = tk.Tk()
t0 = time.time()

os.environ['SDL_VIDEO_WINDOW_POS'] = "200,200"
display_width = 600
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

clock = pygame.time.Clock()

heartimg = pygame.image.load("heart.jpg")
clearimg = pygame.image.load("clearbubble.png")
enemyList = []
heartList = []
def makeEnemy(speed):
    
    r = randint(1,4)
    if r == 1 :
        XYstart = ((randint(0,600)),0)
        XYend = ((randint(0,600)),600)  ###find perimeter randomly and on other side
    if r == 2 :
        XYstart = (600,(randint(0,600)))
        XYend = (0,(randint(0,600)))
    if r == 3 :
        XYstart = ((randint(0,600)),600)
        XYend = (randint(0,600),0)
    if r == 4 :
        XYstart = (0,(randint(0,600)))
        XYend = (600,(randint(0,600)))


    elocx = float(XYstart[0])              ####enemies location: initial
    elocy = float(XYstart[1])
    emovex = (XYend[0] - XYstart[0])/600    #### how far it should move
    emovey = (XYstart[1]- XYend[1])/600      ### per screenUpdate
    
    enemyList.append([elocx,elocy,emovex,emovey,speed]) ###logistics of new enemy


speed = 1.5
often = 0.4


def enemyevery(): ###how often
    global speed
    global often
    if often > 0.05:
        often -= 0.003
    threading.Timer(often, enemyevery).start()
    speed  += 0.02
    makeEnemy(speed) ##speed

def heartspawn():
    global heartList
    threading.Timer(randint(5,12), heartspawn).start()
    if not heartList:
        heartList.append([randint(0,display_width - 60),randint(0,display_height - 42)])    

        
heartspawn()

enemyevery()
extralife = False

while True:        
    gameDisplay.fill((255,255,255))

####heart
    if len(heartList)>0:
        heart = gameDisplay.blit(heartimg,(heartList[0]))

        
####player
    if 200 <= root.winfo_pointerx() <= 770 and 200<= root.winfo_pointery() <=770:
        dX = root.winfo_pointerx() - 200
        dY = root.winfo_pointery() - 200
        player = pygame.draw.rect(gameDisplay,(255,0,0),[dX, dY, 30, 30])

    if len(heartList) == 1:
        if pygame.Rect.colliderect(player,heart):
            extralife = True
            heartList.pop(0)



    for i in enemyList:
        i[0] += (i[2] * i[4])
        i[1] += (i[3] * i[4])
        if i[0]> 600 or 0>i[0] or i[1]> 600 or 0>i[1] :
            enemyList.remove(i)
        else:
            enemy = pygame.draw.rect(gameDisplay,(0,0,0),[i[0],i[1], 15, 15])
            if pygame.Rect.colliderect(player,enemy):
                if extralife == True:
                    extralife = False
                    enemyList.remove(i)
                    break
                else :
                    t1 = time.time()
                    pygame.quit()
                    root.destroy()
                                        
                






    pygame.display.update()
    clock.tick(120)

pygame.quit()





