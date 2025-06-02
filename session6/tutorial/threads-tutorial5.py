"""
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
"""

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
