
import queue
import threading
import time

lock = threading.Lock()
shared_data = 0

def increment_with_lock():
    global shared_data
    for _ in range(1_000_000):
        with lock: # Acquire lock; it introduces overhead but ensures that only one thread can access the shared data at a time
            shared_data += 1
        # Release lock

def increment_no_lock():
    global shared_data
    for _ in range(1_000_000):
        shared_data += 1

def producer(q):
    for i in range(5):
        q.put(i)

def consumer(q):
    while True:
        data = q.get()
        print(f"Data: {data}")
        q.task_done()

def test_lock():
    time_start = time.time()
    threads = [threading.Thread(target=increment_no_lock) for _ in range(25)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    time_end = time.time()
    print(f"Shared data with threading: {shared_data}")
    print(f"Time taken: {time_end - time_start}")

    # With no threading
    # shared_data_no_thread = 0
    # time_start = time.time()
    # for _ in range(10_000_000):
    #     shared_data_no_thread += 1
    # print(f"Shared data without threading: {shared_data_no_thread}")
    # time_end = time.time()
    # print(f"Time taken without threading: {time_end - time_start}")

if __name__ == "__main__":
    test_lock()
