import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    def dfs(cur):
        if not (0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x]) and maze[cur.x][cur.y] == WHITE):
            return False
        path.append(cur)
        maze[cur.x][cur.y] = BLACK
        if cur == e:
            return True
        
        if any(
            map(
                dfs,
                map(Coordinate, (cur.x - 1, cur.x + 1, cur.x, cur.x), (cur.y, cur.y, cur.y - 1, cur.y + 1))
        )):
            return True

        del path[-1]
        return False
    
    path = []
    dfs(s)
    return path
    # path = []
    # visited = set()
    # found = [False]
    # def dfs(x, y):
    #     print(found)
    #     if (x, y) in visited or found[0]:
    #         return
    #     visited.add((x, y))
    #     path.append(Coordinate(x, y))
    #     if x == e.x and y == e.y:
    #         found[0] = True
    #         return
    #     offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #     for offset in offsets:
    #         new_x, new_y = x + offset[0], y + offset[1]
    #         if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]):
    #             dfs(new_x, new_y)
    #     path.pop()
    #     visited.remove((x, y))
    # dfs(s.x, s.y)
    # return len(path) > 0


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
