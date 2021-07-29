from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    '''
    let k = final_score, n = len(individual_play_scores)
    time: O(kn), space O(kn)
    space can be improved to O(n) 
    '''
    individual_play_scores.sort()
    memo = [[1] + [0 for _ in range(final_score)] for _ in range(len(individual_play_scores))]
    for i in range(len(memo)):
        n = individual_play_scores[i]
        for j in range(1, len(memo[0])):                
            memo[i][j] = memo[i][j - n] if j - n >= 0 else 0
            memo[i][j] += memo[i - 1][j] if i - 1 >= 0 else 0
    return memo[-1][-1]





    #count = [0]
    #def r(score, start):
    #    if score == 0:
    #        count[0] += 1
    #    elif score < 0:
    #        return
    #    else:
    #        for i in range(start, len(individual_play_scores)):
    #            n = individual_play_scores[i]
    #            r(score - n, i)
    #r(final_score, 0)

    #return count[0]

    '''
    scores = 2, 3, 7
    final_score = 12

    include 2 or not include 2
    include 3 or not include 3
    include 7 or not include 7

    2 2 2 2 2 2 
              7

    3

    7
    '''

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
