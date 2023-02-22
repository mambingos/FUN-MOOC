"""         Auteur:             Samuel MAmbingo
            Date:               08/02/2022
            But:                Écrire un programme qui lit trois entiers a, b et c en input. Ensuite :
                                si l’entier c est égal à 1, alors le programme affiche la valeur de a + b ;
                                si c vaut 2, alors le programme affiche la valeur de a - b ;
                                si c est égal à 3, alors l’output sera la valeur de a.b (produit de a par b) ;
                                enfin, si la valeur 4 est assignée à la variable c, alors le programme affiche la valeur de a^2 + a.b ;
                                et si c contient une autre valeur, le programme affiche le message Erreur."""

a = int(input())
b = int(input())
c = int(input())

if c == 1:
    print(a+b)
elif c == 2:
    print(a-b)
elif c == 3:
    print(a*b)
elif c == 4:
    print(a**2+a*b)
else:
    print("Erreur")