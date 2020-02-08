import unittest
from algorithms_101.algorithmic_warm_up.fibonacci_numbers import get_nth_fib_number
from algorithms_101.algorithmic_warm_up import last_digit_of_fib


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

    def test_last_digit_0_or_1(self):
        # arrange

        n_0 = 0
        n_1 = 1

        # act
        result_0 = last_digit_of_fib(n_0)
        result_1 = last_digit_of_fib(n_1)

        # assert
        self.assertEqual(result_0, n_0)
        self.assertEqual(result_1, n_1)

    def test_last_digit_small(self):
        # arrange

        n = 10

        # act
        result = last_digit_of_fib(n)

        # assert
        self.assertEqual(result, 5)

    def test_last_digit_large(self):
        # arrange

        n = 250

        # act
        result = last_digit_of_fib(n)

        # assert
        self.assertEqual(result, 5)

    def test_last_digit_huge(self):
        # arrange

        n = 327305

        # act
        result = last_digit_of_fib(n)

        # assert
        self.assertEqual(result, 5)





