import unittest
import random
from algorithms_101.algorithmic_toolbox.max_pairwise_product import get_max_pairwise_product


class TestMaxPairwiseProduct(unittest.TestCase):

    def test_max_pairwise_product_small_example(self):
        # arrange

        test_numbers = [1, 4, 20, 3, 5, 9]

        # act
        result = get_max_pairwise_product(test_numbers)

        # assert
        self.assertEqual(result, 180)

    def test_max_pairwise_product_multiple_max(self):
        # arrange

        test_numbers = [1, 2, 3, 7, 7, 6]

        # act
        result = get_max_pairwise_product(test_numbers)

        # assert
        self.assertEqual(result, 49)

    def test_max_pairwise_product_large_numbers(self):
        # arrange

        test_numbers = [1, 2, int(10e11), 3, int(pow(2, 7))]

        # act
        result = get_max_pairwise_product(test_numbers)

        # assert
        self.assertEqual(result, 128000000000000)

    def test_max_pairwise_product_large_list(self):
        # arrange

        random.seed(1234)
        test_numbers = list(range(int(pow(2, 16))))
        random.shuffle(test_numbers)

        # act
        result = get_max_pairwise_product(test_numbers)

        # assert
        self.assertEqual(result, 4294770690)
