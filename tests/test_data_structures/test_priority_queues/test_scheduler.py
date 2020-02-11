import unittest
from data_structures.prioritiy_queues.scheduler import assign_jobs, AssignedJob


class TestScheduler(unittest.TestCase):

    def test_assign_jobs_more_threads_than_jobs(self):
        # arrange

        threads = 4
        jobs = [10, 10, 2]

        # act
        result = assign_jobs(threads, jobs)

        # assert
        expected_result = [AssignedJob(0, 0), AssignedJob(1, 0), AssignedJob(2, 0)]
        self.assertSequenceEqual(expected_result, result)

    def test_assign_job_one_thread_only(self):
        # arrange

        threads = 1
        jobs = [4, 6, 1, 2]

        # act
        result = assign_jobs(threads, jobs)

        # assert
        expected_result = [AssignedJob(0, 0), AssignedJob(0, 4), AssignedJob(0, 10), AssignedJob(0, 11)]
        self.assertSequenceEqual(expected_result, result)

    def test_assign_job_multiple_threads_in_competition(self):
        # arrange

        threads = 3
        jobs = [4, 4, 2, 2, 3]

        # act
        result = assign_jobs(threads, jobs)

        # assert
        expected_result = [AssignedJob(0, 0), AssignedJob(1, 0), AssignedJob(2, 0), AssignedJob(2, 2),
                           AssignedJob(0, 4)]
        self.assertSequenceEqual(expected_result, result)
