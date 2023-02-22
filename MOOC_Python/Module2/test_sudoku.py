#import de module:
from copy import deepcopy
possibilite = {1,2,3,4,5,6,7,8,9}
# recherche des candidats par carre:
def empty_case(grid):
    completed_grid = [[0] * 9 for i in range(9)]
    completed_grid = grid
    return completed_grid
print(empty_case([[4, 0, 3, 0, 9, 6, 0, 1, 8],
                      [0, 0, 2, 8, 0, 1, 0, 0, 3],
                      [0, 1, 0, 0, 0, 0, 0, 0, 7],
                      [0, 4, 0, 7, 0, 0, 0, 2, 6],
                      [5, 0, 7, 0, 1, 0, 4, 0, 9],
                      [1, 2, 0, 0, 0, 3, 0, 8, 0],
                      [2, 0, 0, 0, 0, 0, 0, 7, 0],
                      [7, 0, 0, 2, 0, 9, 8, 0, 0],
                      [0, 6, 0, 1, 5, 0, 3, 0, 2]]))