import unittest
from algorithms_101.algorithmic_warm_up import get_gcd


class TestGreatestCommonDivisor(unittest.TestCase):

    def test_get_gcd_same_number(self):
        # arrange

        n = int(10e6)
        m = int(10e6)

        # act
        result = get_gcd(n, m)

        # assert
        self.assertEqual(result, int(10e6))

    def test_get_gcd_multiple(self):
        # arrange

        n = 32
        m = 8

        # act
        result = get_gcd(n, m)

        # assert
        self.assertEqual(result, 8)

    def test_get_gcd_no_common_factors(self):
        # arrange

        n = 101
        m = 49

        # act
        result = get_gcd(n, m)

        # assert
        self.assertEqual(result, 1)

    def test_get_gcd_large(self):
        # arrange

        n = 178732
        m = 83736

        # act
        result = get_gcd(n, m)

        # assert
        self.assertEqual(result, 4)

    def test_get_gcd_larger(self):
        # arrange

        n = 28851538
        m = 1183019

        # act
        result = get_gcd(n, m)

        # assert
        self.assertEqual(result, 17657)
