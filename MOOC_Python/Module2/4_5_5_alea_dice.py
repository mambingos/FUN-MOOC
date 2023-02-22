"""     Auteur:         Samuel MAMBINGO
        Date:           08/02/2022
        But:            simule le lancé de 3 dés et vérifie s'ils forment un 421 ou non"""

# importation des modules#

import random


# Définition de la fonction #

def alea_dice(s):
    random.seed(s)
    a = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    b = sorted(a, key = None, reverse = True)
    e = [4, 2, 1]
    return b==e
    print(b==e)

    print(a)
    print(b)


alea_dice(25)