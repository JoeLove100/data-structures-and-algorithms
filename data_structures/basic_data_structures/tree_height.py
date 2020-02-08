import sys
import threading
from typing import Any, List


class TreeNode:

    def __init__(self,
                 key: Any):

        self.key = key
        self._child_nodes = []

    def add_child(self,
                  bn: "TreeNode") -> None:
        """
        assign a child tree to this tree
        """

        self._child_nodes.append(bn)

    def get_height(self):

        if len(self._child_nodes) == 0:
            return 1

        max_height = 0
        for child in self._child_nodes:
            max_height = max(max_height, child.get_height())

        return 1 + max_height


def compute_height(n: int,
                   parents: List[int]) -> int:
    """
    construct a tree based on the input definitions
    and calculate its depth
    """

    nodes = [TreeNode(i) for i in range(n)]
    root_index = None

    for i, p in enumerate(parents):
        if p == -1:
            root_index = i
            continue
        else:
            parent = nodes[p]
            child = nodes[i]
            parent.add_child(child)

    root = nodes[root_index]
    depth = root.get_height()
    return depth


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
