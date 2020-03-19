import unittest
from graph_algorithms.graph_basics.connected_components import DisjointSets


class TestConnectedComponents(unittest.TestCase):

    def test_number_of_connected_components(self):
        # arrange

        ds = DisjointSets()
        for i in range(1, 5):
            ds.make_set(i)

        # act
        ds.union(1, 2)
        ds.union(3, 2)
        result = ds.number_of_connected_components()

        # assert
        self.assertEqual(2, result)

