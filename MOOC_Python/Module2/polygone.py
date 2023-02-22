"""Auteur: Samuel Mambingo
   date : 01/02/2020
   but du programme : dessine des polygônes réguliers de différentes couleurs inscrits dans un cercle de rayon r

"""
# importation des modules
import turtle
from math import pi
from math import cos
from math import sin
import random

# Choix des couleurs
choix = ["blue","red", "yellow", "green"]
# Définitions des fonctions (couleur pour le choix et polygone_turtle pour le traçage)
def couleur(choix):
    return random.choice(choix)

def polygone_turtle(x, y, n,rayon,couleur):
    turtle.color(cc)
    turtle.begin_fill()
    for i in range(1, n + 1):
        turtle.goto(x + rayon * cos(i * 2 * pi / n), y + rayon * sin(i * 2 * pi / n))
    turtle.end_fill()

#programme principal
while True:
    rayon = float(random.randint(1,10))             # choix du rayon du cercle
    n = random.randint(3,10)                        # choix du nombre de côté
    x = random.randint(-200,200)                   # choix de l'abscisse de départ
    x = float(x)
    y = random.randint(-200,200)                   # choix de l'ordonnée de départ
    y = float(y)
    turtle.up()
    turtle.goto(x + rayon, y)                       # déplacement de la tortue aux coordonnées choisies
    turtle.down()
    cc = str(couleur(choix))                        # appel au choix de la couleur

    polygone_turtle(x, y, n, rayon,"cc")            # appel au traçage et remplissage

turtle.mainloop()
