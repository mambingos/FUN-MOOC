"""     Auteur:         Samuel MAMBINGO
        Date:           01/03/2022
        But:            Écrire une fonction valeurs(dico) qui doit fournir, à partir du dictionnaire donné en paramètre,
                        une liste des valeurs du dictionnaire triées selon leur clé."""

def valeur(dico):
    dico =sorted(dico.items(), key= lambda t: t[0], reverse=False)
    dico = dict(dico)

    n = len(dico)
    print(n)
    d = []
    for key in dico:
        d.append(dico[key])

    return d
print(valeur({'three': 'trois', 'two': 'deux', 'one': 'un'}))
