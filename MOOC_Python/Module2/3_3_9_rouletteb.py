"""     Auteur:         Samuel MAMBINGO
        Date:           08/02/2022
        But:            Dans mon casino, ma roulette comporte 13 numéros de 0 à 12 comme montrés ci-dessous :
                        Le joueur a plusieurs types de paris possibles :

                            il peut choisir de parier sur le numéro sortant, et dans ce cas, s’il gagne, il remporte douze fois sa mise ;

                            il peut choisir de parier sur la parité du numéro sortant (pair ou impair), et dans ce cas, s’il gagne, il remporte deux fois sa mise ;

                            enfin, il peut choisir de parier sur la couleur du numéro sortant (rouge ou noir), et dans ce cas aussi, s’il gagne, il remporte deux fois sa mise.

                            Si le joueur perd son pari, il ne récupère pas sa mise.

                        Pour simplifier, on suppose que le numéro 0 n’est ni rouge ni noir, mais est pair.
                        Pour simplifier encore, on suppose que le joueur mise systématiquement 10 euros."""
import random
Noire = [2, 4, 6, 8, 10,11]
Rouge = [1, 3, 5, 7, 9, 12]

Noire = [2, 4, 6, 8, 10,11]
Rouge = [1, 3, 5, 7, 9, 12]

user_choice = int(input())
secret = int(input())

if user_choice == secret:
    print("120")

elif user_choice == 13 and secret % 2 == 0 \
    or user_choice == 14 and secret % 2 != 0 \
    or user_choice == 15 and secret in Rouge \
    or user_choice == 16 and secret in Noire:
    print("20")

else:
    print("0")

