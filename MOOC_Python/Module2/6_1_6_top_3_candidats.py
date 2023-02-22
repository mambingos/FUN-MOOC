"""     Auteur:         Samuel MAMBINGO
        Date:           01/03/2022
        But:            Afin de récompenser les trois candidats ayant obtenu la meilleure moyenne, nous vous demandons d’écrire une fonction top_3_candidats(moyennes)
                        qui reçoit un dictionnaire contenant comme clés les noms des candidats et comme valeurs la moyenne que chacun a obtenue.
                        Cette fonction doit retourner un tuple contenant les noms des trois meilleurs candidats, par ordre décroissant de leurs moyennes."""

def top_3_candidats(moyennes):
    #for name in moyennes:
        # print(moyennes[name])
    a = sorted(moyennes.items(), key= lambda t: t[1], reverse=True)
        # a = sorted(moyennes[name], reverse= True)
    print((a[0][0],a[1][0],a[2][0]))

top_3_candidats({'Candidat 7': 2, 'Candidat 2': 38, 'Candidat 6': 85,
                 'Candidat 1': 8, 'Candidat 3': 17, 'Candidat 5': 83,
                 'Candidat 4': 33})
top_3_candidats({'Candidat 5': 94, 'Candidat 1': 84, 'Candidat 2': 76, 'Candidat 4': 22, 'Candidat 3': 43})