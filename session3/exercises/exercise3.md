### Exercise 3: Sum of squares

The following script calculates the sum of squares of integer numbers calculated from 0 up to a specified number.

```python
def sum_square(number):
    s = 0
    for i in range(number):
        s += i * i
    return s
```

> If you call `sum_square(3)`, the function will compute:
>
> - 0^2=0
> - 1^2=1
> - 2^2=4
>
> And will return the sum of these squares, which is 0+1+4=5. Note that 3 is excluded.

Here is an example of the serial run using 20 thousand numbers.

```python
def serial_runner2():
    start=time.perf_counter()
    for i in range(20000):
        sum_square(i)
    end=time.perf_counter()
    print(f'Serial: {end-start} second(s)')
```

Task 1: Convert this script to a parallel run using the `ProcessPoolExecutor` and 4 workers.

```python
def parallel_runner6():
    start=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
        executor.map(sum_square, range(20000))
    end=time.perf_counter()
    print(f'Parallel (process poolmap - 2): {end-start} second(s)')
```

Task 2: Explore and run the following script.

```python
import multiprocessing

def parallel_map():
    t1 = time.perf_counter()
    with multiprocessing.Pool() as p:
        p.map(sum_square, range(20000))
    t2 = time.perf_counter()
    print(f'Parallel (processes) {t2-t1} second(s)')
```

> The `multiprocessing.Pool` is a class provided by Python's `multiprocessing` module. It offers a convenient means of parallelizing the execution of a function across multiple input values, distributing the input data across processes (data parallelism). This is particularly useful for performing CPU-intensive operations concurrently on multiple processors, which can significantly speed up the execution of a function that is applied to many items.

