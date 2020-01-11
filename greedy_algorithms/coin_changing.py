import math
from typing import List


def get_min_number_of_coins(change: int,
                            coin_vals: List[int]) -> int:
    """
    get the number of coins required to make up
    value change from the valid coin values
    """

    coin_count = 0
    remaining_value = change
    coin_vals.sort(reverse=True)

    for val in coin_vals:
        coin_count += math.floor(remaining_value / val)
        remaining_value = remaining_value % val

        if remaining_value == 0:
            break

    return coin_count


if __name__ == "__main__":

    value = int(input())
    print(get_min_number_of_coins(value, [1, 5, 10]))


