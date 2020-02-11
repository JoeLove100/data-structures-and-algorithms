from typing import List


class Database:
    def __init__(self,
                 row_counts: List[int]):

        # set the row counts
        self._row_counts = row_counts
        self.max_row_count = max(row_counts)

        # set the ranks
        n_tables = len(row_counts)
        self._ranks = [1] * n_tables
        self._parents = list(range(n_tables))

    def merge(self,
              src: int,
              dst: int) -> bool:
        """
        merge the source and destination tables
        using union by rank heuristics and update
        the max table size
        """
        src_parent = self._get_parent(src)
        dst_parent = self._get_parent(dst)

        if src_parent == dst_parent:
            # no union required
            return False

        rank_src = self._ranks[src_parent]
        rank_dst = self._ranks[dst_parent]
        new_row_count = self._row_counts[src_parent] + self._row_counts[dst_parent]

        if rank_src > rank_dst:
            self._parents[dst_parent] = src_parent
            self._row_counts[src_parent] = new_row_count
        else:
            self._parents[src_parent] = dst_parent
            self._row_counts[dst_parent] = new_row_count
            if rank_src == rank_dst:
                self._ranks[dst_parent] += 1

        self.max_row_count = max(self.max_row_count, new_row_count)

        return True

    def _get_parent(self,
                    table: int) -> int:
        """
        return the parent table id based on the
        given child table id and compress the
        path
        """
        if table != self._parents[table]:
            # compress path with recursive call
            self._parents[table] = self._get_parent(self._parents[table])
        return self._parents[table]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
