from math import inf
from typing import List, Tuple


def _get_diagonals(n: int) -> List[Tuple[int, int]]:
    """
    utility method to generate successive upper
    diagonals required for our tabulation
    """

    diagonals = []

    for j in range(n):
        i = 0
        while i + j < n:
            diagonals.append((i, i + j))
            i += 1

    return diagonals


def evaluate(a: int,
             b: int,
             op: str) -> int:
    """
    evaluate the binary operation
    defined by op in a/b
    """
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        raise ValueError("{0} not recognised as an operation".format(op))


def get_maximum_value(data_set: str):
    """
    get the max value of the expression
    described in the input string
    """

    numbers = list(map(int, data_set[::2]))
    operations = list(data_set[1::2])

    min_arr = [[0 for _ in range(len(numbers))] for _ in range(len(numbers))]
    max_arr = [[0 for _ in range(len(numbers))] for _ in range(len(numbers))]

    diagonals = _get_diagonals(len(numbers))

    for i, j in diagonals:

        if i == j:
            # single number - no operator in involved
            min_arr[i][j] = max_arr[i][j] = numbers[i]

        else:

            max_val = -inf
            min_val = inf

            for k in range(i, j):
                op = operations[k]
                v_1 = evaluate(max_arr[i][k], max_arr[k + 1][j], op)
                v_2 = evaluate(max_arr[i][k], min_arr[k + 1][j], op)
                v_3 = evaluate(min_arr[i][k], max_arr[k + 1][j], op)
                v_4 = evaluate(min_arr[i][k], min_arr[k + 1][j], op)

                max_val = max(v_1, v_2, v_3, v_4, max_val)
                min_val = min(v_1, v_2, v_3, v_4, min_val)

            max_arr[i][j] = max_val
            min_arr[i][j] = min_val

    return max_arr[0][-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
