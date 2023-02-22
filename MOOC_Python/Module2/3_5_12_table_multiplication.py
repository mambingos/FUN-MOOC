"""     Auteur:         Samuel MAMBINGO
        Date:           08/02/2022
        But:            Écrivez un code qui lit un nombre entier strictement positif n et affiche sur n lignes une table de multiplication de taille  n x n,
                        avec, pour i entre 1 et n,  les n premières valeurs multiples de i strictement positives sur la ième ligne.
                        Ainsi, les n premiers multiples de 1 strictement positifs (0 non compris) sont affichés sur la première ligne,
                         les n premiers multiples de 2 sur la deuxième, et cætera."""


a = 1
n = int(input())

"""for i in range (a, a*(n+1), a):
    print(i, end = ' ')"""
for i in range (a, n+1):
    for i in range(a, a*(n+1), a):
        print(i, end=' ')
    a += 1
    print()

