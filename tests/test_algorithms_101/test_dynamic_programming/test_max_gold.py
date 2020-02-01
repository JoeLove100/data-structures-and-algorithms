import unittest
from algorithms_101.dynamic_programming.max_gold import get_optimal_weight


class TestMaxGold(unittest.TestCase):

    def test_max_gold_one_bar_too_big(self):
        # arrange

        max_weight = 10
        weights = [11]

        # act
        result = get_optimal_weight(max_weight, weights)

        # assert
        self.assertEqual(0, result)

    def test_max_gold_one_bar_exact_size(self):
        # arrange

        max_weight = 10
        weights = [10]

        # act
        result = get_optimal_weight(max_weight, weights)

        # assert
        self.assertEqual(10, result)

    def test_max_gold_one_bar_smaller_than_max(self):
        # arrange

        max_weight = 10
        weights = [8]

        # act
        result = get_optimal_weight(max_weight, weights)

        # assert
        self.assertEqual(8, result)

    def test_max_gold_greedy_approach_fails(self):
        # arrange

        max_weight = 20
        weights = [15, 5, 16]

        # act
        result = get_optimal_weight(max_weight, weights)

        # assert
        self.assertEqual(20, result)

    def test_max_gold_exact_solution_exists(self):
        # arrange

        max_weights = 9
        weights = [8, 4, 1]

        # act
        result = get_optimal_weight(max_weights, weights)

        # assert
        self.assertEqual(9, result)

    def test_max_gold_multiple_solutions(self):
        # arrange

        max_weight = 12
        weights = [8, 4, 4, 10, 2]

        # act
        result = get_optimal_weight(max_weight, weights)

        # assert
        self.assertEqual(12, result)


