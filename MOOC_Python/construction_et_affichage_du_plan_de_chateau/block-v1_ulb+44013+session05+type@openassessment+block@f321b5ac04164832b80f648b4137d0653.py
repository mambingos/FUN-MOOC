# -*- coding: utf-8 -*-

"""
LE PROJET « CHÂTEAU DU PYTHON DES NEIGES
Jeu de labyrinthe isssu du cours FUN MOOC "Apprendre à coder avec Python
Auteur : Pierre-Alexandre
Date: 22-04-18
Version 1

"""

# importation des modules et fichier
import turtle
from CONFIGS import *
# pas de constante global car importées avec le fichier CONFIGS

# ----------- Définitions des fonction -------------

# ----------- Fonctions de dessins -----------------


# Définition du pas de la matrice en prenant en compte les dimenssions de la zone (l x L)
# utilisation du // pour tomber sur un chiffre entier
def pas(matrix):
    largeur = abs(ZONE_PLAN_MINI[0]) + ZONE_PLAN_MAXI[0]
    longeur = abs(ZONE_PLAN_MINI[1]) + ZONE_PLAN_MAXI[1]
    return min((largeur // len(matrix[0])), (longeur // len(matrix)))


# Détermination des coordonnés pixel du personnage en fonction sa position dans la matrice
def coordo_perso(ligne, colonne, dim):
    x = ZONE_PLAN_MINI[0] + dim * (0.5 + colonne)
    y = ZONE_PLAN_MAXI[1] - dim * (0.5 + ligne)
    return x, y


# Détermination des coordonnés pixel des cases
def coordo_carre(ligne, colonne, dim):
    x = ZONE_PLAN_MINI[0] + dim * colonne
    y = ZONE_PLAN_MAXI[1] - dim * ligne
    return x, y


# fonction qui permet de tracer un carré
def carre(longeur, couleur):
    turtle.hideturtle()
    turtle.color(COULEUR_EXTERIEUR, couleur)
    turtle.begin_fill()
    for i in range(4):  # traçage du carré
        turtle.forward(longeur)
        turtle.right(90)
    turtle.end_fill()


# fonction permettant de tracé le carré de la couleur vue en fonction de ses coordonées dans la matrice
# avec un choix de la couleur
def carre_vu(ligne, colonne, couleur):
    x_carre, y_carre = coordo_carre(ligne, colonne, cote)
    turtle.up()
    turtle.goto(x_carre, y_carre)
    turtle.down()
    carre(cote, couleur)


# création d'un personnage indépendant (2eme tortue)
def perso(x, y, dim, couleur):
    personnage = turtle.Turtle()
    personnage.speed(0)
    personnage.up()
    personnage.goto(x, y)
    personnage.dot(RATIO_PERSONNAGE * dim, couleur)


# traçage du labyrinthe
# map_castel = liste délimitant le plan (matrice) du chateau
# long = longueur du carré
def plan(map_castel, long):
    # initialisation du laby au coin sup gauche
    x = -240
    y = 200
    turtle.tracer(0)
    for j in map_castel:
        for i in j:
            turtle.up()
            turtle.goto(x, y)
            turtle.down()
            carre(long, COULEURS[i])
            x += long
        x = -240
        y -= long


# Effaçage des zones de texte pour actualisation du texte
def effacer_zone(zone):
    turtle.tracer(0)
    message = turtle.Turtle()  # Creaton d'une tortue pour l'affichage des annonces
    x, y = zone
    message.hideturtle()
    message.up()
    # Traçage du rectangle blanc pour effacer la zone
    message.goto(x - 3, y + 15)
    message.down()
    message.color(COULEUR_EXTERIEUR)
    message.begin_fill()
    for i in range(2):
        message.forward(POINT_AFFICHAGE_ANNONCES[1] * 2)
        message.right(90)
        message.forward(POINT_AFFICHAGE_ANNONCES[1] - POINT_AFFICHAGE_INVENTAIRE[1])
        message.right(90)
    message.end_fill()


# Affichage des messages annonces et inventaires
def affiche_message(texte, zone):
    effacer_zone(zone)
    turtle.tracer(0)
    message = turtle.Turtle()  # Creaton d'une tortue pour l'affichage des annonces
    x, y = zone
    # Ecriture du message Zone annonce
    message.up()
    message.goto(x, y)
    message.color(COULEUR_ECRITURE)
    message.write(texte)


# ----------- Fonctions de lecture de fichiers -----------------


# lecture du fichier et enregistrement du plan (matrice) sous form de liste
def lire_matrice(fichier):
    with open(fichier, encoding='utf-8') as Fichier:
        return [[int(colonne) for colonne in ligne.split()] for ligne in Fichier]


# lecture des fichiers pour renvoie vers un dictionnaire
def lire_dicos(fichier):
    dico = {}
    with open(fichier, encoding='utf-8') as Fichier:
        for i in Fichier:
            a, b = eval(i)
            dico[a] = b
    return dico


# Question
def interrogation(ligne, colonne):
    affiche_message("La porte est fermée ! ", POINT_AFFICHAGE_ANNONCES)
    question = portes[(ligne, colonne)][0]
    reponse = turtle.textinput("Répondez à la question pour ouvrir la porte :", question)
    turtle.listen()
    return reponse


# ----------- Fonctions de gestions des déplacements -----------------


# Empêcher de jouer à nouveau
def stop():
    return None


def fin():
    turtle.onkeypress(stop, "Down")
    turtle.onkeypress(stop, "Up")
    turtle.onkeypress(stop, "Left")
    turtle.onkeypress(stop, "Right")


# Détermination des nouvelles coordoné en pixel du personnage en fonction du sens du déplacement
def new_coor_perso(x, y, dim, sens):
    if sens == "Down":
        y -= dim
    if sens == "Up":
        y += dim
    if sens == "Right":
        x += dim
    if sens == "Left":
        x -= dim
    return x, y


# Deplacement du personnage en créeant un nouveau point
# 1) passe le carré dans la couleur vue
# 2) Changment de position si la nvelle case est un objet ou une porte alors elle devient blanche
# 3) Création du persnnage
def new_point(x_p, y_p, dim, matrix, ligne_matrix, colonne_matrix, l_provisoire, c_provisoire, sens):
    carre_vu(ligne_matrix, colonne_matrix, COULEUR_VUE)
    ligne_matrix = l_provisoire
    colonne_matrix = c_provisoire
    x_p, y_p = new_coor_perso(x_p, y_p, dim, sens)
    if matrix[ligne_matrix][colonne_matrix] == 3 or matrix[ligne_matrix][colonne_matrix] == 4:
        carre_vu(ligne_matrix, colonne_matrix, COULEUR_CASES)

    perso(x_p, y_p, dim, COULEUR_PERSONNAGE)


# Rassemblement des fonction de déplacement pour créer le déplacement
# 1) déplacement du personnage
# 2) définssion et retour des nouvelles coordonnées pixel et matrice
def deplacement(x_p, y_p, dim, matrix, ligne_matrix, colonne_matrix, l_provisoire, c_provisoire, sens):
    new_point(x_p, y_p, dim, matrix, ligne_matrix, colonne_matrix, l_provisoire, c_provisoire, sens)
    new_x_perso, new_y_perso = new_coor_perso(x_p, y_p, dim, sens)
    new_ligne_matrice, new_colonne_matrice = l_provisoire, c_provisoire
    return new_x_perso, new_y_perso, new_ligne_matrice, new_colonne_matrice


# Deplacements
def deplacer_bas():
    # definition de variable globale
    global x_perso, y_perso, cote, matrice, ligne_matrice, colonne_matrice, objets, sac, portes

    # Sens de déplacement
    sens = "Down"

    # determination de la valeur (0,1,2,3 ou 4) de la future position dans la matrice
    l_provisoire = ligne_matrice + 1
    c_provisoire = colonne_matrice + 0
    val_pos_provisoire = matrice[l_provisoire][c_provisoire]

    # Si couloir Ok on passe
    if val_pos_provisoire == 0:
        x_perso, y_perso, ligne_matrice, colonne_matrice = \
            deplacement(x_perso, y_perso, cote, matrice, ligne_matrice, colonne_matrice, l_provisoire, c_provisoire,
                        sens)

    # Si Sortie
    elif val_pos_provisoire == 2:
        # Si tous les objets
        if len(sac) == len(objets):
            x_perso, y_perso, ligne_matrice, colonne_matrice = \
                deplacement(x_perso, y_perso, cote, matrice, ligne_matrice, colonne_matrice, l_provisoire, c_provisoire,
                            sens)
            affiche_message("Vous avez gagné ! ", POINT_AFFICHAGE_ANNONCES)
            fin()
        else:
            affiche_message("Il vous manque des objets ! ", POINT_AFFICHAGE_ANNONCES)

    # Si Porte
    elif val_pos_provisoire == 3:
        reponse = interrogation(l_provisoire, c_provisoire)

        if reponse == portes[(l_provisoire, c_provisoire)][1]:
            x_perso, y_perso, ligne_matrice, colonne_matrice = \
                deplacement(x_perso, y_perso, cote, matrice, ligne_matrice, colonne_matrice, l_provisoire, c_provisoire,
                            sens)
            matrice[ligne_matrice][colonne_matrice] = 0  # passage à 0 si on repasse sur la même case
            affiche_message("Bonne réponse, la porte est ouverte ! ", POINT_AFFICHAGE_ANNONCES)
        else:
            affiche_message("Mauvaise réponse, la porte est toujours fermée ! ", POINT_AFFICHAGE_ANNONCES)

    # Si Objet
    elif val_pos_provisoire == 4:
        x_perso, y_perso, ligne_matrice, colonne_matrice = \
            deplacement(x_perso, y_perso, cote, matrice, ligne_matrice, colonne_matrice, l_provisoire, c_provisoire,
                        sens)
        matrice[ligne_matrice][colonne_matrice] = 0
        sac.append(objets[(ligne_matrice, colonne_matrice)])
        # Affichage message
        for i in range(len(sac)):
            # POINT_AFFICHAGE_INVENTAIRE[1]-20*(i+1))) permet de décaler le y en fonction du nombre d'onjet
            # récolté pour éviter les supperpositions
            affiche_message(f"Objet N°{i + 1} : {sac[i]}", (POINT_AFFICHAGE_INVENTAIRE[0],
                                                            POINT_AFFICHAGE_INVENTAIRE[1] - 20 * (i + 1)))

    # pas besoin de deffinir si hors zone ou 1 car si ce n'est pas 0 ou 2 ou 3 ou 4 le prog ne fait rien


# Deplacements
def deplacer_droite():
    # definition de variable globale
    global x_perso, y_perso, cote, matrice, ligne_matrice, colonne_matrice, objets, sac, portes

    # Sens de déplacement
    sens = "Right"

    # determination de la valeur (0,1,2,3 ou 4) de la future position dans la matrice
    l_provisoire = ligne_matrice + 0
    c_provisoire = colonne_matrice + 1
    val_pos_provisoire = matrice[l_provisoire][c_provisoire]

    # Si couloir Ok on passe
    if val_pos_provisoire == 0:
        x_perso, y_perso, ligne_matrice, colonne_matrice = \
            deplacement(x_perso, y_perso, cote, matrice, ligne_matrice, colonne_matrice, l_provisoire, c_provisoire,
                        sens)

    # Si Sortie
    elif val_pos_provisoire == 2:
        # Si tous les objets
        if len(sac) == len(objets):
            x_perso, y_perso, ligne_matrice, colonne_matrice = \
                deplacement(x_perso, y_perso, cote, matrice, ligne_matrice, colonne_matrice, l_provisoire, c_provisoire,
                            sens)
            affiche_message("Vous avez gagné ! ", POINT_AFFICHAGE_ANNONCES)
            fin()
        else:
            affiche_message("Il vous manque des objets ! ", POINT_AFFICHAGE_ANNONCES)

    # Si Porte
    elif val_pos_provisoire == 3:
        reponse = interrogation(l_provisoire, c_provisoire)

        if reponse == portes[(l_provisoire, c_provisoire)][1]:
            x_perso, y_perso, ligne_matrice, colonne_matrice = \
                deplacement(x_perso, y_perso, cote, matrice, ligne_matrice, colonne_matrice, l_provisoire, c_provisoire,
                            sens)
            matrice[ligne_matrice][colonne_matrice] = 0  # passage à 0 si on repasse sur la même case
            affiche_message("Bonne réponse, la porte est ouverte ! ", POINT_AFFICHAGE_ANNONCES)
        else:
            affiche_message("Mauvaise réponse, la porte est toujours fermée ! ", POINT_AFFICHAGE_ANNONCES)

    # Si Objet
    elif val_pos_provisoire == 4:
        x_perso, y_perso, ligne_matrice, colonne_matrice = \
            deplacement(x_perso, y_perso, cote, matrice, ligne_matrice, colonne_matrice, l_provisoire, c_provisoire,
                        sens)
        matrice[ligne_matrice][colonne_matrice] = 0
        sac.append(objets[(ligne_matrice, colonne_matrice)])
        # Affichage message
        for i in range(len(sac)):
            # POINT_AFFICHAGE_INVENTAIRE[1]-20*(i+1))) permet de décaler le y en fonction du nombre d'onjet
            # récolté pour éviter les supperpositions
            affiche_message(f"Objet N°{i + 1} : {sac[i]}", (POINT_AFFICHAGE_INVENTAIRE[0],
                                                            POINT_AFFICHAGE_INVENTAIRE[1] - 20 * (i + 1)))


# Deplacements
def deplacer_haut():
    # definition de variable globale
    global x_perso, y_perso, cote, matrice, ligne_matrice, colonne_matrice, objets, sac, portes

    # Sens de déplacement
    sens = "Up"

    # determination de la valeur (0,1,2,3 ou 4) de la future position dans la matrice
    l_provisoire = ligne_matrice - 1
    c_provisoire = colonne_matrice + 0
    val_pos_provisoire = matrice[l_provisoire][c_provisoire]

    # Si couloir Ok on passe
    if val_pos_provisoire == 0:
        x_perso, y_perso, ligne_matrice, colonne_matrice = \
            deplacement(x_perso, y_perso, cote, matrice, ligne_matrice, colonne_matrice, l_provisoire, c_provisoire,
                        sens)

    # Si Sortie
    elif val_pos_provisoire == 2:
        # Si tous les objets
        if len(sac) == len(objets):
            x_perso, y_perso, ligne_matrice, colonne_matrice = \
                deplacement(x_perso, y_perso, cote, matrice, ligne_matrice, colonne_matrice, l_provisoire, c_provisoire,
                            sens)
            affiche_message("Vous avez gagné ! ", POINT_AFFICHAGE_ANNONCES)
            fin()
        else:
            affiche_message("Il vous manque des objets ! ", POINT_AFFICHAGE_ANNONCES)

    # Si Porte
    elif val_pos_provisoire == 3:
        reponse = interrogation(l_provisoire, c_provisoire)

        if reponse == portes[(l_provisoire, c_provisoire)][1]:
            x_perso, y_perso, ligne_matrice, colonne_matrice = \
                deplacement(x_perso, y_perso, cote, matrice, ligne_matrice, colonne_matrice, l_provisoire, c_provisoire,
                            sens)
            matrice[ligne_matrice][colonne_matrice] = 0  # passage à 0 si on repasse sur la même case
            affiche_message("Bonne réponse, la porte est ouverte ! ", POINT_AFFICHAGE_ANNONCES)
        else:
            affiche_message("Mauvaise réponse, la porte est toujours fermée ! ", POINT_AFFICHAGE_ANNONCES)

    # Si Objet
    elif val_pos_provisoire == 4:
        x_perso, y_perso, ligne_matrice, colonne_matrice = \
            deplacement(x_perso, y_perso, cote, matrice, ligne_matrice, colonne_matrice, l_provisoire, c_provisoire,
                        sens)
        matrice[ligne_matrice][colonne_matrice] = 0
        sac.append(objets[(ligne_matrice, colonne_matrice)])
        # Affichage message
        for i in range(len(sac)):
            # POINT_AFFICHAGE_INVENTAIRE[1]-20*(i+1))) permet de décaler le y en fonction du nombre d'onjet
            # récolté pour éviter les supperpositions
            affiche_message(f"Objet N°{i + 1} : {sac[i]}", (POINT_AFFICHAGE_INVENTAIRE[0],
                                                            POINT_AFFICHAGE_INVENTAIRE[1] - 20 * (i + 1)))


# Deplacements
def deplacer_gauche():
    # definition de variable globale
    global x_perso, y_perso, cote, matrice, ligne_matrice, colonne_matrice, objets, sac, portes

    # Sens de déplacement
    sens = "Left"

    # determination de la valeur (0,1,2,3 ou 4) de la future position dans la matrice
    l_provisoire = ligne_matrice + 0
    c_provisoire = colonne_matrice - 1
    val_pos_provisoire = matrice[l_provisoire][c_provisoire]

    # Si couloir Ok on passe
    if val_pos_provisoire == 0:
        x_perso, y_perso, ligne_matrice, colonne_matrice = \
            deplacement(x_perso, y_perso, cote, matrice, ligne_matrice, colonne_matrice, l_provisoire, c_provisoire,
                        sens)

    # Si Sortie
    elif val_pos_provisoire == 2:
        # Si tous les objets
        if len(sac) == len(objets):
            x_perso, y_perso, ligne_matrice, colonne_matrice = \
                deplacement(x_perso, y_perso, cote, matrice, ligne_matrice, colonne_matrice, l_provisoire, c_provisoire,
                            sens)
            affiche_message("Vous avez gagné ! ", POINT_AFFICHAGE_ANNONCES)
            fin()
        else:
            affiche_message("Il vous manque des objets ! ", POINT_AFFICHAGE_ANNONCES)

    # Si Porte
    elif val_pos_provisoire == 3:
        reponse = interrogation(l_provisoire, c_provisoire)

        if reponse == portes[(l_provisoire, c_provisoire)][1]:
            x_perso, y_perso, ligne_matrice, colonne_matrice = \
                deplacement(x_perso, y_perso, cote, matrice, ligne_matrice, colonne_matrice, l_provisoire, c_provisoire,
                            sens)
            matrice[ligne_matrice][colonne_matrice] = 0  # passage à 0 si on repasse sur la même case
            affiche_message("Bonne réponse, la porte est ouverte ! ", POINT_AFFICHAGE_ANNONCES)
        else:
            affiche_message("Mauvaise réponse, la porte est toujours fermée ! ", POINT_AFFICHAGE_ANNONCES)

    # Si Objet
    elif val_pos_provisoire == 4:
        x_perso, y_perso, ligne_matrice, colonne_matrice = \
            deplacement(x_perso, y_perso, cote, matrice, ligne_matrice, colonne_matrice, l_provisoire, c_provisoire,
                        sens)
        matrice[ligne_matrice][colonne_matrice] = 0
        sac.append(objets[(ligne_matrice, colonne_matrice)])
        # Affichage message
        for i in range(len(sac)):
            # POINT_AFFICHAGE_INVENTAIRE[1]-20*(i+1))) permet de décaler le y en fonction du nombre d'onjet
            # récolté pour éviter les supperpositions
            affiche_message(f"Objet N°{i + 1} : {sac[i]}", (POINT_AFFICHAGE_INVENTAIRE[0],
                                                            POINT_AFFICHAGE_INVENTAIRE[1] - 20 * (i + 1)))


# ----------- Programme principale -----------------


# 1) ouvertures des fichiers et captures des éléments dans les variables +
#  création d'une liste d'objet vide à implémenter
matrice = lire_matrice(fichier_plan)
portes = lire_dicos("dico_portes.txt")
objets = lire_dicos("dico_objets.txt")
sac = []

# 2) calcul de la dimenssion (dim) du carré et définitions des positions
cote = pas(matrice)
ligne_matrice, colonne_matrice = POSITION_DEPART
x_perso, y_perso = coordo_perso(ligne_matrice, colonne_matrice, cote)

# 3) traçage du plan, des messages et du personnage
plan(matrice, cote)
affiche_message("Bienvenu dans le labyrinthe du Chateau du Python des neige", POINT_AFFICHAGE_ANNONCES)
affiche_message("Inventaire", POINT_AFFICHAGE_INVENTAIRE)
perso(x_perso, y_perso, cote, COULEUR_PERSONNAGE)

# 4) Interrection avec le joueur
turtle.listen()
turtle.onkeypress(deplacer_bas, 'Down')
turtle.onkeypress(deplacer_droite, 'Right')
turtle.onkeypress(deplacer_haut, 'Up')
turtle.onkeypress(deplacer_gauche, 'Left')
turtle.mainloop()
