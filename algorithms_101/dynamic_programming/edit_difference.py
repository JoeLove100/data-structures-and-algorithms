from itertools import permutations


def get_min_edit_difference(string_1: str,
                            string_2: str) -> int:
    """
    wrapper for recursive function to get
    the min edit difference between two
    strings
    """

    width = len(string_1) + 1
    length = len(string_2) + 1

    arr = [[0 for _ in range(width)] for _ in range(length)]

    for i in range(width):
        arr[0][i] = i

    for j in range(length):
        arr[j][0] = j

    for i in range(1, width):
        for j in range(1, length):
            insertion_cost = arr[j - 1][i] + 1
            deletion_cost = arr[j][i - 1] + 1
            substitution_cost = arr[j - 1][i - 1] + 1
            if string_1[i - 1] == string_2[j - 1]:
                substitution_cost -= 1

            arr[j][i] = min(insertion_cost, substitution_cost, deletion_cost)

    return arr[-1][-1]


if __name__ == "__main__":
    print(get_min_edit_difference(input(), input()))
