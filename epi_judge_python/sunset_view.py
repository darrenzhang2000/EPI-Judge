from typing import Iterator, List

from test_framework import generic_test


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    s = []
    maxHeight = float('-inf')
    for i in range(len(sequence) -1, -1, -1):
        height = sequence[i]
        if not s or height > maxHeight:
            s.append(i)
            maxHeight = height
    return s


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
