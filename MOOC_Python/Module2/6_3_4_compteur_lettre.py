"""     Auteur:         Samuel MAMBINGO
        Date:           01/03/2022
        But:            Écrire une fonction compteur_lettres(texte) qui renvoie un dictionnaire contenant toutes les lettres
                        de l’alphabet associées à leur nombre d’apparition dans texte."""

import string
def listAlphabet():
  return list(string.ascii_lowercase)

def compteur_lettres(texte):
    liste_alphabet = listAlphabet()
    print(liste_alphabet)
    d = {}.fromkeys(liste_alphabet,0)
    mot = texte.lower()
    for character in mot:
        if not character.isalpha():
            mot.replace(character," ")
        elif character.isalpha():
            d[character] +=1
    return d

print(compteur_lettres("Dessine-moi un mouton !"))