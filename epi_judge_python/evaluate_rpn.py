from test_framework import generic_test


def evaluate(expression: str) -> int:
    s = []
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b
    }
    for _, c in enumerate(expression.split(",")):
        if c not in operators:
            s.append(c)
        else:
            operand1 = int(s.pop())
            operand2 = int(s.pop())
            s.append(operators[c](operand1, operand2))
    return int(s[-1])

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
