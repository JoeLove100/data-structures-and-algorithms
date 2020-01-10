import sys
from algorithmic_warm_up.greatest_common_divisor import get_gcd


def get_lcm(n: int,
            m: int) -> int:
    """
    get the lowest common multiple of n, m
    where we assume n > m
    """

    gcd = get_gcd(n, m)
    lcm = m * n / gcd  # type: int
    return lcm


if __name__ == "__main__":
    input_data = sys.stdin.read()
    n_1, n_2 = map(int, input_data.split())
    if n_1 > n_2:
        print(get_lcm(n_1, n_2))
    else:
        print(get_lcm(n_2, n_1))
