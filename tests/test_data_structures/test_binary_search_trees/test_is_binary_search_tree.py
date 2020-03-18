import unittest
from data_structures.binary_search_trees.is_binary_search_tree import get_min_key, get_max_key, \
    is_binary_search_tree
from data_structures.binary_search_trees.is_binary_search_tree_2 import is_binary_search_tree_with_duplicates


class TestIsBinarySearchTree(unittest.TestCase):

    @staticmethod
    def get_small_tree(is_binary_search: bool):

        if is_binary_search:
            tree = [[2, 1, 2], [1, -1, -1], [3, -1, -1]]
        else:
            tree = [[2, 1, 2], [3, -1, -1], [2, -1, -1]]

        return tree

    @staticmethod
    def get_small_tree_with_dupes(is_binary_search: bool):

        if is_binary_search:
            tree = [[2, 1, 2], [1, -1, -1], [2, -1, -1]]
        else:
            tree = [[2, 1, 2], [2, -1, -1], [3, -1, -1]]

        return tree

    def test_get_min_key_of_leaf(self):
        # arrange

        tree = self.get_small_tree(is_binary_search=True)
        start_index = 2
        pre_computed = [None] * 3

        # act
        result = get_min_key(tree, start_index, pre_computed)

        # assert
        self.assertEqual(3, result)
        self.assertSequenceEqual([None, None, 3], pre_computed)

    def test_get_min_key_pre_computed(self):
        # arrange

        tree = self.get_small_tree(is_binary_search=True)
        start_index = 1
        pre_computed = [None, 1, None]

        # act
        result = get_min_key(tree, start_index, pre_computed)

        # assert
        self.assertEqual(result, 1)

    def test_get_max_key_of_leaf(self):
        # arrange

        tree = self.get_small_tree(is_binary_search=True)
        start_index = 2
        pre_computed = [None] * 3

        # act
        result = get_max_key(tree, start_index, pre_computed)

        # assert
        self.assertEqual(result, 3)

    def test_get_min_key_recursive(self):
        # arrange

        tree = self.get_small_tree(is_binary_search=True)
        start_index = 0
        pre_computed = [None] * 3

        # act
        result = get_min_key(tree, start_index, pre_computed)

        # assert
        self.assertEqual(result, 1)
        self.assertSequenceEqual([1, 1, 3], pre_computed)

    def test_get_max_key_recursive(self):
        # arrange

        tree = self.get_small_tree(is_binary_search=True)
        start_index = 0
        pre_computed = [None] * 3

        # act
        result = get_max_key(tree, start_index, pre_computed)

        # assert
        self.assertEqual(result, 3)
        self.assertSequenceEqual([3, 1, 3], pre_computed)

    def test_is_binary_search_tree_true(self):
        # arrange
        tree = self.get_small_tree(is_binary_search=True)

        # act
        result = is_binary_search_tree(tree)

        # assert
        self.assertTrue(result)

    def test_is_binary_search_tree_false(self):
        # arrange
        tree = self.get_small_tree(is_binary_search=False)

        # act
        result = is_binary_search_tree(tree)

        # assert
        self.assertFalse(result)

    def test_is_binary_search_tree_unbalanced_true(self):
        # arrange
        tree = [[1, -1, 1], [2, -1, 2], [3, -1, 3], [4, -1, 4], [5, -1, -1]]

        # act
        result = is_binary_search_tree(tree)

        # assert
        self.assertTrue(result)

    def test_is_binary_search_tree_unbalanced_false(self):
        # arrange
        tree = [[4, 1, -1], [2, 2, 3], [1, -1, -1], [5, -1, -1]]

        # act
        result = is_binary_search_tree(tree)

        # assert
        self.assertFalse(result)

    def test_is_binary_tree_with_dupes_true(self):
        # arrange
        tree = self.get_small_tree_with_dupes(is_binary_search=True)

        # act
        result = is_binary_search_tree_with_duplicates(tree)

        # assert
        self.assertTrue(result)

    def test_is_binary_tree_with_dupes_false(self):
        # arrange
        tree = self.get_small_tree_with_dupes(is_binary_search=False)

        # act
        result = is_binary_search_tree_with_duplicates(tree)

        # assert
        self.assertFalse(result)

