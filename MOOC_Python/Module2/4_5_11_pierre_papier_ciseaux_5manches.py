"""     Auteur:         Samuel MAMBINGO
        Date:           18/02/2022
        But:            Écrire un programme qui réalise 5 manches du jeu Pierre-feuille-ciseaux entre l’ordinateur et le joueur. Chaque manche va consister en :
                        la génération (pseudo) aléatoire d’un nombre entre 0 et 2 compris, à l’aide de la fonction randint du module random, qui va représenter le coup de l’ordinateur (0 valant Pierre, 1, Feuille et 2, Ciseaux) ;
                        la lecture en entrée (input) d’une valeur entière entre 0 et 2 compris qui représente le coup du joueur ; l’affichage du résultat sous une des formes :
                            coup_o bat coup_j : points
                            coup_o est battu par coup_j : points
                            coup_o annule coup_j : points
                        où coup_o et coup_j sont respectivement le coup de l’ordinateur et du joueur : "Pierre" s’il a joué 0, "Feuille" s’il a joué 1 et "Ciseaux" s’il a joué 2.
                        points donne le résultat des manches jusqu’à présent sachant que le compteur points part de zéro, et est incrémenté de un chaque fois que le joueur gagne une manche, et décrémenté de un chaque fois que l’ordinateur gagne une manche (les match nuls ne modifiant pas le compteur points).
                        À la fin des cinq manches, votre programme affichera : Perdu, Nul ou Gagné suivant que le compteur est négatif, nul ou strictement positif."""
# importation du module
import random

# definition des constantes

# definition de la fonction bat:
def bat(joueur_1, joueur_2):
    res = joueur_1 == 0 and joueur_2 == 2\
        or joueur_1 == 1 and joueur_2 == 0\
        or joueur_1 == 2 and joueur_2 == 1
    return res

# definition du gain:
def gain (joueur_1, joueur_2):
    if bat(joueur_1, joueur_2) == True:
        g = 1
    elif joueur_1 == joueur_2:
        g = 0
    else:
        g = -1
    return g




# definition de la fonction print:
def printer(t):
    a = {"0": "Pierre", "1": "Feuille", "2": "Ciseaux"}
    print(a[str(joueur_2)], end =" ")
    if bat(joueur_1, joueur_2) == True:

        print("est battu par", end =" ")
        print(a[str(joueur_1)], end =" : ")
        print(t + gain(joueur_1, joueur_2), end = "\n")

    elif joueur_1 == joueur_2:
        b= 0
        print("annule", end =" ")
        print(a[str(joueur_1)], end =" : ")
        print(t + gain(joueur_1, joueur_2), end = "\n")

    else:
        b = -1
        print("bat", end =" ")
        print(a[str(joueur_1)], end=" : ")
        print(t + gain(joueur_1, joueur_2), end= "\n")

    return t + gain(joueur_1, joueur_2)



# programme principal
t = 0
s = int(input())
random.seed(s)
for i in range(5):
    joueur_1 = int(input())
    joueur_2 = random.randint(0, 2)
    printer(t)
    t += gain(joueur_1, joueur_2)


if t > 0:
    print("Gagné")
elif t == 0:
    print("Nul")
else:
    print("Perdu")
