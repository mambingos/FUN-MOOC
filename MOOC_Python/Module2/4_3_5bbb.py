def soleil_leve(a, b, x,):
    if a == b == 0:
        res = True
    elif a == b == 12:
        res = False
    elif x == a:
        res = True

    elif a < b:
        res = a < x < b
    else:
        res = a < x or x < b
    return res

a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(24):
    x = i
    if soleil_leve(a,b,x) or soleil_leve(c,d,x):
            x = ""
    else:
        x = " *"
    print(str(i)+x)