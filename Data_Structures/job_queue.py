# python3

from collections import namedtuple
import numpy as np

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    result = [ ]
    workers = np.zeros(n_workers, dtype=int)
    for job in jobs:
        next_worker = np.argmin(workers)
        result.append((next_worker, workers[next_worker]))
        workers[next_worker] += job
    return result


def assign_jobs_old(n_workers, jobs):
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

    #n_workers, jobs = 2, [1,2,3,4,5]
    #n_workers, jobs = 4, [1]*20
    #n_jobs = len(jobs)

    assigned_jobs = assign_jobs(n_workers, jobs)

    for worker,started_at in assigned_jobs:
        print(worker, started_at)


if __name__ == "__main__":
    main()
