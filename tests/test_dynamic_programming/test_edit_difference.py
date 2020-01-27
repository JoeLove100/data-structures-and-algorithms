import unittest
from dynamic_programming.edit_difference import get_min_edit_difference


class TestEditDifference(unittest.TestCase):

    def test_edit_difference_same_word(self):
        # arrange
        s_1 = "ab"
        s_2 = "ab"

        # act
        result = get_min_edit_difference(s_1, s_2)

        # assert
        self.assertEqual(0, result)

    def test_edit_difference_needs_deletions(self):
        # arrange
        s_1 = "abc"
        s_2 = "a"

        # act
        result = get_min_edit_difference(s_1, s_2)

        # assert
        self.assertEqual(2, result)

    def test_edit_difference_needs_insertions(self):
        # arrange
        s_1 = "a"
        s_2 = "abc"

        # act
        result = get_min_edit_difference(s_1, s_2)

        # assert
        self.assertEqual(2, result)

    def test_edit_difference_needs_substitutions(self):
        # arrange
        s_1 = "abc"
        s_2 = "ade"

        # act
        result = get_min_edit_difference(s_1, s_2)

        # assert
        self.assertEqual(2, result)

    def test_edit_difference_needs_all_three(self):
        # arrange
        s_1 = "distance"
        s_2 = "editing"

        # act
        result = get_min_edit_difference(s_1, s_2)

        # assert
        self.assertEqual(5, result)
