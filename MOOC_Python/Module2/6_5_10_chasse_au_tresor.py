"""     Auteur:         Samuel MAMBINGO
        Date:           14/03/2022
        But:            Écrire une fonction create_map(size, trapsNbr) qui reçoit deux entiers en paramètres, size, compris entre 2 et 100, et trapsNbr,
                        de valeur strictement inférieure à size x size, et qui retourne un dictionnaire implémentant comme dans l’exemple précédent
                        une carte de taille size et dans laquelle figurent trapsNbr cases contenant un piège (modélisé par la valeur -1) et une case contenant un trésor
                        (modélisé par la valeur 1). L’emplacement de ces cases sera aléatoire.

                        Écrire une fonction play_game(map_size, treasure_map) qui reçoit un entier et une carte de taille map_size x map_size,
                        telle que celles obtenues grâce à la fonction create_map, et qui demande à l’utilisateur d’entrer les coordonnées d’une case,
                         jusqu’à tomber sur une case occupée. Si l’utilisateur a trouvé le trésor, la fonction retourne la valeur True,
                         sinon l’utilisateur est tombé sur un piège et la fonction retourne False."""

# import de module
import random

# création de la carte au trésor:
def create_map(size,trapsNbr):
    MY_PRECIOUS = 1
    TRAP = -1
    my_map = {}
    my_map[(random.randint(1, size), random.randint(1, size))] = MY_PRECIOUS
    while len(my_map) < trapsNbr:
        a = (random.randint(1, size), random.randint(1, size))
        if a not in my_map:
            my_map[a] = TRAP
    return my_map

# creation du jeu:
def play_game(map_size, treasure_map):
    coordones = input().split()
    for a in range(len(coordones)):
        coordones[a] = int(coordones[a])
    (x, y) = tuple(coordones)
    if (x, y) in treasure_map and treasure_map[(x, y)] == -1:
        res = False
    elif (x, y) in treasure_map and treasure_map[(x, y)] == 1:
        res = True
    else:
        while (x, y) not in treasure_map or x > map_size or y > map_size:
            coordones = input().split()
            for a in range(len(coordones)):
                coordones[a] = int(coordones[a])
            (x, y) = tuple(coordones)

        if treasure_map[(x, y)] == 1:
            res = True

        elif treasure_map[(x, y)] == -1:
            res = False

    return res


print(play_game(2, {(1, 2): -1, (1, 1): -1, (2, 1): -1, (2, 2): 1}))





