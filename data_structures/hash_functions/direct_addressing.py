from typing import List


class PhoneBook:

    def __init__(self,
                 size: int = 3):

        self._size = size
        self._arr = [None] * int(10 ** size)

    @staticmethod
    def _hash_phone_number(number: int) -> int:
        """
        hash phone number using direct
        addressing
        """

        return number

    def add_number(self,
                   number: int,
                   name: str) -> None:
        """
        store number and name in our
        phone book
        """

        if len(str(number)) > self._size:
            # need to resize our array
            self._arr += [None] * (10 ** len(str(number)) - 10 ** self._size)
            self._size = len(str(number))

        hash_n = self._hash_phone_number(number)
        self._arr[hash_n] = name

    def remove_number(self,
                      number: int):
        """
        remove number stored for given name
        if it exists
        """
        
        try:
            self._arr[number] = None
        except IndexError:
            pass

    def get_name_for_number(self,
                            number: int) -> str:
        """
        return the name associated with a given
        number, or not found if there is no
        such name
        """
        
        try:
            name = self._arr[number]
        except IndexError:
            return "not found"
        
        if name is None:
            name = "not found"

        return name


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries(manual_input: List[str] = None):

    if manual_input is None:
        n = int(input())
        return [Query(input().split()) for _ in range(n)]
    else:
        return [Query(query.split()) for query in manual_input]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries: List[Query],
                    phone_book: PhoneBook) -> List[str]:
    """
    process each query one by one and build a list
    of the results
    """

    result = []

    for cur_query in queries:
        if cur_query.type == 'add':
                phone_book.add_number(cur_query.number, cur_query.name)
        elif cur_query.type == 'del':
                phone_book.remove_number(cur_query.number)
        else:
            response = phone_book.get_name_for_number(cur_query.number)
            result.append(response)

    return result


# if __name__ == '__main__':
#
#     with open("queries.txt") as input_file:
#         queries = input_file.read()
#         queries = queries.split("\n")
#     queries = read_queries(queries)
#     write_responses(process_queries(queries))

if __name__ == "__main__":

    pb = PhoneBook()
    write_responses(process_queries(read_queries(), pb))



