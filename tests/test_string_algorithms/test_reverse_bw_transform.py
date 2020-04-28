import unittest
from string_algorithms.burrows_wheeler.reverse_bw_transform import get_start_positions, build_first_last_mapping, \
    reverse_bw_transform


class TestReverseBwTransform(unittest.TestCase):

    def test_get_start_positions(self):
        # arrange
        text = "$GAGACACA"

        # act
        result = get_start_positions(text)

        # assert
        expected_result = {"$": 0, "A": 1, "C": 5, "G": 7}
        self.assertDictEqual(expected_result, result)

    def test_build_first_last_mapping(self):
        # arrange
        text = "AGGGAA$"

        # act
        result = build_first_last_mapping(text)

        # assert
        expected_result = {0: 1, 1: 4, 4: 2, 2: 5, 5: 3, 3: 6, 6: 0}
        self.assertDictEqual(expected_result, result)

    def test_reverse_bw_transform(self):
        # arrange
        text = "AGGGAA$"

        # act
        result = reverse_bw_transform(text)

        # assert
        self.assertEqual("GAGAGA$", result)
