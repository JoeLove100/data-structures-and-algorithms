import sys


def get_gcd(n: int,
            m: int) -> int:
    """
    recursive algorithm to find the greatest
    int which is a factor of m and n, where we
    assume n > m
    """

    if m == 0:
        return n
    else:
        remainder = n % m
        return get_gcd(m, remainder)


if __name__ == "__main__":
    input_data = sys.stdin.read()
    n_1, n_2 = map(int, input_data.split())
    if n_1 > n_2:
        print(get_gcd(n_1, n_2))
    else:
        print(get_gcd(n_2, n_1))
