'''
ecrit par Yohan en avril 2022

Petit jeu dans le cadre du FUNmooc Cours "Apprendre à coder avec Python"

Le programme récupère trois fichiers en entrée qui permettent de dessiner le plan d'un chateau
Les deux autres fichiers servent pour lister les objets et les enigmes du chateau 

à faire :
- centrer la zone de la carte en largeur et longueur par rapport aux autres zones
'''
import turtle
from CONFIGS import *

ZONE_ANNONCE=(-200,205)#Titre de la zone Annonce)
A=POINT_AFFICHAGE_ANNONCES[0]
B=POINT_AFFICHAGE_ANNONCES[1]
EXTREMITE_GH=(POINT_AFFICHAGE_ANNONCES[1],POINT_AFFICHAGE_ANNONCES[0])
EXTREMITE_DH=(240,240)
INVENTAIRE_G=70
INVENTAIRE_TXTX=80
INVENTAIRE_TXTY=160
ANNONCE_BAS=205
ECART_TXT=20
POLICE_TITRE=("Arial",12, "normal")
POLICE_AUTRE=('Arial',10, 'normal')
Xplan=ZONE_PLAN_MAXI[0]
Yplan=ZONE_PLAN_MAXI[1]

def annonce(pos,obst):
    '''Ecrit dans la zone annonce le résultat du déplacement
    en cas de d'item trouvé
    renvoie également si le déplacement demandé est impossible
    La fonction prend en entrée la position et le chiffre qui correspond au type d'obstacle
    La position sert uniquement l'obstacle
    La fonction est aussi appelé en cas de questions
    la fonction ne retourne rien et ne modifie pas les entrées'''
    annonce_text=''
    annonce_pen.clear()
    if obst==0 :
        annonce_text=''
    elif obst==1 :
        annonce_text='Chemin Impossible'    
    elif obst==2 :
        annonce_text='Sortie'
        turtle.onkeypress(None, "Left")
        turtle.onkeypress(None, "Right")
        turtle.onkeypress(None, "Down")
        turtle.onkeypress(None, "Up")
    elif obst==3 :
        annonce_text='Cette porte est fermée.'
    elif obst==4 :
        ramasser_objet(pos)
        annonce_text='Vous avez trouvé : '+Objets[pos]
    elif obst==5 :
        annonce_text="La porte s'ouvre"

    elif obst==6 :
        annonce_text="Mauvaise Reponse"    
    annonce_pen.up()
    annonce_pen.goto(ZONE_ANNONCE)
    annonce_pen.pencolor("blue")
    annonce_pen.down()
    annonce_pen.write(annonce_text, font=POLICE_AUTRE)

def poser_question(matriceQ,pos) :
    '''
    Pose la question correspondant à la position dans la matrice
    au déplacement que veut faire le personnage
    Si la réponse à la question est VRAIE la matrice du jeu est modifié
    (n'utilise pas une copie de matrice)
    La fonction ne renvoie  rien mais relance turtle.listen()
    ne modifie pas la position 
    '''
    pos=pos[0],pos[1]
    reponse = turtle.textinput('question',Questions[pos][0])
    if reponse ==Questions[pos][1]:
        matriceQ[pos[0]][pos[1]]=0
        annonce(pos,5)
        tracer_case(pos, COULEUR_COULOIR,nbrCase)
    else : annonce(pos,6)
    turtle.listen()

def inventaire():
    '''
    fonction pour écrire dans la zone inventaire l'objet ramassé
    utilise le dictionnaire des objets
    ne renvoie rien
    '''
    X=0
    inventaire_pen.clear()
    for k in Objets_trouve :
        inventaire_pen.up()
        inventaire_pen.goto(INVENTAIRE_TXTX,INVENTAIRE_TXTY-ECART_TXT*X)
        inventaire_pen.pencolor("green")
        inventaire_pen.down()
        if len(k)<24: # pour faire un retour à la ligne et que le texte tienne dans le zone inventaire
            inventaire_pen.write(k, font=POLICE_AUTRE)
        else :
            for nombre in range(round(len(k)/ECART_TXT)): 
                inventaire_pen.up()
                inventaire_pen.goto(INVENTAIRE_TXTX,INVENTAIRE_TXTY-ECART_TXT*X)
                inventaire_pen.down()
                ecrit=k[0+19*nombre:19*(1+nombre)]+'↲'
                inventaire_pen.write(ecrit,font=POLICE_AUTRE)
                X+=1
            inventaire_pen.up() # possible d'arrondir avec +1 dans la boucle for mais implique le caractère ↲ en plus 
            inventaire_pen.goto(INVENTAIRE_TXTX,INVENTAIRE_TXTY-ECART_TXT*X)
            inventaire_pen.down()
            ecrit=k[0+19*(nombre+1):]
            inventaire_pen.write(ecrit,font=POLICE_AUTRE)
        X+=1

def ramasser_objet(pos):
    '''
    utilise le dico "Objets" et la position du joueur pour ajouter dans la liste objets trouvés
    MODIFIE Objets_trouve
    '''
    matrice[pos[0]][pos[1]]=0
    Objets_trouve.append(Objets[(pos[0],pos[1])])
    return inventaire()
    
def matrice_plan(fichier):
    ''' lis le fichier du plan en entrée pour renvoyer :
    - la matrice;
    - le nombre de ligne.
    - le nombre de Colonne.
    '''
    fichier=open(fichier,'r',encoding='utf-8')  
    Tab_Lignes=[]
    for l in fichier :
        texte=''
        for c in l:
            texte=texte+c
        texte=texte.replace("\n"," ")
        a=texte.split()
        Tab_Lignes.append(a)
    matriceJeu=trans_matrice(Tab_Lignes.copy())
    fichier.close()
    nbrCase_lig=len(matriceJeu)
    nbrCase_Col=len(matriceJeu[0])
    return (matriceJeu,nbrCase_lig,nbrCase_Col)

def trans_matrice(tab):
    '''fonction qui transforme chaque str de la matrice en int
    renvoie la matrice transformée
    '''
    for m in range(0,len(tab)) :
        for n in range(0,len(tab[m])) :
            tab[m][n]=int(tab[m][n])
    return tab

#Gestion des déplacements du joueur
def deplacer_gauche():
    ''' Verifie si le joueur peut se déplacer vers la direction indiquée
    modifie la position du joueur
    Verifie si la case de destination est libre, un obstacle ou impossible
    '''
    turtle.onkeypress(None, "Left")
    if matrice[joueur[0]][joueur[1]-1]==0 or matrice[joueur[0]][joueur[1]-1]==2 or matrice[joueur[0]][joueur[1]-1]==4 :
        tracer_case(joueur, COULEUR_VUE, nbrCase)
        joueur[1]=joueur[1]-1
        place_joueur(joueur)
        annonce((joueur[0],joueur[1]),matrice[joueur[0]][joueur[1]])
    elif matrice[joueur[0]][joueur[1]-1]==3:
        annonce((joueur[0],joueur[1]),matrice[joueur[0]][joueur[1]-1])
        poser_question(matrice,[joueur[0],joueur[1]-1])    
    else : annonce((joueur[0],joueur[1]),1)
    turtle.onkeypress(deplacer_gauche, "Left")
def deplacer_droite():
    ''' Verifie si le joueur peut se déplacer vers la direction indiquée
    modifie la position du joueur
    Verifie si la case de destination est libre, un obstacle ou impossible
    '''
    turtle.onkeypress(None, "Right")
    if matrice[joueur[0]][joueur[1]+1]==0 or matrice[joueur[0]][joueur[1]+1]==2 or matrice[joueur[0]][joueur[1]+1]==4  :
        tracer_case(joueur, COULEUR_VUE, nbrCase)
        joueur[1]=joueur[1]+1
        place_joueur(joueur)
        annonce((joueur[0],joueur[1]),matrice[joueur[0]][joueur[1]])
    elif matrice[joueur[0]][joueur[1]+1]==3:
        annonce((joueur[0],joueur[1]),matrice[joueur[0]][joueur[1]+1])
        poser_question(matrice,[joueur[0],joueur[1]+1])
    else : annonce((joueur[0],joueur[1]),1)
    turtle.onkeypress(deplacer_droite, "Right")
def deplacer_bas():
    ''' Verifie si le joueur peut se déplacer vers la direction indiquée
    modifie la position du joueur
    Verifie si la case de destination est libre, un obstacle ou impossible
    '''
    turtle.onkeypress(None, "Down")
    if matrice[joueur[0]+1][joueur[1]]==0 or matrice[joueur[0]+1][joueur[1]]==2 or matrice[joueur[0]+1][joueur[1]]==4 :
        tracer_case(joueur, COULEUR_VUE, nbrCase)
        joueur[0]=joueur[0]+1
        place_joueur(joueur)
        annonce((joueur[0],joueur[1]),matrice[joueur[0]][joueur[1]])
    elif matrice[joueur[0]+1][joueur[1]]==3:
        annonce((joueur[0],joueur[1]),matrice[joueur[0]+1][joueur[1]])
        poser_question(matrice,[joueur[0]+1,joueur[1]])
    else : annonce((joueur[0],joueur[1]),1)
    turtle.onkeypress(deplacer_bas, "Down")
def deplacer_haut():
    ''' Verifie si le joueur peut se déplacer vers la direction indiquée
    modifie la position du joueur
    Verifie si la case de destination est libre, un obstacle ou impossible
    '''
    turtle.onkeypress(None, "Up")
    if matrice[joueur[0]-1][joueur[1]]==0 or matrice[joueur[0]-1][joueur[1]]==2 or matrice[joueur[0]-1][joueur[1]]==4:
        tracer_case(joueur, COULEUR_VUE, nbrCase)
        joueur[0]=joueur[0]-1
        place_joueur(joueur)
        annonce((joueur[0],joueur[1]),matrice[joueur[0]][joueur[1]])
    elif matrice[joueur[0]-1][joueur[1]]==3:
        annonce((joueur[0],joueur[1]),matrice[joueur[0]-1][joueur[1]])
        poser_question(matrice,[joueur[0]-1,joueur[1]])
    else : annonce((joueur[0],joueur[1]),1)
    turtle.onkeypress(deplacer_haut, "Up")
#fin de la gestion des déplacements  
  
def creer_dictionnaire_des_objets(fichier_des_objets):
    '''
    fonction qui utilise un fichier txt en entrée pour créer le dictionnaire des objet
    Le dictionnaire a pour index les coordonnées des cases
    '''
    f=open(fichier_des_objets,encoding='utf-8')
    dico_objet={}
    for l in f :
        g,h=eval(l)
        dico_objet[g]=h
    return dico_objet
    
def place_joueur(tuple):
    '''recoit des coordonnées de la matrice du chateau et place le
    joueur sur cette matrice
    le programme fait appel une première fois à cette fonction à
    partir de la première ligne de la matrice
    Turtle finit en mode up'''
    turtle.up()
    D,E=coordonnees(tuple,nbrCase)
    turtle.goto(D+nbrCase*RATIO_PERSONNAGE/2,E)
    turtle.color(COULEUR_PERSONNAGE)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(nbrCase*RATIO_PERSONNAGE/2)
    turtle.end_fill()
    turtle.up()
    
def calculer_pas(d,c):
    '''
    fonction qui utilise le nombre de colonnes et lignes de la matrice
    Renvoie la taille (pixel) d'une case du plan
    Cette taille est utilisée pour la conversion vers le coordonnée en case
    '''
    largeur=(Xplan-A)/c
    hauteur=(Yplan-A)/d
    return int(min(largeur,hauteur))

def coordonnees(case, pas):
    '''transforme la case de la matrice en coordonnée de zone turtle'''
    X=ZONE_PLAN_MINI[0]+case[1]*pas
    Y=200-nbrCase-case[0]*pas
    return X,Y

def tracer_carre(dimension):
    '''
    trace un carré dont le coté est la dimension entrée en paramètre
    le dessin  commence à partir de la position turtle
    Turtle finit en position up
    '''
    turtle.width(0)
    turtle.down()
    turtle.begin_fill()
    X=turtle.xcor()
    Y=turtle.ycor()
    turtle.goto(X+dimension,Y)
    turtle.goto(X+dimension,Y+dimension)
    turtle.goto(X,Y+dimension)
    turtle.goto(X,Y)
    turtle.end_fill()
    turtle.up()
    
def tracer_case(case, couleur, pas):
    '''
    Utilise les coordonnes du chateau, la couleur de la case et longueur d'une case
    pour tracer une case du plan
    utilise les fonctions annexes suivantes: tracer_carre et coordonnees
    Finit en turtle up 
    '''
    turtle.color(couleur)
    turtle.up()
    turtle.goto(coordonnees(case,pas))
    tracer_carre(pas)

def tracer_rectangle(Point1,Point2,Point3,Point4):
    '''
    Trace un rectangle en prenant les coordonnées de chacun des coins du carré
    '''
    turtle.up()
    turtle.goto(Point1)
    turtle.down()
    turtle.goto(Point2)
    turtle.goto(Point3)
    turtle.goto(Point4)
    turtle.goto(Point1)
    turtle.up()
    
#parametre Turtle
turtle.tracer(0, 0)#permet d'accélérer les animations et diminue le nombre de crash de turle
turtle.hideturtle()
turtle.width(2)
inst2turtle=turtle.Turtle()
inst3turtle=turtle.Turtle()
annonce_pen=inst2turtle.getpen()# permet de faire une instance Turtle spécifique pour les annonces
inventaire_pen=inst3turtle.getpen()# pour la zone inventaire

b=matrice_plan(fichier_plan)
matrice=b[0]
nbrCase=calculer_pas(b[1],b[2])
tracer_rectangle(ZONE_PLAN_MINI,POINT_AFFICHAGE_ANNONCES,EXTREMITE_DH,EXTREMITE_GH)#zone dessin
tracer_rectangle((INVENTAIRE_G,Yplan),(B,Yplan),EXTREMITE_GH,(INVENTAIRE_G,A))#zone inventaire
tracer_rectangle(POINT_AFFICHAGE_ANNONCES,EXTREMITE_DH,(B,ANNONCE_BAS),(A,ANNONCE_BAS))#zone Annonce

turtle.goto(-40,220)
turtle.down()
turtle.write('Annonce :', font=(POLICE_TITRE))
turtle.up()
turtle.goto(100,200-20)
turtle.down()
turtle.write('Inventaire :', font=(POLICE_TITRE))

for L,i in enumerate(matrice) :#enumerate permet de conserver le numero de ligne de la matrice
    for C,j in enumerate(i) :    
        if j == 0 and L==0 :
            joueur=[L,C]#remplace la constante POSITION_DEPART pour fonctionner sur d'autre fichier que celui fournit         
        tracer_case((L,C),COULEURS[j],nbrCase)

place_joueur(joueur)
turtle.listen()    # Déclenche l’écoute du clavier
Objets=creer_dictionnaire_des_objets(fichier_objets)
Questions=creer_dictionnaire_des_objets(fichier_questions)
Objets_trouve=[]
turtle.onkeypress(deplacer_gauche, "Left")   # Associe à la touche Left une fonction appelée deplacer_gauche
turtle.onkeypress(deplacer_droite, "Right")
turtle.onkeypress(deplacer_haut, "Up")
turtle.onkeypress(deplacer_bas, "Down")
turtle.mainloop()    # Place le programme en position d’attente d’une action du joueur