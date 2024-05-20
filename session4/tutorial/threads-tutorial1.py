"""
This script demonstrates the difference between running tasks serially and in parallel using threads in Python. 
It contains two main parts:
1. Serial Runner: Executes a function sequentially three times.
2. Parallel Runner: Executes the same function concurrently using three threads.

The function `foo()` prints messages and sleeps for 1 second to simulate work. The time taken for both serial 
and parallel executions is measured and printed.

Functions:
- foo(): Prints messages and sleeps for 1 second.
- serial_runner(): Runs the foo() function three times sequentially and measures the time taken.
- parallel_runner1(): Runs the foo() function three times concurrently using threads and measures the time taken.

Execution:
- The script runs the serial runner first and then the parallel runner, printing the time taken for each.
"""

import time
import threading

def foo():
    print("In foo...")
    print("Running...")
    time.sleep(1)

# Serial runner
def serial_runner():
    start = time.perf_counter()
    for i in range(3):
        foo()
    end = time.perf_counter()
    print(f'Serial: {end - start} second(s)')

# Parallel thread runner
def parallel_runner1():
    start = time.perf_counter()

    t1 = threading.Thread(target=foo)
    t2 = threading.Thread(target=foo)
    t3 = threading.Thread(target=foo)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    end = time.perf_counter()
    print(f'Parallel: {end - start} second(s)')

if __name__ == '__main__':
    serial_runner()
    parallel_runner1()
