"""     Auteur:         Samuel MAMBINGO
        Date:           03/03/2022
        But:            Écrire une fonction booléenne bonne_planete(diametre) qui reçoit en paramètre un nombre représentant le diamètre, en mètres, d'une planète candidate.
                        La fonction retourne la valeur True ou False selon que la planète convient ou non.
                        Écrire ensuite un programme qui lit un diamètre depuis l'entrée et affiche
                         - la chaîne de caractères "Bonne planète" si le résultat de l'appel à la fonction bonne_planete est True
                         - la chaîne de caractères "Trop petite" sinon"""
# import de pi
from math import pi

#definition de constantes
TAILLE_ARBRE = 50
N_ARBRE = 1000
TAILLE_ARBRES = TAILLE_ARBRE * N_ARBRE

# definition de fonction booléenne (vrai si la planète convient)
def bonne_planete(diametre):
    return TAILLE_ARBRES <= 4 * pi * (diametre/2)**2

# programme principal (affiche le texte"bonne planète" si la planète convient, sinon "mauvaise planète
diametre = int(input())
if bonne_planete(diametre) == True:
    print("Bonne planète")
else:
    print("Trop petite")
