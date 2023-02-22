"""     Auteur:         Samuel MAMBINGO
        Date:           10/03/2022
        But:            - Écrire une fonction file_histogram(fileName) qui prend en paramètre le nom, sous forme d’une chaîne de caractères,
                        d’un fichier texte, et qui renvoie un dictionnaire associant à chaque caractère du texte contenu dans ce fichier son nombre d’occurrences.
                        - Écrire une fonction words_by_length(fileName) qui prend en paramètre le nom, sous forme d’une chaîne de caractères, d’un fichier texte,
                        et qui renvoie un dictionnaire associant à une longueur l la liste triée (dans l’ordre utf-8 croissant)
                        des mots de longueur l présents dans le texte contenu dans le fichier. Ces mots seront écrits en minuscules."""

def file_hitogram (fileName):
    dico = {}
    with open(fileName, encoding="utf-8") as file:
        mots = file.read()
        for character in mots:
            if character not in dico:
                dico[character] = 1
            else:
                dico[character] += 1
        return dico

def words_by_length (fileName):
    dico = {}
    with open(fileName, encoding="utf-8") as file:
        file_1 = file.read()
        file_1 = file_1.lower()
        for character in file_1:
            if not character.isalpha():
                file_1 = file_1.replace(character, " ")
        file_2 = file_1.split()
        for word in file_2:
            l = len(word)
            if l not in dico:
                dico[l] = [word]
            else:
                if word not in dico[l]:
                    dico[l].append(word)
                    dico[l] = sorted(dico[l])

    return dico




print(file_hitogram("Zola.txt"))
print(words_by_length("Zola.txt"))
        