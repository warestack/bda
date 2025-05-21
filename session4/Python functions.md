### Python functions

Let's explore all common ways to define a `sum_of_2` function in Python, focusing on different combinations of:

- Positional arguments
- Default values
- Keyword arguments
- Dictionary unpacking

1. Basic positional arguments

```python
def sum_of_2(a, b):
    return a + b

# Usage
print(sum_of_2(3, 5))  # 8
```

2. With default values

```python

def sum_of_2(a=0, b=0):
    return a + b

# Usage
print(sum_of_2())         # 0
print(sum_of_2(2))        # 2 (b=0)
print(sum_of_2(2, 3))     # 5
```

3. Named parameters with defaults

```python
def sum_of_2(num1=0, num2=0):
    return num1 + num2

# Usage
print(sum_of_2(num1=5, num2=10))  # 15
```

4. Using `\*args` (positional arguments tuple)

```
def sum_of_2(*args):
    return sum(args[:2])  # Only sum the first two

# Usage
print(sum_of_2(1, 2))         # 3
print(sum_of_2(1, 2, 3, 4))   # 3 (ignores extra)
```

5. Using `\**kwargs` (keyword arguments dict)

```python
def sum_of_2(**kwargs):
    return kwargs.get("a", 0) + kwargs.get("b", 0)

# Usage
print(sum_of_2(a=4, b=6))  # 10
print(sum_of_2())          # 0
```

6. Accepting a dictionary as a single argument

```
def sum_of_2(input_dict):
    return input_dict.get("a", 0) + input_dict.get("b", 0)

# Usage
print(sum_of_2({"a": 5, "b": 7}))  # 12
```

7. Unpacking a dictionary into parameters

```python
def sum_of_2(a=0, b=0):
    return a + b

# Usage
params = {"a": 2, "b": 3}
print(sum_of_2(**params))  # 5
```

8. Function with input type checking

```python
def sum_of_2(a=0, b=0):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Inputs must be numbers.")
    return a + b
```

---

### Summary Table

| Pattern                                | Example Call                   |
| -------------------------------------- | ------------------------------ |
| `def sum_of_2(a, b)`                   | `sum_of_2(1, 2)`               |
| `def sum_of_2(a=0, b=0)`               | `sum_of_2()`, `sum_of_2(1)`    |
| `def sum_of_2(**kwargs)`               | `sum_of_2(a=1, b=2)`           |
| `def sum_of_2(input_dict)`             | `sum_of_2({"a": 1, "b": 2})`   |
| `def sum_of_2(*args)`                  | `sum_of_2(1, 2, 3)`            |
| `def sum_of_2(a, b=0)`                 | `sum_of_2(5)`                  |
| `def sum_of_2(**kwargs)` + default     | `sum_of_2()`                   |
| `def sum_of_2(a=0, b=0)` + dict unpack | `sum_of_2(**{"a": 2, "b": 3})` |



------