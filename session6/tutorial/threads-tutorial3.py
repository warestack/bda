"""
This script demonstrates the difference between running tasks serially, in parallel using threads, 
and in parallel using processes in Python. It contains three main parts:
1. Serial Runner: Executes a function sequentially for a given range.
2. Thread Runner: Executes the same function concurrently using a thread pool for the same range.
3. Process Runner: Executes the same function concurrently using a process pool for the same range.

The function `sum_square(number)` calculates the sum of squares from 0 to `number-1`. 
The time taken for serial, threaded, and process-based executions is measured and printed.

Functions:
- sum_square(number): Calculates the sum of squares from 0 to `number-1`.
- serial_runner(arange): Runs the sum_square() function sequentially for each number in the range `arange` and measures the time taken.
- thread_runner(arange): Runs the sum_square() function concurrently using a thread pool for each number in the range `arange` and measures the time taken.
- process_runner(arange): Runs the sum_square() function concurrently using a process pool for each number in the range `arange` and measures the time taken.

Execution:
- The script runs the serial runner, the thread runner, and the process runner sequentially, printing the time taken for each.
"""

import time
import concurrent.futures

def sum_square(number):
    s = 0
    for i in range(number):
        s += i * i
    return s
    
def serial_runner(arange):
    start = time.perf_counter()
    for i in range(arange):
        sum_square(i)
    end = time.perf_counter()
    print(f'Serial: {end - start} second(s)')

def thread_runner(arange):
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(sum_square, range(arange))
    end = time.perf_counter()
    print(f'Parallel (threads): {end - start} second(s)')

def process_runner(arange):
    start=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(sum_square, range(arange))
    end=time.perf_counter()
    print(f'Parallel (processes): {end-start} second(s)')

if __name__ == '__main__':
    arange = 20000
    serial_runner(arange)
    thread_runner(arange)
    process_runner(arange)
