'''
Tutorial 1 Script Overview:

This script demonstrates the difference in performance and execution methodology between serial processing and multiprocessing in Python. 

Features:
* Serial Execution: Runs a set of tasks sequentially, one after the other, showing the total time taken to complete all tasks without parallel processing.
* Multiprocessing Execution: Utilizes the multiprocessing. Process class to run the same set of tasks in parallel, showcasing the reduced time required to complete tasks simultaneously.

The script provides examples of:
* Setting up and starting multiprocessing.Process instances manually.
* Synchronizing tasks using the start() and join() methods to ensure that the main program waits for all processes to complete before finishing.

Usage:
* Run the script directly from the command line to see the output of serial vs. multiprocessing execution times.
* Adjust the number of tasks or complexity of tasks to see how multiprocessing can scale compared to serial execution.
'''

import time
import multiprocessing

def foo():
    print("In foo...")
    print("Running...")
    time.sleep(1)

# Serial runner
def serial_runner():
    start=time.perf_counter()
    for i in range(3):
        foo()
    end=time.perf_counter()
    print(f'Serial: {end-start} second(s)')

# Parallel process runner
def parallel_runner1():
    
    start=time.perf_counter()

    p1 = multiprocessing.Process(target=foo)
    p2 = multiprocessing.Process(target=foo) 
    p3 = multiprocessing.Process(target=foo)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    end=time.perf_counter()
    print(f'Parallel: {end-start} second(s)')

if __name__ == '__main__':
    serial_runner()
    parallel_runner1()