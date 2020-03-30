import heapq
import math
from functools import total_ordering


@total_ordering
class Point:

    def __init__(self,
                 coord,
                 mst_distance):
        self.coord = coord
        self.mst_distance = mst_distance

    def __eq__(self, other):
        return self.mst_distance == other.mst_distance

    def __ne__(self, other):
        return self.mst_distance != other.mst_distance

    def __le__(self, other):
        return self.mst_distance < other.mst_distance


def get_distance(coord_1,
                 coord_2):
    return math.sqrt((coord_1[0] - coord_2[0]) ** 2 + (coord_1[1] - coord_2[1]) ** 2)


def get_min_spanning_tree_length(all_coords,
                                 start_coord):
    mst = set()
    path_length = 0
    point_priority_queue = [Point(start_coord, 0)]
    heapq.heapify(point_priority_queue)
    total_vertices = len(all_coords)

    while len(mst) < total_vertices:

        current_point = heapq.heappop(point_priority_queue)
        if current_point.coord in mst:
            continue
        else:
            mst.add(current_point.coord)
            all_coords.remove(current_point.coord)
            path_length += current_point.mst_distance

        for other_coord in all_coords:
            distance_to_current = get_distance(current_point.coord, other_coord)
            heapq.heappush(point_priority_queue, Point(other_coord, distance_to_current))

    return path_length


def read_coords_from_stdin():

    all_coords = set()
    n_coords = int(input())

    for _ in range(n_coords):
        all_coords.add(tuple(map(int, input().split())))

    return all_coords


if __name__ == "__main__":

    ac = read_coords_from_stdin()
    first_coord = list(ac)[0]
    length = get_min_spanning_tree_length(ac, first_coord)
    print("{0:.7f}".format(length))
