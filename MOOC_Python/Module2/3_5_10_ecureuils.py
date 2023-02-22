"""     Auteur:         Samuel MAMBINGO
        Date:           09/02/2022
        But:            À la fin votre programme dira si oui ou non la noisette a été atteinte ou non.

                        En pratique, après avoir lu les deux valeurs saut et position_cible,
                        votre programme affichera chaque valeur de position_courante sur une ligne différente
                        à partir de la seconde valeur (sauf la position_courante initiale qui vaut toujours 0).
                        La dernière position_courante affichée sera soit 0 soit la dernière valeur de position_courante
                         avant qu’elle n’aie la valeur de position_cible, si l’écureuil trouve la noisette.
                         Votre programme terminera en affichant, sur une nouvelle ligne, le message donnant le résultat :

                            - "Cible atteinte" si l’écureuil a trouvé la noisette,
                            - "Pas trouvée" si l’écureuil est revenu en position 0 sans trouver la noisette.
                            - Vous pouvez supposer que les valeurs lues sont bien des entiers qui respectent les consignes."""
import sys
saut = int(input())
position_cible = int(input())
position_courante = 0


while position_courante != position_cible:
    position_courante = (position_courante + saut) % 100
    if position_courante == position_cible:
        print("Cible atteinte")
        sys.exit()
    elif position_courante != position_cible and position_courante != 0:
        print(position_courante)
    elif position_courante == 0:
        print(position_courante)
        break
print("Pas trouvée")
