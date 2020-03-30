import unittest
from collections import OrderedDict
from graph_algorithms.shortest_paths.optimal_paths import get_optimal_paths, Edge


class TestGetOptimalPaths(unittest.TestCase):

    def test_all_nodes_unreachable_from_start(self):
        # arrange
        graph = {1: [], 2: [Edge(1, 3)], 3: [Edge(2, 2)]}

        # act
        result = get_optimal_paths(graph, 1)

        # assert
        self.assertDictEqual({1: 0, 2: float("inf"), 3: float("inf")}, result)

    def test_all_nodes_reachable_from_negative_cycle(self):
        # arrange
        graph = {1: [Edge(1, 2)], 2: [Edge(1, 3), Edge(10, 4)], 3: [Edge(-5, 1)], 4: [Edge(10, 5)], 5: []}

        # act
        result = get_optimal_paths(graph, 1)

        # assert
        expected_result = OrderedDict({i: -float("inf") for i in range(1, 6)})
        self.assertDictEqual(expected_result, result)

    def test_no_negative_cycles(self):
        # arrange
        graph = {1: [Edge(3, 3), Edge(1, 4)], 2: [], 3: [Edge(-1, 4)], 4: []}

        # act
        result = get_optimal_paths(graph, 1)

        # assert
        self.assertDictEqual({1: 0, 2: float("inf"), 3: 3, 4: 1}, result)

    def test_mix_of_all_cases(self):
        # arrange
        graph = {1: [Edge(10, 2), Edge(100, 3)], 2: [Edge(5, 3)], 3: [Edge(7, 5)],
                 4: [Edge(-18, 3)], 5: [Edge(10, 4)], 6: [Edge(-1, 1)]}

        # act
        result = get_optimal_paths(graph, 1)

        # assert
        self.assertDictEqual({1: 0, 2: 10, 3: -float("inf"), 4: -float("inf"),
                              5: -float("inf"), 6: float("inf")}, result)

    def test_not_starting_from_1(self):
        # arrange
        graph = {1: [Edge(1, 2)], 2: [Edge(2, 3)], 3: [Edge(-5, 1)], 4: [Edge(2, 1)], 5: []}

        # act
        result = get_optimal_paths(graph, 4)

        # assert
        self.assertDictEqual({1: -float("inf"), 2: -float("inf"), 3: -float("inf"), 4: 0, 5: float("inf")},
                             result)
