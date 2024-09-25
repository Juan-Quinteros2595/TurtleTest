from turtle import *
from math import *

speed(0)
bgcolor("black")
goto(0,-40)

for i in range(16):
    for j in range(18):
        color('#FFA216'), rt(90)
        circle(150-j*6,90), lt(90)
        circle(150-j*6,90), rt(180)
    circle(40,24)

color('black') 
shape('circle')
shapesize(0.5)
fillcolor('#8B4513')
golden_ang=137.508
phi = golden_ang*(pi/180)

for i in range(140):
    r = 4*sqrt(i)
    theta = i*phi
    x = r*cos(theta)
    y = r*sin(theta)
    penup(), goto(x,y)
    setheading(i*golden_ang)
    pendown(), stamp()

def circulo(x, y):
    penup(), goto(x, y), pendown()
    color('black'), fillcolor('#FFA216')
    begin_fill(), circle(3), end_fill()

def dibujar_J(x, y):
    pos_m = [(x,y), (x, y+4), (x, y+8), (x, y+12), (x, y+16),
             (x, y+20), (x, y+24), (x-4, y), (x-8, y), (x-12, y), (x-16, y), (x-20, y),
             (x-20, y+4), (x-20, y+8), (x-20, y+12), (x-4,y+24), (x-8,y+24), (x-12,y+24)]

    for pos in pos_m:
        circulo(*pos)

def dibujar_I(x, y):
    pos_i = [(x, y), (x+4, y), (x+8, y), (x+12, y), 
             (x+6, y+4), (x+6, y+8), (x+6, y+12), 
             (x+6, y+16), (x+6, y+20), (x+6, y+24),
             (x, y+24), (x+4, y+24), (x+8, y+24), (x+12, y+24)]

    for pos in pos_i:
        circulo(*pos)

def dibujar_M(x, y):
    pos_m = [(x,y), (x, y+4), (x, y+8), (x, y+12), (x, y+16),
             (x, y+20), (x, y+24), (x+3, y+21), (x+6, y+18),
             (x+9, y+15), (x+12, y+12), (x+15, y+15), (x+18, y+18),
             (x+21, y+21), (x+24, y+24), (x+24, y+20), (x+24, y+16),
             (x+24, y+12), (x+24, y+8), (x+24, y+4), (x+24, y)]

    for pos in pos_m:
        circulo(*pos)
       
def dibujar_E(x, y):
    pos_e = [(x, y), (x, y+4), (x, y+8), (x, y+12),
             (x, y+16), (x, y+20), (x, y+24), (x+4, y+24),
             (x+8, y+24), (x+12, y+24), (x+16, y+24), (x+20, y+24), 
             (x+4, y+12), (x+8, y+12), (x+12, y+12), 
             (x+16, y+12), (x+4, y), (x+8, y), (x+12, y), (x+16, y), (x+20, y)]

    for pos in pos_e:
        circulo(*pos)

dibujar_J(-4, 4), dibujar_I(10, 4)
dibujar_M(-28, -30), dibujar_E(10, -30)
#circulo(32, -10), circulo(34, -6)

hideturtle()
done()