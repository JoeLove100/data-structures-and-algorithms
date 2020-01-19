import unittest
from random import Random
from divide_and_conquer.quick_sort import _partition_three, randomized_quick_sort


class TestQuickSort(unittest.TestCase):

    def test_partition_three_duplicates(self):
        # arrange

        arr = [8, 4, 6, 8, 9, 1, 3, 6, 7, 20, 8]

        # act
        result = _partition_three(arr, 0, 10)

        # assert
        self.assertSequenceEqual((6, 8), result)

    def test_partition_three_no_duplicates(self):
        # arrange

        arr = [5, 8, 1, 3, 4, 7, 7, 7, 9, 10]

        # act
        result = _partition_three(arr, 0, 9)

        # assert
        self.assertSequenceEqual((3, 3), result)

    def test_quick_sort_no_duplicates(self):
        # arrange

        arr = [5, 1, 3, 89, 2, 777, 6, -2, 9]
        rnd = Random(1000)

        # act
        randomized_quick_sort(arr, rnd)

        # assert
        self.assertSequenceEqual([-2, 1, 2, 3, 5, 6, 9, 89, 777], arr)

    def test_quick_sort_duplicates(self):
        # arrange

        arr = [100, 7, 7, 7, 7, 7, 7, 7, 7, 9, 1, 2]
        rnd = Random(1000)

        # act
        randomized_quick_sort(arr, rnd)

        # assert
        self.assertSequenceEqual([1, 2, 7, 7, 7, 7, 7, 7, 7, 7, 9, 100], arr)

    def test_quick_sort_non_consecutive_duplicates(self):
        # arrange

        arr = [4, 5, 6, 7, 3, 7, 7, 7, 8, 10]
        rnd = Random(1000)

        # act
        randomized_quick_sort(arr, rnd)

        # assert
        self.assertSequenceEqual([3, 4, 5, 6, 7, 7, 7, 7, 8, 10], arr)



