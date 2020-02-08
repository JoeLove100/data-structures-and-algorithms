import unittest
from data_structures.basic_data_structures.tree_height import compute_height


class TestTreeHeight(unittest.TestCase):

    def test_get_height_root_only(self):
        # arrange

        parents = [-1]

        # act
        result = compute_height(len(parents), parents)

        # assert
        self.assertEqual(1, result)

    def test_get_height_height_two(self):
        # arrange

        parents = [1, -1, 1]

        # act
        result = compute_height(len(parents), parents)

        # assert
        self.assertEqual(2, result)

    def test_get_height_height_three(self):
        # arrange

        parents = [4, -1, 4, 1, 1]

        # act
        result = compute_height(len(parents), parents)

        # assert
        self.assertEqual(3, result)

    def test_get_height_unbalanced_tree(self):
        # arrange

        parents = [-1, 0, 4, 0, 3]

        # act
        result = compute_height(len(parents), parents)

        # assert
        self.assertEqual(4, result)
