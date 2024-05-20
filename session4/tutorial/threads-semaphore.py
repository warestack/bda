import concurrent.futures
import threading
import time

semaphore = threading.Semaphore(2)
n = 5

def do_something(i):
    print("In something thread",i)
    time.sleep(1)

def worker(thread_id):
    semaphore.acquire()
    print(f"Thread {thread_id} is working")
    time.sleep(1)
    print(f"Thread {thread_id} is done")
    semaphore.release()

with concurrent.futures.ThreadPoolExecutor(max_workers=n) as executor:
    futures1 = [executor.submit(do_something, i) for i in range(n)]
    futures2 = [executor.submit(worker, i) for i in range(n)]
    # for future in concurrent.futures.as_completed(futures):
    #     future.result()
