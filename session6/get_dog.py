# This script fetches a random dog image from the Dog CEO API and saves it locally.
# It prints the image URL and saves the image using the original filename from the URL.

import requests
import os

def fetch_and_save_dog_image():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)

    if response.status_code == 200:
        image_url = response.json()['message']
        print(f"Downloading image from: {image_url}")

        # Extract filename from the URL
        filename = os.path.basename(image_url)

        # Download the image content
        image_data = requests.get(image_url).content

        # Save it to a file
        with open(filename, 'wb') as file:
            file.write(image_data)

        print(f"Image saved as: {filename}")
    else:
        print("Failed to fetch dog image.")

# Run the function
fetch_and_save_dog_image()
