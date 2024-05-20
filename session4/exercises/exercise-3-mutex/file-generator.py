import threading
import time
from faker import Faker
import os

# Create a Faker object to generate random phrases
faker = Faker()

# Create a lock object to ensure only one thread writes to the file at a time
file_lock = threading.Lock()

# Specify the folder and file name
folder_name = "output"
file_name = "phrases.txt"
file_path = os.path.join(folder_name, file_name)

# Create the folder if it doesn't exist
os.makedirs(folder_name, exist_ok=True)

# Function to simulate a thread generating a phrase and saving it to a file
def generate_phrase_and_save(thread_id):
    # Generate a random phrase
    phrase = faker.sentence()
    print(f"Thread {thread_id} is generating phrase: {phrase}")
    time.sleep(2)  # Simulate time taken to generate the phrase

    # Acquire the file lock before writing to the file
    file_lock.acquire()
    try:
        with open(file_path, "a") as file:
            log_entry = f"Thread {thread_id}: {phrase}\n"
            file.write(log_entry)
        print(f"Thread {thread_id} has saved the phrase to the file.")
    finally:
        # Release the lock after writing to the file
        file_lock.release()

# List of thread identifiers (for demonstration purposes)
thread_ids = [0, 1, 2, 3]

# Create and start threads
threads = []
for thread_id in thread_ids:
    thread = threading.Thread(target=generate_phrase_and_save, args=(thread_id,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All phrases have been saved to the file.")
