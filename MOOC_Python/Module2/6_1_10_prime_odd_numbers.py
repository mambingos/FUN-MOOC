"""     Auteur:         Samuel MAMBINGO
        Date:           03/03/2022
        But:            Écrire une fonction prime_odd_numbers(numbers) qui reçoit une liste de nombres et qui renvoie un couple d’ensembles contenant respectivement les nombres premiers présents dans la liste et les nombres impairs.
                        Pour cela, nous vous demandons d’écrire au préalable deux fonctions annexes qui seront appelées dans le corps de la fonction prime_odd_numbers :
                            - la fonction even qui accepte un nombre entier en paramètre et renvoie l’ensemble des nombres naturels pairs qui lui sont inférieurs ou égaux
                            - la fonction prime_numbers qui accepte un nombre entier en paramètre et renvoie l’ensemble des nombres premiers qui lui sont inférieurs ou égaux."""

# import de modules:
from math import sqrt

def premier(n):
    c = int(round(sqrt(n)))
    if n <= 1:
        res = False
    elif n == 2:
        res = True
    elif n > 2:
        for i in range(2, c+1):
            if n % i == 0:
                res = False
                break
            elif n % i != 0:
                res = True
    return res

# defintion fonction liste de nombres premier
def prime_numbers(nombre):
    if not isinstance(nombre, int) or nombre < 0:
        liste =None
    else:
        a = 2
        liste = set()
        while a <= nombre:
            if premier(a):
                liste.add(a)
                a += 1
                continue
            else:
                a += 1
                continue
    return liste


# defintion de la fonction even
def even(nombre):
    liste = set()
    for i in range (nombre+1):
        if i % 2 ==0:
            liste.add(i)
    return liste
# definition de la fonction prime_odd_numbers
def prime_odd_numbers(nombre):
    max_= max(nombre)
    liste_1 = even(max_)
    liste_2 = prime_numbers(max_)
    (x,y) = (set(),set())
    for element in nombre:
        if element not in liste_1:
            x.add(element)
        if element in liste_2:
            y.add(element)



    return (y,x)




print(prime_numbers(73))
print(even(34))
print(prime_odd_numbers([0, 19, 38, 57, 76, 95]))