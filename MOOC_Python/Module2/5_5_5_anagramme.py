"""     Auteur:         Samuel MAMBINGO
        Date:           21/02/2022
        But:            Écrire une fonction anagrammes(v, w) qui renvoie la valeur booléenne True si les mots v et w sont des anagrammes.
                        La fonction retourne la valeur booléenne False dans le cas contraire."""

def anagrammes(v,w):
    return sorted(list(v)) == sorted(list(w))