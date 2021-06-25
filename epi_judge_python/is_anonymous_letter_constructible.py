from test_framework import generic_test
from collections import Counter

def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    letter_char_count = Counter(letter_text)
    magazine_char_count = Counter(magazine_text)
    for c in letter_char_count.keys():
        freq = letter_char_count[c]
        if not magazine_char_count[c] or freq > magazine_char_count[c]:
            print(c, freq, magazine_char_count[c])
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
