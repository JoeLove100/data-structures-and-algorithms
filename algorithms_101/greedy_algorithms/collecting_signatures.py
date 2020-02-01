import sys
from collections import namedtuple
from typing import List

Segment = namedtuple('Segment', 'start end')


def get_optimal_points(segments: List[Segment]):
    """
    get a set of points of minimal size such that
    each segment contains at least one point
    """

    segments.sort(key=lambda x: x.end, reverse=True)
    points = []

    while len(segments) > 0:

        leftmost_line_end = segments.pop().end
        points.append(leftmost_line_end)
        segments = [s for s in segments if s.start > leftmost_line_end]

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    s = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    p = get_optimal_points(s)
    print(len(p))
    print(*p)
