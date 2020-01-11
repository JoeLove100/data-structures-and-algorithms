import sys
from algorithmic_warm_up.sum_of_fibonacci_numbers import get_nth_fib_sum_modulon_m


def get_partial_fib_sum(n: int,
                        m: int,
                        k: int) -> int:
    """
    get the sum of the fibonacci numbers from
    m to n (where we assume m < m) modulo k
    """

    total_sum = get_nth_fib_sum_modulon_m(n, k)
    sum_to_remove = get_nth_fib_sum_modulon_m(m - 1, k)
    partial_sum = (total_sum - sum_to_remove) % k
    return partial_sum


if __name__ == "__main__":

    input_data = sys.stdin.read()
    input_data = sorted(list(map(int, input_data.split())))
    print(get_partial_fib_sum(input_data[1], input_data[0], 10))

