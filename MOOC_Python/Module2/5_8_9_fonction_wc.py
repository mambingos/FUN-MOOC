"""     Auteur:         Samuel MAMBINGO
        Date:           25/02/2022
        But:            Écrire une fonction wc(nomFichier) qui ouvre le fichier en question et renvoie un tuple de trois nombres :
                            - le nombre de caractères (y compris les caractères de retour à la ligne)
                            - le nombre de mots
                            - le nombre de lignes..."""
def my_filter_1(lst,f):
    liste = []
    for i in range(len(lst)):
        if f(lst[i]) == True and lst[i] not in liste:
            liste.append(lst[i])
    return liste

def wc(nomFichier):
    (a, b, c) = (0,0,0)
    for ligne in open(nomFichier, encoding= "utf-8"):
        c += 1
    with open(nomFichier,encoding="utf-8") as file:
        f = file.read()
        for character in f:
                a += 1

    with open(nomFichier, encoding="utf-8") as file_1:
        fo = file_1.read()
        fou = fo.split()
        b = len(my_filter_1(fou, lambda x: x.isalnum()))
        print(b)

        print(fou)




    return (a, b, c)

print(wc("Zola.txt"))
print(wc("petit.txt"))
print(wc("wc1.txt"))