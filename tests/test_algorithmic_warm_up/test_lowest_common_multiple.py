import unittest
from algorithmic_warm_up.lowest_common_multiplier import get_lcm


class TestLowestCommonMultiple(unittest.TestCase):

    def test_get_lcm_same_number(self):

        # arrange
        n_1 = 100
        n_2 = 100

        # act
        result = get_lcm(n_1, n_2)

        # assert
        self.assertEqual(result, 100)

    def test_get_lcm_small_numbers(self):

        # arrange

        n_1 = 8
        n_2 = 6

        # act
        result = get_lcm(n_1, n_2)

        # assert
        self.assertEqual(result, 24)

    def test_get_lcm_large_numbers(self):

        # arrange

        n_1 = 761457
        n_2 = 614573

        # act
        result = get_lcm(n_1, n_2)

        # assert
        self.assertEqual(result, 467970912861)

