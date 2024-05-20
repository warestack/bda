import threading
import time

counter = 0
lock = threading.Lock() # mutex

def do_something(i):
    print("In something thread",i)
    time.sleep(1)

def increment_counter():
    global counter
    lock.acquire()
    counter += 1
    lock.release()

threads1 = []
threads2 = []

for i in range(3):
    thread1 = threading.Thread(target=do_something, args=[i])
    thread2 = threading.Thread(target=increment_counter)

    threads1.append(thread1)
    threads2.append(thread2)
    thread1.start()
    thread2.start()

for thread in threads1:
    thread.join()

for thread in threads2:
    thread.join()

print(f"Final counter value: {counter}")
