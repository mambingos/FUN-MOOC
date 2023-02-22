"""     Auteur:         Samuel MAMBINGO
        Date:           25/02/2022
        But:            Écrire une fonction wc(nomFichier) qui ouvre le fichier en question et renvoie un tuple de trois nombres :
                            - le nombre de caractères (y compris les caractères de retour à la ligne)
                            - le nombre de mots
                            - le nombre de lignes..."""


def wc(nomFichier):
    (a, b, c,d) = (0,0,0,0)


    with open(nomFichier,"r",encoding = "utf-8") as file:
        for lignes in file:
            d = lignes
            c += 1
            for characters in lignes:
                a+=1

                if not str(characters).isalnum():
                   lignes = lignes.replace(str(characters)," ")

            lignes = lignes.split()

            b += len(lignes)



    return (a, b, c,d)

print(wc("Zola.txt"))
#print(wc("petit.txt"))
print(wc("wc1.txt"))