from typing import List

from test_framework import generic_test


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    color = image[x][y]
    flipped_color = 1 - color
    def flip_if_color(x, y):
        if not (0 <= x < len(image) and 0 <= y < len(image[0])) or image[x][y] != color:
            return
        
        image[x][y] = flipped_color
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in offsets:
            flip_if_color(x + dx, y + dy)

    flip_if_color(x, y)
    return image    

def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
