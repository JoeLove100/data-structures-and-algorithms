import unittest
from graph_algorithms.directional_graphs.topological_orderings import Graph, Node


class TestTopologicalOrderings(unittest.TestCase):

    def test_get_topological_ordering_all_connected(self):
        # arrange
        nodes_by_key = {1: Node(1, [2]), 2: Node(2, []), 3: Node(3, [1]), 4: Node(4, [1])}
        graph = Graph(nodes_by_key)

        # act
        result = graph.get_topological_ordering()

        # assert
        self.assertSequenceEqual([4, 3, 1, 2], result)

    def test_get_topological_ordering_single_nodes(self):
        # arrange
        nodes_by_key = {1: Node(1, []), 2: Node(2, []), 3: Node(3, [1]), 4: Node(4, [])}
        graph = Graph(nodes_by_key)

        # act
        result = graph.get_topological_ordering()

        # assert
        self.assertSequenceEqual([4, 3, 2, 1], result)

    def test_get_topological_ordering_multiple_components(self):
        # arrange
        nodes_by_key = {1: Node(1, []), 2: Node(2, [1]), 3: Node(3, [1, 2]),
                        4: Node(4, [1, 3]), 5: Node(5, [2, 3])}
        graph = Graph(nodes_by_key)

        # act
        result = graph.get_topological_ordering()

        # assert
        self.assertSequenceEqual([5, 4, 3, 2, 1], result)
