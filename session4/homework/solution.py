import threading
import time
import math

# Create locks for each log file
log1_lock = threading.Lock()
log2_lock = threading.Lock()
log3_lock = threading.Lock()

log_files = ["log1.txt", "log2.txt", "log3.txt"]
log_locks = [log1_lock, log2_lock, log3_lock]

def calculate_factorial_and_log(number, thread_id):
    # Calculate the factorial of the number
    result = math.factorial(number)
    log_data = f"Thread {thread_id}: factorial({number}) = {result}\n"

    # Try to acquire a lock and write to the first available log file
    for i in range(len(log_files)):
        if log_locks[i].acquire(blocking=False):
            try:
                with open(log_files[i], "a") as file:
                    file.write(log_data)
                print(f"Thread {thread_id} wrote to {log_files[i]}")
                break
            finally:
                log_locks[i].release()
        else:
            continue
    else:
        print(f"Thread {thread_id} could not acquire a lock, logging failed")

# List of numbers to calculate the factorial of
numbers = [5, 7, 10, 12, 15, 20]

# Create and start threads
threads = []
for i, number in enumerate(numbers):
    thread = threading.Thread(target=calculate_factorial_and_log, args=(number, i))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All factorial calculations have been logged.")
