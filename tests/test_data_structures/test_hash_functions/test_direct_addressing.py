import unittest
from data_structures.hash_functions.direct_addressing import PhoneBook


class TestsDirectAddressing(unittest.TestCase):

    def test_add_name_to_phone_book(self):
        # arrange

        number = 12567
        name = "test"
        pb = PhoneBook()

        # act
        pb.add_number(number, name)

        # assert
        self.assertEqual("test", pb._arr[12567])

    def test_del_name_from_phone_book(self):
        # arrange

        number = 1234
        pb = PhoneBook(size=4)
        pb._arr[1234] = "test"

        # act
        pb.remove_number(number)

        # assert
        self.assertIsNone(pb._arr[1234])

    def test_get_name_from_phone_book_exists(self):
        # arrange

        number = 4321
        pb = PhoneBook(size=4)
        pb._arr[4321] = "test"

        # act
        result = pb.get_name_for_number(number)

        # assert
        self.assertEqual("test", result)

    def test_get_name_from_phone_book_not_exists(self):
        # arrange

        number = 4321
        pb = PhoneBook(size=4)

        # act
        result = pb.get_name_for_number(number)

        # assert
        self.assertEqual("not found", result)

    def test_get_name_from_phone_book_larger_than_array(self):
        # arrange

        number = 4321
        pb = PhoneBook(size=2)

        # act
        result = pb.get_name_for_number(number)

        # assert
        self.assertEqual("not found", result)

    def test_multiple_adds(self):

        pb = PhoneBook(size=1)
        pb.add_number(100, "test_1")
        pb.add_number(101, "test_2")
        pb.ad


