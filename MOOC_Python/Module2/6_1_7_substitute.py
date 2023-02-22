"""     Auteur:         Samuel MAMBINGO
        Date:           01/03/2022
        But:            Écrire une fonction substitue(message, abreviation) qui renvoie une copie de la chaîne de caractères message dans laquelle les mots
                        qui figurent parmi les clés du dictionnaire abreviation sont remplacés par leur signification (valeur)."""

def substitue(message, abreviation):
    message = message.split()
    a = []
    for c in message:
        if c in abreviation:
            a.append(abreviation[c])
        else:
            a.append(c)
    a=" ".join(a)
    return a



print(substitue('C. N. cpt  2 to inf', {'C.' : 'Chuck',
                                 'N.' : 'Norris',
                                 'cpt' : 'counted',
                                 '2' : 'two times',
                                 'inf' : 'infinity'}))
print(substitue('viva C. N. : C. N. cpt 2 to inf and even further', {'cpt': 'counted', 'inf': 'infinity', 'N.': 'Norris', 'C.': 'Chuck', '2': '2 times'}))