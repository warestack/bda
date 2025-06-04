```
import requests, os

def fetch_and_save_dog_image(index):
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)

    if response.status_code == 200:
        image_url = response.json()['message']
        print(f"[{index}] Downloading 🐕: {image_url}")

        # Extract filename from URL
        filename = f"{index}_" + os.path.basename(image_url)

        # Download the image content
        image_data = requests.get(image_url).content

        # Save to file
        with open(filename, 'wb') as file:
            file.write(image_data)

        print(f"[{index}] Image saved as: {filename}")
    else:
        print(f"[{index}] Failed to fetch dog image.")

semaphore = Semaphore(2)

def fetch_and_save_dog_image_semaphore2(index):
    semaphore.acquire()
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)

    if response.status_code == 200:
        image_url = response.json()['message']
        print(f"[{index}] Downloading 🐕: {image_url}")

        # Extract filename from URL
        filename = f"{index}_" + os.path.basename(image_url)

        # Download the image content
        image_data = requests.get(image_url).content

        # Save to file
        with open(filename, 'wb') as file:
            file.write(image_data)

        print(f"[{index}] Image saved as: {filename}")
    else:
        print(f"[{index}] Failed to fetch dog image.")
    semaphore.release()
# Task 1: Download 4 photos serial runner /time required
import time
def serial_runner(indexes):
    start = time.time()
    for i in indexes:
        fetch_and_save_dog_image(i)
    end = time.time()
    return end-start
from concurrent.futures import ThreadPoolExecutor

# Task 2: Download 4 photos parallel runner /time required
def parallel_runner(indexes):
    start = time.time()
    with ThreadPoolExecutor() as executor:
        executor.map(fetch_and_save_dog_image, indexes)
    end =time.time()
    return end-start   

from concurrent.futures import Semaphore
# Task 3: Download only 2 photos at a time (in parallel)
def parallel_runner_limit2(indexes):
    start = time.time()
    # Limit - Semaphore
    semaphore = Semaphore(2)

    def limited_fetch(i):
        with semaphore:
            fetch_and_save_dog_image(i)

    with ThreadPoolExecutor as executor:
        executor.map(limited_fetch, indexes)

    end = time.time()
    return end-start

if __name__ == '__main__':
    indexes = range(400) # [0,1,2,3]
    serial_runner(indexes)
    parallel_runner(indexes)
    parallel_runner_limit2(indexes)
```

