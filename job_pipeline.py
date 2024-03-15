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
"""

import multiprocessing
import queue

def worker():
    pass

def process_job(job):
    pass

def main():
    pass

if __name__ == "__name__":
    main()
