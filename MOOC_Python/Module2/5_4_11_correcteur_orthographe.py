"""     Auteur:         Samuel MAMBINGO
        Date:           21/02/2022
        But:            écrire une fonction correcteur(mot, liste_mots) où mot est le mot que Joao écrit
                        et liste_mots est une liste qui contient les mots (ayant la bonne orthographe) que Joao est susceptible d’utiliser.
                        Cette fonction doit retourner le mot dont l’orthographe a été corrigée."""

# definition distance mot
def distance_mots(mot_1,mot_2):
    m = len(mot_1)
    a = 0
    for i in range(m):
        if mot_1[i] != mot_2[i]:
            a += 1
    return a

# definition du correcteur
def correcteur(mot,liste_mot):
    h = len(liste_mot)
    for i in range(h):
        if len(mot) == len(liste_mot[i]) and distance_mots(mot,liste_mot[i]) <= 1:
            mot = liste_mot[i]
    return mot

print(correcteur("bonvour", ["chien", "chat", "train", "voiture", "bonjour", "merci"]))