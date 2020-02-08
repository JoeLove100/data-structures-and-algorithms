import unittest
from algorithms_101.dynamic_programming import get_change


class TestMoneyChanging(unittest.TestCase):

    def test_money_changing_one_only(self):
        # arrange

        money = 10
        coins = [1]

        # act
        result = get_change(money, coins)

        # assert
        self.assertEqual(10, result)

    def test_money_changing_multiple_of_coin(self):
        # arrange

        money = 25
        coins = [1, 3, 5]

        # act
        result = get_change(money, coins)

        # assert
        self.assertEqual(5, result)

    def test_money_changing_multiple_greedy_fails(self):
        # arrange

        money = 25
        coins = [1, 8, 20]

        # act
        result = get_change(money, coins)

        # assert
        self.assertEqual(4, result)

    def test_money_changing_multiple_coins_required(self):
        # arrange
        money = 34
        coins = [1, 3, 4]

        # act
        result = get_change(money, coins)

        # assert
        self.assertEqual(9, result)
