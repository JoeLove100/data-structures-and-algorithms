import unittest
from greedy_algorithms.max_salary import _concat_compare, get_max_salary


class TestMaxSalary(unittest.TestCase):

    def test_is_less_than_equal(self):
        # arrange
        a = "567"
        b = "567"

        # act
        result = _concat_compare(a, b)

        # assert
        self.assertEqual(result, 0)

    def test_is_less_than_b_smaller(self):
        # arrange
        a = "890"
        b = "889"

        # act
        result = _concat_compare(a, b)

        # assert
        self.assertEqual(result, -1)

    def test_is_less_than_a_smaller(self):
        # arrange

        a = "890"
        b = "891"

        # act
        result = _concat_compare(a, b)

        # assert
        self.assertEqual(result, 1)

    def test_is_less_than_one_v_two_digt(self):
        # arrange

        a = "3"
        b = "23"

        # assert
        result = _concat_compare(a, b)

        # act
        self.assertEqual(result, -1)

    def test_is_less_than_one_v_three_digits(self):
        # arrange

        a = "3"
        b = "299"

        # assert
        result = _concat_compare(a, b)

        # act
        self.assertEqual(result, -1)

    def test_is_less_than_same_first_digit_different_length(self):
        # arrange
        a = "32"
        b = "3"

        # act
        result = _concat_compare(a, b)

        # assert
        self.assertEqual(result, 1)

    def test_is_less_than_same_first_two_digts_different_length(self):
        # arrange
        a = "26"
        b = "263"

        # act
        result = _concat_compare(a, b)

        # assert
        self.assertEqual(result, 1)

    def test_get_max_salary_one_digit(self):
        # arrange
        figures = [1, 4, 5, 6, 3, 7]

        # act
        result = get_max_salary(figures)

        # assert
        self.assertEqual(result, 765431)

    def test_get_max_salary_same_first_digit(self):
        # arrange
        figures = [3, 32, 332]

        # act
        result = get_max_salary(figures)

        # assert
        self.assertEqual(result, 333232)
