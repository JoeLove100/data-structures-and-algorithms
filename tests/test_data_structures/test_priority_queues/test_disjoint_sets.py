import unittest
from data_structures.prioritiy_queues.disjoint_sets import Database


class TestDisjointSets(unittest.TestCase):

    def test_merge_with_self(self):
        # arrange

        row_counts = [10, 10, 20]
        db = Database(row_counts)

        # act
        db.merge(0, 0)
        db.merge(1, 1)
        db.merge(2, 2)

        # assert
        self.assertEqual(20, db.max_row_count)

    def test_merge_all(self):
        # arrange

        row_count = [5, 10, 20, 35]
        db = Database(row_count)

        # act
        db.merge(0, 2)
        db.merge(1, 3)
        db.merge(0, 1)

        # assert
        self.assertEqual(70, db.max_row_count)

    def test_handles_repeated_merges(self):
        # arrange

        row_count = [1, 20, 5, 20]
        db = Database(row_count)

        # act
        db.merge(0, 3)
        db.merge(3, 0)
        db.merge(1, 2)
        db.merge(2, 1)

        # assert
        self.assertEqual(25, db.max_row_count)
