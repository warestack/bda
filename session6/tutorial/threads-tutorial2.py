"""
This script demonstrates the difference between running tasks serially and in parallel using a thread pool in Python.
It contains two main parts:
1. Serial Runner: Executes a function sequentially for a given list of durations.
2. Parallel Runner: Executes the same function concurrently using a thread pool for the same list of durations.

The function `boo(sec)` prints messages and sleeps for the specified number of seconds to simulate work. 
The time taken for both serial and parallel executions is measured and printed.

Functions:
- boo(sec): Prints messages and sleeps for the given number of seconds.
- serial_runner2(secs): Runs the boo() function sequentially for each duration in the list `secs` and measures the time taken.
- parallel_runner4(secs): Runs the boo() function concurrently using a thread pool for each duration in the list `secs` and measures the time taken.

"""

import time
import concurrent.futures

def boo(sec):
    print("In foo...")
    print(f"Running for {sec} second(s)")
    time.sleep(sec)

def serial_runner2(secs):
    start = time.perf_counter()
    for i in secs:
        boo(i)
    end = time.perf_counter()
    print(f'Serial: {end - start} second(s)')

def parallel_runner4(secs):
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(boo, secs)
    end = time.perf_counter()
    print(f'Parallel (thread pool map): {end - start} second(s)')

if __name__ == '__main__':
    secs = [1, 2, 3]
    serial_runner2(secs)
    parallel_runner4(secs)
