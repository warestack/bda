'''
Tutorial 4 Script Overview:

Functions:
- sum_square(number): Calculates the sum of squares from 0 to the specified number.
- serial_runner2(arange): Executes the `sum_square` function serially across a range of numbers and measures the execution time.
- parallel_runner5(arange): Runs the `sum_square` function in parallel using a process pool and measures the execution time.
- parallel_runner6(arange): Similar to `parallel_runner5` but explicitly sets the number of worker processes to 2 to provide a comparative baseline against parallel execution with default settings.

Usage:
- The script automatically runs these functions when executed, using a predefined range of 20000.
- To compare performance, `serial_runner2` runs without parallelism, while `parallel_runner5` and `parallel_runner6` utilize parallel processing to potentially enhance performance.

Purpose:
- The primary goal of this script is to highlight how parallel processing can improve execution efficiency for CPU-intensive tasks compared to traditional serial execution.
- By adjusting the `arange` value or modifying the functions, users can explore different aspects of concurrency and its impact on performance.

Note:
- The results will vary based on the machine's CPU capabilities and current system load. Therefore, multiple runs might yield slightly different timings.
- In `parallel_runner6`, if  `max_workers=1` you can simulate parallel execution overhead without actual concurrency to serve as a control group in performance tests.
'''

import time
import concurrent.futures

def sum_square(number):
    s = 0
    for i in range(number):
        s += i * i
    return s
    
def serial_runner2(arange):
    start=time.perf_counter()
    for i in range(arange):
        sum_square(i)
    end=time.perf_counter()
    print(f'Serial: {end-start} second(s)')

def parallel_runner5(arange):
    start=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(sum_square, range(arange))
    end=time.perf_counter()
    print(f'Parallel (process poolmap): {end-start} second(s)')

def parallel_runner6(arange):
    start=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        executor.map(sum_square, range(arange))
    end=time.perf_counter()
    print(f'Parallel (process poolmap - 2 workers): {end-start} second(s)')

if __name__ == '__main__':
    arange = 20000
    serial_runner2(arange)
    parallel_runner5(arange)
    parallel_runner6(arange)