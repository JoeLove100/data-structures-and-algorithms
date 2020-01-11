import unittest
from algorithmic_warm_up.sum_of_fibonacci_squares import get_last_digit_of_fib_sum_squares


class TestSumOfFibonacciSquares(unittest.TestCase):

    def test_get_last_digit_of_fib_sum_squares_small(self):
        # arrange

        n = 7

        # act
        result = get_last_digit_of_fib_sum_squares(n)

        # assert
        self.assertEqual(result, 3)

    def test_get_last_digit_of_fib_sum_squares_medium(self):
        # arrange

        n = 73

        # act
        result = get_last_digit_of_fib_sum_squares(n)

        # assert
        self.assertEqual(result, 1)

    def test_get_last_digit_of_fib_sum_squares_large(self):
        # arrange

        n = 1234567890

        # act
        result = get_last_digit_of_fib_sum_squares(n)

        # assert
        self.assertEqual(result, 0)
