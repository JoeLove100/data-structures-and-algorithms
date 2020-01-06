import unittest
from algorithmic_toolbox.a_plus_b import sum_of_two_digits


class TestAPlusB(unittest.TestCase):

    def test_a_plus_b_two_positive(self):
        # arrange

        a = 1
        b = 2.5

        # act
        result = sum_of_two_digits(a, b)

        # assert
        self.assertEqual(result, 3.5)

    def test_a_plus_b_one_negative(self):
        # arrange

        a = 8
        b = -2

        # act
        result = sum_of_two_digits(a, b)

        # assert
        self.assertEqual(result, 6)




