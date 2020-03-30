import sys


class DisjointSets:

    def __init__(self):

        self._parents = dict()
        self._ranks = dict()

    def make_set(self,
                 number: int) -> None:

        if number in self._parents:
            return

        self._parents[number] = number
        self._ranks[number] = 0

    def find(self,
             number: int) -> int:

        if number != self._parents[number]:
            number = self.find(self._parents[number])

        return self._parents[number]

    def union(self,
              first_number: int,
              second_number: int):

        first_parent = self.find(first_number)
        second_parent = self.find(second_number)

        if first_parent == second_parent:
            # both already in the same set
            return

        if self._ranks[first_parent] > self._ranks[second_parent]:
            self._parents[second_parent] = first_parent
            self._ranks.pop(second_parent)
        elif self._ranks[first_parent] < self._ranks[second_parent]:
            self._parents[first_parent] = second_parent
            self._ranks.pop(first_parent)
        else:
            self._parents[first_parent] = second_parent
            self._ranks[second_parent] += 1
            self._ranks.pop(first_parent)

    def reach(self,
              first_number: int,
              second_number: int) -> bool:

        first_parent = self.find(first_number)
        second_parent = self.find(second_number)
        return first_parent == second_parent

    def number_of_connected_components(self) -> int:

        return len(self._ranks)


if __name__ == '__main__':

    # read in data from stdin
    raw_input = sys.stdin.read()
    data = list(map(int, raw_input.split()))
    n, m = data[0:2]
    data = data[2:]

    # set up our disjoint set class
    disjoint_sets = DisjointSets()
    for i in range(1, n + 1):
        disjoint_sets.make_set(i)

    # union all edges
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    for an_edge in edges:
        disjoint_sets.union(*an_edge)

    # find if  our x, y are in the same set
    print(disjoint_sets.number_of_connected_components())
