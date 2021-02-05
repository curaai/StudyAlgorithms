# https://www.codewars.com/kata/529bf0e9bdf7657179000008
# Sudoku Solution Validator

from itertools import product

def valid_solution(arr):
    def grid(idx):
        r, c = idx
        idx_cells = product(range(c-3, c), range(r-3, r))
        return list(map(lambda rc: arr[rc[0]][rc[1]], idx_cells))
    def row(r):
        return list(map(lambda i: arr[r][i], range(9)))
    def col(c):
        return list(map(lambda i: arr[i][c], range(9)))

    def check_cells(func, target):
        check = lambda cells: len(set(cells)) == 9
        return all(map(check, map(func, target)))

    r1 = check_cells(grid, product([3, 6, 9], [3, 6, 9]))
    r2 = check_cells(row, range(9))
    r3 = check_cells(col, range(9))
    return r1 and r2 and r3

import unittest
class TestSudoku(unittest.TestCase):
    def testcase1(self):
        res = validSolution([
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]) 
        self.assertTrue(res)

    def testcase2(self):
        res = validSolution([
            [5, 3, 4, 6, 7, 8, 9, 1, 2], 
            [6, 7, 2, 1, 9, 0, 3, 4, 8],
            [1, 0, 0, 3, 4, 2, 5, 6, 0],
            [8, 5, 9, 7, 6, 1, 0, 2, 0],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 0, 1, 5, 3, 7, 2, 1, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 0, 0, 4, 8, 1, 1, 7, 9]
        ])
        self.assertFalse(res)

if __name__ == "__main__":
    unittest.main()