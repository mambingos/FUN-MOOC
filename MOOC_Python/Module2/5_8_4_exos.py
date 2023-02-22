"""     Auteur:         Samuel MAMBINGO
        Date:           20/02/2022
        But:            1. Écrivez un script qui n’affiche que les mots qui ne contiennent pas de “e”
                        et calculez le pourcentage de ceux-ci par rapport à l’ensemble des mots du fichier mots.txt.
                        2. Par exemple, si nous voulons écrire une fonction booléenne texte_sans_e qui renvoie
                        True si le texte contenu dans le fichier reçu en paramètre ne contient nulle part la lettre "e"
                        (ni les lettres é, è, ê, ë), une solution est donnée ci-dessous."""


with open('mots.txt', encoding="utf-8") as mots:
    a = 0
    max_ = 0
    for m in mots:
        max_ += 1
        if "e" in m:
            a+=1
    taux = a/max_*100
    print(taux)

def texte_sans_e(fichier_recu):
    """renvoie True si le texte contenu dans fichier_recu ne contient pas la lettre e,
    ni les lettres ``é``, ``è``, ``ê``, ``ë``
    Hypothèse: le fichier existe
    """
    with open(fichier_recu, encoding="utf-8") as fichier:
        texte = fichier.read()
        texte = texte.replace('é', 'e')
        texte = texte.replace('è', 'e')
        texte = texte.replace('ê', 'e')
        texte = texte.replace('ë', 'e')
    return 'e' not in texte
print(texte_sans_e('mots.txt'))