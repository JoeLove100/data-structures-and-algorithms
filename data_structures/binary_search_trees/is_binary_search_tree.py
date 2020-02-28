import sys
import threading
from typing import List

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def get_max_key(tree: List[List[int]],
                start_index: int,
                pre_computed: List[int]) -> int:
    """
    get the max key in the sub-tree starting
    the node at our start index
    """

    if pre_computed[start_index]:
        # already calculated so can just use this value
        max_val = pre_computed[start_index]
    else:
        current_key = tree[start_index][0]
        right_child_index = tree[start_index][2]
        if right_child_index != -1:
            # has right child to get max value iteratively
            max_val = get_max_key(tree, start_index, pre_computed)
        else:
            # no right child so must be the max at this node
            max_val = current_key

        pre_computed[start_index] = max_val

    return max_val


def get_min_val(tree: List[List[int]],
                start_index: int,
                pre_computed: List[int]) -> int:
    """
    get the min value in the sub-tree starting with
    the node at our start index
    """

    if pre_computed[start_index]:
        # already calculated so can just use this value
        min_val = pre_computed[start_index]
    else:
        current_key = tree[start_index][0]
        left_child_index = tree[start_index][1]
        if left_child_index != -1:
            # has left child so get min recursively
            min_val = get_min_val(tree, start_index, pre_computed)
        else:
            # no left child so must be min at this node
            min_val = current_key

        pre_computed[start_index] = min_val

    return min_val


def is_binary_search_tree(tree: List[List[int]]) -> bool:
    """
    check tree to see if it satisfies the conditions
    of a binary search tree
    """






def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))

    if is_binary_search_tree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
