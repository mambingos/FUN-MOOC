"""     Auteur:         Samuel MAMBINGO
        Date:           20/02/2022
        But:            Écrire une fonction prime_numbers qui reçoit comme paramètre un nombre entier nb et qui renvoie la liste des nb premiers nombres premiers.
                        Si le paramètre n’est pas du type attendu, ou ne correspond pas à un nombre entier positif ou nul, la fonction renvoie None."""
# definition nombre premier
def premier(n):
    if n <= 1:
        res = False
    elif n == 2:
        res = True
    elif n > 2:
        for i in range(2, n):
            if n % i == 0:
                res = False
                break
            if n % i != 0:
                res = True
    return res
# defintion fonction liste de nombres premier
def prime_numbers(nombre):
    if not isinstance(nombre, int) or nombre < 0:       # entrée invalide
        liste = None
    else:                                               # entrée valide
        a = 2
        liste = [a]*nombre
        for i in range(len(liste)):
            for c in liste:
                if premier(a):
                    liste[i] = a
                    a += 1
                else:
                    a += 1
    return liste

print(prime_numbers(-1))
print(prime_numbers(0))
print(prime_numbers(4))