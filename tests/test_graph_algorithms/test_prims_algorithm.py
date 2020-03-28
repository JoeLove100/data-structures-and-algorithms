import unittest
import math
from graph_algorithms.spanning_trees.prims_algorithm import get_distance, get_min_spanning_tree_length


class TestPrimsAlgorithm(unittest.TestCase):

    def test_get_distance(self):
        # arrange
        coord_1 = (-1, 0)
        coord_2 = (1, 2)

        # act
        result = get_distance(coord_1, coord_2)

        # assert
        self.assertEqual(math.sqrt(8), result)

    def test_get_min_spanning_tree_in_straight_line(self):
        # arrange
        all_coords = {(1, 1), (2, 1), (4, 1), (-3, 1)}

        # act
        result = get_min_spanning_tree_length(all_coords, (1, 1))

        # assert
        self.assertEqual(7, result)

    def test_get_min_spanning_tree_in_square(self):
        # arrange
        all_coords = {(0, 0), (0, 1), (1, 0), (1, 1)}

        # act
        result = get_min_spanning_tree_length(all_coords, (0, 0))

        # assert
        self.assertEqual(3, result)

    def test_get_min_spanning_tree(self):
        # arrange
        all_coords = {(0, 0), (0, 2), (1, 1), (3, 0), (3, 2)}

        # act
        result = get_min_spanning_tree_length(all_coords, (0, 0))

        # assert
        expected_result = 2 + 2 * math.sqrt(2) + math.sqrt(5)
        self.assertEqual(expected_result, result)

