def deux_egaux (x, y, z):
    res = x == y or x == z or y == z
    return res

x = int(input())
y = int(input())
z = int(input())

a = deux_egaux(x,y,z)
print(a)

