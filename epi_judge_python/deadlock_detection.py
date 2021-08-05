import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

UNPROCESSED, INPROGRESS, PROCESSED = range(3)
class GraphVertex:
    def __init__(self) -> None:
        self.edges: List['GraphVertex'] = []
        self.state = UNPROCESSED


def is_deadlocked(graph: List[GraphVertex]) -> bool:
    '''
    Reasonings:
    If a vertex has dependencies, it has to wait until all of the dependencies have
    finished processing before it can complete its own.
    '''
    stack = []
    for vertex in graph:
        stack.append(vertex)
        while stack:
            if vertex.state == UNPROCESSED:
                vertex.state = 1
                for neighbor in vertex.edges:
                    if neighbor.state == PROCESSED:
                        return True
                    stack.append(neighbor)
            elif vertex.state == INPROGRESS:
                vertex.state = PROCESSED
            else:
                stack.pop()
    return False
        


@enable_executor_hook
def is_deadlocked_wrapper(executor, num_nodes, edges):
    if num_nodes <= 0:
        raise RuntimeError('Invalid num_nodes value')
    graph = [GraphVertex() for _ in range(num_nodes)]

    for (fr, to) in edges:
        if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_deadlocked, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('deadlock_detection.py',
                                       'deadlock_detection.tsv',
                                       is_deadlocked_wrapper))
