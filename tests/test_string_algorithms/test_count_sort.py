import unittest
from string_algorithms.suffix_array.count_sort import get_sorted_text


class TestCountSort(unittest.TestCase):

    def test_get_sorted_text_one_letter(self):
        # arrange
        text = "aaaa"

        # act
        result = get_sorted_text(text)

        # assert
        self.assertSequenceEqual([0, 1, 2, 3], result)

    def test_get_sorted_text_no_repeated_letters(self):
        # arrange
        text = "agbec"

        # assert
        result = get_sorted_text(text)

        # assert
        self.assertSequenceEqual([0, 4, 1, 3, 2], result)

    def test_get_sorted_text(self):
        # arrange
        text = "abcaabcdb"

        # assert
        result = get_sorted_text(text)

        # assert
        self.assertSequenceEqual([0, 3, 6, 1, 2, 4, 7, 8, 5], result)
