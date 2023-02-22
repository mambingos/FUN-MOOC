"""     Auteur:         Samuel MAMBINGO
        Date:           01/03/2022
        But:            Écrire une fonction construction_dict_amis qui reçoit une liste de couples (prenom1, prenom2)
                        signifiant que prenom1 déclare prenom2 comme étant son ami.
                        La fonction construit et renvoie un dictionnaire dont les clés sont les prénoms des personnes nommées,
                        et la valeur de chaque entrée est l’ensemble des amis de la personne"""

def construction_dict_amis(amis):
    liste = {}
    for prenom1,prenom2 in amis:
        if prenom1 not in liste:
            liste[prenom1] = {prenom2}
        else:
            liste[prenom1].add(prenom2)
        if prenom2 not in liste:
            liste[prenom2] = set()
    return liste
print(construction_dict_amis([('Bernadette', 'Thierry'), ('Pierre', 'Thierry')]))





