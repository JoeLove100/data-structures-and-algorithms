import unittest
from algorithms_101.algorithmic_warm_up.sum_of_fibonacci_numbers_partial import get_partial_fib_sum


class TestFibonacciNumbersPartial(unittest.TestCase):

    def test_get_partial_fib_sum_same_number(self):
        # arrange

        n = 10
        m = 10

        # act

        result = get_partial_fib_sum(m, n, 10)

        # assert
        self.assertEqual(result, 5)

    def test_get_partial_fib_sum_small_numbers(self):
        # arrange

        n = 7
        m = 3

        # act
        result = get_partial_fib_sum(n, m, 10)

        # assert
        self.assertEqual(result, 1)

    def test_get_partial_fib_sum_large_numbers(self):
        # arrange

        n = 200
        m = 10

        # act
        result = get_partial_fib_sum(n, m, 10)

        # assert
        self.assertEqual(result, 2)

