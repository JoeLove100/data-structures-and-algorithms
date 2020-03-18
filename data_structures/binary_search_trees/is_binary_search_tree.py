import math
import sys
import threading
from typing import List, Union

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def get_max_key(tree: List[List[int]],
                start_index: int,
                pre_computed: List[Union[int, None]]) -> int:
    """
    get the max key in the sub-tree starting
    the node at our start index
    """

    if pre_computed[start_index]:
        # already calculated so can just use this value
        max_val = pre_computed[start_index]
    else:
        current_key = tree[start_index][0]

        left_child_index = tree[start_index][1]
        if left_child_index != -1:
            # get max value on left side
            max_val_left = get_max_key(tree, left_child_index, pre_computed)
        else:
            max_val_left = -math.inf

        right_child_index = tree[start_index][2]
        if right_child_index != -1:
            # has right child to get max value iteratively
            max_val_right = get_max_key(tree, right_child_index, pre_computed)
        else:
            # no right child so must be the max at this node
            max_val_right = -math.inf

        max_val = max(max_val_right, max_val_left, current_key)
        pre_computed[start_index] = max_val

    return max_val


def get_min_key(tree: List[List[int]],
                start_index: int,
                pre_computed: List[Union[int, None]]) -> int:
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
            # get min on the left side
            min_val_left = get_min_key(tree, left_child_index, pre_computed)
        else:
            min_val_left = math.inf

        right_child_index = tree[start_index][2]
        if right_child_index != -1:
            # get min val on right side
            min_val_right = get_min_key(tree, right_child_index, pre_computed)
        else:
            min_val_right = math.inf

        min_val = min(min_val_left, min_val_right, current_key)
        pre_computed[start_index] = min_val

    return min_val


def is_binary_search_tree(tree: List[List[int]]) -> bool:
    """
    check tree to see if it satisfies the conditions
    of a binary search tree
    """

    min_values = [None] * len(tree)
    max_values = [None] * len(tree)

    for node in reversed(tree):

        value = node[0]
        if node[1] != -1:
            max_on_left = get_max_key(tree, node[1], max_values)
        else:
            max_on_left = -math.inf

        if node[2] != -1:
            min_on_right = get_min_key(tree, node[2], min_values)
        else:
            min_on_right = math.inf

        if value < max_on_left or value > min_on_right:
            return False

    return True


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
