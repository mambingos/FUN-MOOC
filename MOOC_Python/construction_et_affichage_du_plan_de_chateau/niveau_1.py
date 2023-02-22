"""     Auteur:         Samuel MAMBINGO
        Date:           14/03/2022
        But:             """

# import de module
from CONFIGS import *
import turtle

# Constantes:
(X_Min, Y_Min) = ZONE_PLAN_MINI
(X_Max, Y_Max) = ZONE_PLAN_MAXI


# DEFINTION DES FONCTIONS
def lire_matrice(fichier):
# fonction lecture du fichier : récupère les données d'un fichier et transmet une matrice en sorti
    with open(fichier, encoding="utf-8") as file:
        matrice = []
        for line in file:
            line = line.split()                         #Transformation des lignes en liste de caractère
            matrice.append(line)
        for i in range(len(matrice)):
            for j in range(len(matrice[0])):
                matrice[i][j] = int(matrice[i][j])      #Conversion du caractère de la liste en entier
    return matrice



def calculer_pas(matrice):
# fonction qui récupère la matrice et retourne le pas de déplacement de la tortue (dimension du carré)
    (a, b) = (len(matrice[0]), len(matrice))
    largeur = (X_Max-X_Min) // a
    hauteur = (Y_Max-Y_Min) // b
    pas = min(largeur, hauteur)
    return pas

def coordonnees(case, pas):
# fonction qui calcule les coordonnées auxquelles doit se déplacer la tortue pour commencer son tracé
    cordonnees = (X_Min + case[0]*pas, Y_Min + (len(matrice)-case[1]) * pas)
    return cordonnees


def tracer_carre(dimension):
# petite fonction qui trace un carre dont la dimension est donnée en paramètre
    for i in range(4):
        turtle.forward(dimension)
        turtle.left(90)

def tracer_case(case, couleur, pas):
#fonction de traçage de carré d'une couleur
    turtle.speed(100*pas)
    turtle.up()
    turtle.goto(coordonnees(case, pas))
    turtle.down
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    tracer_carre(pas)
    turtle.end_fill()

def afficher_plan(matrice):
#  Trace pour chaque élement de la matrice un carré d'un couleur donnée
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            case = (j,i)                                    # inversion j et i pour une lecture par ligne
            tracer_case(case, couleur=COULEURS[matrice[i][j]], pas = calculer_pas(matrice))



# CORPS DU PROGRAMME

matrice = lire_matrice(fichier_plan)
pas = calculer_pas(matrice)

afficher_plan(matrice)
turtle.done




