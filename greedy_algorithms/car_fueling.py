import sys
from typing import List


def compute_min_refills(total_distance: int,
                        car_distance: float,
                        stops: List[int]) -> int:
    """
    get the min number of times that the car has to
    refill based on the total distance, the position of
    the petrol stops and the total distance
    """

    stops.insert(0, 0)
    stops.append(total_distance)

    if any([stops[i + 1] - stops[i] > car_distance for i in range(len(stops) - 1)]):
        # journey is not possible
        return -1

    number_of_refills = 0
    current_refill = 0

    while current_refill < len(stops) - 1:

        last_refill = current_refill

        while current_refill < len(stops) - 1 and stops[current_refill + 1] - stops[last_refill] <= car_distance:
            current_refill += 1

        if current_refill < len(stops) - 1:
            number_of_refills += 1

    return number_of_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
