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

### Threads mutex

1. **Initialize a counter variable**: This line sets the initial value of the counter to 0.
2. **Create a lock (mutex) for synchronizing access to shared resources**: This line initializes a lock to control access to shared resources and prevent race conditions.
3. **Define a function to perform some task, simulating a delay**: This function prints a message and sleeps for 1 second to simulate a task.
4. **Define a function to increment the counter safely using a lock**: This function increments the global counter variable, ensuring that only one thread can modify the counter at a time by using the lock.
5. **Lists to hold thread objects**: These lines initialize empty lists to store the thread objects for the two different tasks.
6. **Create and start threads**: This comment indicates the beginning of the section where threads are created and started.
7. **Create a new thread for the do_something function**: This line creates a new thread object to execute the `do_something` function with the current loop index as an argument.
8. **Create a new thread for the increment_counter function**: This line creates a new thread object to execute the `increment_counter` function.
9. **Append the created threads to their respective lists**: This line adds the created thread objects to their respective lists.
10. **Start the threads, beginning their execution**: This line starts the execution of the created threads.
11. **Wait for all threads in threads1 to finish**: This comment indicates the beginning of the section where the script waits for all threads in `threads1` to complete.
12. **Wait for all threads in threads2 to finish**: This comment indicates the beginning of the section where the script waits for all threads in `threads2` to complete.
13. **Print the final value of the counter**: This line prints the final value of the counter after all threads have finished executing.

```python
import threading
import time

# Initialize a counter variable
counter = 0

# Create a lock (mutex) for synchronizing access to shared resources
lock = threading.Lock()

# Define a function to perform some task, simulating a delay
def do_something(i):
    print("In something thread", i)
    time.sleep(1)

# Define a function to increment the counter safely using a lock
def increment_counter():
    global counter
    # Acquire the lock before accessing the shared counter
    lock.acquire()
    counter += 1
    # Release the lock after modifying the shared counter
    lock.release()

# Lists to hold thread objects
threads1 = []
threads2 = []

# Create and start threads
for i in range(3):
    # Create a new thread for the do_something function
    thread1 = threading.Thread(target=do_something, args=[i])
    # Create a new thread for the increment_counter function
    thread2 = threading.Thread(target=increment_counter)

    # Append the created threads to their respective lists
    threads1.append(thread1)
    threads2.append(thread2)
    
    # Start the threads, beginning their execution
    thread1.start()
    thread2.start()

# Wait for all threads in threads1 to finish
for thread in threads1:
    thread.join()

# Wait for all threads in threads2 to finish
for thread in threads2:
    thread.join()

# Print the final value of the counter
print(f"Final counter value: {counter}")
```

### Threads semaphore

1. **Initialization**: A semaphore with a value of 2 is created, and the number of threads (`n`) is set to 5.

2. **Function Definitions**: Two functions (`do_something` and `worker`) are defined. The `worker` function uses the semaphore to control access to its critical section.

3. **Thread Pool**: A thread pool with a maximum of 5 threads is created using `ThreadPoolExecutor`.

4. Submitting Tasks

   :

   - `do_something` tasks are submitted to the thread pool, creating 5 futures in `futures1`.
   - `worker` tasks are submitted to the thread pool, creating 5 futures in `futures2`.

5. **Optional Waiting**: The main thread can wait for all futures to complete if the commented-out section is uncommented.

6. **Concurrency Control**: The semaphore ensures that only up to 2 `worker` threads can be in their critical section at the same time, demonstrating synchronization and concurrency control.

By using the semaphore, this code ensures that the `worker` function's critical section is never accessed by more than 2 threads simultaneously, while the `do_something` function runs without such restrictions. The `ThreadPoolExecutor` manages the creation and execution of threads, simplifying the process of working with multiple threads.

```python
import concurrent.futures
import threading
import time

# Initialize a semaphore with a value of 2, allowing up to 2 threads to access a resource simultaneously
semaphore = threading.Semaphore(2)

# Number of threads to be created
n = 5

def do_something(i):
    # Function that simulates some work by printing a message and sleeping for 1 second
    print("In something thread", i)
    time.sleep(1)

def worker(thread_id):
    # Acquire the semaphore before performing the work
    semaphore.acquire()
    print(f"Thread {thread_id} is working")
    time.sleep(1)  # Simulate some work by sleeping for 1 second
    print(f"Thread {thread_id} is done")
    # Release the semaphore after the work is done
    semaphore.release()

# Use a ThreadPoolExecutor to manage a pool of threads
with concurrent.futures.ThreadPoolExecutor(max_workers=n) as executor:
    # Submit 'do_something' tasks to the executor for each thread
    futures1 = [executor.submit(do_something, i) for i in range(n)]
    
    # Submit 'worker' tasks to the executor for each thread
    futures2 = [executor.submit(worker, i) for i in range(n)]
    
    # Optional: Wait for all futures to complete and retrieve their results
    # Uncomment the following lines if you want to wait for all futures to complete
    for future in concurrent.futures.as_completed(futures1 + futures2):
        future.result()
```

