from test_framework import generic_test


def snake_string(s: str) -> str:
    top = []
    mid = []
    bot = []
    for i, c in enumerate(s):
        if i % 2 == 0:
            mid.append(c)
        elif i % 4 == 1:
            top.append(c)
        else:
            bot.append(c)
    return "".join(top + mid + bot)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))
