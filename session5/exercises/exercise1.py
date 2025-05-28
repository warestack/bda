import time
import multiprocessing

import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def generate_and_sort_numbers():
    numbers = []
    for _ in range(10000):
        numbers.append(random.uniform(0, 100))
    bubble_sort(numbers)
    return numbers

# Serial runner
def serial_runner():
    start=time.perf_counter()
    for i in range(3):
        generate_and_sort_numbers()
    end=time.perf_counter()
    print(f'Serial run was completed in {round(end-start,2)} second(s)')

def parallel_runner2():
    start=time.perf_counter()
    processes = []
    for _ in range(3):
        p = multiprocessing.Process(target=generate_and_sort_numbers)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    end=time.perf_counter()
    print(f'Parallel run was completed in {round(end-start,2)} second(s)')

if __name__ == '__main__':
    serial_runner()
    parallel_runner2()