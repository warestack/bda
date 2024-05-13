### Exercise 2: Downloading and processing text files

Develop a Python script to download books from the provided URLs using parallel programming techniques. The script should efficiently handle the download process in parallel to optimise performance.

```python
urls = [
        'http://www.gutenberg.org/files/1342/1342-0.txt',  # Pride and Prejudice by Jane Austen
        'http://www.gutenberg.org/cache/epub/11/pg11.txt',  # Alice’s Adventures in Wonderland by Lewis Carroll
        'http://www.gutenberg.org/files/84/84-0.txt',  # Frankenstein by Mary Shelley
        'http://www.gutenberg.org/files/1080/1080-0.txt',  # A Modest Proposal by Jonathan Swift
        'http://www.gutenberg.org/files/98/98-0.txt',  # A Tale of Two Cities by Charles Dickens
        'http://www.gutenberg.org/files/2701/2701-0.txt',  # Moby Dick by Herman Melville
        'http://www.gutenberg.org/files/2600/2600-0.txt',  # War and Peace by Leo Tolstoy
        'http://www.gutenberg.org/files/174/174-0.txt',  # The Picture of Dorian Gray by Oscar Wilde
        'http://www.gutenberg.org/files/43/43-0.txt',  # The Strange Case of Dr. Jekyll and Mr. Hyde by Robert Louis Stevenson
        'http://www.gutenberg.org/files/1661/1661-0.txt'  # The Adventures of Sherlock Holmes by Arthur Conan Doyle
    ]
```

Here are supporting scripts to help you start.

1. The following script demonstrates how to download a single book.

```python
import requests
url = 'http://www.gutenberg.org/cache/epub/11/pg11.txt'
response = requests.get(url)
book = response.text
print(book[1452:1800])
```

The output of this script is the following:

> CHAPTER I. Down the Rabbit-Hole  Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, “and what is the use of a book,” thought Alice “without pictures or conversations?”

2. The following script demonstrates how to extract the book name from the URL.

```python
import re

# URL containing the filename
url = "http://www.gutenberg.org/files/1661/1661-0.txt"

# Regex to extract the filename, in this case 1661-0.txt
pattern = r'[^/]+$'

# Search the URL for the filename using the regex pattern
filename = re.search(pattern, url).group(0)

print("Extracted filename:", filename)
```

The output is:

> 1661-0.txt

3. Finally, the following script demonstrates how to save a text list into a `txt` file.

```python
text_list = ['hello','world','!']
filename = 'myfile.txt'
with open(filename, 'w', encoding='utf-8') as file:
  for text in text_list:
    file.write(text + '\n')
```

4. Compare the serial and parallel case, do you notice a difference?

**Exercise 2**

* Considering the above code samples, create a function to store a list of strings into a file. Use the following specification.

```python
def save_text_to_file(text_list, filename):
 	...
```

* Develop a function to download a book using a specific `url` .  The function should download the book using the url, and then use the `save_text_to_file` to export the file.

```python
def download_book(url):
	...
  
  ...
  save_text_to_file(book,title)
  ...
```

* Create a function named `serial_downloader()` that downloads books in a serial manner and measures the time taken to complete the downloads. You will need to use Python’s `requests` library for fetching the data from the internet and the `time` module to keep track of the duration.
* Then, use the `multiprocessing.Process` to download the books in parallel. Measure the time taken to complete the downloads.
* Compare the serial and parallel case, do you notice a difference?