### Exercise 3: Sum of squares

Create a script to calculate the sum of squares of integer numbers.

```python
def sum_square(number):
    ...
```

> [!TIP]
>
> What is the `sum_square(3)`?
>
> If you call `sum_square(3)`, the function will compute:
>
> - `0^2=0`
> - `1^2=1`
> - `2^2=4`
>
> And will return the sum of these squares, which is `0+1+4=5`. Note that `3` is excluded.

**Task 1**

Run the calculation of the `sum_square(20000)` in serial and calculate the time needed to do so.

```python
def serial_runner():
   ...
```

**Task 2**

Convert this script using the `ProcessPoolExecutor` and four workers. The script will execute the calculation in parallel and return the results. How long does it take to run it?

```python
def parallel_runner():
   ...
   with concurrent.futures.ProcessPoolExecutor()
   ...
```

**Task 3**

Using the `multiprocessing.Pool`, measure the time taken to run and compare it against the `parallel_runner`. Do you notice any difference?

```python
def parallel_map():
    ...
    with multiprocessing.Pool() as p:
    ...
```

> [!NOTE]
>
> The `multiprocessing.Pool` is a class provided by Python's `multiprocessing` module. It offers a convenient means of parallelising the execution of a function across multiple input values, distributing the input data across processes (data parallelism). This is particularly useful for performing CPU-intensive operations concurrently on multiple processors, which can significantly speed up the execution of a function that is applied to many items.

**Task 4**

What is the difference between `multiprocessing.Pool()` and `concurrent.futures.ProcessPoolExecutor` in Python?

- `multiprocessing.Pool()`: Best suited for straightforward parallel processing tasks where you want to quickly distribute a task among processes, especially when dealing with simple, independent data processing.
- `ProcessPoolExecutor`: Ideal for more complex applications requiring better error handling, future-based programming, or integration with other concurrent execution features.

