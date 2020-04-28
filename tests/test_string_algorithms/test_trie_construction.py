import unittest
from string_algorithms.suffix_trees.trie_construction import Trie, Node


class TestTrieConstruction(unittest.TestCase):

    def test_add_to_trie_root(self):
        # arrange
        trie = Trie(Node(0, None))
        words = ["abcd", "abc"]

        # act
        for w in words:
            trie.add_to_trie(w)

        # assert
        self.assertEqual(5, trie._key_count)

