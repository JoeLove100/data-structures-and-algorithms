from typing import List


class Query:

    def __init__(self,
                 query: List[str]):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:

    def __init__(self,
                 bucket_count: int,
                 multiplier: int = 263,
                 prime: int = 1000000007):
        self._multiplier = multiplier
        self._prime = prime
        self.bucket_count = bucket_count
        self.elems = [None] * bucket_count

    def _hash_func(self,
                   s: str) -> int:
        """
        hash string using a polynomial hash
        """
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    @staticmethod
    def write_search_result(was_found: bool) -> None:
        """
        print yes/no for whether an item was
        contained in our set
        """
        print('yes' if was_found else 'no')

    @staticmethod
    def write_chain(chain: List[str]) -> None:
        """
        print chain to the console
        """

        print(' '.join(chain))

    @staticmethod
    def read_query() -> Query:
        """
        read line form stdin and wrap
        as query object
        """
        return Query(input().split())

    def process_query(self,
                      query: Query) -> None:
        """
        process query object and write the
        appropriate output to stdout
        """

        if query.type == "add":
            hash_n = self._hash_func(query.s)
            if self.elems[hash_n] is None:
                self.elems[hash_n] = [query.s]

            if query.s not in self.elems[hash_n]:
                self.elems[hash_n].insert(0, query.s)

        elif query.type == "del":
            hash_n = self._hash_func(query.s)

            if self.elems[hash_n] is None:
                return

            if query.s in self.elems[hash_n]:
                self.elems[hash_n].remove(query.s)

        elif query.type == "find":
            hash_n = self._hash_func(query.s)

            if self.elems[hash_n] is not None and query.s in self.elems[hash_n]:
                self.write_search_result(True)
            else:
                self.write_search_result(False)

        elif query.type == "check":
            if self.elems[query.ind] is None or len(self.elems[query.ind]) == 0:
                print("")
            else:
                self.write_chain(self.elems[query.ind])

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    bc = int(input())
    proc = QueryProcessor(bc)
    proc.process_queries()

# if __name__ == "__main__":
# 
#     with open("chaining.txt") as input_file:
#         input_data = input_file.read()
#         input_data = input_data.split("\n")
# 
#     queries = [Query(s.split(" ")) for s in input_data[2:]]
#     qp = QueryProcessor(bucket_count=int(input_data[0]))
# 
#     for q in queries:
#         qp.process_query(q)
