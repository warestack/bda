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

**Exercise 1 tasks**

Using the code above, design a Python function named `generate_and_sort_numbers` that generates `n` number of floating-point numbers (e.g. 10,000), each randomly ranging from 0 to 100. The function uses the bubble sort method to sort numbers in ascending order,

```python
def generate_and_sort_numbers():
  numbers = []
	...

	return numbers
```

Here is the code for the `bubble_sort` method.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

> Why is data generation essential in data science?
>
> * In software development, having a tool to generate predictable yet random datasets is invaluable for stress-testing applications and ensuring that they can handle large volumes of data effectively.
> * Analysts often work with large datasets that aren't in a usable format. Generating and sorting synthetic data helps develop and test data processing algorithms.
> * Software developers can use such functions to benchmark the performance of sorting algorithms. Developers can measure how performance scales with data size by generating large datasets.

For generating numbers, feel free to use the following script.

```python
import random

rand_list = []
for _ in range(10000):
	rand_list.append(random.uniform(0, 100))
```

* Implement a sorting algorithm within this function to sort the array of numbers. Specifically, use the bubble sort technique, as seen in previous classes. You can reuse the code of lab 1. 
* The function does not accept any arguments and returns the returns the sorted list. Assume that you always need to generate 10,000 numbers. 

**Serial vs Multiprocessing**

Then, complete the following tasks.

* Implement a function named `serial_runner` that sequentially executes the `generate_and_sort_numbers()` function three times. This function should record the start and end times using `time.perf_counter()` to measure the total duration required to complete the three sequential runs. The function should print the total execution time labelled as "Serial".

* Create a function called `parallel_runner2` that executes the same `generate_and_sort_numbers()` function three times but in parallel. Utilize Python's `multiprocessing.Process` to achieve parallelism. Start each process, add it to a list of processes, and ensure each process completes by joining each one. Measure the total execution time for all processes to run concurrently and print this duration, labelled as "Parallel".

**Here is the output of my screenshots; note that your times should be different.**

```python
...
if __name__ == '__main__':
    serial_runner()
    parallel_runner2()

# Serial run was completed in 18.95 second(s)
# Parallel run was completed in 6.63 second(s)
```

