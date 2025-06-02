### Exercise 3

**Extract random text using the `Faker` library and store it in a file.** 

* Using a serial programming approach, use the following scripts to generate data from the `Faker` library.
* Then, use `Threads` or the  `ThreadPoolExecutor`  to generate data in parallel.
* Compare the time taken for both tasks.

**Supporting material.**

You can use the following scripts as your starting point. 

* Explore the following scripts that create a new record in a file using the faker library. Firstly, install the library.

```
pip3 install Faker
```

* Study and run the following script.

```python
from faker import Faker
import os, time

# Create a Faker object to generate random phrases
faker = Faker()

# Specify the folder and file name
folder_name = "output"
file_name = "phrases.txt"
file_path = os.path.join(folder_name, file_name)

# Create the folder if it doesn't exist
os.makedirs(folder_name, exist_ok=True)

# Generate a random sentence using Faker
phrase = faker.sentence()

# Open the file in append mode
with open(file_path, "a") as file:
    # Create a log entry with the generated phrase
    log_entry = f"Saved: {phrase}\n"
    
    # Write the log entry to the file
    file.write(log_entry)

```

* You will need to use a `lock` to write data to the file.

```python
# Create a lock object to ensure only one thread writes to the file at a time
file_lock = threading.Lock()
...
# Acquire the file lock before writing to the file
file_lock.acquire()
...write to a file...
# Release the lock
file_lock.release()
```

* You can use the following script to create your threads.

```python
import threading

# List of thread IDs to create
thread_ids = [0, 1, 2, 3]

# List to hold the created thread objects
threads = []

# Iterate over each thread ID
for thread_id in thread_ids:
  
    # Create a new thread to run the generate_phrase_and_save function
    # Pass the thread ID as an argument to the function
    thread = threading.Thread(target=generate_phrase_and_save, args=(thread_id,))
    
    # Append the created thread to the list of threads
    threads.append(thread)
    
    # Start the thread, beginning its execution
    thread.start()

# Wait for all threads to finish
for thread in threads:
  
    # Join each thread, ensuring that the main thread waits for their completion
    thread.join()
```

