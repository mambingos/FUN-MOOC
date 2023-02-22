def soleil_leve(a, b, c, d):
    if a < b:
        if x < a:
            if x == c:
                res = True
            elif c < d:
                res = c < x < d
            else:
                res = c < x or x < d
        elif x == a:
            res = True

        elif a < x < b:
            res = True

        elif x > b:
            if x < c:
                res = False
            elif x == c:
                res = True
            elif c < d:
                res = c < x < d
            else:
                res = c < x or x < d
    elif a > b:
        if x < a:
            if x == c:
                res = True
            elif c < d:
                res = c < x < d
            else:
                res = c < x or x < d
        elif x == a:
            res = True

        elif a < x < b:
            res = True

        elif x > b:
            if x < c:
                res = False
            elif x == c:
                res = True
            elif c < d:
                res = c < x < d
            else:
                res = c < x or x < d




    return res


a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(24):
    x = i
    x = soleil_leve(a, b, c, d)
    if x == True:
        x = " "
    else:
        x = " *"
    print(i, x)

