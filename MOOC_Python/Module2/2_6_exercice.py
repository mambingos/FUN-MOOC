import math
long = float(input())
(a1, a2) = long, 0.0
(b1, b2) = long * math.cos((math.pi)/3), long * math.sin((math.pi)/3)
(c1, c2) = long * math.cos((math.pi)*2/3), long * math.sin((math.pi)*2/3)
(d1, d2) = -long, 0.0
(e1, e2) = -long * math.cos((math.pi)/3), -long * math.sin((math.pi)/3)
(f1, f2) = long * math.cos((math.pi)/3), -long * math.sin((math.pi)/3)

print(a1, a2)
print(b1, b2)
print(c1, c2)
print(d1, d2)
print(e1, e2)
print(f1, f2)


