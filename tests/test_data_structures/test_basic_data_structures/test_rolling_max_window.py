import unittest
from data_structures.basic_data_structures.rolling_max_window import max_in_sliding_window


class TestRollingMaxWindow(unittest.TestCase):

    def test_max_in_sliding_window_one_window(self):
        # arrange

        sequence = [1, 2, 3, 4, 5, 3]
        window_size = 10

        # act
        result = max_in_sliding_window(sequence, window_size)

        # assert
        self.assertSequenceEqual([5], result)

    def test_max_in_sliding_window_multiple_windows(self):
        # arrange

        sequence = [1, 2, 3, 4, 5, 3]
        window_size = 3

        # act
        result = max_in_sliding_window(sequence, window_size)

        # assert
        self.assertSequenceEqual([3, 4, 5, 5], result)

    def test_max_in_sliding_window_window_size_one(self):
        # arrange

        sequence = [5, 10, 1, 3, 65, 2]
        window_size = 1

        # act
        result = max_in_sliding_window(sequence, window_size)

        # assert
        self.assertSequenceEqual([5, 10, 1, 3, 65, 2], result)

    def test_max_in_sliding_window_descending_order(self):
        # arrange

        sequence = [100, 96, 75, 32, 32, 15, 8, 2, 1]
        window_size = 3

        # act
        result = max_in_sliding_window(sequence, window_size)

        # assert
        self.assertSequenceEqual([100, 96, 75, 32, 32, 15, 8], result)

    def test_max_in_sliding_window(self):
        # arrange

        sequence = [1, 7, 8, 4, 10, 10, 6, 1, 2, 0]
        window_size = 3

        # act
        result = max_in_sliding_window(sequence, window_size)

        # assert
        self.assertSequenceEqual([8, 8, 10, 10, 10, 10, 6, 2], result)
