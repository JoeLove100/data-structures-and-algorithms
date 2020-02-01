import unittest
from data_structures.basic_data_structures.unmatchted_brackets import _are_matching, find_mismatch


class TestUnmatchedBrackets(unittest.TestCase):

    def test_are_matching_matched_pair(self):
        # arrange

        left = "["
        right = "]"

        # act
        result = _are_matching(left, right)

        # assert
        self.assertTrue(result)

    def test_are_matching_wrong_order(self):
        # arrange

        left = "]"
        right = "["

        # act
        result = _are_matching(left, right)

        # assert
        self.assertFalse(result)

    def test_are_matching_wrong_type(self):
        # arrange

        left = "["
        right = "}"

        # act
        result = _are_matching(left, right)

        # assert
        self.assertFalse(result)

    def test_are_matching_not_bracket(self):
        # arrange

        left = "a"
        right = "]"

        # act
        result = _are_matching(left, right)

        # assert
        self.assertFalse(result)

    def test_find_mismatch_single_open_bracket(self):
        # arrange

        text = "["

        # act
        result = find_mismatch(text, "")

        # assert
        self.assertEqual("1", result)

    def test_find_mismatch_single_closed_bracket(self):
        # arrange

        text = "}"

        # act
        result = find_mismatch(text, "")

        # assert
        self.assertEqual("1", result)

    def test_find_mismatch_wrong_bracket_type(self):
        # arrange

        text = "{([])]"

        # act
        result = find_mismatch(text, "")

        # assert
        self.assertEqual("6", result)

    def test_find_mismatch_contains_other_characters(self):
        # arrange

        test = "(abcd[ef]ghijk))lmno"

        # act
        result = find_mismatch(test, "")

        # assert
        self.assertEqual("16", result)

    def test_find_mismatch_all_match(self):
        # arrange

        text = "(ab)cd{e([]f)ghij}k{l}[m]((n))"

        # act
        result = find_mismatch(text, "test")

        # assert
        self.assertEqual("test", result)
