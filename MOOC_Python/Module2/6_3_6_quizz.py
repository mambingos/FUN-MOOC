def anagramme_str1(a, b):
    res = False
    if len(a) == len(b):
        liste_b = list(b)
        res = True
        for i in a:
            if i in liste_b:
                liste_b.remove(i)
            else:
                res = False
    return res


a= "bernadn"
b= "Eebradn"
print(anagramme_str1(a,b))
print(a)