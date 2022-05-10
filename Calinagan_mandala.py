"""
Sarah Nicole D. Calinagan
BSCS_1B

Mandala art midterm
"""

import turtle
import math

screen = turtle.Screen()
turtle.bgcolor('black')
turtle.setworldcoordinates(-2000,-2000,2000,2000)
turtle.speed(0)

turtle.pencolor("light green")
def ekko(x,y,tilt,radius):
    
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.seth(tilt-35)
    turtle.circle(radius,70)
    turtle.left(90)
    turtle.circle(radius,90)

for tilt in range(0,360,30): 
    ekko(0,0,tilt,1000)

turtle.pencolor("sky blue")

def powder(x,y,length,direction):
    turtle.up()
    turtle.goto(x-length/(2**0.5)*math.cos(math.radians(direction+45)),y-length/(2**0.5)*math.sin(math.radians(direction+45)))
    turtle.seth(direction)
    turtle.down()
    for _ in range(4):
        turtle.fd(length)
        turtle.left(90)

def firelight(radius,direction,n):
    length = 2*radius*math.sin(math.radians(180/n))
    length = length/(2**0.5)
    for _ in range(n):
        powder(radius*math.cos(math.radians(180/n))*math.cos(math.radians(direction)),\
                    radius*math.cos(math.radians(180/n))*math.sin(math.radians(direction)),\
                    length, direction+45)
        direction += 360/n

def jinx(radius,direction,n):
    if radius < 10: return
    firelight(radius,direction,n)
    chomp = radius*math.cos(math.radians(180/n))-radius*math.sin(math.radians(180/n))
    jinx(chomp,direction+180/n,n)
    
jinx(800,0,11)


turtle.done()