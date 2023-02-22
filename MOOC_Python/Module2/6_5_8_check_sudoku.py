def check_cols(grid):
    nouvelle_grid = [[row[i] for row in grid]for i in range(9)]                     # tranposition de matrice (les colonnes deviennent des lignes)

    res = True
    for row in nouvelle_grid:
        row = sorted(row)
        res = row == [1,2,3,4,5,6,7,8,9]
        if res == False:
            break

    return res

def check_rows(grid):
    res = True
    for row in grid:
        row = sorted(row)
        res = row == [1,2,3,4,5,6,7,8,9]
        if res == False:
            break

    return res


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

def check_sudoku(grid):
    return check_regions(grid)==check_rows(grid)==check_cols(grid)==True

print(check_sudoku([[1, 2, 3, 4, 5, 6, 7, 8, 9],
              [2, 3, 4, 5, 6, 7, 8, 9, 1],
              [3, 4, 5, 6, 7, 8, 9, 1, 2],
              [4, 5, 6, 7, 8, 9, 1, 2, 3],
              [5, 6, 7, 8, 9, 1, 2, 3, 4],
              [6, 7, 8, 9, 1, 2, 3, 4, 5],
              [7, 8, 9, 1, 2, 3, 4, 5, 6],
              [8, 9, 1, 2, 3, 4, 5, 6, 7],
              [9, 1, 2, 3, 4, 5, 6, 7, 8]]))