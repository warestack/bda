import time, threading

def foo():
    print("In foo...")
    print("Running...")
    time.sleep(1)

def serial_runner():
    start =time.perf_counter()
    for _ in range(3):
        foo()
    end = time.perf_counter()
    print(f'Serial: {end - start} second(s)')

def parallel_runner():
    start =time.perf_counter()

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
    parallel_runner()