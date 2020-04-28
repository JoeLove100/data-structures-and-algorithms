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

        # act
        result = get_sorted_text(text)

        # assert
        self.assertSequenceEqual([0, 2, 4, 3, 1], result)

    def test_get_sorted_text(self):
        # arrange
        text = "abcaabcdb"

        # act
        result = get_sorted_text(text)

        # assert
        self.assertSequenceEqual([0, 3, 4, 1, 5, 8, 2, 6, 7], result)

