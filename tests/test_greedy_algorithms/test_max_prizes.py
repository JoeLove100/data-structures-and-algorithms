import unittest
from greedy_algorithms.max_prizes import optimal_summands


class TestMaxPrizes(unittest.TestCase):

    def test_max_prizes_single_prize(self):
        # arrange
        n = 1

        # act
        result = optimal_summands(n)

        # assert
        self.assertSequenceEqual(result, [1])

    def test_max_prizes_triangular_number(self):
        # arrange

        n = 6

        # act
        result = optimal_summands(n)

        # assert
        self.assertSequenceEqual(result, [1, 2, 3])

    def test_max_prizes_non_triangular_number(self):
        # arrange

        n = 14

        # act
        result = optimal_summands(n)

        # assert
        self.assertSequenceEqual(result, [1, 2, 3, 8])
