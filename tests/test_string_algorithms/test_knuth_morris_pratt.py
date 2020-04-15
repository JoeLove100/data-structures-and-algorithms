import unittest
from string_algorithms.pattern_matching.knuth_morris_pratt import get_all_prefixes, get_pattern_occurrences


class TestKnuthMorrisPratt(unittest.TestCase):

    def test_get_border_lengths_no_prefixes(self):
        # arrange
        text = "GATACA"

        # act
        result = get_all_prefixes(text)

        # assert
        self.assertSequenceEqual([0, 0, 0, 0, 0, 0], result)

    def test_get_border_lengths_prefixes(self):
        # arrange
        text = "abababcaab"

        # act
        result = get_all_prefixes(text)

        # assert
        self.assertSequenceEqual([0, 0, 1, 2, 3, 4, 0, 1, 1, 2], result)

    def test_get_pattern_occurrences_pattern_longer_than_text(self):
        # arrange
        text = "abcd"
        pattern = "ababc"

        # act
        result = get_pattern_occurrences(text, pattern)

        # assert
        self.assertSequenceEqual([], result)

    def test_get_pattern_occurrences_no_occurrences(self):
        # arrange
        text = "abcde"
        pattern = "ac"

        # act
        result = get_pattern_occurrences(text, pattern)

        # assert
        self.assertSequenceEqual([], result)

    def test_get_pattern_occurrences(self):
        # arrange
        pattern = "ATAT"
        text = "GATATATGCATATACTT"

        # act
        result = get_pattern_occurrences(text, pattern)

        # assert
        self.assertSequenceEqual([1, 3, 9], result)
