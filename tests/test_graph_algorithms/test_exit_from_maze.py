import unittest
from graph_algorithms.graph_basics.exit_from_maze import DisjointSets


class TestExitFromMaze(unittest.TestCase):

    @staticmethod
    def get_disjoint_sets_for_unions() -> DisjointSets:

        ds = DisjointSets()
        ds._parents = {5: 5, 1: 1, 13: 13, 3: 3, 6: 5, 7: 5, 10: 1, 12: 1, 8: 3, 9: 8}
        ds._ranks = {5: 1, 1: 1, 13: 0, 3: 2}
        return ds


    def test_disjoint_sets_make_set(self):
        # arrange
        ds = DisjointSets()

        # act
        ds.make_set(10)

        # assert
        self.assertDictEqual({10: 10}, ds._parents)
        self.assertDictEqual({10: 0}, ds._ranks)

    def test_disjoint_sets_find_no_recursion(self):
        # arrange
        ds = DisjointSets()
        ds._parents = {10: 10, 2: 2}

        # act
        result = ds.find(10)

        # assert
        self.assertEqual(10, result)

    def test_disjoint_sets_find_needs_recursion(self):
        # arrange
        ds = DisjointSets()
        ds._parents = {10: 3, 3: 6, 6: 8, 8: 8, 9: 4, 18: 1}

        # act
        result = ds.find(10)

        # assert
        self.assertEqual(8, result)

    def test_disjoint_sets_union_same_rank(self):
        # arrange
        ds = self.get_disjoint_sets_for_unions()

        # act
        ds.union(5, 1)

        # arrange
        self.assertEqual(ds._parents[5], 1)
        self.assertEqual(ds._parents[1], 1)
        self.assertEqual(ds._ranks[1], 2)

    def test_disjoint_sets_different_rank(self):
        # arrange
        ds = self.get_disjoint_sets_for_unions()

        # act
        ds.union(13, 3)

        # assert
        self.assertEqual(ds._parents[13], 3)
        self.assertEqual(ds._parents[3], 3)
        self.assertEqual(ds._ranks[3], 2)

    def test_disjoint_sets_reach_in_same_set(self):
        # arrange
        ds = self.get_disjoint_sets_for_unions()

        # act
        result = ds.reach(3, 9)

        # assert
        self.assertTrue(result)

    def test_disjoint_sets_reach_in_different_set(self):
        # arrange
        ds = self.get_disjoint_sets_for_unions()

        # act
        result = ds.reach(3, 10)

        # assert
        self.assertFalse(result)



