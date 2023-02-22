"""     Auteur:         Samuel MAMBINGO
        Date:           09/02/2022
        But:            Écrire un programme qui génère de manière (pseudo) aléatoire un entier (nombre secret) compris entre 0 et 100.
                        Ensuite, le joueur doit deviner ce nombre en utilisant le moins d’essais possible.
                        À chaque tour, le joueur est invité à proposer un nombre et le programme doit donner une réponse parmi les suivantes :
                            - « Trop grand » : si le nombre secret est plus petit que la proposition et qu’on n’est pas au maximum d’essais
                            - « Trop petit » : si le nombre secret est plus grand que la proposition et qu’on n’est pas au maximum d’essais
                            - « Gagné en n essai(s) ! » : si le nombre secret est trouvé
                            - « Perdu ! Le secret était nombre » : si le joueur a utilisé six essais sans trouver le nombre secret."""

import random


SECRET = random.randint(0, 100)

ESSAIS = 6
t=1

for i in range(ESSAIS):
    choix = int(input())
    if choix == SECRET:
        break

    elif choix < SECRET and t < 6:
        print("Trop petit")
        t += 1
        continue
    elif choix > SECRET and t < 6:
        print("Trop grand")
        t += 1
        continue
    elif choix!= SECRET and t == 6:
        break

if choix == SECRET:
    print(f"Gagné en {i+1} essai(s) !")
else:
    print(f"Perdu ! Le secret était {SECRET}")






