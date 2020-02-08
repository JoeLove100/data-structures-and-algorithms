import unittest
from algorithms_101.algorithmic_warm_up import get_nth_fib_sum_modulon_m


class TestSumOfFibonacciNumbers(unittest.TestCase):

    def test_get_nth_fib_sum_modulo_m_multiple(self):
        """
        test where the n+2th value is a multiple of m to
        ensure we handle the modulo correctly
        """

        # arrange

        n = 6
        m = 7

        # act
        result = get_nth_fib_sum_modulon_m(n, m)

        # assert
        self.assertEqual(result, 6)

    def test_get_nth_fib_sum_modulo_m(self):
        # arrange

        n = 100
        m = 10

        # act
        result = get_nth_fib_sum_modulon_m(n, m)

        # assert
        self.assertEqual(result, 5)
