"""     Auteur:         Samuel MAMBINGO
        Date:           08/02/2022
        But:            Écrire un programme qui lit une valeur flottante x en entrée et imprime une approximation de sin(x)
                        Cette approximation sera obtenue en additionnant successivement les différents termes de la série
                        jusqu’à ce que la valeur du terme devienne inférieure (en valeur absolue) à une constante
                        \epsilon que l’on fixera à 10^{-6}."""

x = float(input())
epsilon = 10**(-6)
n = 1
a = 1
fact = 1

terme = (x ** n)/fact
somme = terme
while abs(terme) > epsilon:
    n += 2
    a += 1
    fact = fact * ((n-1) ** 2 + (n-1))
    signe = (-1) ** (a+1)
    terme = (signe * x ** n) /fact
    somme += terme
print(somme)






