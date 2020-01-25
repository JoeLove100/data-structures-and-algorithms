import sys
from typing import List, Dict


def _get_optimal_sequence(n: int,
                          memo: Dict[int, List[int]])-> List[int]:
    """
    get the shortest sequence of operations required
    in order to reach the number 1 from n
    """

    # print(f"Recursion level {count}, n is {n}")

    if n == 1:
        return [1]

    potential_sequences = []

    for k in [2, 3]:

        if n % k == 0:
            remaining_sequence = memo.get(n // k)
            if remaining_sequence is None:
                remaining_sequence = _get_optimal_sequence(n // k, memo)
                memo.update({n // k: remaining_sequence.copy()})

            potential_sequences.append(remaining_sequence)

    for k in [1]:

        if n - k >= 1 and len(potential_sequences) < 2:
            remaining_sequence = memo.get(n - k)
            if remaining_sequence is None:
                remaining_sequence = _get_optimal_sequence(n - k, memo)
                memo.update({n - k: remaining_sequence.copy()})

            potential_sequences.append(remaining_sequence)

    shortest_sequence = min(potential_sequences, key=lambda s: len(s)).copy()
    shortest_sequence.append(n)
    return shortest_sequence


def get_optimal_sequence(n: int) -> List[int]:
    """
    wrapper function for recursive method for
    finding optimal sequence to 1
    """

    memo = dict()
    optimal_sequence = _get_optimal_sequence(n, memo)
    return optimal_sequence


if __name__ == "__main__":

    input_data = sys.stdin.read()
    number = int(input_data)
    sequence = list(get_optimal_sequence(number))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
