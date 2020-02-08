import unittest
from algorithms_101.algorithmic_warm_up.pisanto_periods import get_pisanto_period_sequence
from algorithms_101.algorithmic_warm_up.pisanto_periods import get_nth_fib_modulo_m


class TestPisantoPeriods(unittest.TestCase):

    def test_get_pisanto_sequence(self):
        # arrange

        m = 7

        # act
        result = get_pisanto_period_sequence(m)

        # assert
        expected_result = [0, 1, 1, 2, 3, 5, 1, 6, 0, 6, 6, 5, 4, 2, 6, 1]
        self.assertSequenceEqual(result, expected_result)

    def test_get_nth_fib_modulo_m_small_numbers(self):
        # arrange

        n = 239
        m = 1000

        # act
        result = get_nth_fib_modulo_m(n, m)

        # assert
        self.assertEqual(result, 161)

    def test_get_nth_fib_module_m_large_numbers(self):
        # arrange

        n = 2816213588
        m = 239

        # act
        result = get_nth_fib_modulo_m(n, m)

        # assert
        self.assertEqual(result, 151)
