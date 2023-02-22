"""     Auteur:         Samuel MAMBINGO
        Date:           01/03/2022
        But:            Écrire un programme qui lit depuis l’entrée deux chaînes de caractères, représentant les noms des deux fichiers décrits ci-dessus (dans l’ordre,
                        le fichier de type “result-pass-fail.csv” suivi du fichier du type “result-count.csv”), et qui imprime la liste des intitulés,
                        un par ligne, dans l’ordre décroissant des « valeurs » calculées comme suit.
                        La « valeur » d’un intitulé est le nombre des « apprenants fiables » ayant réussi l’exercice correspondant.
                        Un « apprenant fiable » est un apprenant qui n’a jamais testé plus de dix fois chacun des codes qu’il a essayé de valider."""
# import de module
from copy import deepcopy
from operator import itemgetter,attrgetter
# constante
NOMBRE_MAX_ESSAIS = 10


# definitions des fonctions
def lecture(fichier):
    # fonction de lecture des fichiers resultats (1 si succes, -1 si echec et 0 si pas d'essais)
    res = []
    with open(fichier, encoding="utf-8") as file:

        for line in file:
            line = line.strip()
            line = line.split(sep=";")
            res.append(line)

        for i in range(1, len(res)):
            for j in range(len(res[0])):
                if res[i][j] == "VRAI":
                    res[i][j] = 1
                elif res[i][j] == "FAUX":
                    res[i][j] = -1
                else:
                    res[i][j] = 0

        return res


def lecture_2(fichier):
    # fonction de lecture du fichier conteur (renvoi la matrice nombre de fois qu'un étudiant a essayé de faire un exercice, sinon 0)
    res = []
    with open(fichier, encoding="utf-8", newline="") as file:
        for line in file:
            line = line.strip()
            line = line.split(sep=";")
            res.append(line)

        for i in range(1, len(res)):
            for j in range(len(res[0])):
                if res[i][j].isdigit():
                    res[i][j] = int(res[i][j])
                else:
                    res[i][j] = 0
        return res


def suppression(reussite, conteur, NOMBRE_MAX_ESSAIS):
    # écarte les résultats des apprenants non fiables (plus de 10 tentatives sur un exercice)

    conteur_2 = []
    conteur_2.append(conteur[0])
    reussite_2=[]
    reussite_2.append(reussite[0])

    for i in range(1, len(conteur), 1):
        line = []
        for j in range(len(conteur_2[0])):
            if conteur[i][j] < NOMBRE_MAX_ESSAIS:
                line.append(conteur[i][j])
        if len(line) == len(conteur_2[0]):
            conteur_2.append(line)
            reussite_2.append(reussite[i])
        else:
            n = len(line)
            del line[0:n]




    return conteur_2, reussite_2


def dico(reussite, conteur):
    # renvoie la liste par ordre décroissant de réussite
    dico = {}
    for j in range(len(conteur[0])):
        s = 0
        for i in range(0, len(conteur)):
            if conteur[i][j] != 0 and reussite[i][j] == 1:
                s += 1
            dico[conteur[0][j]] = s


    liste = sorted(dico.items(), key=lambda t: t[0], reverse=True)
    liste =sorted(liste,key=itemgetter(1),reverse=True)




    return liste


fichier_1 = input()
fichier_2 = input()
#fichier_1 = "result-pass-fail-0.csv"
#fichier_2 = "result-count-0.csv"
reussite = lecture(fichier_1)

conteur = lecture_2(fichier_2)

(conteur_2, reussite_2) = suppression(reussite, conteur, NOMBRE_MAX_ESSAIS)

tri = (dico(reussite_2, conteur_2))
print(tri)
for element in tri:
    print(element[0],end="")
print()
