"""     Auteur:         Samuel MAMBINGO
        Date:           20/02/2022
        But:            Écrire une fonction intersection(v, w) qui calcule l’intersection entre deux chaînes de caractères v et w.
                        On définit l’intersection de deux mots comme étant la plus grande partie commune à ces deux mots.
                        Par exemple, l’intersection de « programme » et « grammaire » est « gramm ».
                        Si les deux chaînes n’ont aucun caractère en commun, la fonction retourne la chaîne vide, ''.
                        Si plusieurs solutions sont possibles, la fonction retournera la sous-chaîne d’indice minimal dans v.
                        Par exemple, intersection('bbaacc', 'aabb') renvoie 'bb'.."""

def intersection (v,w):
    longueur = len(v)
    m = len(w)
    res =""
    for i in range(longueur):
        if len(res) >= longueur - i:
            break

        for j in range(i + len(res), longueur):
            if v[i:j+1] not in w:
                break
            if len(v[i:j+1]) >= len(res):
                res = v[i:j+1]

    return res

print(intersection('programme', 'grammaire'))
