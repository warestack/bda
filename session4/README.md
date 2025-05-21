### Python dictionaries recap

A **dictionary** is a **collection of key-value pairs**. Think of it like a real dictionary: a word (key) maps to a definition (value).

#### Creating a Dictionary

1. Using `{}`:

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "London"
}
```

2. Using `dict()`:

```python
person = dict(name="Alice", age=25, city="London")
```

#### Accessing Dictionary Values

```python
print(person["name"])  # Alice

# Safer way to access (avoids KeyError)
print(person.get("job", "Not found"))  # Not found
```

#### Modifying a Dictionary

1. Add a new key-value pair:

```python
person["job"] = "Engineer"
```

2. Update an existing value:

```python
person["age"] = 26
```

3. Removing Items

```python
del person["city"]          # Remove by key
job = person.pop("job")     # Remove and get value
person.clear()              # Empty the dictionary
```

#### Looping Through a Dictionary

```python
for key in person:
    print(key)  # Print keys

for value in person.values():
    print(value)  # Print values

for key, value in person.items():
    print(f"{key}: {value}")  # Key-value pairs
```

#### Dictionary Length

```python
print(len(person))  # Number of key-value pairs
```

#### Nested Dictionaries

```python
students = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 22}
}

print(students["student1"]["name"])  # Alice
```

#### Useful Dictionary Methods

| Method          | Description                               |
| --------------- | ----------------------------------------- |
| `dict.get(key)` | Returns value or default if key not found |
| `dict.keys()`   | Returns all keys                          |
| `dict.values()` | Returns all values                        |
| `dict.items()`  | Returns list of (key, value) tuples       |
| `dict.update()` | Adds or updates key-value pairs           |
| `dict.pop(key)` | Removes and returns a value by key        |

#### Tips

- Keys must be immutable (string, number, tuple).
- Values can be any type (string, list, dict, etc.).
- Keys are unique—you can’t have duplicates.

---

#### How do they work?

Python dictionaries are implemented using a hash table under the hood. This means they map each key to a location in memory using a hash function.

> A hash table is a data structure that stores key-value pairs and allows fast access to values using keys — usually in O(1) time on average.
>
> * Hash Function: Converts a key (like "name") into a number (called a hash).
>
> * Indexing: That number points to a specific location (bucket) in memory.
>
> * Storage: The value is stored in that bucket with its key.
>
> ```python
> d = {"name": "Alice"}
> ```
>
> Behind the scenes:
>
> - `"name"` is hashed to an index (e.g., `42`)
> - `"Alice"` is stored at index `42`
>
> What If Two Keys Hash to Same Index?
>
> This is called a collision. Python handles it using a method like open addressing or chaining.

#### Common Dictionary Operations & Their Complexity

| Operation          | Average Case | Worst Case | Description                    |
| ------------------ | ------------ | ---------- | ------------------------------ |
| `d[key]`           | O(1)         | O(n)       | Lookup a value by key          |
| `d[key] = value`   | O(1)         | O(n)       | Insert or update a key         |
| `del d[key]`       | O(1)         | O(n)       | Delete a key-value pair        |
| `key in d`         | O(1)         | O(n)       | Check if key exists            |
| Iterating over `d` | O(n)         | O(n)       | Loop through keys/values/items |

#### Why Worst Case is O(n)?

In very rare cases, Python's hash table might:

- Have many hash collisions
- Degenerate into scanning a list (like a backup plan)

Example: If many keys hash to the same location (bad luck or deliberate attack), the performance drops to O(n). But Python handles this very well in practice.

#### What Makes Dictionaries So Fast?

- Hash tables give nearly constant-time access.
- Python optimizes memory layout, caching, and resizing.
- In Python 3.6+, dictionaries preserve insertion order, but it doesn’t affect time complexity.

```python
# Lookup (O(1) average)
d = {"a": 1, "b": 2, "c": 3}
print(d["b"])  # Fast

# Insertion (O(1) average)
d["d"] = 4

# Deletion (O(1) average)
del d["a"]
```

