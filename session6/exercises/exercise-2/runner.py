from tools import *
import time
from concurrent.futures import ThreadPoolExecutor


def load_txt_to_tuples(file_path):
    tuples_list = []
    with open(file_path, 'r') as file:
        for line in file:
            # Strip whitespace and split the line by commas
            parts = line.strip().split(', ')
            # Convert the parts to a tuple, ensuring proper types (int, str, str)
            tuple_item = (int(parts[0]), parts[1], parts[2])
            # Append the tuple to the list
            tuples_list.append(tuple_item)
    return tuples_list


def main():
    data = load_txt_to_tuples('data_small.txt')
    print("Data is loaded")
    t1 = time.perf_counter()
    for i in data:
        fetch_currency_conversion(i)
    t2 = time.perf_counter()
    print(f'Serial finished in {t2-t1} seconds')

    t1 = time.perf_counter()
    with ThreadPoolExecutor() as executor: # max_workers=1000
        executor.map(fetch_currency_conversion, data)

    t2 = time.perf_counter()
    print(f'Threads finished in {t2-t1} seconds')

if __name__ == "__main__":
    main()