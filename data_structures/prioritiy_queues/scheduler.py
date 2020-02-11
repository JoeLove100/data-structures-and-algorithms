from collections import namedtuple, deque
import heapq
from typing import List

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers: int,
                jobs: List[int]) -> List[AssignedJob]:
    """
    assign each job to a worker thread and return a
    list of all assigned jobs
    """

    all_assigned_jobs = []
    all_jobs = deque(jobs)
    n_workers = [(0, thread) for thread in range(n_workers)]
    heapq.heapify(n_workers)

    while len(all_jobs) > 0:

        # get the next job and available thread, update current time
        current_job_length = all_jobs.popleft()
        next_available_thread = heapq.heappop(n_workers)
        current_time = next_available_thread[0]

        # add assigned job, starting at the current time
        all_assigned_jobs.append(AssignedJob(next_available_thread[1], current_time))

        # push thread back to heap with updated finish time
        heapq.heappush(n_workers, (current_time + current_job_length, next_available_thread[1]))

    return all_assigned_jobs


def assign_jobs_slow(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
