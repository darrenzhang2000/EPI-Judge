from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import deque

class QueueWithMax:
    def __init__(self):
        self._q = deque([])
        self.maxDeque = deque([])
        
    def enqueue(self, x: int) -> None:
        self._q.append(x)
        while self.maxDeque and x > self.maxDeque[-1]:
            self.maxDeque.pop()
        self.maxDeque.append(x)

    def dequeue(self) -> int:
        el = self._q.popleft()
        if el == self.maxDeque[0]:
            self.maxDeque.popleft()
        return el

    def max(self) -> int:
        return self.maxDeque[0]


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_with_max.py',
                                       'queue_with_max.tsv', queue_tester))
