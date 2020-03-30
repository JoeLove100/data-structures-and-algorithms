import unittest
from graph_algorithms.directional_graphs import _create_scc, Node, get_strongly_connected_components


class TestFindingCycles(unittest.TestCase):

    def test_create_scc(self):
        # arrange
        current_node = Node(4, [])
        node_stack = [Node(2, []), current_node, Node(5, []), Node(6, [])]

        # act
        result = _create_scc(current_node, node_stack)

        # assert
        self.assertSequenceEqual([6, 5, 4], result)

    def test_get_strongly_connected_components_linear(self):
        # arrange
        nodes_by_key = {0: Node(0, [1]), 1: Node(1, [2]), 2: Node(2, [])}

        # act
        result = get_strongly_connected_components(nodes_by_key)

        # assert
        self.assertSequenceEqual([[2], [1], [0]], result)

    def test_get_strongly_connected_components_two_distinct(self):
        # arrange
        nodes_by_key = {0: Node(0, []), 1: Node(1, [2]), 2: Node(2, [1])}

        # act
        result = get_strongly_connected_components(nodes_by_key)

        # assert
        self.assertSequenceEqual([[0], [2, 1]], result)

    def test_get_strongly_connected_components_one_component(self):
        # arrange
        nodes_by_key = {10: Node(10, [11]), 11: Node(11, [12, 13]), 12: Node(12, [13]),
                        13: Node(13, [10])}

        # act
        result = get_strongly_connected_components(nodes_by_key)

        # assert
        self.assertSequenceEqual([[13, 12, 11, 10]], result)

    def test_get_strongly_connected_two_components(self):
        # arrange
        nodes_by_key = {0: Node(0, []), 1: Node(1, [0, 2]), 2: Node(2, [3]), 3: Node(3, [1])}

        # act
        result = get_strongly_connected_components(nodes_by_key)

        # assert
        self.assertSequenceEqual([[0], [3, 2, 1]], result)

    def test_get_strongly_connected_components(self):
        """
        example from wiki page
        """
        # arrange
        nodes_by_key = {1: Node(1, [2]), 2: Node(2, [3]), 3: Node(3, [1]),
                        4: Node(4, [2, 3, 6]), 5: Node(5, [3, 7]),
                        6: Node(6, [4, 5]), 7: Node(7, [5]), 8: Node(8, [6, 8])}

        # act
        result = get_strongly_connected_components(nodes_by_key)

        # assert
        self.assertSequenceEqual([[3, 2, 1], [7, 5], [6, 4], [8]], result)





