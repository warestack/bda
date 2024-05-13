### Exercise 1: Sorting numbers

Examine and run the following script. 

* This Python script demonstrates the difference in execution time between running a simple function serially versus in parallel using the `multiprocessing` module. 
* The function `foo` simply pauses for 1 second. 
* The script defines three functions: `serial_runner`, which runs `foo` three times in a row, and `parallel_runner` and `parallel_runner2`, which run three instances of `foo` concurrently using multiprocessing. 
* Each function measures and prints the total execution time. 
* The `parallel_runner` creates and starts processes individually, while `parallel_runner2` uses a loop to create and manage a list of process objects.

```python
import time
import multiprocessing

def foo():
    time.sleep(1)

# Serial runner
def serial_runner():
    start=time.perf_counter()
    for i in range(3):
        foo()
    end=time.perf_counter()
    print(f'Serial: {end-start} second(s)')

def parallel_runner():
    start=time.perf_counter()
    processes = []
    for _ in range(3):
        p = multiprocessing.Process(target=foo)
        p.start()
        processes.append(p)
   
    for p in processes:
        p.join()

    end=time.perf_counter()
    print(f'Serial: {end-start} second(s)')

if __name__ == '__main__':
    serial_runner()
    parallel_runner()
```

**Exercise 1**

Using the code above, design a Python function named `generate_and_sort_numbers` that first generates 10,000 floating-point numbers, each randomly ranging from 0 to 100. 

> Why is data generation essential in data science?
>
> * In software development, having a tool to generate predictable yet random datasets is invaluable for stress-testing applications and ensuring that they can handle large volumes of data effectively.
> * Analysts often work with large datasets that aren't in a usable format. Generating and sorting synthetic data helps develop and test data processing algorithms.
> * Software developers can use such functions to benchmark the performance of sorting algorithms. By generating large datasets, developers can measure how performance scales with data size.

For generating numbers, feel free to use the following script.

```python
import random

rand_list = []
for _ in range(10000):
	rand_list.append(random.uniform(0, 100))
```

* Implement a sorting algorithm within this function to sort the array of numbers. Specifically, use the bubble sort technique, as seen in previous classes. You can reuse the code of lab 1. 
* The function does not accept any arguments and returns the returns the sorted list.

Make sure you test your function with a smaller generation, e.g., ten numbers, to ensure that it works appropriately. The list is sorted.

Then, complete the following tasks.

* Implement a function named `serial_runner` that sequentially executes the `generate_and_sort_numbers()` function three times. This function should record the start and end times using `time.perf_counter()` to measure the total duration required to complete the three sequential runs. The function should print the total execution time labeled as "Serial".

* Create a function called `parallel_runner2` that executes the same `generate_and_sort_numbers()` function three times, but in parallel. Utilize Python's `multiprocessing.Process` to achieve parallelism. Start each process, add it to a list of processes, and ensure each process completes by joining each one. Measure the total execution time for all processes to run concurrently and print this duration, labeled as "Parallel".
