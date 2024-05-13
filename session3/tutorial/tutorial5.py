'''
Tutorial 5 Script Overview:

This script evaluates the performance differences between serial and parallel processing using Python's concurrent.futures.ProcessPoolExecutor and multiprocessing.Pool.

Functions:
- sum_square(number): Calculates the sum of squares for numbers from 0 to the specified 'number'. This function is used as the computation task in serial and parallel executions.
- serial_runner2(arange): Runs the sum_square function serially across numbers up to 'arange', measuring and printing the total execution time.
- parallel_runner5(arange): Executes the sum_square function in parallel using concurrent.futures.ProcessPoolExecutor, measuring and displaying the total execution time. This demonstrates the potential time-saving benefits of parallel execution using process pools.
- parallel_map(arange): Similar to parallel_runner5 but utilizes multiprocessing.Pool to achieve parallel execution, providing a practical comparison between two popular methods for managing parallel tasks in Python.

Usage:
- The script is executed with 'arange' set to 20000 to provide a substantial computational workload for noticeable performance comparison.
- Users can modify 'arange' to test different scales of computation or to analyze performance impacts more granularly.

Purpose:
- To illustrate how parallel processing can significantly reduce computation time compared to serial processing for large-scale data processing tasks.
- To provide insights into the effective use of Python's concurrency and parallelism features like ProcessPoolExecutor and multiprocessing.Pool.

Performance Notes:
- Parallel execution is typically more efficient for large 'arange' values where the overhead of process creation and management is offset by faster overall computation times.
- The choice between ProcessPoolExecutor and multiprocessing.Pool may depend on specific use cases and the nature of the tasks.

Run Instructions:
- Directly run this script from the command line. Ensure Python 3.5+ is installed due to the use of concurrent.futures module.
'''

import time
import concurrent.futures
import multiprocessing

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

def parallel_map(arange):
    t1 = time.perf_counter()
    with multiprocessing.Pool() as p:
        p.map(sum_square, range(arange))
    t2 = time.perf_counter()
    print(f'Parallel (processes) {t2-t1} second(s)' )

if __name__ == '__main__':
    arange = 20000
    serial_runner2(arange)
    parallel_runner5(arange)
    parallel_map(arange)