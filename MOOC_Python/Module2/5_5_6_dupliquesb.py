"""     Auteur:         Samuel MAMBINGO
        Date:           21/02/2022
        But:            Écrire une fonction dupliques qui reçoit une séquence en paramètre.
                        La fonction doit renvoyer la valeur booléenne True si la séquence passée en paramètre contient
                        des éléments dupliqués, et la valeur booléenne False sinon.."""

def dupliques(liste):
    res = False

    for i in range(len(liste)):
        res = liste[i] in liste[i+1:len(liste)+1]
        if res == True:
            break



    return res

print(dupliques(['a', 'b', 'c', 'b']))
print(dupliques('abcde'))
print(dupliques([1,2,3,4]))