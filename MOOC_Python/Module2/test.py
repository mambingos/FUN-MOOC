
import turtle
from turtle import *
from math import pi
from math import cos
from math import sin
import random

rayon = float(random.randint(1, 50))
n = 6
 #couleur(choix)#
x = random.randint(0, 100)
x = float(x)
y = random.randint(0, 100)
y = float(y)
turtle.up()
turtle.goto(x + rayon, y)
turtle.down()

for i in range(1, n + 1):
    turtle.color("black","black")
    turtle.begin_fill()
    turtle.goto(x + rayon * cos(i * 2 * pi / n), y + rayon * sin(i * 2 * pi / n))
turtle.end_fill()
turtle.up()
turtle.goto(-50,-50)
turtle.down()
turtle.begin_fill()
turtle.goto(-100, -50)
turtle.goto(-100,0)
turtle.goto(-50,0)
turtle.goto(-50,-50)
turtle.end_fill()
turtle.mainloop()

