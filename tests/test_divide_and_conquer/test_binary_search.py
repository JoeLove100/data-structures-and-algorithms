import unittest
from divide_and_conquer.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):

    @staticmethod
    def get_array():
        return [1, 45, 78, 99, 100, 102, 203, 450, 9977]

    def test_binary_search_key_not_found(self):
        # arrange
        arr = self.get_array()
        key = 2

        # act
        result = binary_search(arr, key)

        # assert
        self.assertEqual(-1, result)

    def test_binary_search_key_in_array(self):
        # arrange
        arr = self.get_array()
        key = 450

        # act
        result = binary_search(arr, key)

        # assert
        self.assertEqual(7, result)

    def test_binary_search_too_big(self):
        # arrange
        arr = self.get_array()
        key = 100000

        # act
        result = binary_search(arr, key)

        # assert
        self.assertEqual(-1, result)

    def test_binary_search_too_low(self):
        # arrange
        arr = self.get_array()
        key = -3

        # act
        result = binary_search(arr, key)

        # assert
        self.assertEqual(-1, result)

    def test_binary_search_with_duplicates(self):
        # arrange
        arr = self.get_array()
        arr.insert(2, 78)
        key = 78

        # act
        result = binary_search(arr, key)

        # assert
        self.assertEqual(2, result)
