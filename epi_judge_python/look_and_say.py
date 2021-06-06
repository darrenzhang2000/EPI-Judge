from test_framework import generic_test


def look_and_say(n: int) -> str:
    if n == 1:
        return '1'
    prev = '1'
    for _ in range(1, n):
        cur = []
        start = 0
        end = 0
        while True:
            while end < len(prev) and prev[end] == prev[start]:
                end += 1
            cur.append(str(end - start)) # how many
            cur.append(prev[start]) # of this number
            if end == len(prev):
                break
            start = end
        prev = "".join(cur)
    return prev



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
