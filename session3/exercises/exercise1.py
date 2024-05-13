import time
import multiprocessing

import random

def generate_and_sort_numbers():
    numbers = []
    for _ in range(10000):
        numbers.append(random.uniform(0, 100))
    # numbers = [random.uniform(0, 100) for _ in range(10000)]
    n = len(numbers)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break
    return numbers

# Serial runner
def serial_runner():
    start=time.perf_counter()
    for i in range(3):
        generate_and_sort_numbers()
    end=time.perf_counter()
    print(f'Serial run took {round(end-start,2)} second(s)')

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
    print(f'Parallel took {round(end-start,2)} second(s)')

if __name__ == '__main__':
    serial_runner()
    parallel_runner2()