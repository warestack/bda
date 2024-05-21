## Threads 

Explore the following tutorials on how to use threads for parallel processing. 

* Study and run the scripts.

### Tutorial 1

This script demonstrates the difference between running tasks serially and in parallel using threads in Python. It contains two main parts:

1. Serial Runner: Executes a function sequentially three times.
2. Parallel Runner: Executes the same function concurrently using three threads.

The function `foo()` prints messages and sleeps for `1 second` to simulate some work. The time taken for both serial and parallel executions is measured and printed.

Functions:
- `foo()`: Prints messages and sleeps for `1 second`.
- `serial_runner()`: Runs the `foo()` function three times sequentially and measures the time taken.
- `parallel_runner1()`: Runs the `foo()` function thrice using threads and measures the time taken.

```python
import time
import threading

def foo():
    print("In foo...")
    print("Running...")
    time.sleep(1)

# Serial runner
def serial_runner():
    start = time.perf_counter()
    for i in range(3):
        foo()
    end = time.perf_counter()
    print(f'Serial: {end - start} second(s)')

# Parallel thread runner
def parallel_runner1():
    start = time.perf_counter()

    t1 = threading.Thread(target=foo)
    t2 = threading.Thread(target=foo)
    t3 = threading.Thread(target=foo)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    end = time.perf_counter()
    print(f'Parallel: {end - start} second(s)')

if __name__ == '__main__':
    serial_runner()
    parallel_runner1()
```

### Tutorial 2

This script demonstrates the difference between running tasks serially and in parallel using a thread pool in Python. It contains two main parts:
1. Serial Runner: Executes a function sequentially for a given list of durations.
2. Parallel Runner: Executes the same function concurrently using a thread pool for the same list of durations.

The function `boo(sec)` prints messages and sleeps for a specified number of seconds to simulate work. 
The time taken for both serial and parallel executions is measured and printed.

Functions:
- `boo(sec)`: Prints messages and sleeps for the given number of seconds.
- `serial_runner2(secs)`: Runs the `boo()` function sequentially for each duration in the list `secs` and measures the time taken.
- `parallel_runner4(secs)`: Runs the `boo()` function concurrently using a thread pool for each duration in the list `secs` and measures the time taken.

```python
import time
import concurrent.futures

def boo(sec):
    print("In foo...")
    print(f"Running for {sec} second(s)")
    time.sleep(sec)

def serial_runner2(secs):
    start = time.perf_counter()
    for i in secs:
        boo(i)
    end = time.perf_counter()
    print(f'Serial: {end - start} second(s)')

def parallel_runner4(secs):
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(boo, secs)
    end = time.perf_counter()
    print(f'Parallel (thread pool map): {end - start} second(s)')

if __name__ == '__main__':
    secs = [1, 2, 3]
    serial_runner2(secs)
    parallel_runner4(secs)
```

### Tutorial 3

This script demonstrates the difference between running tasks serially, in parallel using threads, 
and parallel using processes in Python. It contains three main parts:

1. Serial Runner: Executes a function sequentially for a given range.
2. Thread Runner: Executes the same function concurrently using a thread pool for the same range.
3. Process Runner: Executes the same function concurrently using a process pool for the same range.

The function `sum_square(number)` calculates the sum of squares from 0 to `number-1`. 
The time taken for serial, threaded, and process-based executions is measured and printed.

Functions:
- sum_square(number): Calculates the sum of squares from 0 to `number-1`.
- serial_runner(arange): Runs the sum_square() function sequentially for each number in the range `arange` and measures the time taken.
- thread_runner(arange): Runs the sum_square() function concurrently using a thread pool for each number in the range `arange` and measures the time taken.
- process_runner(arange): Runs the sum_square() function concurrently using a process pool for each number in the range `arange` and measures the time taken.

```python
import time
import concurrent.futures

def sum_square(number):
    s = 0
    for i in range(number):
        s += i * i
    return s
    
def serial_runner(arange):
    start = time.perf_counter()
    for i in range(arange):
        sum_square(i)
    end = time.perf_counter()
    print(f'Serial: {end - start} second(s)')

def thread_runner(arange):
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(sum_square, range(arange))
    end = time.perf_counter()
    print(f'Parallel (threads): {end - start} second(s)')

def process_runner(arange):
    start=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(sum_square, range(arange))
    end=time.perf_counter()
    print(f'Parallel (processes): {end-start} second(s)')

if __name__ == '__main__':
    arange = 20000
    serial_runner(arange)
    thread_runner(arange)
    process_runner(arange)
```

### Tutorial 4

This script simulates multiple threads performing work and then printing documents. Each thread generates a document, simulates some work, and then prints the document. A lock (mutex) is used to ensure that only one thread can access the
printer at a time, ensuring thread-safe printing.

Functions:
- perform_work_and_print(thread_id, document): Simulates a thread generating and printing a document. 
  Uses a lock to ensure exclusive access to the printer.

Execution:
- A list of documents to be generated and printed by different threads is specified.
- Threads are created and started for each document.
- The script waits for all threads to finish before printing a final message.

List of documents:
- Doc1, Doc2, Doc3, Doc4

```python
import threading
import time

# Create a lock object to simulate a mutex for the printer
printer_lock = threading.Lock()

# Function to simulate a thread performing work and then printing a document
def perform_work_and_print(thread_id, document):
    # Simulate performing some work in parallel
    print(f"Thread {thread_id} is generating document: {document}")
    time.sleep(2)  # Simulate time taken to generate the document
    print(f"Thread {thread_id} has finished generating document: {document}")

    # Acquire the printer lock before printing
    printer_lock.acquire()
    try:
        print(f"Thread {thread_id} is printing document: {document}")
        time.sleep(2)  # Simulate time taken to print the document
        print(f"Thread {thread_id} has finished printing document: {document}")
    finally:
        # Release the lock after printing is done
        printer_lock.release()

# List of documents to be generated and printed by different threads
documents = ["Doc1", "Doc2", "Doc3", "Doc4"]

# Create and start threads
threads = []
for i, doc in enumerate(documents):
    thread = threading.Thread(target=perform_work_and_print, args=(i, doc))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All documents have been printed.")
```

### Tutorial 5

This script simulates multiple threads performing work and then printing documents using a semaphore to control access to
a limited number of printers. Each thread generates a document, simulates some work, and then prints the document.
A semaphore with a count of 3 is used to allow up to three threads to print at the same time.

Functions:
- perform_work_and_print(thread_id, document): Simulates a thread generating and printing a document.
  Uses a semaphore to control access to the printers.

Execution:
- A list of documents to be generated and printed by different threads is specified.
- Threads are created and started for each document.
- The script waits for all threads to finish before printing a final message.

List of documents:
- Doc1, Doc2, Doc3, Doc4, Doc5, Doc6

```python
import threading
import time

# Create a semaphore with a count of 3 to simulate three printers
printer_semaphore = threading.Semaphore(3)

# Function to simulate a thread performing work and then printing a document
def perform_work_and_print(thread_id, document):
    # Simulate performing some work in parallel
    print(f"Thread {thread_id} is generating document: {document}")
    time.sleep(2)  # Simulate time taken to generate the document
    print(f"Thread {thread_id} has finished generating document: {document}")

    # Acquire the semaphore before printing
    printer_semaphore.acquire()
    try:
        print(f"Thread {thread_id} is printing document: {document}")
        time.sleep(2)  # Simulate time taken to print the document
        print(f"Thread {thread_id} has finished printing document: {document}")
    finally:
        # Release the semaphore after printing is done
        printer_semaphore.release()

# List of documents to be generated and printed by different threads
documents = ["Doc1", "Doc2", "Doc3", "Doc4", "Doc5", "Doc6"]

# Create and start threads
threads = []
for i, doc in enumerate(documents):
    thread = threading.Thread(target=perform_work_and_print, args=(i, doc))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All documents have been printed.")

```

