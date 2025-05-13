### Lab 3: CSV Analysis with Python (Netflix Dataset)

**Learning goals:**

* Load and parse CSV files using Python.
* Build custom reusable functions to process tabular data.
* Use generators with `yield` to write memory-efficient code.
* Filter and analyze records from a dataset using conditional logic.
* Create summaries, counters, and frequency tables using `for` loops and dictionaries.
* Perform basic sorting, aggregation, and statistical operations manually.

---

1. **Load the data in Python as a dictionary.**

Read the CSV data into a list of dictionaries, for later usage.

```python
import csv

with open('netflix_titles.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

print(data[1])
```

**Here is the function implemenation.**

```python
import csv

def load_data(filename):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

netflix_data = load_data('netflix_titles.csv')
print(netflix_data[0])  # Print first entry
```

**Time Complexity**: `O(n·m)`

- Opening file: `O(1)`
- Reading file line by line: `O(n)`, where n is the number of rows (excluding the header)
- Parsing each row into a dictionary: `O(n·m)`, where m is the number of columns (fields)
  - Each field is mapped to a key, so constructing a dict is `O(m)`
- List comprehension to store all rows: `O(n)`

**Space Complexity**: `O(n·m)`

* Data stores all n rows in memory
* Each row is a dictionary with m key-value pairs

------

2. **Create a function called `my_head(alist,limit)` to return the `n` first records of the dataset in a new list.**

```python
def my_head(alist, limit):
    for i in range(limit):
        if i < len(alist):
            yield alist[i]
        else:
            break

# Example usage:
for item in my_head(netflix_data, 5):
    print(item)
```

**Why use `yield`?**

- You get one item at a time (no list built in memory).
- It’s more efficient when you only need a few items from a large list or stream.
- Works well in pipelines or streaming scenarios.

Time Complexity: `O(k)` where `k = min(limit, len(alist))`

Space complexity: `O(1)` — Just one item is in memory at any moment

---

3. **Create a function called `my_head_col(alist,col,limit)`  to return the first records of a sepcific column from the dataset as a list.**

```python
def head_col(alist,col,limit):
  return_data=[]
  for i in alist:
    if limit==0:
      break
    return_data.append(i[col])
    limit-=1
  return return_data

head_col(data,"title",5)
```

Time complexity: `O(n)` — worst case limit is the amount of data

Space Complexity: `O(k)` where `k = limit`  (You’re storing `limit` values, not `n`)

---

4. **Filters `titles` added in the year `2021`.**

**Develop a function for `shows_added_in_2021(data)` for `titles` from United States**

* **Solution with `return`**

```python
def shows_added_in_year(data,col,year):
    result = []
    for row in data:
        if year in row['date_added']:
            result.append(row[col])
    return result
 
shows_added_in_year(data,'title','2021')
```

Time complexity: `O(n)` — where `n` is the number of rows in `data`

Space complexity: `O(n)` — builds and stores a list of up to `limit` values in memory.

* **Solution with `yield`**

```python
def shows_added_in_year(data, col, year):
    for row in data:
        if year in row['date_added']:
            yield row[col]
            
for title in shows_added_in_year(data, 'title', '2021'):
    print(title)
```

**Why use `yield`?**

- **Time Complexity**: `O(n)` — same as the original.
- **Space Complexity**: `O(1)` — only one matching item is held in memory at a time.

---

6. **Develop a function for `shows_added_in_2021(data)` for `titles` from United States**

Lists titles where country is `United States`.

* **Solution with `return`**

```python
def shows_added_in_2021(data):
    result = []
    for row in data:
        if '2021' in row['date_added']:
            result.append(row['title'])
    return result
```

Complexities are the same as 5 `return`.

* **Solution with `yield`**

```python
def shows_added_in_2021(data):
    for row in data:
        if '2021' in row['date_added']:
            yield row['title']
for title in shows_added_in_2021(data):
    print(title)
```

**Complexity**

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` — yields one item at a time, no list built in memory.

---

7. **Titles with `love` (any case).**

Searches for titles containing the word `love` (case-insensitive).

* **Solution with `return`**

```python
def titles_with_blood(data):
    result = []
    for row in data:
        if 'love' in row['title'].lower():
            result.append(row['title'])
    return result
```

* **Solution with `yield`**

```python
def titles_with_love(data):
    for row in data:
        if 'love' in row['title'].lower():
            yield row['title']
for title in titles_with_love(data):
    print(title)
```

Time: `O(n·m)` — where `n` is the number of rows and `m` is the average length of each title (`lower()` and `'blood' in ...` are O(m) string operations per row).

Space: `O(n)` — where `n` is the number of matching titles that contain "love".

---

8. **PG-13 Movies**

Finds all movies with a `PG-13` rating.

* **Solution with `return`**

```python
def pg13_movies(data):
    result = []
    for row in data:
        if row['rating'] == 'PG-13' and row['type'] == 'Movie':
            result.append(row['title'])
    return result
```

**Time Complexity: `O(n)`**

- The function loops over all `n` rows in the dataset once.
- Each condition check and append operation is constant time.

 **Space Complexity: `O(k)`**

- Where `k` is the number of matching entries (`PG-13` movies).
- The function builds a list containing only the matches.

* **Solution with `yield`**

```python
def pg13_movies(data):
    for row in data:
        if row['rating'] == 'PG-13' and row['type'] == 'Movie':
            yield row['title']
for title in pg13_movies(data):
    print(title)

```

**Time Complexity: `O(n)`**

- Loops through each of the `n` rows in `data`.
- Performs constant-time comparisons and yields matches.
- Same as the list version.

**Space Complexity: `O(1)`**

- **Does not** store results in a list.
- Only holds **one matching title in memory at a time**.

---

9. **Develop the `my_len` function, to count the total entries**

Counts the number of rows in the dataset.

```python
def my_len(alist):
  count=0
  for i in alist:
    count+=1
  return count

my_len(data)
```

**Can I use yield?**

No, you **should not use `yield`** for `my_len`, because:

- `yield` is used to **produce values one-by-one**
- `my_len` is a function that returns a **single final count**, not a stream

**Time Complexity: `O(n)`**

- The loop runs once for every element in `alist`
- Simple increment per item → linear time

 **Space Complexity: `O(1)`**

- Only one variable (`count`) is used for tracking
- No new data structures are created or stored

---

10. **Count Types**

Counts how many entries are `TV Show` vs. `Movie`.

```python
def count_types(data):
    tv, movie = 0, 0
    for row in data:
        if row['type'] == 'TV Show':
            tv += 1
        elif row['type'] == 'Movie':
            movie += 1
    return {'TV Show': tv, 'Movie': movie}
```

**Time Complexity: `O(n)`**

- The function loops over all `n` rows in the dataset.
- Each comparison and increment is constant time → total is linear.

 **Space Complexity: `O(1)`**

- Only two counters (`tv` and `movie`) are maintained.
- The final result is a fixed-size dictionary with two keys.

------

11. **Count Per Category**

Generate a frequency table

```python
def count_type_frequency(data):
    type_counts = {}
    for row in data:
        content_type = row["type"]
        if content_type in type_counts:
            type_counts[content_type] += 1
        else:
            type_counts[content_type] = 1
    return type_counts

# Example usage
frequency = count_type_frequency(data)
```

**Time Complexity: `O(n)`**

- The function iterates over all `n` rows once.
- Dictionary operations (`in`, `+= 1`, assignment) are on average **O(1)**.
- So the total time is **O(n)**.

**Space Complexity: `O(t)`**, where `t` is the number of unique content types

- A dictionary `type_counts` is built with one entry per unique type (e.g., "Movie", "TV Show", etc.).
- In practice, `t` is small, so this is often treated as **O(1)**.

---

12. **Average TV show seasons**

Calculates average number of seasons for TV shows.

```python
def average_tv_seasons(data):
    total, count = 0, 0
    for row in data:
        if row['type'] == 'TV Show' and 'Season' in row['duration']:
            try:
                total += int(row['duration'].split()[0])
                count += 1
            except:
                continue
    return total / count if count else 0
```

**Time Complexity: `O(n)`**

- Iterates through all `n` rows.
- For each row, it performs:
  - A string check (`'Season' in row['duration']`) → O(1)
  - A string split and conversion to `int()` → O(1)
- All operations inside the loop are constant time → **O(n)** overall.

**Space Complexity: `O(1)`**

- Only two variables (`total`, `count`) are used.
- No new data structures or collections are created.

---

13. Sort by release year using `Bubble sort`.

```python
def sort_by_release_year(data):
    sorted_data = data[:]  # Copy to avoid modifying the original
    n = len(sorted_data)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            year_j = int(sorted_data[j]['release_year'])
            year_next = int(sorted_data[j + 1]['release_year'])
            if year_j > year_next:
                sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]
    
    return [row['title'] for row in sorted_data]
```

**How Bubble Sort Works:**

- Repeatedly compares adjacent elements
- Swaps them if they're in the wrong order
- "Bubbles" the largest value to the end in each pass

Time complexity: `O(n^2)`

Space complexity: `O(n)` — due to copying the list

---

14. **Convert durations**

The function extracts numeric values from the `"duration"` field and groups them into a dictionary based on units like `"min"`, `"Season"`, or `"Seasons"`. It skips empty or malformed entries.

*It works on a list of dictionaries where each dictionary has a `'duration'` key.*

```python
def group_durations(data):
    result = {}
    for row in data:
        duration = row.get('duration', '').strip()
        if not duration:
            continue
        parts = duration.split()
        if len(parts) != 2:
            continue
        num, unit = parts
        try:
            num = int(num)
        except ValueError:
            continue
        if unit not in result:
            result[unit] = []
        result[unit].append(num)
    return result


group_durations(netflix_data)
```

**Output**

```python
{
    "min": [90, 91, 125, 104, 127, 91,...],
    "Seasons": [2, 2, 9,..],
    "Season": [1, 1, 1, 1, 1,...]
}
```

---

15. **What is the distribution of content types (TV Show vs Movie)?**

Create a **bar chart** showing how many titles fall into each type.

```python
import matplotlib.pyplot as plt

def plot_type_distribution(data):
    # Count how many of each type (e.g., Movie, TV Show)
    type_counts = {}
    for row in data:
        typ = row["type"]
        if typ in type_counts:
            type_counts[typ] += 1
        else:
            type_counts[typ] = 1

    # Plot using matplotlib
    plt.figure(figsize=(6, 4))
    plt.bar(type_counts.keys(), type_counts.values())
    plt.title("Distribution of Content Types")
    plt.xlabel("Type")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

# Call the function on your dataset
plot_type_distribution(data)
```

![Bar chart](bar-chart.png)