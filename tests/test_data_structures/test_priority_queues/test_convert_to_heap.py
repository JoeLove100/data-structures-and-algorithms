import unittest
from data_structures.prioritiy_queues.convert_to_heap import _right_child, _left_child, _parent, \
    _shift_down, build_heap


class TestConvertToHeap(unittest.TestCase):

    def test_get_left_child(self):
        # arrange

        i = 10

        # act
        result = _left_child(i)

        # assert
        self.assertEqual(20, result)

    def test_get_right_child(self):
        # arrange

        i = 10

        # act
        result = _right_child(i)

        # assert
        self.assertEqual(21, result)

    def test_get_parent(self):
        # arrange

        i = 10

        # act
        result = _parent(i)

        # assert
        self.assertEqual(5, result)

    def test_shift_down_already_in_place(self):
        # arrange

        data = [1, 2, 3, 4, 5, 6]
        swaps = []

        # act
        _shift_down(1, data, swaps)

        # assert
        self.assertSequenceEqual([1, 2, 3, 4, 5, 6], data)  # check data is as expected
        self.assertSequenceEqual([], swaps)  # check swaps are as expected

    def test_shift_down_shift_left(self):
        # arrange

        data = [1, 4, 6, 2, 5, 3]
        swaps = []

        # act
        _shift_down(2, data, swaps)

        # assert
        self.assertSequenceEqual([1, 2, 6, 4, 5, 3], data)
        self.assertSequenceEqual([(1, 3)], swaps)

    def test_shift_down_shift_to_right(self):
        # arrange

        data = [1, 4, 6, 5, 2, 3]
        swaps = []

        # act
        _shift_down(2, data, swaps)

        # assert
        self.assertSequenceEqual([1, 2, 6, 5, 4, 3], data)
        self.assertSequenceEqual([(1, 4)], swaps)

    def test_shift_down_root(self):
        # arrange

        data = [5, 6, 2, 3, 4, 1]
        swaps = []

        # act
        _shift_down(1, data, swaps)

        # assert
        self.assertSequenceEqual([2, 6, 1, 3, 4, 5], data)
        self.assertSequenceEqual([(0, 2), (2, 5)], swaps)

    def test_shift_down_leaf(self):
        # arrange

        data = [5, 6, 2, 3, 4, 1]
        swaps = []

        # act
        _shift_down(5, data, swaps)

        # assert
        self.assertSequenceEqual([5, 6, 2, 3, 4, 1], data)
        self.assertSequenceEqual([], swaps)

    def test_build_heap_in_order(self):
        # arrange

        data = [1, 2, 3, 4, 5]

        # act
        result = build_heap(data)

        # assert
        self.assertSequenceEqual([1, 2, 3, 4, 5], data)
        self.assertSequenceEqual([], result)

    def test_build_heap_out_of_order(self):
        # arrange

        data = [5, 4, 3, 2, 1]

        # act
        result = build_heap(data)

        # assert
        self.assertSequenceEqual([1, 2, 3, 5, 4], data)
        self.assertSequenceEqual([(1, 4), (0, 1), (1, 3)], result)
