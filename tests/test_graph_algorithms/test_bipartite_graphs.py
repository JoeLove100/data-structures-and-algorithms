import unittest
from graph_algorithms.breadth_first_search.bipartite_graph import is_bipartite


class TestBipartiteGraph(unittest.TestCase):

    def test_single_node_is_bipartite(self):
        # arrange
        graph = {1: []}

        # act
        result = is_bipartite(graph, 1)

        # assert
        self.assertEqual(1, result)

    def test_linear_graph_is_bipartite(self):
        # arrange
        graph = {1: [2], 2: [3], 3: [4], 4: [5], 5: []}

        # act
        result = is_bipartite(graph, 1)

        # assert
        self.assertEqual(1, result)

    def test_triangle_graph_is_not_bipartite(self):
        # arrange
        graph = {1: [2], 2: [3], 3: [1]}

        # assert
        result = is_bipartite(graph, 1)

        # assert
        self.assertEqual(0, result)

    def test_graph_with_self_loop_not_bipartite(self):
        # arrange
        graph = {1: [2], 2: [3], 3: [4], 4: [5], 5: [5]}

        # act
        result = is_bipartite(graph, 1)

        # assert
        self.assertEqual(0, result)

