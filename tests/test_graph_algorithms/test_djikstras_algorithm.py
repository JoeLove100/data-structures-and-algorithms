import unittest
from graph_algorithms.shortest_paths.djikstras_algorithm import get_shortest_path, Edge, Node


class TestDjikstrasAlgorithm(unittest.TestCase):

    def test_shortest_path_to_start_is_zero(self):
        # arrange
        graph = {0: []}

        # act
        result = get_shortest_path(graph, 0, 0)

        # assert
        self.assertEqual(0, result)

    def test_shortest_path_in_straight_line(self):
        # arrange
        graph = {1: [Edge(2, 2)], 2: [Edge(1, 3)], 3: [Edge(0, 4)], 4: [Edge(3, 5)], 5: []}

        # act
        result = get_shortest_path(graph, 1, 5)

        # assert
        self.assertEqual(6, result)

    def test_shortest_path_with_edge_to_self(self):
        # arrange
        graph = {1: [Edge(1, 1), Edge(3, 2)], 2: [Edge(2, 3)], 3: [Edge(3, 4)], 4: []}

        # act
        result = get_shortest_path(graph, 1, 4)

        # assert
        self.assertEqual(8, result)

    def test_graph_with_cycle(self):
        # arrange
        graph = {1: [Edge(2, 2)], 2: [Edge(4, 3)], 3: [Edge(5, 4)], 4: [Edge(1, 2)]}

        # act
        result = get_shortest_path(graph, 1, 2)

        # assert
        self.assertEqual(2, result)

    def test_graph_multiple_paths_from_start(self):
        # arrange
        graph = {1: [Edge(1, 2), Edge(5, 3)], 2: [Edge(2, 3)], 3: [], 4: Edge(2, 1)}

        # act
        result = get_shortest_path(graph, 1, 3)

        # assert
        self.assertEqual(3, result)

    def test_no_path_returns_minus_one(self):
        # arrange
        graph = {1: [Edge(7, 2), Edge(5, 3)], 2: [Edge(2, 3)], 3: []}

        # act
        result = get_shortest_path(graph, 3, 2)

        # assert
        self.assertEqual(result, -1)

    def test_multiple_shortest_paths(self):
        # arrange
        graph = {1: [Edge(2, 3), Edge(4, 2)], 2: [Edge(3, 3), Edge(3, 5), Edge(2, 4)],
                 3: [Edge(1, 2), Edge(4, 4), Edge(4, 5)], 4: [], 5: [Edge(1, 4)]}

        # act
        result = get_shortest_path(graph, 1, 5)

        # assert
        self.assertEqual(result, 6)

    def test_node_equal_to(self):
        # arrange
        n_1 = Node(1, 2)
        n_2 = Node(2, 2)

        # act
        result = n_1 == n_2

        # assert
        self.assertTrue(result)

    def test_node_not_equal(self):
        # arrange
        n_1 = Node(2, 1)
        n_2 = Node(2, 2)

        # act
        result = n_1 != n_2

        # assert
        self.assertTrue(result)

    def test_node_greater_than(self):
        # arrange
        n_1 = Node(1, 5)
        n_2 = Node(2, 3)

        # act
        result = n_1 > n_2

        # assert
        self.assertTrue(result)
