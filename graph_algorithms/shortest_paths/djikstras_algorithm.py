import heapq
from functools import total_ordering
from collections import namedtuple


Edge = namedtuple("Edge", ["weight", "destination"])
Node = namedtuple("Node", ["key", "shortest_path"])


@total_ordering
class Node:

    def __init__(self,
                 key: int,
                 shortest_path: int):

        self.key = key
        self.shortest_path = shortest_path

    def __eq__(self, other):
        return self.shortest_path == other.shortest_path

    def __ne__(self, other):
        return self.shortest_path != other.shortest_path

    def __lt__(self, other):
        return self.shortest_path < other.shortest_path


def get_shortest_path(graph,
                      start: int,
                      end: int):
    """
    find the shortest path from start to end
    in the graph using djikstras algorithm
    """

    visited = set()
    distances = dict()
    for i in graph:
        distances[i] = float("inf")

    distances.update({start: 0})
    priority_queue = [Node(start, 0)]
    heapq.heapify(priority_queue)

    while priority_queue:
        current_node = heapq.heappop(priority_queue)
        if current_node.key in visited:
            continue
        else:
            visited.add(current_node.key)

        current_edges = graph[current_node.key]
        for edge in current_edges:
            destination_key = edge.destination
            distance_via_current = distances[current_node.key] + edge.weight
            distances[destination_key] = min(distances[destination_key], distance_via_current)
            heapq.heappush(priority_queue, Node(destination_key, distances[destination_key]))

    if distances[end] == float("inf"):
        return -1
    else:
        return distances[end]


def read_directed_weighted_graph_from_stdin():

    graph = dict()
    n_nodes, n_vertices = list(map(int, input().split()))

    for n in range(1, n_nodes + 1):
        graph.update({n: []})

    for _ in range(n_vertices):
        start, end, weight = list(map(int, input().split()))
        graph[start].append(Edge(weight, end))

    return graph


if __name__ == "__main__":

    g = read_directed_weighted_graph_from_stdin()
    s, e = list(map(int, input().split()))
    shortest_path = get_shortest_path(g, s, e)
    print(shortest_path)



