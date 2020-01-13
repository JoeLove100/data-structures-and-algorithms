import unittest
from greedy_algorithms.collecting_signatures import get_optimal_points, Segment


class TestCollectingSignatures(unittest.TestCase):

    def test_get_optimal_one_point(self):
        # arrange
        segments = [Segment(1, 3), Segment(2, 5), Segment(3, 6)]

        # act
        result = get_optimal_points(segments)

        # assert
        self.assertSequenceEqual(result, [3])

    def test_get_optimal_multiple_points(self):
        # arrange
        segments = [Segment(4, 7), Segment(1, 3), Segment(2, 5), Segment(5, 6)]

        # act
        result = get_optimal_points(segments)

        # assert
        self.assertSequenceEqual(result, [3, 6])



