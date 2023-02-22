"""     Auteur:         Samuel MAMBINGO
        Date:           21/02/2022
        But:            L’exercice est le même que le précédent, mais ici, si les paramètres ont le type attendu,
                        la fonction modifie la liste en place et ne retourne rien. Si les paramètres ne sont pas valides, une erreur se produit à l’exécution."""

def my_insert(m,n):
    assert isinstance(n, int) and n not in m
    m.append(n)
    m.sort()
    res = m
    return res


print(my_insert([1,5,78], 39))