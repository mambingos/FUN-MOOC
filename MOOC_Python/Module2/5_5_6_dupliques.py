"""     Auteur:         Samuel MAMBINGO
        Date:           21/02/2022
        But:            Écrire une fonction dupliques qui reçoit une séquence en paramètre.
                        La fonction doit renvoyer la valeur booléenne True si la séquence passée en paramètre contient
                        des éléments dupliqués, et la valeur booléenne False sinon.."""

def dupliques(liste):
    res = False
    a = 0
    for i in range(len(liste)):
        a += 1
        for n in range(a, len(liste)):
            res = liste[i] == liste[n]
            if res == True:
                break
            else:
                res = False
                continue
    return res
print(dupliques(['a', 'b', 'c', 'b']))


