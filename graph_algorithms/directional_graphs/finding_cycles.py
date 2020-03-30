"""
https://www.youtube.com/watch?v=TyWtx7q2D7Y
https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
"""


class Node:

    def __init__(self,
                 key: int,
                 neighbours):
        self.key = key
        self.neighbours = neighbours
        self.is_on_stack = False
        self.dfs_index = None
        self.lowest_reachable_index = None

    def is_root(self) -> bool:
        return self.dfs_index == self.lowest_reachable_index

    def is_unvisited(self) -> bool:
        return self.dfs_index is None


def _create_scc(current_node: Node,
                node_stack):
    """
    backtrack through the stack to generate our
    strongly connected component
    """

    strongly_connected_component = []
    while True:
        node = node_stack.pop()
        node.is_on_stack = False
        strongly_connected_component.append(node.key)
        if node.key == current_node.key:
            return strongly_connected_component


def _update_current_lowest_reachable_index(neighbour_node: Node,
                                           current_node: Node,
                                           nodes_by_key,
                                           counter: int,
                                           node_stack,
                                           all_scc) -> None:
    """
    update the lowest reachable index of our current node
    based on the neighbour node
    """

    if neighbour_node.is_unvisited():
        _add_strongly_connected_components(neighbour_node, nodes_by_key, counter, node_stack, all_scc)
        current_node.lowest_reachable_index = min(current_node.lowest_reachable_index,
                                                  neighbour_node.lowest_reachable_index)
    elif neighbour_node.is_on_stack:
        current_node.lowest_reachable_index = min(current_node.lowest_reachable_index,
                                                  neighbour_node.dfs_index)


def _add_strongly_connected_components(current_node: Node,
                                       nodes_by_key,
                                       counter: int,
                                       node_stack,
                                       all_scc) -> None:
    """
    depth first search from the node with the
    given key, and record the strongly connected
    components
    """

    current_node.dfs_index = counter
    current_node.lowest_reachable_index = counter
    counter += 1

    node_stack.append(current_node)
    current_node.is_on_stack = True

    for neighbour_key in current_node.neighbours:
        neighbour_node = nodes_by_key[neighbour_key]
        _update_current_lowest_reachable_index(neighbour_node, current_node, nodes_by_key, counter,
                                               node_stack, all_scc)

    if current_node.is_root():
        scc = _create_scc(current_node, node_stack)
        all_scc.append(scc)


def get_strongly_connected_components(nodes_by_key):
    """
    return the strongly connected components of a
    graph as the keys of the graph using Tarjan's
    algorithm
    """

    strongly_connected_components = []
    dfs_counter = 0

    for node in nodes_by_key.values():
        if node.is_unvisited():
            node_stack = []
            _add_strongly_connected_components(node, nodes_by_key, dfs_counter, node_stack,
                                               strongly_connected_components)

    return strongly_connected_components


def read_graph_from_stdin():

    number_of_nodes, number_of_edges = list(map(int, input().split(" ")))
    nodes_by_key = {i: Node(i, []) for i in range(1, number_of_nodes + 1)}

    for _ in range(number_of_edges):
        start, end = list(map(int, input().split(" ")))
        nodes_by_key[start].neighbours.append(end)

    return nodes_by_key


if __name__ == "__main__":
    graph = read_graph_from_stdin()
    scc = get_strongly_connected_components(graph)
    if len(scc) == len(graph):
        print(0)
    else:
        print(1)





