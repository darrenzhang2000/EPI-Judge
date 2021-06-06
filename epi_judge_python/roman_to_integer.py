from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    exceptions = {'IX': 9, 'IV': 4, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    total = 0
    toContinue = False
    for i, c in enumerate(s):
        if toContinue:
            toContinue = False
            continue
        if i + 1 < len(s) and s[i:i+2] in exceptions:
            total += exceptions[s[i:i+2]]
            toContinue = True
        else:
            total += values[c]
    return total



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
