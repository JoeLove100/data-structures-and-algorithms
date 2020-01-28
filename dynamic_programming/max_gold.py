import sys
from typing import List, Dict


def _get_optimal_weight(max_weight: int,
                        weights: List[int],
                        end: int,
                        memo: Dict) -> int:
    """
    recursive function to get the
    optimal weight possible based on the
    max_weight specified
    """

    if end == 0:
        if weights[0] <= max_weight:
            return weights[0]
        else:
            return 0

    last_weight = weights[end]
    remaining_capacity = max_weight - last_weight
    if remaining_capacity >= 0:
        if (remaining_capacity, end) in memo:
            max_with_last_weight = last_weight + memo[(remaining_capacity, end - 1)]
        else:
            max_from_remainder = _get_optimal_weight(remaining_capacity, weights, end - 1, memo)
            max_with_last_weight = last_weight + max_from_remainder
            memo.update({(remaining_capacity, end - 1): max_from_remainder})
    else:
        max_with_last_weight = 0

    if (max_weight, end) in memo:
        max_without_last_weight = memo[(max_weight, end)]
    else:
        max_without_last_weight = _get_optimal_weight(max_weight, weights,
                                                      end - 1, memo)
        memo.update({(max_weight, end - 1): max_without_last_weight})

    return max(max_with_last_weight, max_without_last_weight)


def get_optimal_weight(max_weight: int,
                       weights: List[int]) -> int:
    """
    wrapper for recursive function _get_optimal_weight
    """

    return _get_optimal_weight(max_weight, weights, len(weights) - 1, dict())


if __name__ == '__main__':
    input_data = sys.stdin.read()
    W, n, *w = list(map(int, input_data.split()))
    print(get_optimal_weight(W, w))





