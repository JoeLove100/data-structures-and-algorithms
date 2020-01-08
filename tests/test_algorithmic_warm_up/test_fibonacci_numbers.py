import unittest
from algorithmic_warm_up.fibonacci_numbers import get_nth_fib_number


class TestFibonacciNumbers(unittest.TestCase):

    def test_get_nth_fib_number_0_or_1(self):
        # arrange

        n_0 = 0
        n_1 = 1

        # act
        result_0 = get_nth_fib_number(n_0)
        result_1 = get_nth_fib_number(n_1)

        # assert
        self.assertEqual(result_0, 0)
        self.assertEqual(result_1, 1)

    def test_get_nth_fib_number_small(self):
        # arrange

        n = 13

        # act
        result = get_nth_fib_number(n)

        # assert
        self.assertEqual(233, result)

    def test_get_nth_fib_number_big(self):
        # arrange

        n = 200

        # act
        result = get_nth_fib_number(n)

        # assert
        self.assertEqual(280571172992510140037611932413038677189525, result)
