import unittest
from greedy_algorithms.maximum_loot_value import get_maximal_loot_value


class TestMaximumLootValue(unittest.TestCase):

    def test_get_maximal_loot_value_one_item(self):
        # arrange

        weight = 10
        loot = [(5, 20)]

        # act
        result = get_maximal_loot_value(loot, weight)

        # assert
        self.assertEqual(result, 2.5)

    def test_get_maximal_loot_value_more_space_than_items(self):
        # arrange

        weight = 10
        loot = [(3, 1), (2, 6)]

        # act
        result = get_maximal_loot_value(loot, weight)

        # assert
        self.assertEqual(result, 5)

    def test_get_maximal_loot_value(self):
        # arrange

        weight = 50
        loot = [(60, 20), (100, 50), (120, 30)]

        # act
        result = get_maximal_loot_value(loot, weight)

        # assert
        self.assertEqual(result, 180)
