import pyglet
from pyglet.gl import *   #import modules
import datetime
import math
import time
#from pyglet.gl import GL_AMBIENT_AND_DIFFUSE, glBegin, glClearColor
window = pyglet.window.Window(resizable= True, width = 800, height = 800, caption = "Clock" )
#changes the size

def hourhandxy(length):
    now = datetime.datetime.now()
    timeH = ((now.hour + now.minute/60))
    if timeH > 12 :
        timeH -= 12
    if 3<timeH<6 or  9<timeH<12:
        angle = 90 -  (timeH  % 3) * 30   #find the angle and account for it in
    else :                                # each quartile 
        angle = 0 -  (timeH  % 3) * 30
    #print (angle, "angle")
    #print (timeH, "hours")
    x = round((math.sin(math.radians(angle))) * length) #use triganometry to find the  
    y = round((math.cos(math.radians(angle))) * length) #length of hand
    if 0<=timeH<3:
        return (-x, (y)) #return pos/neg x/y depeding on quartile
    if 3<=timeH<6:
        return (x,-abs(y))
    if 6<=timeH<9:
        return (-abs(x),-abs(y))
    if 9<=timeH<12:
        return (-abs(x),y)

def minutehandxy(length):
    now = datetime.datetime.now()
    timeM = (now.minute )
    if 15<timeM<30 or  45<timeM<60:
        angle = 90 -   (timeM  % 15)  * 6
    else :
        angle = (timeM  % 15)  * 6
    x = round((math.sin(math.radians(angle))) * length)
    y = round((math.cos(math.radians(angle))) * length)
    if 0<=timeM<15:
        return (x,y)
    if 15<=timeM<30:
        return (x,-abs(y))
    if 30<=timeM<45:
        return (-abs(x),-abs(y))
    if 45<=timeM<60:
        return (-abs(x),y)

    
def secondhandxy(length):
    now = datetime.datetime.now()
    timeS = (now.second + now.microsecond/1000000)
    if 15<timeS<30 or  45<timeS<60:
        angle = 90 -   (timeS  % 15)  * 6
    else :
        angle = (timeS  % 15)  * 6
    x = round((math.sin(math.radians(angle))) * length)
    y = round((math.cos(math.radians(angle))) * length)
    if 0<=timeS<15:
        return (x,y)
    if 15<=timeS<30:
        return (x,-abs(y))
    if 30<=timeS<45:
        return (- abs(x),- abs(y))
    if 45<=timeS<60:
        return (-abs(x),y)

def timetocolor():
    now = datetime.datetime.now()
   # return  (((round(now.second + now.microsecond/1000000*(4.25)))/100))
    b =  round((((1.666666 *( now.second + now.microsecond/1000000))/100)),2)
    a = 1-b  #using the time to convert into python r,g,b for back ground and hands
   
    return (a,b)
frame = 0
def update_frame(x , y):
    global frame
    if frame == None :
        frame = 0
    else:
        frame += 1   #frame update
   

@window.event



def on_draw():
    
    pyglet.gl.glClearColor(timetocolor()[0],timetocolor()[0],timetocolor()[0],timetocolor()[0])
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(4)
    glBegin(GL_LINES)  #initializing and drawing
    
    
    gl.glColor3f(timetocolor()[1], timetocolor()[1], timetocolor()[1])
    glVertex2i(+window.width//2,window.height//2)
    glVertex2i( hourhandxy(window.width//4)[0] +window.width//2, hourhandxy(window.height//4)[1] +window.height//2)
    #hour hand, quarter of screen width
    
    gl.glColor3f(timetocolor()[1], timetocolor()[1],timetocolor()[1] )
    glVertex2i(+window.width//2,+window.height//2)
    glVertex2i( minutehandxy(window.width//3)[0] +window.width//2, minutehandxy(window.height//3)[1] +window.height//2)
    #minute hand, third of screen width
    
    gl.glColor3f(timetocolor()[1], timetocolor()[1],timetocolor()[1])
    glVertex2i(+window.width//2,+window.height//2)
    glVertex2i( secondhandxy(window.width//2.2)[0] +window.width//2, secondhandxy(window.height//2.2)[1] +window.height//2)
    #seconds hand, 2.2 of screen width
    
    glEnd()
    
pyglet.clock.schedule(update_frame, 1/500) #update every 500 frames             
pyglet.app.run()


    
