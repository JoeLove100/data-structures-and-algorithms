import unittest
from dynamic_programming.max_expression import _get_diagonals, get_maximum_value


class TestMaxExpression(unittest.TestCase):

    def test_get_diagonals(self):
        # arrange

        n = 3

        # act
        result = _get_diagonals(n)

        # assert
        expected_result = [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (0, 2)]
        self.assertSequenceEqual(expected_result, result)

    def test_get_maximum_value_single_operation(self):
        # arrange

        data_set = "1+2"

        # act
        result = get_maximum_value(data_set)

        # assert
        self.assertEqual(3, result)

    def test_get_maximum_two_operations(self):
        # arrange

        data_set = "6+5*2"

        # act
        result = get_maximum_value(data_set)

        # assert
        self.assertEqual(22, result)

    def test_get_maximum_several_operations(self):
        # arrange

        data_set = "5-8+7*4-8+9"

        # act
        result = get_maximum_value(data_set)

        # assert
        self.assertEqual(200, result)
