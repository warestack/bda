"""
This script simulates multiple threads performing database operations using a semaphore to control access to a limited 
number of database connections. Each thread prepares to access the database, performs the database operation, and then 
releases the connection. A semaphore with a count of 10 is used to allow up to ten threads to access the database simultaneously.

Functions:
- perform_db_operation(thread_id): Simulates a thread preparing for and performing a database operation.
  Uses a semaphore to control access to the database.

Execution:
- The script creates and starts 20 threads to simulate 20 threads needing database access.
- Each thread runs the perform_db_operation function.
- The script waits for all threads to finish before printing a final message.

List of threads:
- Simulates 20 threads needing database access.
"""

import threading
import time

# Create a semaphore with a count of 10 to simulate ten database connections
db_semaphore = threading.Semaphore(10)

# Function to simulate a thread performing a database operation
def perform_db_operation(thread_id):
    # Simulate performing some work before accessing the database
    print(f"Thread {thread_id} is preparing to access the database.")
    time.sleep(2)  # Simulate time taken to prepare
    print(f"Thread {thread_id} is ready to access the database.")

    # Acquire the semaphore before accessing the database
    db_semaphore.acquire()
    try:
        print(f"Thread {thread_id} is accessing the database.")
        time.sleep(2)  # Simulate time taken for database operation
        print(f"Thread {thread_id} has finished accessing the database.")
    finally:
        # Release the semaphore after accessing the database
        db_semaphore.release()

# List of threads that need to perform database operations
threads = []
for i in range(20):  # Simulate 20 threads needing database access
    thread = threading.Thread(target=perform_db_operation, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All database operations have been completed.")
