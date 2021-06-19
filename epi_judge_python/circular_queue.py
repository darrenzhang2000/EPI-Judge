from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    '''
    [1, 1, 1]
     |
           |
    '''
    def __init__(self, capacity: int) -> None:
        self.arr = [None] * capacity
        self._size = 0
        self.capacity = capacity
        self.start, self.end = 0, 0
        return

    def enqueue(self, x: int) -> None:
        print('e', x)
        if self._size == self.capacity:
            return
        self.arr[self.end] = x
        self.end = (self.end + 1) % self.capacity
        self._size += 1

    def dequeue(self) -> int:
        if self._size == 0:
            return
        self._size -= 1
        n = self.arr[self.start]
        self.start = (self.start + 1 + self.capacity) % self.capacity
        print('d', n)
        return n


    def size(self) -> int:
        return self._size


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
