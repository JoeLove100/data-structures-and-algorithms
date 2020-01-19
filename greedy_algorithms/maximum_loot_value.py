import sys
from typing import List, Tuple


def get_maximal_loot_value(loot: List[Tuple[int, int]],
                           maximum_weight) -> float:
    """
    get the max value of the loot which can be taken
    with based on the maximal available weight
    """

    # sort the loot by value per unit weight
    loot.sort(key=lambda x: x[0] / x[1])

    # set up some utility variables
    available_weight = maximum_weight
    total_value = 0

    while available_weight > 0 and len(loot) > 0:
        # take as much of the best available loot as possible
        selected_loot = loot.pop()
        loot_weight = min(selected_loot[1], available_weight)

        # update the total value and remaining weight
        total_value += loot_weight * (selected_loot[0] / selected_loot[1])
        available_weight -= loot_weight

    return total_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    max_weight = data[1]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    loot_data = [(v, w) for v, w in zip(values, weights)]
    print(get_maximal_loot_value(loot_data, max_weight))



