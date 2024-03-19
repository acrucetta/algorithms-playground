"""
The system needs to process N types of jobs; type A, B, C

The pipeline of jobs should be independent of the job type.
A type jobs only block A jobs.

The results from each type of job queues should be delivered in the order
of input.

                 +-----------+
                 |  Input    |
                 |  Queues   |
                 +-----+-----+
                       |
           +-----------+-----------+
           |           |           |
     +-----+-----+ +---+---+ +-----+-----+
     |  Worker   | | Worker| |  Worker   |
     | Processes | |Process| | Processes |
     |  (Type A) | |(Type B| |  (Type C) |
     +-----------+ +-------+ +-----------+
           |           |           |
           +-----------+-----------+
                       |
                 +-----+-----+
                 |  Output   |
                 |  Queues/  |
                 |  Storage  |
                 +-----------+

Number of job types: 3

Jobs:
1. Type: A, ID: 1, Duration: 5
2. Type: B, ID: 1, Duration: 3
3. Type: A, ID: 2, Duration: 2
4. Type: C, ID: 1, Duration: 4
5. Type: B, ID: 2, Duration: 1
6. Type: A, ID: 3, Duration: 3
7. Type: C, ID: 2, Duration: 2
8. Type: B, ID: 3, Duration: 2
9. Type: A, ID: 4, Duration: 4
10. Type: C, ID: 3, Duration: 1
"""

import multiprocessing
import queue

def worker():
    pass

def process_job(job):
    pass

def main():
    num_of_job_types = 3
    return None

if __name__ == "__name__":
    main()
