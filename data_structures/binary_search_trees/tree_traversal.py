import sys
import threading
from typing import List, Optional

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:

    def __init__(self,
                 n: Optional[int] = None,
                 keys: Optional[List[int]] = None,
                 right_children: Optional[List[int]] = None,
                 left_children: Optional[List[int]] = None):
        """
        basic tree class for traversal algorithms
        """

        self._n = n if n else None
        self._keys = keys if keys else []
        self._right_children = right_children if right_children else []
        self._left_children = left_children if left_children else []

    def populate_from_stdin(self) -> None:
        """
        parse a binary tree from stdin
        input
        """

        self._n = int(sys.stdin.readline())

        for _ in range(self._n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self._keys.append(a)
            self._left_children.append(b)
            self._right_children.append(c)

    def _traverse_in_order(self,
                           current_index: int,
                           output: List[int]) -> None:
        """
        recursive in order traversal
        """

        left_child_index = self._left_children[current_index]
        if left_child_index != -1:
            self._traverse_in_order(left_child_index, output)

        output.append(self._keys[current_index])

        right_child_index = self._right_children[current_index]
        if right_child_index != -1:
            self._traverse_in_order(right_child_index, output)

    def traverse_in_order(self) -> List[int]:
        """
        get the in order traversal of
        the tree
        """

        output = []
        self._traverse_in_order(0, output)
        return output

    def _traverse_pre_order(self,
                            current_index: int,
                            output: List[int]) -> None:
        """
        recursive pre order traversal
        """

        output.append(self._keys[current_index])

        left_child_index = self._left_children[current_index]
        if left_child_index != -1:
            self._traverse_pre_order(left_child_index, output)

        right_child_index = self._right_children[current_index]
        if right_child_index != -1:
            self._traverse_pre_order(right_child_index, output)

    def traverse_pre_order(self) -> List[int]:
        """
        get the pre order traversal of
        the tree
        """

        output = []
        self._traverse_pre_order(0, output)
        return output

    def _traverse_post_order(self,
                             current_index: int,
                             output: List[int]):
        """
        recursive post order traversal
        """

        left_child_index = self._left_children[current_index]
        if left_child_index != -1:
            self._traverse_post_order(left_child_index, output)

        right_child_index = self._right_children[current_index]
        if right_child_index != -1:
            self._traverse_post_order(right_child_index, output)

        output.append(self._keys[current_index])

    def traverse_post_order(self) -> List[int]:
        """
        get the post order traversal of
        the tree
        """

        output = []
        self._traverse_post_order(0, output)
        return output


def main():
    tree = TreeOrders()
    tree.populate_from_stdin()
    print(" ".join(str(x) for x in tree.traverse_in_order()))
    print(" ".join(str(x) for x in tree.traverse_pre_order()))
    print(" ".join(str(x) for x in tree.traverse_post_order()))


threading.Thread(target=main).start()
