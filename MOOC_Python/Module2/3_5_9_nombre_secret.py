"""     Auteur:         Samuel MAMBINGO
        Date:           09/02/2022
        But:            Écrire un programme qui génère de manière (pseudo) aléatoire un entier (nombre secret) compris entre 0 et 100.
                        Ensuite, le joueur doit deviner ce nombre en utilisant le moins d’essais possible.
                        À chaque tour, le joueur est invité à proposer un nombre et le programme doit donner une réponse parmi les suivantes :
                            - « Trop grand » : si le nombre secret est plus petit que la proposition et qu’on n’est pas au maximum d’essais
                            - « Trop petit » : si le nombre secret est plus grand que la proposition et qu’on n’est pas au maximum d’essais
                            - « Gagné en n essai(s) ! » : si le nombre secret est trouvé
                            - « Perdu ! Le secret était nombre » : si le joueur a utilisé six essais sans trouver le nombre secret."""
import sys
import random
random.seed(37)

SECRET = random.randint(0, 100)
ESSAIS = 6
t = 1

while ESSAIS > 0:

    choix = int(input())
    if SECRET == choix:
        print(f"Gagné en {t} essai(s) !")
        sys.exit()
    elif SECRET > choix and t < 6:
        print("Trop petit")
        ESSAIS -= 1
        t += 1
    elif SECRET < choix and t < 6:
        print("Trop grand")
        ESSAIS -= 1
        t += 1
    else:
        break

print(f"Perdu ! Le secret était {SECRET} ")
sys.exit()



