import unittest
from unittest.mock import MagicMock, patch, call
from data_structures.hash_functions.chaining import QueryProcessor, Query


class TestChaining(unittest.TestCase):

    def test_adding_to_query_processor(self):
        # arrange

        qp = QueryProcessor(bucket_count=10)
        qp._hash_func = MagicMock(return_value=5)
        q = Query(["add", "test"])

        # act
        qp.process_query(query=q)

        # assert
        self.assertSequenceEqual(qp.elems[5], ["test"])

    def test_adding_multiple_to_query_processor(self):
        # arrange

        qp = QueryProcessor(bucket_count=10)
        qp._hash_func = MagicMock(side_effect=[3, 7, 3])
        queries = [Query(["add", f"test_{i}"]) for i in range(3)]

        # act
        for query in queries:
            qp.process_query(query)

        # assert
        self.assertSequenceEqual(qp.elems[7], ["test_1"])
        self.assertSequenceEqual(qp.elems[3], ["test_2", "test_0"])

    def test_adding_same_to_query_processor(self):
        # arrange

        qp = QueryProcessor(bucket_count=10)
        qp._hash_func = MagicMock(return_value=0)
        q = Query(["add", "test"])

        # act
        qp.process_query(query=q)
        qp.process_query(query=q)

        # assert
        self.assertSequenceEqual(qp.elems[0], ["test"])

    def test_deleting_address_is_none(self):
        # arrange

        qp = QueryProcessor(bucket_count=10)
        qp._hash_func = MagicMock(return_value=2)
        q = Query(["del", "test"])

        # act
        qp.process_query(query=q)

        # assert
        self.assertIsNone(qp.elems[2])

    def test_deleting_not_at_address(self):
        # arrange

        qp = QueryProcessor(bucket_count=10)
        qp._hash_func = MagicMock(return_value=3)
        qp.elems[3] = ["test_1", "test_2", "test_3"]
        q = Query(["del", "test"])

        # act
        qp.process_query(query=q)

        # assert
        self.assertSequenceEqual(qp.elems[3], ["test_1", "test_2", "test_3"])

    def test_deleting_is_at_address(self):
        # arrange

        qp = QueryProcessor(bucket_count=10)
        qp._hash_func = MagicMock(return_value=7)
        qp.elems[7] = ["test_0", "test_1", "test", "test_2"]
        q = Query(["del", "test"])

        # act
        qp.process_query(query=q)

        # assert
        self.assertSequenceEqual(qp.elems[7], ["test_0", "test_1", "test_2"])

    def test_find_is_in_processor(self):
        # arrange

        qp = QueryProcessor(bucket_count=10)
        qp._hash_func = MagicMock(return_value=1)
        qp.elems[1] = ["a", "b", "c", "test", "d"]
        q = Query(["find", "test"])

        # act
        mock_write_found = MagicMock()
        qp.write_search_result = mock_write_found
        qp.process_query(query=q)

        # assert
        mock_write_found.assert_called_with(True)

    def test_find_not_in_processor(self):
        # arrange

        qp = QueryProcessor(bucket_count=10)
        qp._hash_func = MagicMock(return_value=3)
        qp.elems[3] = ["a", "b", "c", "d"]
        q = Query(["find", "test"])

        # act
        mock_write_found = MagicMock()
        qp.write_search_result = mock_write_found
        qp.process_query(query=q)

        # assert
        mock_write_found.assert_called_with(False)

    def test_find_address_is_none(self):
        # arrange

        qp = QueryProcessor(bucket_count=10)
        qp._hash_func = MagicMock(return_value=9)
        q = Query(["find", "test"])

        # act
        mock_write_found = MagicMock()
        qp.write_search_result = mock_write_found
        qp.process_query(query=q)

        # assert
        mock_write_found.assert_called_with(False)

    @patch("builtins.print")
    def test_check_nothing_at_address(self, mock_print):
        # arrange

        qp = QueryProcessor(bucket_count=10)
        qp.elems[5] = []
        queries = [Query(["check", "2"]), Query(["check", "5"])]

        # act
        for query in queries:
            qp.process_query(query)

        # assert
        mock_print.assert_has_calls(calls=[call(""), call("")])

    @patch("builtins.print")
    def test_check_items_at_address(self, mock_print):
        # arrange

        qp = QueryProcessor(bucket_count=10)
        qp.elems[3] = ["test_1", "test_2", "test_3"]
        q = Query(["check", "3"])

        # act
        qp.process_query(q)

        # assert
        mock_print.assert_has_calls(calls=[call("test_1 test_2 test_3")])
