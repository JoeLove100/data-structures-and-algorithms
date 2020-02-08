import unittest
from data_structures.basic_data_structures.network_packets_sim import process_requests, Buffer, Request, Response


class TestNetworkPacketsSim(unittest.TestCase):

    def test_process_requests_no_packets(self):
        # arrange

        requests = []
        buffer = Buffer(size=1)

        # act
        result = process_requests(requests, buffer)

        # assert
        self.assertSequenceEqual([], result)

    def test_process_requests_one_request(self):
        # arrange

        requests = [Request(1, 10)]
        buffer = Buffer(size=1)

        # act
        result = process_requests(requests, buffer)

        # assert
        expected_result = [Response(False, 1)]
        self.assertSequenceEqual(expected_result, result)

    def test_process_requests_drop_last_request(self):
        # arrange

        requests = [Request(2, 10), Request(5, 10), Request(9, 5)]
        buffer = Buffer(size=2)

        # act
        result = process_requests(requests, buffer)

        # assert
        expected_result = [Response(False, 2), Response(False, 12), Response(True, -1)]
        self.assertSequenceEqual(expected_result, result)

    def test_process_requests_drop_second_last_request(self):
        # arrange

        requests = [Request(2, 10), Request(5, 10), Request(8, 5), Request(13, 1)]
        buffer = Buffer(size=2)

        # act
        result = process_requests(requests, buffer)

        # assert
        expected_result = [Response(False, 2), Response(False, 12), Response(True, -1), Response(False, 22)]
        self.assertSequenceEqual(expected_result, result)

    def test_process_requests_multiple_at_same_time(self):
        # arrange

        requests = [Request(8, 4), Request(11, 3), Request(11, 4), Request(11, 5)]
        buffer = Buffer(size=3)

        # act
        result = process_requests(requests, buffer)

        # assert
        expected_result = [Response(False, 8), Response(False, 12), Response(False, 15), Response(True, -1)]
        self.assertSequenceEqual(expected_result, result)

    def test_process_requests_zero_processing_time(self):
        # arrange

        requests = [Request(2, 0), Request(2, 0), Request(2, 2), Request(2, 3)]
        buffer = Buffer(size=1)

        # act
        result = process_requests(requests, buffer)

        # assert
        expected_result = [Response(False, 2), Response(False, 2), Response(False, 2), Response(True, -1)]
        self.assertSequenceEqual(expected_result, result)

