"""     Auteur:         Samuel MAMBINGO
        Date:           01/03/2022
        But:            Écrire une fonction next_line(line) qui reçoit une liste d’entiers, et qui retourne la liste correspondant à la ligne suivante.
                        Notez que les valeurs de la liste reçue sont toujours entières, mais cette dernière peut ne pas correspondre à une suite de Conway
                        (par exemple [4,2] pourrait être donné)."""

def next_line(line):
    liste = []
    n = len(line)
    a = 1
    if n == 0:
        liste = []
    elif n == 1:
        a = 1
        liste.append(a)
        liste.append(line[0])
    else:
        i =0
        while i < n-1:
            a = 1
            while line[i] == line[i+1]:
                a += 1
                i += 1
                if i+1 == n:
                    break

            liste.append(a)
            liste.append(line[i])


            if line[i] != line[i+1]:
                liste.append(1)
                liste.append(line[i])
                i += 1

                if i+1 == n:
                    break


    return liste

print(next_line([1, 2, 1, 1,1]))
print(next_line([4]))