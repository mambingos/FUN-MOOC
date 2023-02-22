"""     Auteur:         Samuel MAMBINGO
        Date:           14/03/2022
        But:             """

# import de module
from CONFIGS import *
from copy import deepcopy
import turtle

# Constantes:
(X_Min, Y_Min) = ZONE_PLAN_MINI
(X_Max, Y_Max) = ZONE_PLAN_MAXI


# DEFINTION DES FONCTIONS CONSTRUCTION ET AFFICHAGE DU CHATEAU
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
    cordonnees = (X_Min + case[1]*pas, Y_Min + (len(matrice)-case[0]) * pas)
    return cordonnees

def tracer_carre(dimension):
# petite fonction qui trace un carre dont la dimension est donnée en paramètre
    for i in range(4):
        turtle.forward(dimension)
        turtle.left(90)

def tracer_case(case, couleur, pas):
#fonction de traçage de carré d'une couleur
    turtle.speed(0)
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
            case = (i,j)
            tracer_case(case, COULEURS[matrice[i][j]], pas)

# DEFINITION DES FONCTIONS DE DEPLACEMENTS
def deplacer_gauche():
    global matrice, position
    turtle.onkeypress(None, "Left")  # Désactive la touche Left
    # traitement associé à la flèche gauche appuyée par le joueur
    turtle.onkeypress(deplacer_gauche, "Left")  # Réassocie la touche Left à la fonction deplacer_gauche
    position = (int((Y_Min - turtle.pos()[1] + 0.5 * pas) / pas + len(matrice)), int((turtle.pos()[0] - X_Min - 0.5 * pas) / pas))
    if matrice[position[0]][position[1]-1] == 0:
        mouvement = (0, -1)
        deplacer(matrice, position, mouvement)




def deplacer_droite():
    global matrice, position
    turtle.onkeypress(None, "Right")  # Désactive la touche Right
    ...  # traitement associé à la flèche doroite appuyée par le joueur
    turtle.onkeypress(deplacer_droite, "Right")  # Réassocie la touche Left à la fonction deplacer_droite
    position = (int((Y_Min - turtle.pos()[1] + 0.5 * pas) / pas + len(matrice)), int((turtle.pos()[0] - X_Min - 0.5 * pas) / pas))
    if matrice[position[0]][position[1]+1] == 0:
        mouvement = (0, 1)
        deplacer(matrice,position,mouvement)
    elif matrice[position[0]][position[1]+1] == 3:
        reponse = turtle.textinput("Question", dico_portes[case][0])
        turtle.listen()
        mouvement = (1, 0)
        deplacer(matrice, position, mouvement)

def deplacer_haut():
    global matrice, position
    turtle.onkeypress(None, "Up")  # Désactive la touche Up
    ...  # traitement associé à la flèche haut appuyée par le joueur
    turtle.onkeypress(deplacer_haut, "Up")  # Réassocie la touche Up à la fonction deplacer_haut
    position =(int((Y_Min - turtle.pos()[1] + 0.5 * pas) / pas + len(matrice)), int((turtle.pos()[0]-X_Min - 0.5 * pas)/pas))
    print(matrice[position[0]-1][position[1]])
    if matrice[position[0]-1][position[1]] == 0:
        tracer_case(position, COULEURS[matrice[position[0]][position[1]]], pas)
        mouvement = (-1, 0)
        deplacer(matrice,position,mouvement)




def deplacer_bas():
    global matrice,position
    turtle.onkeypress(None, "Down")  # Désactive la touche Down
    ...  # traitement associé à la flèche bas appuyée par le joueur
    turtle.onkeypress(deplacer_bas, "Down")  # Réassocie la touche Down à la fonction deplacer_down
    position = (int((Y_Min - turtle.pos()[1] + 0.5 * pas) / pas + len(matrice)), int((turtle.pos()[0] - X_Min - 0.5 * pas) / pas))
    if matrice[position[0]+1][position[1]] == 0:
        mouvement = (1, 0)
        deplacer(matrice, position, mouvement)
    elif matrice[position[0]+1][position[1]] == 3:
        reponse = turtle.textinput("Question", dico_portes[case][0])
        turtle.listen()
        mouvement = (1, 0)
        deplacer(matrice, position, mouvement)



def deplacer(matrice, position, mouvement):
    tracer_case(position,COULEUR_VUE, pas)
    position = (position[0] + mouvement[0], position[1] + mouvement[1])
    place = coordonnees(position, pas)
    turtle.goto(place[0] + pas * 0.5, place[1] + pas * 0.5)
    turtle.dot(RATIO_PERSONNAGE * pas, COULEUR_PERSONNAGE)









# CORPS DU PROGRAMME

matrice = lire_matrice(fichier_plan)
pas = calculer_pas(matrice)

afficher_plan(matrice)
afficher = turtle.clone()


depart = coordonnees(POSITION_DEPART,pas)
#(X_Min + case[1]*pas, Y_Min + (len(matrice)-case[0]) * pas)


depart = (depart[0]+pas*0.5, depart[1]+pas*0.5)
turtle.goto(depart)
position =(int((Y_Min - turtle.pos()[1] + 0.5 * pas) / pas + len(matrice)), int((turtle.pos()[0]-X_Min - 0.5 * pas)/pas))


turtle.dot(pas*RATIO_PERSONNAGE,COULEUR_PERSONNAGE)
turtle.hideturtle()

turtle.listen()    # Déclenche l’écoute du clavier
turtle.onkeypress(deplacer_gauche, "Left")   # Associe à la touche Left une fonction appelée deplacer_gauche
turtle.onkeypress(deplacer_droite, "Right")
turtle.onkeypress(deplacer_haut, "Up")
turtle.onkeypress(deplacer_bas, "Down")
turtle.mainloop()    # Place le programme en position d’attente d’une action du joueur



