import unittest
from divide_and_conquer.number_of_inversions import _merge, merge_sort


class TestNumberOfInversions(unittest.TestCase):

    def test_merge_alredy_sorted(self):
        # arrange
        array = [1, 2, 3, 4, 5, 6, 7, 8]
        low = 0
        m = 4
        high = 7

        # act
        result = _merge(array, low, m, high)

        # assert
        self.assertSequenceEqual([1, 2, 3, 4, 5, 6, 7, 8], array)
        self.assertEqual(0, result)

    def test_merge_opposite_way_round(self):
        # arrange
        array = [5, 6, 7, 8, 1, 2, 3, 4]
        low = 0
        m = 4
        high = 8

        # act
        result = _merge(array, low, m, high)

        # assert
        self.assertSequenceEqual([1, 2, 3, 4, 5, 6, 7, 8], array)
        self.assertEqual(16, result)

    def test_merge_mixed_sort(self):

        # arrange
        array = [1, 3, 4, 7, 2, 5, 6, 8]
        low = 0
        m = 4
        high = 7

        # act
        result = _merge(array, low, m, high)

        # assert
        self.assertSequenceEqual([1, 2, 3, 4, 5, 6, 7, 8], array)
        self.assertEqual(5, result)

    def test_merge_part_of_array(self):

        # arrange
        array = [1, 3, 4, 5, 2, 6, 8, 9]
        low = 0
        m = 2
        high = 4

        # act
        result = _merge(array, low, m, high)

        # assert
        self.assertSequenceEqual([1, 3, 4, 5, 2, 6, 8, 9], array)
        self.assertEqual(0, result)

    def test_merge_sort_already_sorted(self):
        # arrange(
        array = [1, 2, 3, 4, 5, 6, 7]

        # act
        result = merge_sort(array)

        # act
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], array)
        self.assertEqual(0, result)

    def test_merge_sort_not_sorted(self):
        # arrange
        array = [2, 3, 9, 2, 9]

        # act
        result = merge_sort(array)

        # act
        self.assertSequenceEqual([2, 2, 3, 9, 9], array)
        self.assertEqual(2, result)

    def test_merge_sort_reverse_sorted(self):
        # arrange
        array = [7, 6, 5, 4, 3, 2, 1]

        # act
        result = merge_sort(array)

        # assert
        self.assertSequenceEqual([1, 2, 3, 4, 5, 6, 7], array)
        self.assertEqual(21, result)


