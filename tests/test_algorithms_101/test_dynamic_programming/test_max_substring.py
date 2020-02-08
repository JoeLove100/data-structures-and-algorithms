import unittest
from algorithms_101.dynamic_programming import get_max_substring_length


class TestMaxSubstring(unittest.TestCase):

    def test_max_substring_no_common_elements(self):
        # arrange
        list_a = [1, 2, 3]
        list_b = [4, 5, 6]

        # act
        result = get_max_substring_length(list_a, list_b)

        # assert
        self.assertEqual(0, result)

    def test_max_substring_a_subset_b(self):
        # arrange

        list_a = [5, 3, 4]
        list_b = [1, 2, 5, 3, 4, 1000]

        # act
        result = get_max_substring_length(list_a, list_b)

        # assert
        self.assertEqual(3, result)

    def test_max_substring_multiple_max(self):
        # arrange

        list_a = [2, 7, 8, 3]
        list_b = [5, 2, 8, 7, 1]

        # act
        result = get_max_substring_length(list_a, list_b)

        # assert
        self.assertEqual(2, result)

    def test_max_substring_different_lengths(self):
        # arrange
        list_a = [2, 3, 9]
        list_b = [2, 9, 7, 8]

        # act
        result = get_max_substring_length(list_a, list_b)

        # assert
        self.assertEqual(2, result)




