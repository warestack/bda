import requests,time
from concurrent.futures import ThreadPoolExecutor
from tools import *

img_urls = load_data('image_urls.txt')

t1 = time.perf_counter()

with ThreadPoolExecutor() as executor: # max_workers=1000
    executor.map(get_img, img_urls)

t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')