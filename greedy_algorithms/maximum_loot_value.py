import sys
from typing import List, Tuple


def get_maximal_loot_value(loot: List[Tuple[int, int]],
                           max_weight) -> float:
    """
    get the max value of the loot which can be taken
    with based on the maximal available weight
    """

    # sort the loot by value per unit weight
    loot.sort(key=lambda x: x[0] / x[1])

    # set up some utility variables
    available_weight = max_weight
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

    with sys.stdin as raw_input:
        input_data = raw_input.read()
        input_data = input_data.split("\n")
        input_data = [list(map(int, row.split(" "))) for row in input_data]

    weight = input_data[0][1]
    loot_data = [(row[0], row[1]) for i, row in enumerate(input_data) if i != 0]


