### BDA Seminar 1 - Part 1 & 2

**Complete the following exercises on computational complexity.**

1. Study the following script. This program implements a `linear_search(arr, x)` function that returns element `x`'s index in the list `arr`. If `x` is not found, it returns `-1`.

```python
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
```

2. Now, let's put your understanding to the test. Can you determine the time complexity of the following script? Take a moment to think about it.

```Py
if __name__ == "__main__":
  data = [10,20,30,40,50,50,60,80,90,100]
  result = linear_search(data,40)
  print(result)
```

| Provide your answer here. |
| ------------------------- |
|                           |

3. What is the space complexity of the above script?

| Provide your answer here. |
| ------------------------- |
|                           |

4. Is this a computationally or data-intensive task?

| Provide your answer here. |
| ------------------------- |
|                           |

> [!TIP]
>
> Start using the conditional statement when creating programs. `if __name__ == "__main__"`
>
> This block often includes test code, demonstration code, or main application logic that you don't want to run if the file is imported as a module in another script.

5. What is the time complexity of the following code?

```python
if __name__ == "__main__":
  data = [10,20,30,40,50,50,60,80,90,100]
  print(data[-1])
```

| Provide your answer here. |
| ------------------------- |
|                           |

6. What is the time complexity of the following code?

```python
def get_it(arr):
    for i in arr:
      return i

if __name__ == "__main__":
  data = [10,20,30,40,50,50,60,80,90,100]
  print(get_it(data))
```

| Provide your answer here. |
| ------------------------- |
|                           |

7. What is the time complexity of the following code?

```python
def sum_elements(arr):
    total = 0
    for num in arr:
        total += num
    return total

if __name__ == "__main__":
  data = [10,20,30,40,50,50,60,80,90,100]
  print(sum_elements(data))
```

| Provide your answer here. |
| ------------------------- |
|                           |

8. Is this a computationally or data-intensive task?

| Provide your answer here. |
| ------------------------- |
|                           |

9. What is the time complexity of the following code?

```python
def count_lines(filename):
  count=0
  with open(filename, 'r') as file:
    for line in file:
      count+=1
            
  return count

if __name__ == "__main__":
  filename = 'file1.txt'
  try:
      counts = count_lines(filename)
      print("Line counts:", counts)
  except FileNotFoundError:
      print("File not found")
```

| Provide your answer here. |
| ------------------------- |
|                           |

> [!IMPORTANT]
>
> ❗To execute the script, ensure that the `file1.txt` is in the same directory as your Python script.

10. What is the space complexity of the above code?

| Provide your answer here. |
| ------------------------- |
|                           |

11. Is this a computationally or data-intensive task?

| Provide your answer here. |
| ------------------------- |
|                           |

12. Compare the following scripts; which one do you prefer and why?

```python
def reverse1(data):
  reverse=[]
  for i in range(len(data) - 1, -1, -1):
    reverse.append(data[i])
  return reverse

def reverse2(data):
    left, right = 0, len(data) - 1
    while left < right:
        # Swap the elements at the left and right indices
        data[left], data[right] = data[right], data[left]
        left += 1
        right -= 1
    return data

if __name__ == "__main__":
  print(reverse1([1,2,3,4,5]))
  print(reverse2([1,2,3,4,5]))
```

12. Pick one of the following options:

    \* `reverse1` is better

    \* `reverse2` is better

    \* Both are the same

| Provide your answer here. |
| ------------------------- |
|                           |

12. What are the time and space complexities for reverse1 and reverse2?

| Provide your answer here. |
| ------------------------- |
| `reverse1`:               |
| `reverse2`:               |

