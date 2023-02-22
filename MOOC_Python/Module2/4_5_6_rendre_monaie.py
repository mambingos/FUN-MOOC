"""     Auteur:         Samuel Mambingo
        Date:           08/02/2022
        But:            calcule le nombre de billets et pieces de ( 20, 10 , 5, 2, 1) à rendre
                        pour l'achat d'un article au prix x avec de billets et pieces de ( 20, 10 , 5, 2, 1)
                        Concrètement on rentre (x, a, b , c, d, e) et le programme calcule si la somme est supérieure
                        ou égale à x. si c'est le cas il retourne (t, y , u, i, o) le nombre d'éléments à rendre"""

def rendre_monnaie(x,a,b,c,d,e):
    if (a * 20 + b * 10 + c * 5 + d * 2 + e * 1) < x:
        m = (None, None, None, None, None)
        return m
    elif (a * 20 + b * 10 + c * 5 + d * 2 + e * 1) == x:
        m = (0, 0, 0, 0, 0)
        return m
    else:
        r = (a * 20 + b * 10 + c * 5 + d * 2 + e * 1) - x
        t = r // 20
        q = r % 20
        y = q // 10
        s = q % 10
        u = s // 5
        d = s % 5
        p = d // 2
        o = d % 2
        m = (t, y, u, p, o)
        return m

print(rendre_monnaie(38, 1,1,1,1,1))
print(rendre_monnaie(56, 5, 0, 0, 0, 0))
print(rendre_monnaie(80, 2, 2, 2, 3, 3))

