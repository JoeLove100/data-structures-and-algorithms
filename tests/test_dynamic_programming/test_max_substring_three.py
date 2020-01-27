import unittest
from dynamic_programming.max_substring_three import  get_max_sub_sequence_length


class TestMaxSubstringThree(unittest.TestCase):

    def test_max_sub_sequence_three_no_common_elements(self):
        # act

        list_a = [1, 2]
        list_b = [4, 3]
        list_c = [5, 6]

        # act
        result = get_max_sub_sequence_length(list_a, list_b, list_c)

        # assert
        self.assertEqual(0, result)

    def test_max_sub_sequence_three_all_sub_sequences(self):
        # act

        list_a = [1, 2]
        list_b = [4, 1, 3, 2]
        list_c = [7, 4, 1, 0, 3, 2, 10]

        # act
        result = get_max_sub_sequence_length(list_a, list_b, list_c)

        # assert
        self.assertEqual(2, result)

    def test_max_sub_string_three_multiple_of_same_length(self):
        # arrange

        list_a = [8, 3, 2, 1, 7]
        list_b = [8, 2, 1, 3, 8, 10, 7]
        list_c = [6, 8, 3, 1, 4, 7]

        # act
        result = get_max_sub_sequence_length(list_a, list_b, list_c)

        # assert
        self.assertEqual(3, result)
