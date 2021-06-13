from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    '''
    make a queue using two stacks

    enqueue -> copy from real queue to temp by popping from real queue and pushing 
        to temp until real queue is empty. push element into temp.

    temp = [2 1]
    real queue = [1 2 3]
    1 2
    e1 e2 e3 d1 d2 e4 e5 d3 d4 d5



    '''
    def __init__(self):
        self._queueAsStack = []
        self._stack = []

    # O(1) time
    def enqueue(self, x: int) -> None:
        self._stack.append(x)

    # O(n) time
    def dequeue(self) -> int:
        if not self._queueAsStack:
            while self._stack:
                self._queueAsStack.append(self._stack.pop())
        return self._queueAsStack.pop()


def queue_tester(ops):
    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    # q = Queue()
    # for v in [1, 2, 3]:
    #     q.enqueue(v)
    # print(q._queueAsStack[-1])

    exit(
        generic_test.generic_test_main('queue_from_stacks.py',
                                       'queue_from_stacks.tsv', queue_tester))
