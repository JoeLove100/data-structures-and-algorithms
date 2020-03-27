from collections import namedtuple

Edge = namedtuple("Edge", ["weight", "destination"])


def is_negative_cycle(graph,
                      start: int,
                      max_val: int = 10 ** 5) -> int:

    distance = dict()
    for i in graph:
        distance[i] = max_val

    distance[start] = 0

    # B-F algorithm to get min distances
    for _ in range(1, len(graph)):
        relax_count = 0
        for node, edges_for_node in graph.items():
            for edge in edges_for_node:
                alt_length = distance[node] + edge.weight
                if distance[edge.destination] > alt_length:
                    relax_count += 1
                    distance[edge.destination] = alt_length

        if relax_count == 0:
            # terminate early if no changes
            return 0

    # one last iteration to find negative cycles
    for node, edges_for_node in graph.items():
        for edge in edges_for_node:
            alt_length = distance[node] + edge.weight
            if alt_length < distance[edge.destination]:
                return 1

    return 0


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
    print(is_negative_cycle(g, 1))
