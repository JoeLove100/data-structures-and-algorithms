import unittest
from string_algorithms.suffix_array.build_suffix_array import get_character_classes, get_order_doubled, \
    get_updated_classes, get_ordered_suffixes


class TestBuildSuffixArray(unittest.TestCase):

    def test_compute_character_classes_no_duplicates(self):
        # arrange
        text = "badc$"

        # act
        result = get_character_classes(text)

        # assert
        self.assertSequenceEqual([2, 1, 4, 3, 0], result)

    def test_compute_character_classes_with_duplicates(self):
        # arrange
        text = "ababaa$"

        # act
        result = get_character_classes(text)

        # assert
        self.assertSequenceEqual([1, 2, 1, 2, 1, 1, 0], result)

    def test_get_order_doubled_length_one(self):
        # arrange
        text = "banana$"
        length = 1
        orders = [6, 1, 3, 5, 0, 2, 4]
        classes = [2, 1, 3, 1, 3, 1, 0]

        # act
        result = get_order_doubled(text, length, orders, classes)

        # assert
        self.assertSequenceEqual([6, 5, 1, 3, 0, 2, 4], result)

    def test_get_order_doubled_length_two(self):
        # arrange
        text = "banana$"
        length = 2
        orders = [6, 5, 1, 3, 0, 2, 4]
        classes = [3, 2, 4, 2, 4, 1, 0]

        # act
        result = get_order_doubled(text, length, orders, classes)

        # assert
        self.assertSequenceEqual([6, 5, 3, 1, 0, 4, 2], result)

    def test_get_updated_classes(self):
        # arrange
        length = 1
        orders = [6, 5, 1, 3, 0, 2, 4]
        classes = [4, 1, 5, 1, 5, 1, 0]

        # act
        result = get_updated_classes(length, orders, classes)

        # assert
        self.assertSequenceEqual([3, 2, 4, 2, 4, 1, 0], result)

    def test_get_ordered_suffixes(self):
        # arrange
        text = "AACGATAGCGGTAGA$"

        # act
        result = get_ordered_suffixes(text)

        # assert
        self.assertSequenceEqual([15, 14, 0, 1, 12, 6, 4, 2, 8, 13, 3, 7, 9, 10, 11, 5], result)

    def test_get_ordered_suffixes_one_letter(self):
        # arrange
        text = "aaa$"

        # act
        result = get_ordered_suffixes(text)

        # assert
        self.assertSequenceEqual([3, 2, 1, 0], result)
