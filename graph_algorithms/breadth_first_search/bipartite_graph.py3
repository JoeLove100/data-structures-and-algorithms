from collections import deque


def is_bipartite(graph,
                 initial) -> int:

    visited = set()
    queue = deque([initial])
    current_colour = 0
    colours = {initial: current_colour}

    while queue:

        current_node = queue.popleft()
        visited.add(current_node)
        successors = graph[current_node]

        for successor_node in successors:
            if successor_node in visited:
                if colours[successor_node] == colours[current_node]:
                    return 0
            else:
                colours[successor_node] = (colours[current_node] + 1) % 2
                queue.append(successor_node)

    return 1


def parse_undirected_graph_from_stdin():
    graph = {}
    n_edges, n_vertices = list(map(int, input().split()))

    for i in range(1, n_edges + 1):
        graph.update({i: []})

    for _ in range(n_vertices):
        start, end = list(map(int, input().split()))
        graph[start].append(end)
        graph[end].append(start)

    return graph


if __name__ == "__main__":

    g = parse_undirected_graph_from_stdin()
    result = is_bipartite(g, 1)
    print(result)

