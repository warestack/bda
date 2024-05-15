import time, os
from multiprocessing import Pool
import concurrent.futures
import multiprocessing
from img_processor import *

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]

def serial_runner():
    start=time.perf_counter()
    for i in img_names:
        process_image(i)
    end=time.perf_counter()
    print(f'Serial: {round(end-start,2)} second(s)')

def parallel_process_executor():
    start=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image, img_names)
    end=time.perf_counter()
    print(f'Parallel (ProcessPoolExecutor): {round(end-start,2)} second(s)')

def parallel_pool():
    start=time.perf_counter()
    with multiprocessing.Pool() as p:
        p.map(process_image, img_names)
    end=time.perf_counter()
    print(f'Parallel (Map): {round(end-start,2)} second(s)')

if __name__ == '__main__':
    os.makedirs('processed', exist_ok=True)
    serial_runner()
    parallel_process_executor()
    parallel_pool()