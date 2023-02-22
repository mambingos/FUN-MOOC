import turtle

import random
import time


def pave(abscisse_centre, ordonnee_centre, longueur_arete, color1, color2, color3):
    """ Dessine avec turtle un pave hexagonal
        en position ( abscisse_centre, ordonnee_centre)
        paramètres :
        - (abscisse_centre, ordonnee_centre) : point centre du pavé
        -  longueur_arete : longueur de chaque arête du pavé
        - color1, color2, color3 : les couleurs des 3 hexagones"""
    # TODO code de fonction pave ici
    turtle.up()
    turtle.goto(abscisse_centre, ordonnee_centre)
    turtle.down()
    turtle.color("black", color1)
    turtle.begin_fill()
    for i in range(0, 2):
        turtle.forward(longueur_arete)
        turtle.left(120)
        turtle.forward(longueur_arete)
        turtle.left(60)
    turtle.end_fill()

    turtle.color("black", color2)
    turtle.begin_fill()
    for i in range(0, 2):
        turtle.forward(longueur_arete)
        turtle.right(120)
        turtle.forward(longueur_arete)
        turtle.right(60)
    turtle.end_fill()

    turtle.left(120)
    turtle.color("black", color3)
    turtle.begin_fill()
    for i in range(0, 2):
        turtle.forward(longueur_arete)
        turtle.left(120)
        turtle.forward(longueur_arete)
        turtle.left(60)
    turtle.end_fill()


# code principal
turtle.hideturtle()
turtle.speed(0)
turtle.reset()
time.sleep(5)

while True:
    pave(random.randint(-300, 300), random.randint(-300, 300),
         random.randint(10, 50), 'black', 'red', 'blue')
    pave(random.randint(-300, 300), random.randint(-300, 300),
         random.randint(10, 50), 'white', 'grey', 'black')

turtle.mainloop()
