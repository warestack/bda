### Lab 2 Questions

1. Download the `rockyou.txt` file
   - Visit [Kaggle](https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt?resource=download), log in, and download the dataset.
   - Use the following script to open the file and load its contents into a list of lines.

```python
with open("rockyou.txt", "r", encoding="latin-1") as file:
    lines = file.readlines()
```

> Time: O(n) – reads all lines once  
> Space: O(n) – stores all lines in memory

---

2. Print the first 5 lines from the file

```python
with open("rockyou.txt", "r", encoding="latin-1") as file:
    lines = file.readlines()

count = 0
for line in lines:
    print(line, count)
    if count == 4:
        break
    count += 1
```

> Time: O(5) ≈ O(1)  
> Space: O(n) – entire file loaded in memory

---

3. Use `strip()` to remove extra whitespace (like newlines) from each line

```python
with open("rockyou.txt", "r", encoding="latin-1") as file:
    lines = file.readlines()

count = 0
for line in lines:
    print(line.strip())
    if count == 4:
        break
    count += 1
```

> Time: O(5)  
> Space: O(n)

---

4. Define a linear search function in `fun.py`

```python
def linear_search(alist, key):
    for item in alist:
        if item == key:
            return True
    return False
```

> Time: O(n) – worst case when key is not found  
> Space: O(1)

---

5. Move the file reading logic into a reusable function

```python
def read_txt(afile):
    with open(afile, "r", encoding="latin-1") as file:
        return file.readlines()
```

> Time: O(n)  
> Space: O(n)

---

6. Use the `main` block to test functions when running `lab2.py` directly

```python
if __name__ == "__main__":
    print(fun.linear_search(lines, "iloveyou\n"))
```

> Purpose: prevents code from executing when the script is imported elsewhere

---

7. Print only the first `x` items in a list

```python
def my_head(alist, x):
    count = 0
    for item in alist:
        print(item)
        count += 1
        if count == x:
            break
```

> Time: O(x)  
> Space: O(1)

---

8. Count how many records (lines) exist in the list

```python
def my_len(alist):
    count = 0
    for item in alist:
        count += 1
    return count
```

> Time: O(n)  
> Space: O(1)

---

9. Count how many items in the list contain only digits

```python
def count_string_digits(alist):
    count = 0
    for item in alist:
        if item.strip().isdigit():
            count += 1
    return count
```

> Time: O(n)  
> Space: O(1)

---

10. Check for duplicate entries using a set

```python
def has_duplicates(data):
    seen = set()
    for item in data:
        item = item.strip()
        if item in seen:
            return True
        seen.add(item)
    return False
```

> Time: O(n)  
> Space: O(n)

---

11. Check for duplicates using nested loops (inefficient)

```python
def has_duplicates_quadratic(data):
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i].strip() == data[j].strip():
                print("Duplicate found:", data[i].strip())
                return True
    print("No duplicates found.")
    return False
```

> Time: O(n²)  
> Space: O(1)

---

12. Measure the execution time of code using `time`

```python
import time

start = time.time()
# code to measure
end = time.time()

print("Execution time:", end - start)
```

> Time: O(1)  
> Space: O(1)

---

13. Write a function called `bubble_sort` that takes a list of passwords and sorts it in ascending order using the Bubble Sort algorithm.

```
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

13. Sort the list in-place and print the first 5 items

```python
lines.sort()
fun.my_head(lines, 5)
```

> Time: O(n log n)  
> Space: O(1) in-place

---

14. Binary search function for sorted lists

```python
def binary_search(alist, key):
    low = 0
    high = len(alist) - 1

    while low <= high:
        mid = (low + high) // 2
        if alist[mid] == key:
            return True
        elif alist[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return False
```

> Time: O(log n)  
> Space: O(1)

---

15. Create a frequency dictionary to count occurrences

```python
def frequency_dict(data):
    freq = {}
    for item in data:
        item = item.strip()
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq
```

> Time: O(n)  
> Space: O(n)

---

16. Find the most frequent item in a frequency dictionary

```python
def get_most_frequent(freq_dict):
    max_key = None
    max_value = 0

    for key in freq_dict:
        if freq_dict[key] > max_value:
            max_value = freq_dict[key]
            max_key = key

    return max_key, max_value
```

> Time: O(n)  
> Space: O(1)
