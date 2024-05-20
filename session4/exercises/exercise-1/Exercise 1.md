### Exercise 1

**Task**

Download the images provided in the `image_urls.txt` file.

* Download the images using serial programming.
* Then, use the `ThreadPoolExecutor`  to download the images.
* Compare the time taken for both tasks.

**Supporting material.**

Study and run the following script, which opens a txt file and reads the text line by line.

```python
# Open the file 'image_urls.txt' in read mode
with open('image_urls.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Strip whitespace characters from the beginning and end of the line
        line_data = line.strip()
        # Print the cleaned line data
        print(line_data)

```

The following script demonstrates how to download a photo from a URL, assign it a name, and store it on disk.

```python
import os  # Import the os module for interacting with the operating system
import random  # Import the random module for generating random numbers (if needed)
import requests  # Import the requests module for making HTTP requests

# Define the output directory where images will be saved
output_dir = "output"

# Create the output directory if it does not exist
os.makedirs(output_dir, exist_ok=True)

# Example URL for demonstration; replace line_data with the actual URL in your code
line_data = "https://example.com/path/to/image.jpg"

# Make an HTTP GET request to download the image content
img_bytes = requests.get(line_data).content

# Define the base name for the image file; you can customize this as needed
name = "photo-1"

# Create the full image file name with the .jpg extension
img_name = f'{name}.jpg'

# Create the full path for saving the image file
full_path = os.path.join(output_dir, img_name)

# Open the image file in write-binary mode and save the image content
with open(full_path, 'wb') as img_file:
    img_file.write(img_bytes)
    print(f'{img_name} was downloaded and saved in {output_dir}...')
```

