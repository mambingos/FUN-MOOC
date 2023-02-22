"""     Auteur:         Samuel MAMBINGO
        Date:           22/02/2022
        But:            Écrire une fonction decompresse qui reçoit une telle liste en paramètre et renvoie la séquence t sous forme d’une nouvelle liste.
                        Par exemple, la liste [(1, 'He'), (2, 'l'), (1,'o')] décrit la séquence "Hello".
                        decompresse([(4, 1), (0, 2), (2, 'test'), (3, 3), (1, 'bonjour')])
                        doit retourner [1, 1, 1, 1, 'test', 'test', 3, 3, 3, 'bonjour']"""

def decompresse_1(liste):
    liste_2 = []
    max_ =0
    for i in range(len(liste)):
        max_ += liste[i][0]

    b = 0
    j = 0
    while j < max_:
        for z in range(liste[b][0]):
            a = liste[b][1]
            liste_2.append(a)
        j += liste[b][0]
        b += 1
    return liste_2

print(decompresse_1([(1, 'He'), (2, 'l'), (1,'o')]))

