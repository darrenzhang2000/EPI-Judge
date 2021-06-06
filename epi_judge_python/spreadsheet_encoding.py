from test_framework import generic_test
from functools import reduce

def ss_decode_col_id(w: str) -> int:
        return reduce(lambda acc, c: 26 * acc + ord(c) - ord('A') + 1 , w, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
