from typing import List
import functools
from test_framework import generic_test


def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    @functools.lru_cache
    def is_suffix_contained(x, y, idx):
        if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]) or not grid[x][y] == pattern[idx]:
            return False

        if idx == len(pattern) - 1:
            return True
        
        new_coors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        return any(is_suffix_contained(*coors, idx + 1) for coors in new_coors)

    return any(is_suffix_contained(i, j, 0) for i in range(len(grid)) for j in range(len(grid[0])))



''' 
def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if dfs(grid, pattern, r, c, 0):
                return True
    return False

def dfs(grid, pattern, x, y, idx):
    if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]) or grid[x][y] != pattern[idx]:
        return False
    
    if idx == len(pattern) - 1:
        return True
    
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for offset in offsets:
        if dfs(grid, pattern, x + offset[0], y + offset[1], idx + 1):
            return True
    
    return False

'''



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
