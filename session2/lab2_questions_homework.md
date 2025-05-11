### Homework Questions (1–10)

Provide the solutions to the following questions using the `rockyou.txt` file.

1. Count how many passwords start with the letter `'a'`.
2. Count how many anagram groups exist in the password list.
   -  *Anagram:* Words that contain the same letters in a different order (e.g., `"listen"` and `"silent"`).
3. Count how many passwords are palindromes.
   -  *Palindrome:* A word that reads the same forward and backward (e.g., `"racecar"`, `"level"`).
4. Find the top 5 most frequent starting letters in the password list.
5. Count how many passwords contain only numerics.

```python
"123".isdigit()      # True
"Ⅻ".isdigit()      # False
"Ⅻ".isnumeric()    # True
"123".isdecimal()   # True
"²".isdecimal()     # False
```

* Use this table as a reference.

| **String** | **Description**             | `.isdecimal()` | `.isdigit()` | `.isnumeric()` | `.isalpha()` |
| ---------- | --------------------------- | -------------- | ------------ | -------------- | ------------ |
| `'123'`    | ASCII digits                | ✅ True         | ✅ True       | ✅ True         | ❌ False      |
| `'²'`      | Superscript 2               | ❌ False        | ✅ True       | ✅ True         | ❌ False      |
| `'Ⅻ'`      | Roman numeral 12            | ❌ False        | ❌ False      | ✅ True         | ❌ False      |
| `'٣'`      | Arabic-Indic digit (3)      | ✅ True         | ✅ True       | ✅ True         | ❌ False      |
| `'１２３'` | Full-width digits (Unicode) | ✅ True         | ✅ True       | ✅ True         | ❌ False      |
| `'10.5'`   | Decimal number with dot     | ❌ False        | ❌ False      | ❌ False        | ❌ False      |
| `'-123'`   | Negative number             | ❌ False        | ❌ False      | ❌ False        | ❌ False      |
| `'abc'`    | Letters only                | ❌ False        | ❌ False      | ❌ False        | ✅ True       |

6. Find the longest password in the list.

7. Count how many passwords are exactly 8 characters long.

8. Count how many passwords are made of only lowercase letters.

9. Count how many passwords contain the substring `"123"`.

10. Calculate the average length of all passwords.