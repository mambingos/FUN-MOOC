
def premier(n):
    
    if n <= 1:
        res = False

    elif n == 2:
        res = True
   
    elif n > 2:

        for i in range(2, n):
            if n % i == 0:
                res = False
                break

            if n % i != 0:
                res = True

    return res

n = int(input())
for i in range(2,n):
    if premier(i):
        print(i)

