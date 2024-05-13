import time
import concurrent.futures

def sum_square(number):
    s = 0
    for i in range(number):
        s += i * i
    return s
    
def serial_runner2():
    start=time.perf_counter()
    for i in range(20000):
        sum_square(i)
    end=time.perf_counter()
    print(f'Serial: {end-start} second(s)')

def parallel_runner5():
    start=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(sum_square, range(20000))
    end=time.perf_counter()
    print(f'Parallel (process poolmap): {end-start} second(s)')

def parallel_runner6():
    start=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        executor.map(sum_square, range(20000))
    end=time.perf_counter()
    print(f'Parallel (process poolmap - 2): {end-start} second(s)')

if __name__ == '__main__':
    serial_runner2()
    parallel_runner5()
    parallel_runner6()