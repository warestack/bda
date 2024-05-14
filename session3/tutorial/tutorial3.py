'''
Tutorial 3 Script Overview:

It utilizes the `concurrent.futures.ProcessPoolExecutor` to run a function in parallel across multiple processes, compared to a serial execution where tasks are processed sequentially.

Key Components:
* boo(sec): Function that simulates a time-consuming task by sleeping for a specified number of seconds and printing execution details.
* serial_runner(secs): Sequentially executes the boo function with a list of time durations, measuring the total execution time.
* parallel_runner4(secs): Utilizes a process pool to execute the same boo function in parallel, significantly reducing the overall execution time for multiple tasks.

Usage:
* Directly run this script to observe the output showing the time taken for both serial and parallel execution.
* Adjust the 'secs' list to include different or additional time durations to explore how execution time scales with number of tasks or task duration.
'''

import time
import concurrent.futures

def boo(sec):
    print("In foo...")
    print(f"Running for {sec} second(s)")
    time.sleep(sec)

def serial_runner2(secs):
    start=time.perf_counter()
    for i in secs:
        boo(i)
    end=time.perf_counter()
    print(f'Serial: {end-start} second(s)')

def parallel_runner4(secs):
    start=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(boo, secs)
    end=time.perf_counter()
    print(f'Parallel (process poolmap): {end-start} second(s)')

if __name__ == '__main__':
    secs = [1,2,3]
    serial_runner2(secs)
    parallel_runner4(secs)