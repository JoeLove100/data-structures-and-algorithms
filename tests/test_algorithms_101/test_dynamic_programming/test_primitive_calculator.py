import unittest
from algorithms_101.dynamic_programming.primitive_calculator import get_optimal_sequence


class TestPrimitiveCalculator(unittest.TestCase):

    def test_get_optimal_sequence_no_operations(self):
        # arrange
        n = 1

        # act
        result = get_optimal_sequence(n)

        # assert
        self.assertSequenceEqual([1], result)

    def test_get_optimal_sequence_multiple_valid(self):
        # arrange
        n = 2

        # act
        result = get_optimal_sequence(n)

        # assert
        self.assertSequenceEqual([1, 2], result)

    def test_get_optimal_sequence_small_number(self):
        # arrange
        n = 10

        # act
        result = get_optimal_sequence(n)

        # assert
        self.assertSequenceEqual([1, 3, 9, 10], result)

    def test_get_optimal_sequence_larger_number(self):
        # arrange
        n = 96234

        # act
        result = get_optimal_sequence(n)

        # assert
        self.assertSequenceEqual([1, 3, 9, 10, 11, 33, 99, 297, 891, 2673, 8019, 16038, 16039, 48117, 96234],
                                 result)
