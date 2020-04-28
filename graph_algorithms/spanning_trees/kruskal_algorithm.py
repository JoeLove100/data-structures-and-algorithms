import math


class Edge:

    def __init__(self,
                 start,
                 end):

        self.start = start
        self.end = end
        self.distance = self.get_distance(start, end)

    @staticmethod
    def get_distance(start, end):
        return math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)


class Kruskal:

    def __init__(self):

        self._parents = dict()
        self._rank = dict()

    def add_point(self,
                  point):

        self._parents.update({point: point})
        self._rank.update({point: 0})

    def find(self,
             point):

        if point != self._parents[point]:
            self._parents[point] = self.find(self._parents[point])

        return self._parents[point]

    def union(self,
              point_1,
              point_2):

        parent_1 = self.find(point_1)
        parent_2 = self.find(point_2)

        if parent_1 == parent_2:
            return

        if self._rank[parent_1] < self._rank[parent_2]:
            self._parents[parent_1] = parent_2
        elif self._rank[parent_1] > self._rank[parent_2]:
            self._parents[parent_2] = parent_1
        else:
            self._parents[parent_1] = parent_2
            self._rank[parent_2] += 1

    def get_all_edges_sorted(self):

        all_points = list(self._parents)
        all_edges = []
        processed = set()

        for point_1 in all_points:
            for point_2 in all_points:
                if point_1 == point_2 or point_2 in processed:
                    continue
                else:
                    all_edges.append(Edge(point_1, point_2))

            processed.add(point_1)

        return sorted(all_edges, reverse=True, key=lambda x: x.distance)

    def get_min_distance(self,
                         k: int):

        trees_in_forest = len(self._rank)
        sorted_edges = self.get_all_edges_sorted()

        while True:
            edge = sorted_edges.pop()
            if self.find(edge.start) == self.find(edge.end):
                continue
            else:
                if trees_in_forest <= k:
                    return edge.distance
                else:
                    self.union(edge.start, edge.end)
                    trees_in_forest -= 1


def read_coords_from_stdin():

    all_coords = set()
    n_coords = int(input())

    for _ in range(n_coords):
        all_coords.add(tuple(map(int, input().split())))

    return all_coords


if __name__ == "__main__":

    coord = read_coords_from_stdin()
    k = int(input())
    kruskal = Kruskal()
    for c in coord:
        kruskal.add_point(c)

    print("{0:.7f}".format(kruskal.get_min_distance(k)))
