'''
Tutorial 2 Script Overview:

Key Components:
* boo(sec): A function that simulates processing by sleeping for 'sec' seconds, while printing the execution status.
* serial_runner2(secs): Runs the boo function serially, iterating over a list of specified durations and calculating the total execution time.
* parallel_runner2(secs): Executes the same tasks as serial_runner2 but in parallel using multiple processes, demonstrating the potential time savings with parallel processing.

Usage:
* The script is executed directly and will run both the serial and parallel functions with predefined durations.
* Modify the 'secs' list to test different execution times or add more tasks to see how the script scales with increased workload.

Purpose:
* This educational script is designed to highlight how parallel processing can reduce total execution time for independent tasks that are not CPU-bound but are instead limited by I/O operations or deliberate delays.

Performance Note:
* Parallel execution may not always be faster for very short tasks due to the overhead associated with starting and managing processes
'''

import time
import multiprocessing

def boo(sec):
    print("In foo...")
    print(f"Running for {sec} second(s)")
    time.sleep(sec)

# Serial runner
def serial_runner2(secs):
    start=time.perf_counter()
    for i in secs:
        boo(i)
    end=time.perf_counter()
    print(f'Serial: {end-start} second(s)')

def parallel_runner2(secs):
    start=time.perf_counter()
    processes = []
    for i in secs:
        p = multiprocessing.Process(target=boo,args=[i])
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    end=time.perf_counter()
    print(f'Serial: {end-start} second(s)')

if __name__ == '__main__':
    secs = [1,2,3]
    serial_runner2(secs)
    parallel_runner2(secs)