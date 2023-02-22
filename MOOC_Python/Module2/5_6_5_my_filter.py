"""     Auteur:         Samuel MAMBINGO
        Date:           22/02/2022
        But:            Écrire une fonction my_filter qui reçoit une liste lst et une fonction booléenne f
                        en paramètres et renvoie une nouvelle liste constituée des éléments de lst pour lesquels la fonction f renvoie True."""

def my_filter_1(lst,f):
    liste = []
    for i in range(len(lst)):
        if f(lst[i]) == True :
            liste.append(lst[i])
    return liste

def my_filter (lst,t): # compréhension non achevée
    liste = []
    liste[i] = lst[j] for j in range(len(lst)) if f(lst[j]==True)
    return liste



print(my_filter(['hello', 666, 42, 'Thierry', 1.5], lambda x :isinstance(x, int)))
