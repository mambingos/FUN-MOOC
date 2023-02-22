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
            tracer_case(case,COULEURS[matrice[i][j]], pas)

# DEFINITION DES FONCTIONS DE DEPLACEMENTS
def deplacer_gauche():
    global matrice, position, point_inventaire,pas_inventaire
    turtle.onkeypress(None, "Left")  # Désactive la touche Left
    # traitement associé à la flèche gauche appuyée par le joueur
    turtle.onkeypress(deplacer_gauche, "Left")  # Réassocie la touche Left à la fonction deplacer_gauche
    position = (int((Y_Min - turtle.pos()[1] + 0.5 * pas) / pas + len(matrice)), int((turtle.pos()[0] - X_Min - 0.5 * pas) / pas))
    mouvement = (0, -1)
    if matrice[position[0]][position[1]-1] == 0:
        deplacer(matrice, position, mouvement)
    elif matrice[position[0]][position[1]-1] == 3:
        case = (position[0], position[1] - 1)
        franchir_porte(case,mouvement,matrice)
    elif matrice[position[0]+mouvement[0]][position[1]+mouvement[1]] == 4:
        case = (position[0]+mouvement[0], position[1]+mouvement[1])
        affichage_inventaire(inventaire,case,point_inventaire,pas_inventaire)
        ramasser_objet(matrice,position,mouvement,case)



def deplacer_droite():
    global matrice, position
    turtle.onkeypress(None, "Right")  # Désactive la touche Right
    ...  # traitement associé à la flèche doroite appuyée par le joueur
    turtle.onkeypress(deplacer_droite, "Right")  # Réassocie la touche Left à la fonction deplacer_droite
    position = (int((Y_Min - turtle.pos()[1] + 0.5 * pas) / pas + len(matrice)), int((turtle.pos()[0] - X_Min - 0.5 * pas) / pas))
    mouvement = (0, 1)
    if matrice[position[0]][position[1]+1] == 0:
        deplacer(matrice,position,mouvement)
    elif matrice[position[0]][position[1]+1] == 3:
        case = (position[0],position[1]+1)
        franchir_porte(case,mouvement,matrice)
    elif matrice[position[0] + mouvement[0]][position[1] + mouvement[1]] == 4:
        case = (position[0] + mouvement[0], position[1] + mouvement[1])
        affichage_inventaire(inventaire, case, point_inventaire, pas_inventaire)
        ramasser_objet(matrice, position, mouvement, case)


def deplacer_haut():
    global matrice, position
    turtle.onkeypress(None, "Up")  # Désactive la touche Up
    ...  # traitement associé à la flèche haut appuyée par le joueur
    turtle.onkeypress(deplacer_haut, "Up")  # Réassocie la touche Up à la fonction deplacer_haut
    position =(int((Y_Min - turtle.pos()[1] + 0.5 * pas) / pas + len(matrice)), int((turtle.pos()[0]-X_Min - 0.5 * pas)/pas))
    mouvement = (-1, 0)
    if matrice[position[0]-1][position[1]] == 0:
        tracer_case(position, COULEURS[matrice[position[0]][position[1]]], pas)
        deplacer(matrice,position,mouvement)
    elif matrice[position[0]-1][position[1]] == 3:
        case = (position[0]-1, position[1])
        franchir_porte(case,mouvement,matrice)
    elif matrice[position[0] + mouvement[0]][position[1] + mouvement[1]] == 4:
        case = (position[0] + mouvement[0], position[1] + mouvement[1])
        affichage_inventaire(inventaire, case, point_inventaire, pas_inventaire)
        ramasser_objet(matrice, position, mouvement, case)

def deplacer_bas():
    global matrice,position
    turtle.onkeypress(None, "Down")  # Désactive la touche Down
    ...  # traitement associé à la flèche bas appuyée par le joueur
    turtle.onkeypress(deplacer_bas, "Down")  # Réassocie la touche Down à la fonction deplacer_down
    position = (int((Y_Min - turtle.pos()[1] + 0.5 * pas) / pas + len(matrice)), int((turtle.pos()[0] - X_Min - 0.5 * pas) / pas))
    mouvement = (1, 0)
    if matrice[position[0]+1][position[1]] == 0:
        deplacer(matrice, position, mouvement)
    elif matrice[position[0]+1][position[1]] == 3:
        case = (position[0]+1, position[1])
        franchir_porte(case,mouvement,matrice)
    elif matrice[position[0] + mouvement[0]][position[1] + mouvement[1]] == 4:
        case = (position[0] + mouvement[0], position[1] + mouvement[1])
        affichage_inventaire(inventaire, case, point_inventaire, pas_inventaire)
        ramasser_objet(matrice, position, mouvement, case)



def deplacer(matrice, position, mouvement):
    tracer_case(position,COULEUR_VUE, pas)
    position = (position[0] + mouvement[0], position[1] + mouvement[1])
    place = coordonnees(position, pas)
    turtle.goto(place[0] + pas * 0.5, place[1] + pas * 0.5)
    turtle.dot(RATIO_PERSONNAGE * pas, COULEUR_PERSONNAGE)

####################### Fonction ramasse_objet + franchir porte
def ramasser_objet(matrice,position,mouvement,case):                 # a finir

    matrice[case[0]][case[1]] = 0                                    # changement de la valeur de case qui devient vide
    position = (position[0]+mouvement[0],position[1] + mouvement[1]) #calcul de la nouvelle position à occuper
    place = coordonnees(position, pas)                               # calcul des coordonnées auxquelles doivent se deplacer la tortue
    turtle.goto(place[0] + pas * 0.5, place[1] + pas * 0.5)
    turtle.dot(RATIO_PERSONNAGE * pas, COULEUR_PERSONNAGE)

def franchir_porte(case,mouvement,matrice):
    reponse = turtle.textinput("Question", dico_portes[case][0])

    if reponse == dico_portes[case][1]:
        matrice[position[0]+mouvement[0]][position[1]+mouvement[1]] = 0
        affichage(afficher, "La porte s'ouvre")
        turtle.listen()
        # mouvement = (0, -1)
        deplacer(matrice, position, mouvement)
    else:
        affichage(afficher, "Porte fermée")
        turtle.listen()


############### fonction creer_dictionnaire_des_objets(fichier_des_objets) créant un dictionnaire d’objets à partir du fichier correspondant,
# présenté précédemment. Cette fonction recevra en argument le nom du fichier_des_objets, et renverra un dictionnaire comportant

def creer_dictionnaire_des_objets(fichier_des_objets):
    d = {}
    with open(fichier_des_objets,encoding="utf-8") as file:
        for line in file:
            a, b = eval(line)
            d[a]=b

    return d

############# AFFICHAGE + INVENTAIRE
def affichage(turtle,texte):
    turtle.undo()
    turtle.up()
    turtle.goto(POINT_AFFICHAGE_ANNONCES)
    turtle.down()
    turtle.write(texte, font = ("Verdana", 15, "normal"))

def affichage_inventaire(turtle,case,point_inventaire, pas_inventaire):
    turtle.up()
    point_inventaire = (point_inventaire[0],point_inventaire[1]-pas_inventaire)
    turtle.goto(point_inventaire)
    turtle.down()
    turtle.write(dico_objet[case], font = ("Verdana", 12, "normal"))






# CORPS DU PROGRAMME
dico_portes = creer_dictionnaire_des_objets(fichier_questions)
dico_objet = creer_dictionnaire_des_objets(fichier_objets)

afficher = turtle.clone()                                                                  # création d'une nouvelle tortue pour la zone d'affichage
afficher.up()
afficher.hideturtle()
afficher.goto(POINT_AFFICHAGE_ANNONCES)
afficher.down()
afficher.write("AFFICHAGE", font = ("Verdana", 15, "normal"))

matrice = lire_matrice(fichier_plan)
pas = calculer_pas(matrice)

inventaire = turtle.clone()                                                                    # creation d'un clone de turlte pour l'inventaire
inventaire.up()
inventaire.hideturtle()
inventaire.goto(POINT_AFFICHAGE_INVENTAIRE)                                                    # deplacement de la tortue vers le point d'affichage d'inventaire pour écrire le titre de la zone
inventaire.down()
inventaire.write("INVENTAIRE:", align="left", font = ("Verdana", 15, "normal"))
pas_inventaire = (POINT_AFFICHAGE_INVENTAIRE[1]-ZONE_PLAN_MINI[1])//(len(dico_objet)+1)
point_inventaire = (inventaire.pos()[0],inventaire.pos()[1])



afficher_plan(matrice)                                              # Traçage du chateau


depart = coordonnees(POSITION_DEPART,pas)                           # calcul des coordonnées de départ de turtle.dot


depart = (depart[0]+pas*0.5, depart[1]+pas*0.5)                     # repositionnement de tortue au centre de la case
turtle.goto(depart)
position =(int((Y_Min - turtle.pos()[1] + 0.5 * pas) / pas + len(matrice)), int((turtle.pos()[0]-X_Min - 0.5 * pas)/pas))       # donne la position de la tortue dans la matrice

turtle.dot(pas*RATIO_PERSONNAGE,COULEUR_PERSONNAGE)
turtle.hideturtle()

turtle.listen()    # Déclenche l’écoute du clavier
turtle.onkeypress(deplacer_gauche, "Left")   # Associe à la touche Left une fonction appelée deplacer_gauche
turtle.onkeypress(deplacer_droite, "Right")
turtle.onkeypress(deplacer_haut, "Up")
turtle.onkeypress(deplacer_bas, "Down")
turtle.mainloop()    # Place le programme en position d’attente d’une action du joueur



