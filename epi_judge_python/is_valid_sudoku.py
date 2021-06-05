from typing import List
import math
from test_framework import generic_test

'''
insert into position, check if valid, recursively call, then remove
'''
# Check if a partially filled matrix has any conflicts.
# def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
#     n = len(partial_assignment)
#     for r in range(n):
#         s = set()
#         for c in range(n):
#             if partial_assignment[r][c] != 0:
#                 s.add(partial_assignment[r][c])
#         l = list(filter(lambda x: x != 0, partial_assignment[r]))
#         if len(s) != len(l):
#             return False

#     for c in range(n):
#         s = set()
#         for r in range(n):
#             if partial_assignment[r][c] != 0:
#                 s.add(partial_assignment[r][c])
#         arr = []
#         for i in range(n):
#             if partial_assignment[i][c] != 0:
#                 arr.append(partial_assignment[i][c])
#         if len(s) != len(arr):
#             return False

#     def isValidGrid(mat, startR, startC):
#         s = set()
#         l = []
#         for i in range(startR, startR + 3):
#             for j in range(startC, startC + 3):
#                 if partial_assignment[i][j] != 0:
#                     s.add(partial_assignment[i][j])
#                     l.append(partial_assignment[i][j])
#         return len(s) == len(l)

#     for startR in [0, 3, 6]:
#         for startC in [0, 3, 6]:
#             if not isValidGrid(partial_assignment, startR, startC):
#                 return False

#     return True



# def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
#     def hasDuplicate(block):
#         filteredBlock = list(filter(lambda x: x != 0, block))
#         return len(filteredBlock) != len(set(filteredBlock))

#     n = len(partial_assignment)
#     for r in range(n):
#         row = partial_assignment[r]
#         if hasDuplicate(row):
#             return False

#     for c in range(n):
#         col = [partial_assignment[r][c] for r in range(n) if partial_assignment[r][c] != 0]
#         if hasDuplicate(col):
#             return False

#     def isValidGrid(mat, startR, startC):
#         s = set()
#         l = []
#         for i in range(startR, startR + 3):
#             for j in range(startC, startC + 3):
#                 if partial_assignment[i][j] != 0:
#                     s.add(partial_assignment[i][j])
#                     l.append(partial_assignment[i][j])
#         return len(s) == len(l)

#     for startR in [0, 3, 6]:
#         for startC in [0, 3, 6]:
#             if not isValidGrid(partial_assignment, startR, startC):
#                 return False

#     return True



# def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
#     def hasDuplicate(block):
#         filteredBlock = list(filter(lambda x: x != 0, block))
#         return len(filteredBlock) != len(set(filteredBlock))

#     n = len(partial_assignment)

#     # if any rows have duplicates
#     if any([hasDuplicate(row) for row in partial_assignment]): 
#         return False

#     # if any columns have duplicates
#     if any(hasDuplicate([partial_assignment[i][j] 
#         for i in range(n)]) 
#         for j in range(n)
#     ):
#         return False

#     def isValidGrid(mat, startR, startC):
#         return not hasDuplicate(partial_assignment[i][j] 
#             for i in range(startR, startR + 3) 
#             for j in range(startC, startC + 3)
#         )

#     regionSize = int(math.sqrt(n))

#     return all(isValidGrid(partial_assignment, startR, startC) 
#         for startR in range(0, n, regionSize) 
#         for startC in range(0, n, regionSize)
#     )

import collections
def is_valid_sudoku(partial_assignment):
    region_size = int(math.sqrt(len(partial_assignment)))
    return max(collections.Counter(
        k for i, row in enumerate(partial_assignment)
        for j, c in enumerate(row) if c != 0
        for k in ((i, str(c)), (str(c), j),
                  (i // region_size, j // region_size, str(c)))).values(),
               default=0) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
