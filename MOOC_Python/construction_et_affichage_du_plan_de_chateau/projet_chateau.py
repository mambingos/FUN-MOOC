"""     Auteur:         Samuel MAMBINGO
        Date:           14/03/2022
        But:            Ce programme est un petit jeu du type jeu d’évasion (escape game) dans lequel le joueur commande au clavier les déplacements d’un personnage
                        au sein d’un « château » représenté en plan. Le château est constitué de cases vides (pièces, couloirs), de murs, de portes,
                        que le personnage ne pourra franchir qu’en répondant à des questions, d’objets à ramasser, qui l’aideront à trouver les réponses à ces questions
                        et de la case de sortie / quête du château. Le but du jeu est d’atteindre cette dernière.
                        Pour être éxécuté, le programme a besoin de 3 fichiers : - un fichier contenant le plan du chateau(sous forme de matrice) dont il faut s'échapper
                                                                                 - un fichier contenant les questions et réponses des portes à franchir et leur emplacement
                                                                                 - un fichier contenant l'emplacement et les objets à récuperer
                        Il n'est possible de finir le jeu si et seulement si le joueur arrive a la sortie en ayant ramassé tous les objets"""


from CONFIGS import *                                   # imports des paramètres de configuration du jeu
# import de module
import turtle

# Constantes:
(X_MIN, Y_MIN) = ZONE_PLAN_MINI
(X_MAX, Y_MAX) = ZONE_PLAN_MAXI


""" ####### DEFINITION DES FONCTIONS DE CONSTRUCTION DU CHATEAU ####### """
def lire_matrice(fichier):
    "fonction lecture du fichier : récupère les données d'un fichier et retourne une matrice qui permettra de construire le chateau"
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
    "fonction qui récupère la matrice et retourne le pas de déplacement de la tortue (dimension du carré)"
    (a, b) = (len(matrice[0]), len(matrice))
    largeur = (X_MAX-X_MIN) // a
    hauteur = (Y_MAX-Y_MIN) // b
    pas = min(largeur, hauteur)
    return pas


def coordonnees(case, pas):
    "fonction qui calcule les coordonnées auxquelles doit se déplacer la tortue pour commencer son tracé "
    cordonnees = (X_MIN + case[1]*pas, Y_MIN + (len(matrice)-case[0]) * pas)
    return cordonnees


def tracer_carre(dimension):
    " petite fonction qui trace un carre dont la dimension est donnée en paramètre "
    for i in range(4):
        turtle.forward(dimension)
        turtle.left(90)


def tracer_case(case, couleur, pas):
    " fonction de traçage de carré d'une couleur"
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(coordonnees(case, pas))
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    tracer_carre(pas)
    turtle.end_fill()


def afficher_plan(matrice):
    """ Trace pour chaque élement de la matrice un carré d'un couleur qui dépend de la veleur de l'élement de la matrice"""
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            case = (i,j)
            tracer_case(case, COULEURS[matrice[i][j]], pas)


""" ######## DEFINITION DES FONCTIONS DE DEPLACEMENTS ######## """

def deplacer_gauche():
    global matrice, position, pas
    turtle.onkeypress(None, "Left")  # Désactive la touche Left
    "traitement associé à la flèche gauche appuyée par le joueur"
    turtle.onkeypress(deplacer_gauche, "Left")      # Réassocie la touche Left à la fonction deplacer_gauche
    position = (int((Y_MIN - turtle.pos()[1] + 0.5 * pas) / pas + len(matrice)), int((turtle.pos()[0] - X_MIN - 0.5 * pas) / pas))
    mouvement = (0, -1)
    deplacer(matrice, position, mouvement, pas)


def deplacer_droite():
    global matrice, position, pas
    turtle.onkeypress(None, "Right")    # Désactive la touche Right
    """traitement associé à la flèche doroite appuyée par le joueur"""
    turtle.onkeypress(deplacer_droite, "Right")     # Réassocie la touche Left à la fonction deplacer_droite
    position = (int((Y_MIN - turtle.pos()[1] + 0.5 * pas) / pas + len(matrice)), int((turtle.pos()[0] - X_MIN - 0.5 * pas) / pas))
    mouvement = (0, 1)
    deplacer(matrice, position, mouvement, pas)


def deplacer_haut():
    global matrice, position, pas
    turtle.onkeypress(None, "Up")  # Désactive la touche Up
    ...  # traitement associé à la flèche haut appuyée par le joueur
    turtle.onkeypress(deplacer_haut, "Up")  # Réassocie la touche Up à la fonction deplacer_haut
    position = (int((Y_MIN - turtle.pos()[1] + 0.5 * pas) / pas + len(matrice)), int((turtle.pos()[0] - X_MIN - 0.5 * pas) / pas))
    mouvement = (-1, 0)
    deplacer(matrice, position, mouvement, pas)


def deplacer_bas():
    global matrice,position, pas
    turtle.onkeypress(None, "Down")  # Désactive la touche Down
    "traitement associé à la flèche bas appuyée par le joueur"
    turtle.onkeypress(deplacer_bas, "Down")
    "Réassocie la touche Down à la fonction deplacer_down"
    position = (int((Y_MIN - turtle.pos()[1] + 0.5 * pas) / pas + len(matrice)), int((turtle.pos()[0] - X_MIN - 0.5 * pas) / pas))
    mouvement = (1, 0)
    deplacer(matrice, position, mouvement, pas)


def deplacer(matrice, position, mouvement,pas):
    """ gère le deplacement de la tortue en fonction du mouvement associé et de la nature de la case vers laquelle se déplace le personnage """
    if matrice[position[0]+mouvement[0]][position[1]+mouvement[1]] == 0:
        "la tortue se déplace vers une case vide"
        tracer_case(position,COULEUR_VUE, pas)
        position = (position[0] + mouvement[0], position[1] + mouvement[1])
        place = coordonnees(position, pas)
        turtle.goto(place[0] + pas * 0.5, place[1] + pas * 0.5)
        turtle.dot(RATIO_PERSONNAGE * pas, COULEUR_PERSONNAGE)
    elif matrice[position[0]+mouvement[0]][position[1]+mouvement[1]] == 3:
        """la tortue se déplace vers une porte"""
        case = (position[0] + mouvement[0], position[1]+mouvement[1])
        franchir_porte(case, mouvement, matrice)
    elif matrice[position[0]+mouvement[0]][position[1]+mouvement[1]] == 4:
        """ la tortue se déplace vers un objet """
        case = (position[0] + mouvement[0], position[1] + mouvement[1])
        ramasser_objet(matrice, position, mouvement, case)
    elif matrice[position[0] + mouvement[0]][position[1] + mouvement[1]] == 2:
        """ la tortue se déplace vers la sortie """
        if len(object_recuperes) == len(dico_objet):
            tracer_case(position, COULEUR_VUE, pas)
            affichage(afficher,"Vous avez gagné !")
            position = (position[0] + mouvement[0], position[1] + mouvement[1])
            place = coordonnees(position, pas)
            turtle.goto(place[0] + pas * 0.5, place[1] + pas * 0.5)
            turtle.dot(RATIO_PERSONNAGE * pas, COULEUR_PERSONNAGE)
        else:
            affichage(afficher, "Cette porte est fermée")



""" ######## DEFINITION DES FONCTIONS DE GESTION DES OBJETS ET DES PORTES ######## """
def ramasser_objet(matrice,position,mouvement,case):
    """ retrace la case actuelle en vue, rammasse l'objet et l'ajoute à l'ensemble inventaire,
    appelle les différents affichages et avance sur la case de l'objet"""
    tracer_case(position, COULEUR_VUE, pas)
    matrice[case[0]][case[1]] = 0  # changement de la valeur de case qui devient vide
    tracer_case(case, COULEUR_CASES, pas)
    affichage_inventaire(inventaire, case, point_inventaire, pas_inventaire)
    affichage(afficher, "Vous avez trouvé: " + dico_objet[case])
    object_recuperes.add(dico_objet[case])
    position = (position[0]+mouvement[0],position[1] + mouvement[1])    #calcul de la nouvelle position à occuper
    place = coordonnees(position, pas)                                  # calcul des coordonnées auxquelles doivent se deplacer la tortue
    turtle.goto(place[0] + pas * 0.5, place[1] + pas * 0.5)
    turtle.dot(RATIO_PERSONNAGE * pas, COULEUR_PERSONNAGE)


def franchir_porte(case,mouvement,matrice):
    """remplace la porte par une case vide si la réponse à la question est juste, sinon la porte reste fermée"""
    reponse = turtle.textinput("Question", dico_portes[case][0])
    if reponse == dico_portes[case][1]:
        matrice[position[0]+mouvement[0]][position[1]+mouvement[1]] = 0
        tracer_case(case, COULEUR_CASES, pas)
        affichage(afficher, "La porte s'ouvre")
        turtle.listen()
        deplacer(matrice, position, mouvement, pas)
    else:
        affichage(afficher, "Cette porte est fermée")
        turtle.listen()



def creer_dictionnaire_des_objets(fichier_des_objets):
    """Elle permet de créer un dictionnaire objets ou portes qui sera utilisé pour ramasser les objets et franchir les portes
# Elle prend pour argument le nom du fichier_des_objets et renvoit un dictionnaire comportant"""
    d = {}
    with open(fichier_des_objets,encoding="utf-8") as file:
        for line in file:
            a, b = eval(line)
            d[a]=b

    return d

""" ######## DEFINITION DES FONCTIONS DE GESTION DE L'AFFICHAGE PRINCIPAL ET L'AFFICHAGE DE L'INVENTAIRE ####### """
def affichage(turtle,texte):
    """Elle gère l'affichage général à l'aide de sa propre tortue (efface l'ancienne donnée affichée pour afficher la suivante"""
    turtle.undo()
    turtle.up()
    turtle.goto(POINT_AFFICHAGE_ANNONCES)
    turtle.down()
    turtle.write(texte, font = ("Verdana", 13, "normal"))


def affichage_inventaire(turtle,case,point_inventaire, pas_inventaire):
    """Elle gère l'affichage de l'inventaire à l'aide de sa propre tortue"""
    turtle.up()
    point_inventaire = (turtle.position()[0], turtle.position()[1]-pas_inventaire)
    turtle.goto(point_inventaire)
    turtle.down()
    turtle.write(dico_objet[case], font = ("Verdana", 10, "normal"))


"""" ######## CORPS DU PROGRAMME ###########  """
dico_portes = creer_dictionnaire_des_objets(fichier_questions)
dico_objet = creer_dictionnaire_des_objets(fichier_objets)

afficher = turtle.clone()                                     # création d'une nouvelle tortue pour la zone d'affichage
afficher.hideturtle()
afficher.penup()
afficher.goto(POINT_AFFICHAGE_ANNONCES)
afficher.pendown()
afficher.write("AFFICHAGE", font = ("Verdana", 13, "normal"))


inventaire = turtle.clone()                                                                    # creation d'un clone de turlte pour l'inventaire
inventaire.penup()
inventaire.hideturtle()
inventaire.goto(POINT_AFFICHAGE_INVENTAIRE)                                                    # deplacement de la tortue vers le point d'affichage d'inventaire pour écrire le titre de la zone
inventaire.pendown()
inventaire.write("INVENTAIRE:", align="left", font = ("Verdana", 13, "normal"))
pas_inventaire = (POINT_AFFICHAGE_INVENTAIRE[1]-ZONE_PLAN_MINI[1])//(len(dico_objet)+1)
point_inventaire = (inventaire.pos()[0], inventaire.pos()[1])

matrice = lire_matrice(fichier_plan)
pas = calculer_pas(matrice)
object_recuperes = set()                                            # ensemble des objets récupérés
turtle.tracer(20)                                                   # accelere l'affichage du chateau
afficher_plan(matrice)                                              # Traçage du chateau

depart = coordonnees(POSITION_DEPART,pas)                           # calcul des coordonnées de départ de turtle.dot
depart = (depart[0]+pas*0.5, depart[1]+pas*0.5)                     # repositionnement de tortue au centre de la case
turtle.up()
turtle.goto(depart)
position =(int((Y_MIN - turtle.pos()[1] + 0.5 * pas) / pas + len(matrice)), int((turtle.pos()[0]-X_MIN - 0.5 * pas)/pas))       # donne la position de la tortue dans la matrice
turtle.dot(pas*RATIO_PERSONNAGE,COULEUR_PERSONNAGE)
turtle.hideturtle()

turtle.listen()    # Déclenche l’écoute du clavier
turtle.onkeypress(deplacer_gauche, "Left")   # Associe à la touche Left une fonction appelée deplacer_gauche
turtle.onkeypress(deplacer_droite, "Right")
turtle.onkeypress(deplacer_haut, "Up")
turtle.onkeypress(deplacer_bas, "Down")
turtle.mainloop()    # Place le programme en position d’attente d’une action du joueur



