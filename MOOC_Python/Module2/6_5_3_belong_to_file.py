"""     Auteur:         Samuel MAMBINGO
        Date:           01/03/2022
        But:            Écrire une fonction belongs_to_file(word, filename) qui reçoit deux chaînes de caractères en paramètre.
                        La première correspond à un mot, et la deuxième au nom d’un fichier contenant une liste de mots, chacun sur sa propre ligne.
                        La fonction vérifie si le mot figure dans cette liste, et retourne True si c’est bien le cas, False sinon."""

def belongs_to_file(word, filename):

    with open(filename, encoding="utf-8") as file:
        file_2 = file.read().strip().split()
        if word in file_2:
            res = True
        else:
            res = False
    return res




print(belongs_to_file("pri", "words.txt"))
print(belongs_to_file('princess',"words.txt"))