"""     Auteur:         Samuel MAMBINGO
        Date:           21/02/2022
        But:            Écrire une fonction my_pow qui prend comme paramètres un nombre entier m et un nombre flottant b,
                        et qui renvoie une liste contenant les m premières puissances de b, c’est-à-dire une liste contenant les nombres allant de b^0 à b^{m - 1}.
                        Si le type des paramètres n’est pas celui attendu, la fonction retournera la valeur None."""

# defintion my_pow:
def my_pow_1(m,p):
    if isinstance(m,int) and isinstance(p, float):
        liste = []
        for i in range(m):
            liste.append(p**i)
    return liste
def my_pow_2(m, p):
    if not isinstance(m,int) or not isinstance(p,float):
        return None
    else:
        return [p**i for i in range(m) if isinstance(m,int) and isinstance(p, float)]
def my_pow(m,b):
    return None if not isinstance(m,int) or not isinstance(p,float) else [b**i for i in range(m)]

print(my_pow_1(3, 5.0))
print(my_pow(3, 5.0))
print(my_pow(1, 4))

print(my_pow(6, 5.1))