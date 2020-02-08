import unittest
from algorithms_101.greedy_algorithms.max_product_of_pairs import get_max_product_of_pairs


class TestMaxProductOfPairs(unittest.TestCase):

    def test_max_product_of_pairs_single_sequence(self):
        # arrange

        a = [10]
        b = [30]

        # act
        result = get_max_product_of_pairs(a, b)

        # assert
        self.assertEqual(result, 300)

    def test_max_product_of_pairs(self):
        # arrange

        a = [1, 3, -5]
        b = [-2, 4, 1]

        # act
        result = get_max_product_of_pairs(a, b)

        # assert
        self.assertEqual(result, 23)
