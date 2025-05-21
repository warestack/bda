#### Building our library

1. This Python code defines a function called `load_csv_from_dict` that reads data from a CSV file whose filename is passed inside a dictionary. The function returns the data as a list of dictionaries.

**Input:**

	- The function expects a dictionary like this:	

```python
{"data": "filename.csv"}
```

**Checks:**

	- If the "data" key is missing, it raises a ValueError.
	- If the file does not exist, it catches the FileNotFoundError and prints an error message.

**Reading the File:**

* It opens the CSV file using Python’s csv.DictReader.

* Each row in the CSV is converted into a dictionary (using the header row as keys).

* All rows are added to a list.

**Output:**

* The function returns a list of dictionaries, one for each row in the CSV file.

```python
import csv

def load_csv_from_dict(input_dict):
    """
    Load data from a CSV file specified in a dictionary.

    Args:
        input_dict (dict): A dictionary containing the key "data" with the CSV filename as a string.
            Example: {"data": "people.csv"}

    Returns:
        list[dict]: A list of dictionaries, where each dictionary represents a row from the CSV file.
                    Keys are the column headers, and values are strings by default.

    Raises:
        ValueError: If the "data" key is missing from the input dictionary.
        FileNotFoundError: If the specified file does not exist.

    Example:
        input_data = {"data": "people.csv"}
        rows = load_csv_from_dict(input_data)
        for row in rows:
            print(row)
    """
    
    filename = input_dict.get("data")
    
    if not filename:
        raise ValueError("No 'data' key provided in the input dictionary.")
    
    data_rows = []
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_rows.append(row)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    
    return data_rows
```

*Usage example*

```python
input_data = {"data": "netflix_titlses.csv"}
rows = load_csv_from_dict(input_data)

for row in rows:
    print(row)
```

2. The `load_csv_generator_from_dict` function is a memory-efficient CSV reader that loads rows one at a time using a Python generator.

```python
import csv

def load_csv_generator_from_dict(input_dict):
  
    filename = input_dict.get("data")

    if not filename:
        raise ValueError("No 'data' key provided in the input dictionary.")

    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                yield row
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return  # Ends the generator silently
```

*Example usage*

```python
input_data = {"data": "netflix_titles.csv"}

for row in load_csv_generator_from_dict(input_data):
    print(row)  # Prints one dictionary per row in the CSV
```

3. Print the first two rows using the `load_csv_generator_from_dict`  function.

```python
def preview_csv_rows(input_dict, n=2):
    """
    Prints the first n rows from a CSV file using a generator.

    Args:
        input_dict (dict): Dictionary with the key "data" pointing to the CSV file path.
        n (int): Number of rows to preview (default is 2).

    Returns:
        None
    """
    row_count = 0
    for row in load_csv_generator_from_dict(input_dict):
        print(row)
        row_count += 1
        if row_count == n:
            break
 
input_data = {"data": "netflix_titles.csv"}
preview_csv_rows(input_data, n=2)
```

4. Stream only movies.

```python
def stream_movies(input_dict):
    """
    Yields rows from the Netflix data where type is 'Movie'.
    """
    for row in load_csv_generator_from_dict(input_dict):
        if row.get("type") == "Movie":
            yield row
            
input_data = {"data": "netflix_titles.csv"}

for movie in stream_movies(input_data):
    print(movie["title"])
    break  # Just show the first movie
```

5. Yield titles from a specific country.

```python
def titles_by_country(input_dict, country_name):
    """
    Yields titles where 'country' matches the given country_name.
    """
    for row in load_csv_generator_from_dict(input_dict):
        country = row.get("country", "")
        if country_name.lower() in country.lower():
            yield row.get("title", "Unknown Title")

input_data = {"data": "netflix_titles.csv"}

for title in titles_by_country(input_data, "South Africa"):
    print(title)
    break  # Show only the first match
```

6. Yield titles in batches (e.g., for paging)

```python
def batched_titles(input_dict, batch_size):
    """
    Yields titles in batches of a specified size.
    """
    batch = []
    for row in load_csv_generator_from_dict(input_dict):
        batch.append(row.get("title", "Unknown Title"))
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch  # Yield remaining titles
input_data = {"data": "netflix_titles.csv"}

for batch in batched_titles(input_data, 3):
    print("Batch:", batch)
    break  # First batch only
```

**Why is this useful?**

| Task                      | Benefit of `yield`               |
| ------------------------- | -------------------------------- |
| Filter by type or country | Memory-efficient, on-the-fly     |
| Paginate titles           | Avoids full list storage         |
| Combine multiple filters  | Easy to layer logic with `yield` |

**TIme and Space analysis**

| Task                              | Time Complexity | Space Complexity | Explanation                                                  |
| --------------------------------- | --------------- | ---------------- | ------------------------------------------------------------ |
| `load_csv_from_dict`              | O(n × m)        | O(n × m)         | Reads all rows and stores all fields in memory. Each of the `n` rows contains `m` fields. |
| `load_csv_generator_from_dict`    | O(n × m)        | O(m)             | Reads one row at a time. Each row has `m` columns, held temporarily in memory. |
| `preview_csv_rows`                | O(m) × 2 = O(m) | O(m)             | Only reads 2 rows; each row has `m` columns.                 |
| `stream_movies`                   | O(n × m)        | O(m)             | Filters each row (checks `"type"`), holding only one row at a time. |
| `titles_by_country`               | O(n × m)        | O(m)             | Each row is read and filtered based on the `"country"` field. |
| `batched_titles` (batch size `b`) | O(n × m)        | O(b)             | Rows are read and accumulated in batches of `b` titles. Each title string uses O(1) space. |

**When to use `yield`**

| Task                      | Use `yield`? | Why?                                                         |
| ------------------------- | ------------ | ------------------------------------------------------------ |
| **Search / Filter**       | ✅ Yes        | You can stop early when you find what you need (e.g. first match). |
| **Streaming large files** | ✅ Yes        | Keeps memory usage low — you don't load everything.          |
| **Iterate lazily**        | ✅ Yes        | You only use the rows/items you need.                        |
| **Pagination / batching** | ✅ Yes        | Return one chunk at a time, good for UI/data pipelines.      |
| **Real-time data**        | ✅ Yes        | Ideal for live or infinite sources (e.g. log readers, sensors). |

**When not to use `yield`**

| Task                           | Use `yield`? | Why Not?                                                     |
| ------------------------------ | ------------ | ------------------------------------------------------------ |
| **Count total rows**           | ❌ No         | You must go through the entire file; better to return a final value. |
| **Summarize all data**         | ❌ No         | You need the full dataset to calculate summary statistics.   |
| **Sort all rows**              | ❌ No         | Sorting needs all data in memory first.                      |
| **Build a complete structure** | ❌ No         | You want a final list, dict, or dataframe.                   |
| **Export or write all data**   | ❌ No         | You need everything loaded before writing.                   |

**`return` vs `yield`**

* Goal: Count how many movies and TV shows are in the dataset.

This is a classic summary/aggregation task — you want a final count, not individual rows.

* Correct Way (No `yield` — just compute and return)

```python
def count_types(input_dict):
    """
    Returns a summary count of how many Movies and TV Shows are in the dataset.
    """
    counts = {"Movie": 0, "TV Show": 0}
    for row in load_csv_generator_from_dict(input_dict):
        type_ = row.get("type")
        if type_ in counts:
            counts[type_] += 1
    return counts
```

* Example Usage

```python
input_data = {"data": "netflix_titles.csv"}
summary = count_types(input_data)
print(summary)  # Example output: {'Movie': 4265, 'TV Show': 1971}
```

**Why `yield` doesn’t work here?**

* If you tried to write this with `yield`, you'd run into trouble. Here's what it might (wrongly) look like:

```python
def yield_type_counts(input_dict):
    """
    Incorrect: This only yields rows — it does not summarize!
    """
    for row in load_csv_generator_from_dict(input_dict):
        yield row.get("type")  # just streams each type
```

*Usage*

```python
for item in yield_type_counts(input_data):
    print(item)
```

**Problem**

- This just gives you `"Movie"`, `"TV Show"`, `"Movie"`, etc., one by one.
- You cannot compute the total inside the generator, unless you do it outside by collecting all values — which defeats the purpose of `yield`.

| Task                          | Use `yield`? | Why / Why Not                                             |
| ----------------------------- | ------------ | --------------------------------------------------------- |
| Count all Movies and TV Shows | ❌ No         | You need a total count — requires full pass + final value |
| Stream only movies            | ✅ Yes        | You can filter row-by-row, stop early, low memory         |

