import sys

sys.setrecursionlimit(200000)  # permitted by course for Python


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


class Graph:

    def __init__(self,
                 nodes_by_key):

        self._nodes_by_key = nodes_by_key
        self._dfs_counter = 0
        self._node_stack = []

    def _create_scc(self,
                    current_node: Node):
        """
        backtrack through the stack to generate our
        strongly connected component
        """

        strongly_connected_component = []
        while True:
            node = self._node_stack.pop()
            node.is_on_stack = False
            strongly_connected_component.append(node.key)
            if node.key == current_node.key:
                return strongly_connected_component

    # def _update_current_lowest_reachable_index(self,
    #                                            neighbour_node: Node,
    #                                            current_node: Node,
    #                                            all_scc) -> None:
    #     """
    #     update the lowest reachable index of our current node
    #     based on the neighbour node
    #     """
    #
    #     # if unvisited, explore the neighbour node
    #     if neighbour_node.is_unvisited():
    #         self._add_strongly_connected_components(neighbour_node, all_scc)
    #         current_node.lowest_reachable_index = min(current_node.lowest_reachable_index,
    #                                                   neighbour_node.lowest_reachable_index)
    #     # if on stack, this is a back edge
    #     elif neighbour_node.is_on_stack:
    #         current_node.lowest_reachable_index = min(current_node.lowest_reachable_index,
    #                                                   neighbour_node.dfs_index)

    def _add_strongly_connected_components(self,
                                           current_node: Node,
                                           all_scc) -> None:
        """
        depth first search from the node with the
        given key, and record the strongly connected
        components
        """

        current_node.dfs_index = self._dfs_counter
        current_node.lowest_reachable_index = self._dfs_counter
        self._dfs_counter += 1

        self._node_stack.append(current_node)
        current_node.is_on_stack = True

        for neighbour_key in current_node.neighbours:
            neighbour_node = self._nodes_by_key[neighbour_key]

            # if unvisited, explore the neighbour node
            if neighbour_node.is_unvisited():
                self._add_strongly_connected_components(neighbour_node, all_scc)
                current_node.lowest_reachable_index = min(current_node.lowest_reachable_index,
                                                          neighbour_node.lowest_reachable_index)
            # if on stack, this is a back edge
            elif neighbour_node.is_on_stack:
                current_node.lowest_reachable_index = min(current_node.lowest_reachable_index,
                                                          neighbour_node.dfs_index)

        if current_node.is_root():
            scc = self._create_scc(current_node)
            all_scc.append(scc)

    def _get_strongly_connected_components(self):
        """
        return the strongly connected components of a
        graph as the keys of the graph using Tarjan's
        algorithm
        """

        strongly_connected_components = []

        for node in self._nodes_by_key.values():
            if node.is_unvisited():
                self._add_strongly_connected_components(node, strongly_connected_components)

        return strongly_connected_components

    def get_number_of_strongly_connected_components(self) -> int:
        """
        apply Tarjan's algorithm to find the strongly
        connected components, and return how many
        there are
        """

        scc = self._get_strongly_connected_components()
        return len(scc)


def read_graph_from_stdin() -> Graph:

    number_of_nodes, number_of_edges = list(map(int, input().split(" ")))
    nodes_by_key = {i: Node(i, []) for i in range(1, number_of_nodes + 1)}

    for _ in range(number_of_edges):
        start, end = list(map(int, input().split(" ")))
        nodes_by_key[start].neighbours.append(end)

    return Graph(nodes_by_key)


if __name__ == "__main__":
    graph = read_graph_from_stdin()
    print(graph.get_number_of_strongly_connected_components())

