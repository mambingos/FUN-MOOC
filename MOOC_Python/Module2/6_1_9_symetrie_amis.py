"""     Auteur:         Samuel MAMBINGO
        Date:           01/03/2022
        But:            Écrire une fonction symetrise_amis qui reçoit un dictionnaire d d’amis où les clés sont des prénoms et les valeurs,
                        des ensembles de prénoms représentant les amis de chacun.
                        Cette fonction modifie le dictionnaire d de sorte que si une clé prenom1 contient prenom2 dans l’ensemble de ses amis, l’inverse soit vrai aussi.
                        La fonction accepte un second paramètre englobe.
                            Si englobe est vrai, la fonction ajoutera les éléments nécessaires pour symétriser le dictionnaire d.
                            Sinon, la fonction enlèvera les éléments nécessaires pour symétriser d."""
from copy import deepcopy

def symetrise_amis(d,englobe):
    a = deepcopy(d)
    if englobe == True:
        for prenom in a:
            for amis in a[prenom]:
                if amis in a[prenom]:
                    d[amis].add(prenom)
    elif englobe == False:
        for prenom in a:
            for amis in a[prenom]:
                if prenom not in a[amis]:
                    d[prenom].remove(amis)









d = {'Thierry': {'Michelle', 'Bernadette'},
     'Michelle': {'Thierry'},
     'Bernadette': set()}
print(d)
# symetrise_amis(d, True)
symetrise_amis(d, True)
print(d)