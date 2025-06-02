
with open('image_urls.txt', 'r') as file:
    for line in file:
        line_data = line.strip()
        print(line_data)

import os, random, requests

output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

img_bytes = requests.get(line_data).content  
name = "photo-1"
img_name = f'{name}.jpg'

full_path = output_dir+'/'+img_name
with open(full_path, 'wb') as img_file:
    img_file.write(img_bytes)
    print(f'{img_name} was downloaded and saved in {output_dir}...')