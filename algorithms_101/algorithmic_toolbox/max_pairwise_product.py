from typing import List


def get_max_pairwise_product(numbers: List[int]):
    """
    return the largest pairwise product of two
    numbers from a list of integers
    """

    max_number = max(numbers)
    numbers.remove(max_number)
    second_max_number = max(numbers)
    max_product = max_number * second_max_number

    return max_product


if __name__ == "__main__":
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(get_max_pairwise_product(input_numbers))
