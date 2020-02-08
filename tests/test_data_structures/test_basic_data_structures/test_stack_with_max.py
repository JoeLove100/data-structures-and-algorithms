import unittest
from data_structures.basic_data_structures.stack_with_max import StackWithMax


class TestStackWithMax(unittest.TestCase):

    def test_stack_with_max_single_element(self):
        # arrange

        stack_with_max = StackWithMax()

        # act
        stack_with_max.push(10)
        result = stack_with_max.max()

        # assert
        self.assertEqual(10, result)

    def test_stack_with_max_push_multiple(self):
        # arrange

        stack_with_max = StackWithMax()

        # act
        for i in [1, 102, 10, -9, 5, 102, 3, -3000]:
            stack_with_max.push(i)
        result = stack_with_max.max()

        # assert
        self.assertEqual(102, result)

    def test_stack_with_max_pop_occurrence_of_max(self):
        # arrange

        stack_with_max = StackWithMax()

        # act
        for i in [1, 102, 10, -9, 5, 102, 3, -3000]:
            stack_with_max.push(i)
        for _ in range(3):
            stack_with_max.pop()

        result = stack_with_max.max()

        # assert
        self.assertEqual(102, result)

    def test_stack_with_max_pop_max(self):
        # arrange

        stack_with_max = StackWithMax()

        # act
        for i in [20, 3, 5, 6, 8, 90, -2]:
            stack_with_max.push(i)
        for _ in range(2):
            stack_with_max.pop()

        result = stack_with_max.max()

        # assert
        self.assertEqual(20, result)
