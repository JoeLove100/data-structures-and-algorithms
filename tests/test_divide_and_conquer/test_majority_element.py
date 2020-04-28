import unittest
from divide_and_conquer.majority_element import get_majority_element, _get_element_orders


class TestMajorityElement(unittest.TestCase):

    def test_get_element_orders_no_greater_than(self):
        # arrange

        arr = [1, 3, 7, 5, 6, 99]
        key = 99

        # act
        result = _get_element_orders(arr, key)

        # assert
        self.assertSequenceEqual(([1, 3, 7, 5, 6], [], 1), result)

    def test_get_element_orders_no_less_than(self):
        # arrange

        arr = [1, 3, 7, 5, 6, 99]
        key = 1

        # act
        result = _get_element_orders(arr, key)

        # assert
        self.assertSequenceEqual(([], [3, 7, 5, 6, 99], 1), result)

    def test_get_element_orders_multiple_of_key(self):
        # arrange

        arr = [4, 10, 2, 9, 4, 5, 7, 8, 4]
        key = 4

        # act
        result = _get_element_orders(arr, key)

        # assert
        self.assertSequenceEqual(([2], [10, 9, 5, 7, 8], 3), result)

    def test_get_majority_element_no_majority(self):
        # arrange
        arr = [2, 3, 2, 4, 2, 1, 7, 9, 2]

        # act
        result = get_majority_element(arr)

        # assert
        self.assertEqual(-1, result)

    def test_get_majority_element_majority_exists(self):
        # arrange
        arr = [3, 2, 2, 4, 2, 1, 2, 9, 2]

        # act
        result = get_majority_element(arr)

        # assert
        self.assertEqual(2, result)
