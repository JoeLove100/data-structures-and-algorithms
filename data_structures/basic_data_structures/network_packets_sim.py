from collections import namedtuple, deque
from typing import List

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self._size = size
        self._current_time = 0
        self._finish_times = deque()

    def process(self,
                request: Request) -> Response:

        self._current_time = request.arrived_at

        while len(self._finish_times) > 0 and self._finish_times[0] <= self._current_time:
            # this time is in the past, so drop from finish times
            self._finish_times.popleft()

        if len(self._finish_times) >= self._size:
            # queue full - drop the request
            return Response(True, -1)
        else:
            if len(self._finish_times) == 0:
                # can start immediately
                start_time = self._current_time
            else:
                # need to wait until last time in queue is processed
                start_time = self._finish_times[-1]

            # add processing time of this new request

            finish_time = start_time + request.time_to_process
            self._finish_times.append(finish_time)
            return Response(False, start_time)


def process_requests(requests: List[Request],
                     buffer: Buffer) -> List[Response]:
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
