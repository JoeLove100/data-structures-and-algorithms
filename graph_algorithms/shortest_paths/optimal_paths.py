from collections import namedtuple, OrderedDict

Edge = namedtuple("Edge", ["weight", "destination"])


def get_optimal_paths(graph,
                      start: int):

    distances = OrderedDict()

    for node in graph:
        distances[node] = float("inf")

    distances[start] = 0

    # B-F to get the min distances
    for _ in range(1, len(graph)):
        relaxation_count = 0
        for node, edges_for_node in graph.items():
            for edge in edges_for_node:
                alt = distances[node] + edge.weight
                if alt < distances[edge.destination]:
                    distances[edge.destination] = alt
                    relaxation_count += 1

        if relaxation_count == 0:
            break

    negative_cycle_nodes = set()

    # get nodes in negative cycles
    for node, edges_for_node in graph.items():
        for edge in edges_for_node:
            alt = distances[node] + edge.weight
            if alt < distances[edge.destination]:
                negative_cycle_nodes.add(edge.destination)

    # finally, dsf negative nodes
    visited = set()
    for node in negative_cycle_nodes:
        if node in visited:
            continue

        node_stack = [node]
        while node_stack:
            current_node = node_stack.pop()
            if current_node in visited:
                continue
            else:
                distances[current_node] = -float("inf")
                visited.add(current_node)

            all_successors = [edge.destination for edge in graph[current_node]]
            for successor in all_successors:
                node_stack.append(successor)

    return distances


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
    s = int(input())
    d = get_optimal_paths(g, s)
    for d, dist in d.items():
        if dist == float("inf"):
            print("*")
        elif dist == -float("inf"):
            print("-")
        else:
            print(dist)










