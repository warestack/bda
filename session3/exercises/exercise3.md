### Exercise 3: Sum of squares

* Considering the above code samples, create a function to store a list of strings into a file. Use the following specification.

```python
def save_text_to_file(text_list, filename):
 	...
```

* Develop a function to download a book using a specific `url` .  The function should download the book using the url, and then use the `save_text_to_file` to export the file.

```python
def download_book(url):
	...
  
  ...
  save_text_to_file(book,title)
  ...
```

* Create a function named `serial_downloader()` that downloads books in a serial manner and measures the time taken to complete the downloads. You will need to use Python’s `requests` library for fetching the data from the internet and the `time` module to keep track of the duration.
* Then, use the `multiprocessing.Process` to download the books in parallel. Measure the time taken to complete the downloads.
* Compare the serial and parallel case, do you notice a difference?

**Part 3**

Explore the following samples that utilize the `concurrent.futures.ProcessPoolExecutor()` that providesx	 a high-level interface for asynchronously executing callables using pools of threads or processes. 

```python
import time
import concurrent.futures

def foo():
    time.sleep(1)

def boo(seconds):
    time.sleep(seconds)

# Serial runner
def serial_runner():
    start=time.perf_counter()
    for i in range(3):
        foo()
    end=time.perf_counter()
    print(f'Serial: {end-start} second(s)')

# Creating three submission
def parallel_runner3():
    start=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(foo)
        f2 = executor.submit(foo)
        f3 = executor.submit(foo)
    end=time.perf_counter()
    print(f'Parallel (process pool): {end-start} second(s)')

# Mapping a function to inputs using a list.
def parallel_runner4():
    start=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(boo, [1,1,1])
    end=time.perf_counter()
    print(f'Parallel (process poolmap): {end-start} second(s)')

# Using max_workers 2 (reduce amount of the parallel runs)
def parallel_runner5():
    start=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        executor.map(boo, [1,1,1])
    end=time.perf_counter()
    print(f'Parallel (process poolmap): {end-start} second(s)')
    
if __name__ == '__main__':
    serial_runner()
    parallel_runner3()
    parallel_runner4()
    parallel_runner5()
```

**Exercise 3**

The following script caclualtes the sum of squares of integer numbers calculates from 0 up to a specified number.

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

