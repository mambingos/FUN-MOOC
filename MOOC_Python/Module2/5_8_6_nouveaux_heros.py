"""     Auteur:         Samuel MAMBINGO
        Date:           20/02/2022
        But:            Écrire une fonction nouveaux_heros dont le but consiste à remplacer les héros d'une histoire. La fonction acceptera deux paramètres :
                            - le premier sera une chaîne de caractères précisant le nom du fichier contenant l'histoire initiale ;
                            - le deuxième sera une chaîne de caractères précisant le nom du fichier dans lequel sera sauvegardée l'histoire modifiée comme précisé ci-dessous.

                        Dans l'histoire initiale, présente dans le fichier dont le nom est donné en premier argument, trois protagonistes interviennent : Pierre, Paul et Jacqueline.
                        La fonction devra remplacer ces trois héros par, respectivement, Paul, Tom et Mathilde.
                        Le texte ainsi modifié sera alors stocké dans le fichier dont le nom est donné en deuxième argument.
                        Aucune autre modification ne sera apportée au texte initial."""


def nouveaux_heros(histoire_1,histoire_2):
    with open(histoire_1) as file_1:
        a = ""
        for mot in file_1:
            a += mot


    with open(histoire_2, "w", encoding='utf-8') as file_2:
        file_2.write(a)
        file_2.close()
        print(a)


    with open(histoire_2, encoding='utf-8') as file_2:
        nouveau_texte = file_2.read()
        nouveau_texte = nouveau_texte.replace("Paul", "Jean")
        nouveau_texte = nouveau_texte.replace("Pierre", "Paul")
        nouveau_texte = nouveau_texte.replace("Jean", "Tom")
        nouveau_texte = nouveau_texte.replace("Jacqueline", "Mathilde")
        print(nouveau_texte)
    with open(histoire_2, "w", encoding='utf-8') as file_2:
        file_2.write(nouveau_texte)


    return histoire_2
nouveaux_heros("histoire_1.txt","histoire_2.txt")




