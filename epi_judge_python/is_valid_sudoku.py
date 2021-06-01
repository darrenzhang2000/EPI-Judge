from typing import List

from test_framework import generic_test

'''
insert into position, check if valid, recursively call, then remove
'''
# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    n = len(partial_assignment)
    for r in range(n):
        s = set()
        for c in range(n):
            if partial_assignment[r][c] != 0:
                s.add(partial_assignment[r][c])
        l = list(filter(lambda x: x != 0, partial_assignment[r]))
        if len(s) != len(l):
            return False

    for c in range(n):
        s = set()
        for r in range(n):
            if partial_assignment[r][c] != 0:
                s.add(partial_assignment[r][c])
        arr = []
        for i in range(n):
            if partial_assignment[i][c] != 0:
                arr.append(partial_assignment[i][c])
        if len(s) != len(arr):
            return False

    def isValidGrid(mat, startR, startC):
        s = set()
        l = []
        for i in range(startR, startR + 3):
            for j in range(startC, startC + 3):
                if partial_assignment[i][j] != 0:
                    s.add(partial_assignment[i][j])
                    l.append(partial_assignment[i][j])
        return len(s) == len(l)

    for startR in [0, 3, 6]:
        for startC in [0, 3, 6]:
            if not isValidGrid(partial_assignment, startR, startC):
                return False

    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
