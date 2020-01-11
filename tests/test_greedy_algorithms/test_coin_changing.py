import unittest
from greedy_algorithms.coin_changing import get_min_number_of_coins


class TestCoinChanging(unittest.TestCase):

    def test_get_min_number_of_coins_multiple_of_max(self):
        # arrange

        n = 80
        coin_vals = [8, 4, 3, 1]

        # act
        result = get_min_number_of_coins(n, coin_vals)

        # assert
        self.assertEqual(result, 8)

    def test_get_min_number_of_coins_ones_only(self):
        # arrange

        n = 17
        coin_vals = [1]

        # act
        result = get_min_number_of_coins(n,  coin_vals)

        # assert
        self.assertEqual(result, 17)

    def test_get_min_number_of_coins(self):
        # arrange

        n = 28
        coin_vals = [10, 5, 1]

        # act
        result = get_min_number_of_coins(n, coin_vals)

        # assert
        self.assertEqual(result, 6)

    def test_get_min_number_of_coins_unsorted(self):
        # arrange

        n = 8
        coin_vals = [1, 10, 5]

        # act
        result = get_min_number_of_coins(n, coin_vals)

        # assert
        self.assertEqual(result, 4)
