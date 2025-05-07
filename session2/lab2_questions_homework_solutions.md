
### ✅ Homework Solutions (1–10) — Using Only `for` Loops

#### 1. Count how many passwords start with the letter `'a'`
```python
def count_start_with_a(passwords):
    count = 0
    for p in passwords:
        if p.strip().startswith('a'):
            count += 1
    return count
```

---

#### 2. Count how many anagram groups exist in the password list
```python
def count_anagram_groups(passwords):
    groups = {}
    for p in passwords:
        key = ''.join(sorted(p.strip()))
        if key in groups:
            groups[key].append(p.strip())
        else:
            groups[key] = [p.strip()]
    
    count = 0
    for group in groups.values():
        if len(group) > 1:
            count += 1
    return count
```

---

#### 3. Count how many passwords are palindromes
```python
def count_palindromes(passwords):
    count = 0
    for p in passwords:
        word = p.strip()
        if word == word[::-1]:
            count += 1
    return count
```

---

#### 4. Find the top 5 most frequent starting letters
```python
def top_5_starting_letters(passwords):
    freq = {}
    for p in passwords:
        word = p.strip()
        if word:
            first = word[0]
            if first in freq:
                freq[first] += 1
            else:
                freq[first] = 1

    items = list(freq.items())
    # Simple bubble sort (descending)
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[j][1] > items[i][1]:
                items[i], items[j] = items[j], items[i]
    
    return items[:5]
```

---

#### 5. Count how many passwords contain only numerics
```python
def count_only_numeric(passwords):
    count = 0
    for p in passwords:
        if p.strip().isnumeric():
            count += 1
    return count
```

---

#### 6. Find the longest password in the list
```python
def find_longest_password(passwords):
    longest = ""
    for p in passwords:
        word = p.strip()
        if len(word) > len(longest):
            longest = word
    return longest
```

---

#### 7. Count how many passwords are exactly 8 characters long
```python
def count_length_8(passwords):
    count = 0
    for p in passwords:
        if len(p.strip()) == 8:
            count += 1
    return count
```

---

#### 8. Count how many passwords are made of only lowercase letters
```python
def count_all_lowercase(passwords):
    count = 0
    for p in passwords:
        word = p.strip()
        if word.islower() and word.isalpha():
            count += 1
    return count
```

---

#### 9. Count how many passwords contain the substring `"123"`
```python
def count_contains_123(passwords):
    count = 0
    for p in passwords:
        if '123' in p.strip():
            count += 1
    return count
```

---

#### 10. Calculate the average length of all passwords
```python
def average_password_length(passwords):
    total = 0
    count = 0
    for p in passwords:
        total += len(p.strip())
        count += 1
    if count == 0:
        return 0
    return total / count
```
