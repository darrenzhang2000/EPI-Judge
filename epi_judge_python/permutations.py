from typing import List

from test_framework import generic_test, test_utils


# def permutations(A: List[int]) -> List[List[int]]:
#     res = []
#     def helper(a, s):
#         if not s:
#             res.append(a[:])
#             return
#         for v in s:
#             a.append(v)
#             helper(a[:], s-{v})   
#     helper([], set(A))
#     return res

def permutations(A: List[int]) -> List[List[int]]:
    def helper(nums):
        if not nums: return [[]]
        
        ans = []

        for num in nums:
            for suffix in helper(nums - {num}):
                ans.append([num]+suffix)

        return ans

    return helper(set(A))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
