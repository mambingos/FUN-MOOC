"""     Auteur:         Samuel MAMBINGO
        Date:           20/02/2022
        But:            Écrire une fonction acrostiche qui reçoit en paramètre le nom d’un fichier et qui retourne
                        la chaîne de caractères formée par les premières lettres de chaque ligne du fichier."""

def acrostiche(fichier):
    with open(fichier, encoding = "utf-8") as line:

        m = ""
        for lig in line:
            m += lig[0]
    return m
