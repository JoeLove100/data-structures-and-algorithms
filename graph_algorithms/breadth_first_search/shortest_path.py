from collections import deque


def get_shortest_path(graph,
                      initial: int,
                      target: int) -> int:
    visited = set()
    queue = deque([initial])
    distances = {initial: 0}

    while queue:
        current = queue.popleft()

        if current == target:
            return distances[current]

        all_successors = graph[current]
        for successor in all_successors:
            if successor not in visited and successor != current:
                visited.add(successor)
                distances[successor] = distances[current] + 1
                queue.append(successor)

    return -1


def get_shortest_path_wrong(graph,
                            initial: int,
                            target: int) -> int:
    visited = set()
    queue = deque([initial])
    distances = {initial: 0}

    while queue:
        current = queue.popleft()

        if current == target:
            return distances[current]

        if current in visited:
            continue
        else:
            visited.add(current)

        all_successors = graph[current]
        for successor in all_successors:

            visited.add(successor)
            distances[successor] = distances[current] + 1
            queue.append(successor)

    return -1


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

    ans = get_shortest_path({1: [4, 1, 1, 5, 1, 1, 1, 1, 3, 2], 2: [3, 1], 3: [2, 1], 4: [1, 5, 5], 5: [1, 4, 4]},
                            1, 5)
    print(ans)

    ans = get_shortest_path_wrong({1: [4, 1, 1, 5, 1, 1, 1, 1, 3, 2], 2: [3, 1], 3: [2, 1], 4: [1, 5, 5], 5: [1, 4, 4]},
                                  1, 5)

    print(ans)

# if __name__ == "__main__":
#     g = parse_undirected_graph_from_stdin()
#     s, t = list(map(int, input().split()))
#     sp = get_shortest_path(g, s, t)
#     print(sp)

# if __name__ == "__main__":
#
#     import random
#     random.seed(1234)
#
#     for _ in range(1000):
#
#         graph = {k: [] for k in range(1, 6)}
#
#         for _ in range(10):
#             n_1 = random.randint(1, 5)
#             n_2 = random.randint(1, 5)
#             graph[n_1].append(n_2)
#             graph[n_2].append(n_1)
#
#         start = 1
#         end = 5
#
#         shortest_path_correct = get_shortest_path(graph, start, end)
#         shortest_path_wrong = get_shortest_path_wrong(graph, start, end)
#
#         if shortest_path_correct == shortest_path_wrong:
#             print("OK")
#         else:
#             print(f"Incorrect for {graph}")
#             print(f"My answer was {shortest_path_wrong}")
#             print(f"Actual answer was {shortest_path_correct}")
#             break
