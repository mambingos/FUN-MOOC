def soleil_leve (x,y,z):
    if x == y == 12 :
        res = False
    elif x == y == 0:
        res = True
    elif x == z:
        res = True
    elif x < y:
        res = x < z < y
    else:
        res = x < z or z < y
    return res

x = int(input())
y = int(input())
z = int(input())
a = soleil_leve(x,y,z)
print(a)