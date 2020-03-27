import unittest
from graph_algorithms.shortest_paths.bellman_ford import is_negative_cycle, Edge


class TestBellmanFord(unittest.TestCase):

    def test_no_cycle_in_linear_graph(self):
        # arrange
        graph = {1: [Edge(-1, 2)], 2: [Edge(3, 3)], 3: [Edge(-4, 4)], 4: []}

        # act
        result = is_negative_cycle(graph, 1)

        # assert
        self.assertEqual(0, result)

    def test_no_negative_cycle_one_node(self):
        # arrange
        graph = {1: []}

        # act
        result = is_negative_cycle(graph, 1)

        # assert
        self.assertEqual(0, result)

    def test_no_negative_cycle_with_self_edge_positive(self):
        # arrange
        graph = {1: [Edge(1, 1), Edge(3, 2)], 2: []}

        # act
        result = is_negative_cycle(graph, 1)

        # assert
        self.assertEqual(0, result)

    def test_negative_cycle_with_self_edge_negative(self):
        # arrange
        graph = {1: [Edge(-1, 1), Edge(3, 2)], 2: []}

        # act
        result = is_negative_cycle(graph, 1)

        # assert
        self.assertEqual(1, result)

    def test_negative_cycle_exists(self):
        # arrange
        graph = {1: [Edge(-5, 2)], 2: [Edge(2, 3)], 3: [Edge(1, 1)], 4: [Edge(2, 1)]}

        # act
        result = is_negative_cycle(graph, 1)

        # assert
        self.assertEqual(1, result)

    def test_negative_cycle_circle(self):
        # arrange
        graph = {i: [Edge(-1, max(i % 9, 1))] for i in range(1, 10)}

        # act
        result = is_negative_cycle(graph, 1)

        # assert
        self.assertEqual(1, result)

    def test_unconnected_graph(self):
        # arrange
        graph = {1: [Edge(1, 2)], 2: [Edge(1, 1)], 3: [Edge(2, 4)], 4: [Edge(1, 5)], 5: [Edge(-5, 3)]}

        # act
        result = is_negative_cycle(graph, 1)

        # assert
        self.assertEqual(1, result)
