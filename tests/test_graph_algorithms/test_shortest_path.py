import unittest
from graph_algorithms.breadth_first_search.shortest_path import get_shortest_path


class TestGetShortestPath(unittest.TestCase):

    def test_get_shortest_path_target_is_initial(self):
        # arrange
        graph = {1: [2], 2: [3], 3: [4], 4: []}

        # act
        result = get_shortest_path(graph, 2, 2)

        # assert
        self.assertEqual(0, result)

    def test_get_shortest_path_no_path(self):
        # arrange
        graph = {1: [2], 2: [3, 1], 3: [4], 4: []}

        # act
        result = get_shortest_path(graph, 4, 1)

        # assert
        self.assertEqual(-1, result)

    def test_get_shortest_path_with_cycle(self):
        # arrange
        graph = {1: [2, 3, 4], 2: [1, 3], 3: [1, 2], 4: [1]}

        # act
        result = get_shortest_path(graph, 2, 4)

        # assert
        self.assertEqual(2, result)

    def test_get_shortest_path_circle(self):
        # arrange
        graph = {1: [5, 2], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 1]}

        # act
        result = get_shortest_path(graph, 3, 1)

        # assert
        self.assertEqual(2, result)

    def test_get_shortest_path_multiple_sections(self):
        # arrange
        graph = {1: [3, 4], 2: [5], 3: [4, 1], 4: [1, 3], 5: [2]}

        # act
        result = get_shortest_path(graph, 1, 2)

        # assert
        self.assertEqual(-1, result)
