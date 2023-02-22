"""     Auteur:         Samuel MAMBINGO
        Date:           21/02/2022
        But:            Écrire une fonction my_insert qui reçoit comme premier paramètre une liste d’entiers relatifs triée par ordre croissant
                        et comme deuxième paramètre un entier relatif n, et qui renvoie une liste correspondant à la liste reçue,
                        mais dans laquelle le nombre n a été inséré à la bonne place.
                        La liste donnée en paramètre ne doit pas être modifiée par votre fonction.
                        Vous pouvez supposer que le premier paramètre sera bien une liste triée d’entiers,
                        mais si le deuxième paramètre n’est pas du bon type, la fonction retourne None.."""

def my_insert(m,n):
    if isinstance(n, int):
        a = m.copy()
        a.append(n)
        res = sorted(a)
        return res

print(my_insert([1, 2, 5], 4))