"""*********************************************************************************************************************
ESCAPE GAME CHATEAU PYTHON

Projet lié au FUN-MOOC (ULB) 'Programmer en Python'
Auteur : Christophe Mécrin
Date : 27/02/2022

Ce fichier a besoin, dans le même dossier, du fichier CONFIGS.py (constantes globales),
ainsi que des 3 fichiers ressources (noms en bas de CONFIGS)

Principe du jeu :
La boule parcourt un labyrinthe, collecte des indices et répond à des énigmes pour ouvrir des portes.
Elle doit parvenir à la sortie.

Note de l'auteur :
******************
Mon code devenait confus et la gestion des variables complexe.
J'ai fait des tutos sur Youtube et suis arrivé à cette programmation en classes. Je crois que c'est ce qu'on appelle
la programmation orientée objet. C'est beaucoup plus facile de s'y retrouver et de gérer les variables.
Je me suis efforcé d'utiliser au mieux ce que j'ai compris de ces outils. J'ai en tout cas beaucoup appris.

La plupart des fonctions prennent place dans les classes et bénéficient ainsi naturellement de toutes les variables
de la classe. Seules deux sont situées hors des classes, en statique : elles ne font appel qu'à des variables globales
(noms des fichiers ressources).

Outre game.run() qui supervise le fonctionnement général, la fonction la plus importante est sans doute
game.mouvement() : elle gère la finalisation d'un déplacement et les interactions avec les cases spéciales.
*********************************************************************************************************************"""

import time
import turtle
from CONFIGS import *

FONT = 'Arial'
FONT_SIZE_TITRE = 12
FONT_SIZE_TEXTE = 10
MAX_CAR_SUR_UNE_LIGNE_INVENTAIRE = 30
DUREE_TRANSITION_INTRO = 2  # secondes (doit être inférieure à la durée d'affichage des annonces)
DUREE_AFFICHAGE_ANNONCES = 4  # secondes


class Carte(turtle.Turtle):
    """ Lit le fichier plan, importe les données de carte et affiche la carte """

    # constantes de la classe, calculée à partir des constantes de CONFIGS.py
    LARGEUR_ZONE_CARTE = ZONE_PLAN_MAXI[0] - ZONE_PLAN_MINI[0]
    HAUTEUR_ZONE_CARTE = ZONE_PLAN_MAXI[1] - ZONE_PLAN_MINI[1]

    def __init__(self):
        super().__init__()
        self.hideturtle()

        # extrait la matrice du fichier
        self.matrice = lire_matrice(fichier_plan)
        self.nb_cases_hauteur = len(self.matrice)
        self.nb_cases_largeur = len(self.matrice[0])

        # calcule le pas et les dimensions de la carte
        self.pas = self.calculer_pas()
        self.hauteur_carte = self.nb_cases_hauteur * self.pas
        self.largeur_carte = self.nb_cases_largeur * self.pas

        # point de départ (coin supérieur gauche de la carte)
        self.carte_x0 = ZONE_PLAN_MINI[0]
        self.carte_y0 = ZONE_PLAN_MAXI[1]

        # plan
        self.afficher_plan()

    def calculer_pas(self):
        """ Renvoie la dimension (maximale) d'une case """
        return int(min(self.LARGEUR_ZONE_CARTE / self.nb_cases_largeur,
                       self.HAUTEUR_ZONE_CARTE / self.nb_cases_hauteur))

    def get_couleur(self, case):
        """ Renvoie la couleur de la case en argument """
        return self.matrice[case[0]][case[1]]

    def set_couleur(self, case, couleur):
        """ Passe la case en argument à la couleur spécifiée en second argument """
        self.matrice[case[0]][case[1]] = couleur
        self.tracer_case(case)

    def coordonnees(self, case, centre=False):
        """ Prend en argument un couple d'indices(ligne i, colonne j) et un booléen centre, par défaut égal à False ;
        renvoie les coordonnées du point supérieur gauche (ou du centre si centre == True) de la case ;
        utilise les coordonnées du coin supérieur gauche de la zone de carte """
        x = self.carte_x0 + self.pas * case[1]
        y = self.carte_y0 - self.pas * case[0]
        if centre:
            x += self.pas // 2
            y -= self.pas // 2
        return x, y

    def tracer_carre(self, couleur):
        """ Trace un carré de la couleur en argument, la position du turtle est gérée juste avant dans tracer_case() """
        self.down()
        # couleur des traits
        self.pencolor(COULEUR_CASES)
        # couleur de remplissage
        self.fillcolor(COULEURS[couleur])
        self.begin_fill()
        for i in range(4):
            self.forward(self.pas)
            self.right(90)
        self.end_fill()
        self.up()

    def tracer_case(self, case, couleur=None):
        """ Reçoit les indices (ligne, colonne) d'une case et la trace ;
        peut recevoir un argument supplémentaire : un numéro de couleur, si on veut tracer dans une couleur différente
        de celle prévue dans le plan (utile dans l'intro) """
        # si aucune couleur n'est passée en argument
        if couleur is None:
            # on va chercher la couleur prévue dans le plan
            couleur = self.get_couleur(case)
        # coin supérieur gauche de la case
        self.goto(self.coordonnees(case))
        self.tracer_carre(couleur)

    def afficher_plan(self):
        """ Appelle tracer_case() sur chaque case, trace les couloirs et les murs """
        for i in range(self.nb_cases_hauteur):
            for j in range(self.nb_cases_largeur):
                # on trace les murs et les couloirs
                if self.get_couleur((i, j)) not in {2, 3, 4}:
                    self.tracer_case((i, j))
                # les cases objets, portes et sortie sont tracées comme des couloirs
                else:
                    self.tracer_case((i, j), couleur=0)

    def on(self, couleur):
        """ Deux fonctions utilisées dans l'intro
        La première trace les cases de la couleur en argument (objets, portes ou sortie)"""
        for i in range(self.nb_cases_hauteur):
            for j in range(self.nb_cases_largeur):
                if self.get_couleur((i, j)) == couleur:
                    self.tracer_case((i, j))

    def off(self, couleur):
        """ La seconde "éteint" les cases de la couleur en argument (elle repasse dessus en couleur couloirs) """
        for i in range(self.nb_cases_hauteur):
            for j in range(self.nb_cases_largeur):
                if self.get_couleur((i, j)) == couleur:
                    self.tracer_case((i, j), couleur=0)


class Annonces(turtle.Turtle):
    """ Gère la zone d'annonces """

    def __init__(self, carte):
        """ Récupère la carte en arguments pour pouvoir appeler carte.on() et carte.off() dans l'intro """
        super().__init__()
        self.carte = carte
        self.penup()
        self.hideturtle()
        # variable de mémorisation de l'annonce diffusée
        self.ancienne_annonce = ['', '']
        self.annonce = ['', '']
        self.font_titre = (FONT, FONT_SIZE_TITRE, 'bold')
        self.font_texte = (FONT, FONT_SIZE_TEXTE, 'normal')
        self.memo_time = 0
        # intro
        self.affiche('Bienvenue dans le chateau du Python Neigeux')
        self.texte_intro = ['Indices tu trouveras',
                            ', portes tu ouvriras',
                            ', sortie tu gagneras']
        self.num_intro = 0
        self.couleur_allumee = None
        self.introducing = True

    def ecrire_titre(self, texte):
        """ Efface le texte précédent, place la tortue dans la bonne position, écrit le titre
        et se positionne en prévision d'une éventuelle deuxième ligne """
        self.clear()
        self.setpos(POINT_AFFICHAGE_ANNONCES)
        self.write(texte, font=self.font_titre)
        self.sety(self.ycor() - int(FONT_SIZE_TITRE * 2))

    def ecrire_texte(self, texte):
        """ Argument move=True : le turtle se déplace en écrivant, utile pour le texte de l'intro affiché en 3 fois """
        self.write(texte, move=True, font=self.font_texte)

    def affiche(self, titre, texte=''):
        """ Prend en argument le titre du texte à afficher et, éventuellement, une deuxième ligne """
        # mémorise l'annonce affichée
        self.annonce[0] = titre
        self.annonce[1] = texte
        self.ancienne_annonce = self.annonce
        # écrit le titre
        self.ecrire_titre(titre)
        # écrit le texte s'il y en a un
        if texte != '':
            self.ecrire_texte(texte)
        # lance le chrono
        self.memo_time = time.time()

    def chrono(self):
        """ Retourne le temps écoulé (en secondes) depuis le lancement du chrono
        (pendant l'intro ou à l'affichage d'une nouvelle annonce) """
        return time.time() - self.memo_time

    def intro(self):
        """ Appelée par game.intro(), présente le jeu au lancement """
        # si la durée de transition est dépassée
        if self.chrono() > DUREE_TRANSITION_INTRO:
            # si l'intro n'est pas finie
            if self.num_intro < len(self.texte_intro):
                # si ce n'est pas le premier passage
                if self.couleur_allumee is not None:
                    # éteint la couleur allumée
                    self.carte.off(self.couleur_allumee)
                # allume la couleur suivante (num_intro: 0 -> 2, alors que couleur_allumee: 4 -> 2)
                self.couleur_allumee = 4 - self.num_intro
                self.carte.on(self.couleur_allumee)
                # écrit le texte correspondant
                self.ecrire_texte(self.texte_intro[self.num_intro])
                # incrémente le compteur
                self.num_intro += 1
                # remet le chrono à zéro
                self.memo_time = time.time()
            # si l'intro est finie
            else:
                self.introducing = False
                # on rallume les cases portes et objets
                self.carte.on(3)
                self.carte.on(4)

    def efface(self):
        """ Appelée dans game.run()
        Si l'annonce n'a pas changé depuis plus de {DUREE_AFFICHAGE_ANNONCES} secondes, réinitialise """
        if self.annonce == self.ancienne_annonce and self.chrono() > DUREE_AFFICHAGE_ANNONCES:
            self.annonce = ['', '']
            self.clear()


class Enigmes:
    """ Lit le fichier portes, importe les données dans le dictionnaire et gère les questions/réponses """

    def __init__(self):
        self.dictionnaire = creer_dictionnaire(fichier_questions)

    def bonne_reponse(self, case):
        """ Affiche la question dans la fenêtre d'input, renvoie un booléen : 'la réponse est bonne'
        Attention : il faudra veiller à relancer l'écoute du clavier juste après """
        return turtle.textinput('Proposez une réponse', self.dictionnaire[case][0]) == self.dictionnaire[case][1]


class Objets(turtle.Turtle):
    """ Lit le fichier objets, importe les données dans le dictionnaire, gère et affiche l'inventaire """

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.dictionnaire = creer_dictionnaire(fichier_objets)
        self.font_titre = (FONT, FONT_SIZE_TITRE, 'bold')
        self.font_texte = (FONT, FONT_SIZE_TEXTE, 'normal')
        self.texte = ''

    def get_indice(self, case): return self.dictionnaire[case]

    def ecrire_titre(self):
        self.setpos(POINT_AFFICHAGE_INVENTAIRE)
        self.write('Inventaire', move=False, align='left', font=self.font_titre)
        self.sety(self.ycor() - int(FONT_SIZE_TITRE * 2))

    def ecrire_ligne(self, ligne):
        self.write(ligne, move=False, align='left', font=self.font_texte)
        self.sety(self.ycor() - int(FONT_SIZE_TEXTE * 2))

    def ecrire_texte(self, texte):
        """ Écrit le texte de l'indice sur une ou plusieurs lignes, en fonction de MAX_CAR_SUR_UNE_LIGNE_INVENTAIRE """
        # si le texte tient sur une ligne, on l'écrit
        if len(texte) <= MAX_CAR_SUR_UNE_LIGNE_INVENTAIRE:
            self.ecrire_ligne(f'- {texte}')

        # sinon
        else:

            # on le décompose en une liste de mots, qu'on dénombre
            liste_mots = texte.split(' ')
            nb_mots_a_ecrire = len(liste_mots)

            # et on le reconstitue sur autant de lignes qu'il le faut
            # initialisation des variables de boucle
            ligne_a_afficher = '- '
            nb_mots_ecrits = 0  # compteur des mots traités, pour ne rien oublier

            # tant qu'il reste des mots à afficher
            while nb_mots_ecrits < nb_mots_a_ecrire:
                # si la longueur de la ligne le permet
                if len(ligne_a_afficher) + len(liste_mots[0]) <= MAX_CAR_SUR_UNE_LIGNE_INVENTAIRE:
                    # on ajoute le premier mot à la ligne, en le supprimant de la liste qui reste à afficher
                    ligne_a_afficher += liste_mots.pop(0) + ' '
                    nb_mots_ecrits += 1
                # sinon on écrit la ligne
                else:
                    self.ecrire_ligne(ligne_a_afficher)
                    ligne_a_afficher = '  '
            # finalement, on écrit la dernière ligne (les lignes complètes ont déjà été affichées)
            self.ecrire_ligne(ligne_a_afficher)

    def ramasser_objet(self, case):
        """ Mise à jour de l'inventaire """
        # actualise l'affichage
        if self.xcor() == 0:
            self.ecrire_titre()
        self.ecrire_texte(self.dictionnaire[case])
        # supprime l'objet du dictionnaire
        self.dictionnaire.pop(case)


class Boule(turtle.Turtle):
    """ Crée le joueur, gère les déplacements """

    def __init__(self, instance_de_jeu):
        """ Récupère l'instance de jeu en argument (donc accès à carte, objets et enigmes) """
        super().__init__()

        # récupération de game
        self.game = instance_de_jeu

        # apparence et réglages
        self.pencolor(COULEUR_PERSONNAGE)
        self.hideturtle()
        self.penup()

        # position par défaut (couple)
        self.position = POSITION_DEPART
        self.teleporte(self.position)

    def teleporte(self, position):
        """ Prend une case (couple) en argument et y téléporte la boule ; utilise la fonction carte.coordonnees() ;
        efface et retrace la boule ; appelée dans game.mouvement() quand les conditions sont vérifiées """
        # efface l'ancienne boule
        self.clear()
        # enregistre la nouvelle position
        self.position = position
        # calcule les coordonnées correspondantes (centre de la case) et effectue le déplacement
        self.goto(self.game.carte.coordonnees(position, centre=True))
        # trace la nouvelle boule
        self.dot(self.game.carte.pas * RATIO_PERSONNAGE, COULEUR_PERSONNAGE)

    def mouvement(self, mouvement):
        """ Prend un mouvement en argument, calcule la position visée
        et appelle game.mouvement() qui traitera le mouvement demandé """
        # case visée par le mouvement
        position_visee = (self.position[0] + mouvement[0], self.position[1] + mouvement[1])
        self.game.mouvement(position_visee)

    def rien(self):
        """ Fonction qui ne fait rien, utilisée ci-dessous
        pour désactiver momentanément les touches flèches du clavier """
        pass

    def deplacer_gauche(self):
        """ 4 fonctions appelées par demande_deplacement(), qui appellent la fonction mouvement() avec le mouvement
        adequat en argument (on prend soin de désactiver les touches pendant que mouvement() fait son travail
        pour qu'elle ne soit pas appelée plusieurs fois) """
        turtle.onkeypress(self.rien, "Left")   # Désactive la touche
        self.mouvement((0, -1))
        turtle.onkeypress(self.game.presse_gauche, "Left")  # Réassocie la touche à la fonction

    def deplacer_droite(self):
        turtle.onkeypress(self.rien, "Right")
        self.mouvement((0, 1))
        turtle.onkeypress(self.game.presse_droite, "Right")

    def deplacer_bas(self):
        turtle.onkeypress(self.rien, "Down")
        self.mouvement((1, 0))
        turtle.onkeypress(self.game.presse_bas, "Down")

    def deplacer_haut(self):
        turtle.onkeypress(self.rien, "Up")
        self.mouvement((-1, 0))
        turtle.onkeypress(self.game.presse_haut, "Up")

    def deplacer(self):
        """ Fonction appelée dans game.run() :
        récupère le dictionnaire d'état du clavier et appelle les fonctions de déplacement si besoin """
        pressed = self.game.pressed
        if pressed['Haut']:
            self.deplacer_haut()
        elif pressed['Bas']:
            self.deplacer_bas()
        elif pressed['Droite']:
            self.deplacer_droite()
        elif pressed['Gauche']:
            self.deplacer_gauche()


class Game:
    """ Lance les instances de toutes les autres classes, contient les fonctions intro() et run() """
    LARGEUR_ECRAN = 540
    HAUTEUR_ECRAN = 580

    def __init__(self):
        """ On définit ici tout ce qui doit être accompli au lancement de l'instance de jeu """

        # variable booléenne de jeu, stoppe la boucle run() si False
        self.running = False

        # fenêtre turtle
        self.screen = self.creer_screen()
        self.screen.listen()

        # dictionnaire de lecture du clavier
        self.pressed = {'Haut': False,
                        'Bas': False,
                        'Droite': False,
                        'Gauche': False}

        # lance les instances des autres classes
        self.carte = Carte()
        self.objets = Objets()
        self.enigmes = Enigmes()
        self.boule = Boule(self)  # passe game en argument : boule disposera de toutes les infos
        self.annonces = Annonces(self.carte)

        # lance le chrono
        self.memo_time = time.time()

    def creer_screen(self):
        """ Création de la fenêtre turtle """
        screen = turtle.Screen()
        turtle.setup(self.LARGEUR_ECRAN, self.HAUTEUR_ECRAN)
        screen.tracer(0)  # on ne trace qu'à la mise à jour de l'écran (méthode screen.update())
        screen.title('Le Python neigeux')
        screen.bgcolor(COULEUR_EXTERIEUR)
        return screen

    """ 8 fonctions qui règlent les valeurs du dictionnaire d'état du clavier """
    def presse_haut(self): self.pressed['Haut'] = True
    def relache_haut(self): self.pressed['Haut'] = False
    def presse_bas(self): self.pressed['Bas'] = True
    def relache_bas(self): self.pressed['Bas'] = False
    def presse_droite(self): self.pressed['Droite'] = True
    def relache_droite(self): self.pressed['Droite'] = False
    def presse_gauche(self): self.pressed['Gauche'] = True
    def relache_gauche(self): self.pressed['Gauche'] = False

    def entrees_clavier(self):
        """ Associe les touches du clavier aux fonctions créées ci-dessus (pour modifier le dictionnaire de clavier)
        Les fonctions onkeypress et onkeyrelease (appuyé et relâché) admettent 2 arguments :
            - une fonction sans argument (d'où la nécessité des 8 fonctions au-dessus, 2 par touche à vérifier)
            - une touche du clavier (ici une touche flèche) """
        self.screen.onkeypress(self.presse_haut, 'Up')
        self.screen.onkeyrelease(self.relache_haut, 'Up')
        self.screen.onkeypress(self.presse_bas, 'Down')
        self.screen.onkeyrelease(self.relache_bas, 'Down')
        self.screen.onkeypress(self.presse_droite, 'Right')
        self.screen.onkeyrelease(self.relache_droite, 'Right')
        self.screen.onkeypress(self.presse_gauche, 'Left')
        self.screen.onkeyrelease(self.relache_gauche, 'Left')

    def vide_clavier(self):
        """ Réinitialise le dictionnaire de clavier """
        for direction in self.pressed:
            self.pressed[direction] = False

    def mouvement(self, position_visee):
        """ Cette fonction est le centre :
        A chaque mouvement demandé au clavier, elle est appelée par boule.mouvement()
        pour décider si le mouvement se fera et dans quelles conditions (cases spéciales) """
        # si le mouvement ne sort pas de la carte
        if position_visee[0] in range(self.carte.nb_cases_hauteur) \
                and position_visee[1] in range(self.carte.nb_cases_largeur):

            # couleur de la case visée
            couleur = self.carte.get_couleur(position_visee)

            # paramètre du mouvement, permet de gérer la sortie
            move = False
            if couleur in {0, 4, 5}:
                move = True

            # si c'est la sortie
            if couleur == 2:
                # s'il reste des indices à collecter
                if len(self.objets.dictionnaire) > 0:
                    self.annonces.affiche('Nul ne sort', 's\'il n\'a collecté toutes les clés')
                else:
                    move = True
                    self.annonces.affiche('Bravo !', 'Vous avez triomphé de toutes les embûches')
                    self.carte.set_couleur(position_visee, 0)
                    self.running = False

            # si c'est une porte (énigme)
            elif couleur == 3:
                # réinitialise le dictionnaire de clavier
                self.vide_clavier()
                self.annonces.affiche('Cette porte est fermée', 'Pour l\'ouvrir, répondez à la question')
                if self.enigmes.bonne_reponse(position_visee):  # contient un turtle.textinput()
                    # ouverture de la porte
                    self.annonces.affiche('La porte est ouverte')
                    self.carte.set_couleur(position_visee, 0)
                else:
                    self.annonces.affiche('Mauvaise réponse', 'La porte reste fermée')
                # on relance l'écoute du clavier après un turtle.textinput()
                self.screen.listen()

            # un objet
            elif couleur == 4:
                self.carte.set_couleur(position_visee, 0)
                self.annonces.affiche('Vous avez trouvé un indice', self.objets.get_indice(position_visee))
                # actualise l'affichage de l'inventaire
                self.objets.ramasser_objet(position_visee)

            # si le mouvement doit être réalisé
            if move:
                # on passe la case actuelle en couleur 'vue'
                self.carte.set_couleur(self.boule.position, 5)
                # on effectue le mouvement
                self.boule.teleporte(position_visee)

    def intro(self):
        """ Boucle de l'introduction """
        while self.annonces.introducing:
            self.annonces.intro()
            self.screen.update()

    def run(self):
        """ Boucle du jeu """
        self.running = True
        self.entrees_clavier()
        while self.running:
            self.boule.deplacer()
            self.annonces.efface()
            self.screen.update()
            time.sleep(0.06)


def lire_matrice(fichier):
    """ Lit le fichier plan et renvoie la matrice de la carte """
    matrice = []
    with open(fichier, 'r', encoding='utf-8') as fichier_texte:
        for ligne in fichier_texte:
            ligne_donnees = []
            for c in ligne:
                if c not in ' \n':
                    ligne_donnees.append(int(c))
            matrice.append(ligne_donnees)
    return matrice


def creer_dictionnaire(fichier):
    """ Ouverture du fichier dico_portes ou dico_objets et construction du dictionnaire correspondant """
    dictionnaire = {}
    with open(fichier, 'r', encoding='utf-8') as fichier_texte:
        for ligne in fichier_texte:
            cle, valeur = eval(ligne)
            dictionnaire[cle] = valeur
    return dictionnaire


# instance du jeu
game = Game()
# boucle d'introduction
game.intro()
# boucle principale
game.run()
# maintient l'écran ouvert
game.screen.mainloop()
