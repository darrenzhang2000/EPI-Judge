from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    base10N = convToBase10(b1, num_as_string)
    return convToBaseB2From10(b2, base10N)

def convToBase10(b1, n):
    total = 0
    for i in range(len(n)):
        power = len(n) - 1 - i
        total +=  int(n[i]) * int(b1)**power
    return total

def convToBaseB2From10(b2, n):
    res = []
    while n:
        res.append(str(n % b2))
        n //= b2
    return int("".join(list(reversed(res))))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
