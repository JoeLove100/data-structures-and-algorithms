import unittest
from data_structures.binary_search_trees.tree_traversal import TreeOrders


class TestTreeTraversal(unittest.TestCase):

    @staticmethod
    def _get_basic_tree():
        n = 5
        keys = [4, 2, 5, 1, 3]
        left_children = [1, 3, -1, -1, -1]
        right_children = [2, 4, -1, -1, -1]

        basic_tree = TreeOrders(n=n, keys=keys, left_children=left_children, right_children=right_children)
        return basic_tree

    def test_in_order_traversal(self):
        # arrange

        tree = self._get_basic_tree()

        # act
        result = tree.traverse_in_order()

        # assert
        self.assertSequenceEqual([1, 2, 3, 4, 5], result)

    def test_pre_order_traversal(self):
        # arrange

        tree = self._get_basic_tree()

        # act
        result = tree.traverse_pre_order()

        # assert
        self.assertSequenceEqual([4, 2, 1, 3, 5], result)

    def test_post_order_traversal(self):
        # arrange

        tree = self._get_basic_tree()

        # act
        result = tree.traverse_post_order()

        # assert
        self.assertSequenceEqual([1, 3, 2, 5, 4], result)



