from typing import List
from collections import deque


def max_in_sliding_window(sequence: List[int],
                          size: int) -> List[int]:
    """
    return a list of the max value in each rolling
    window over the input sequence
    """

    queue = deque()
    max_for_windows = []

    if len(sequence) <= size:
        return [max(sequence)]

    window_start = 0
    window_end = 0
    while window_end < len(sequence):
        current_element = sequence[window_end]

        if (len(queue) != 0) and queue[0][1] < window_start:
            queue.popleft()

        while (len(queue) != 0) and current_element >= queue[-1][0]:
            queue.pop()

        queue.append((current_element, window_end))
        window_end += 1

        if window_end - window_start >= size:
            max_for_windows.append(queue[0][0])
            window_start += 1

    return max_for_windows


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_in_sliding_window(input_sequence, window_size))

#
# if __name__ == "__main__":
#
#     import random
#     from timeit import default_timer as timer
#
#     random.seed(1234)
#     sequence = list(range(100000))
#     sequence.reverse()
#     window_size = 33333
#
#     t_0 = timer()
#     max_in_sliding_window(sequence, size=window_size)
#     t_1 = timer()
#     print(t_1 - t_0)

# if __name__ == "__main__":
#
#     import random
#
#     for _ in range(10000):
#         sequence = [random.randint(0, 10) for _ in range(10)]
#
#         slow_answer = [max(sequence[i: i+3]) for i in range(8)]
#         fast_answer = max_in_sliding_window(sequence, 3)
#
#         if slow_answer == fast_answer:
#             print(f"Correct for {sequence}")
#         else:
#             print(f"Error for {sequence}")
#             print(f"Correct answer is {slow_answer}")
#             print(f"My answer is {fast_answer}")
#             break



