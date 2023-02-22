
def check_regions(grid):
    l = {a: set() for a in range(0, 9)}
    [[l[0].add(grid[i][j]) for j in range(9) if  i // 3 == 0 and j // 3 == 0] for i in range(9)]
    [[l[1].add(grid[i][j]) for j in range(9) if  i // 3 == 0 and j // 3 == 1] for i in range(9)]
    [[l[2].add(grid[i][j]) for j in range(9) if  i // 3 == 0 and j // 3 == 2] for i in range(9)]
    [[l[3].add(grid[i][j]) for j in range(9) if  i // 3 == 1 and j // 3 == 0] for i in range(9)]
    [[l[4].add(grid[i][j]) for j in range(9) if  i // 3 == 1 and j // 3 == 1] for i in range(9)]
    [[l[5].add(grid[i][j]) for j in range(9) if  i // 3 == 1 and j // 3 == 2] for i in range(9)]
    [[l[6].add(grid[i][j]) for j in range(9) if  i // 3 == 2 and j // 3 == 0] for i in range(9)]
    [[l[7].add(grid[i][j]) for j in range(9) if  i // 3 == 2 and j // 3 == 1] for i in range(9)]
    [[l[8].add(grid[i][j]) for j in range(9) if  i // 3 == 2 and j // 3 == 2] for i in range(9)]
    res = True
    for i in range(len(l)):
       
        res = sorted(l[i]) == [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
        if res == False:
            break
    return res
print(check_regions([[5, 3, 4, 6, 7, 8, 9, 1, 2], [6, 7, 2, 1, 9, 5, 3, 4, 8], [1, 9, 8, 3, 4, 2, 5, 6, 7], [8, 5, 9, 7, 6, 1, 4, 2, 3], [4, 2, 6, 8, 5, 3, 7, 9, 1], [7, 1, 3, 9, 2, 4, 8, 5, 6], [9, 6, 1, 5, 3, 7, 2, 8, 4], [2, 8, 7, 4, 1, 9, 6, 3, 5], [3, 4, 5, 2, 8, 6, 1, 7, 9]]))