import unittest
from string_algorithms.burrows_wheeler.burrows_wheeler_transform import get_bw_transform


class TestBurrowsWheelerTransform(unittest.TestCase):

    def test_get_bw_transform_one_letter(self):
        # arrange
        text = "AA$"

        # act
        result = get_bw_transform(text)

        # assert
        self.assertEqual("AA$", result)

    def test_get_bw_transform_repeated_phase(self):
        # arrange
        text = "ACACACAC$"

        # act
        result = get_bw_transform(text)

        # assert
        self.assertEqual("CCCC$AAAA", result)

    def test_get_bw_transform(self):
        # arrange
        text = "AGACATA$"

        # act
        result = get_bw_transform(text)

        # assert
        self.assertEqual("ATG$CAAA", result)
