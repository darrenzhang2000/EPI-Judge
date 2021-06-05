from test_framework import generic_test


def ss_decode_col_id(w: str) -> int:
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        n = 0
        for i in range(len(w)):
            cIdx = letters.index(w[i])
            n = n * 26 + cIdx + 1
        return n


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
