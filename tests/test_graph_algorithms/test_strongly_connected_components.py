import unittest
from graph_algorithms.directional_graphs.strongly_connected_components import Node, Graph


class TestStronglyConnectedComponents(unittest.TestCase):

    def test_get_number_of_strongly_connected_components(self):
        # arrange
        nodes_by_key = {1: Node(1, [2]), 2: Node(2, [3]), 3: Node(3, [1]), 4: Node(4, [1])}
        graph = Graph(nodes_by_key)

        # act
        result = graph.get_number_of_strongly_connected_components()

        # result
        self.assertEqual(2, result)
