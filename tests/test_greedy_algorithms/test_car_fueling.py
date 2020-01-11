import unittest
from greedy_algorithms.car_fueling import compute_min_refills


class TestCarFueling(unittest.TestCase):

    def test_compute_min_refills_not_possible(self):
        # arrange

        total_distance = 10
        stops = [1, 2, 4, 9]
        car_distance = 3

        # act
        result = compute_min_refills(total_distance, car_distance, stops)

        # assert
        self.assertEqual(result, -1)

    def test_compute_min_refills_no_refills(self):
        # arrange

        total_distance = 5
        stops = [1, 2, 3]
        car_distance = 6

        # act
        result = compute_min_refills(total_distance, car_distance, stops)

        # assert
        self.assertEqual(result, 0)

    def test_compute_min_refills_equally_spaced(self):
        # arrange

        total_distance = 10
        stops = [3, 6, 9]
        car_distance = 3

        # act
        result = compute_min_refills(total_distance, car_distance, stops)

        # assert
        self.assertEqual(result, 3)

    def test_compute_min_refills_not_required_stops(self):
        # arrange

        total_distance = 15
        stops = [1, 5, 7, 10, 12]
        car_distance = 5

        # act
        result = compute_min_refills(total_distance, car_distance, stops)

        # assert
        self.assertEqual(result, 2)

    def test_compute_min_refills_too_far_to_first(self):
        # arrange

        total_distance = 10
        stops = [5, 6, 7, 8]
        car_distance = 2

        # act
        result = compute_min_refills(total_distance, car_distance, stops)

        # assert
        self.assertEqual(result, -1)

    def test_compute_min_refills_too_far_to_end(self):
        # arrange

        total_distance = 10
        stops = [1, 3, 5, 7]
        car_distance = 2

        # act
        result = compute_min_refills(total_distance, car_distance, stops)

        # assert
        self.assertEqual(result, -1)



