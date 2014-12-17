from __future__ import print_function
from copy import deepcopy

square = [ [ None, 7, None, None, None, None, None, None, 8 ],
           [ None, None, None, None, 2, 5, None, None, None ],
           [ 3, None, 5, 4, None, 9, 2, 7, None ],
           [ None, 4, None, None, None, None, None, 3, 7 ],
           [ None, None, 3, 6, None, 2, 1, None, None ],
           [ 9, 6, None, None, None, None, None, 2, None ],
           [ None, 2, 8, 9, None, 4, 7, None, 3 ],
           [ None, None, None, 1, 3, None, None, None, None ],
           [ 4, None, None, None, None, None, None, 9, None ] ]

def print_sudoku(square):
    for y in square:
        for x in y:
            if x is None:
                print(' ', end='')
            else: print(x, end='')
        print()
             
def y_range(y) :
   return [i for i in range(9) if i != y]
 
def x_range(x) :
   return [i for i in range(9) if i != x]

def mini_square_range(x, y):
    mini_squares = [[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]],
                   [[3,0],[3,1],[3,2],[4,0],[4,1],[4,2],[5,0],[5,1],[5,2]],
                   [[6,0],[6,1],[6,2],[7,0],[7,1],[7,2],[8,0],[8,1],[8,2]],
                   [[0,3],[0,4],[0,5],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5]],
                   [[3,3],[3,4],[3,5],[4,3],[4,4],[4,5],[5,3],[5,4],[5,5]],
                   [[6,3],[6,4],[6,5],[7,3],[7,4],[7,5],[8,3],[8,4],[8,5]],
                   [[0,6],[0,7],[0,8],[1,6],[1,7],[1,8],[2,6],[2,7],[2,8]],
                   [[3,6],[3,7],[3,8],[4,6],[4,7],[4,8],[5,6],[5,7],[5,8]],
                   [[6,6],[6,7],[6,8],[7,6],[7,7],[7,8],[8,6],[8,7],[8,8]]]
    for mini_square in mini_squares:
        if list((x, y)) in mini_square:
            return [i for i in mini_square if i != list((x,y))]

def valid_at_xy(square, n, x, y):
    if square[y][x] is not None: return False
    for i in y_range(y):
        if square[i][x] == n: return False
    for i in x_range(x):
        if square[y][i] == n: return False
    for i in mini_square_range(x, y):
        if square[i[1]][i[0]] == n: return False
    return True

def solve(square, x,y):
    guesses = [1,2,3,4,5,6,7,8,9]
    return [i for i in guesses if valid_at_xy(square, i, x, y)]

def next_empty_cell(s):
    for y in range(9):
        for x in range(9):
            if s[y][x] is None: return x,y
    return None, None

def solver(square):
    stack = []
    stack.append(deepcopy(square))
    while len(stack) > 0:
        # pop
        candidate = stack.pop()
        # find next empty cell - if no empty cell print it
        x, y = next_empty_cell(candidate)
        if (x is None): print_sudoku(candidate)
        # for each possibility push
        else:
            possibilities = solve(candidate, x, y)
            if len(possibilities) == 0: continue
            for n in possibilities:
                candidate[y][x] = n
                stack.append(deepcopy(candidate))

