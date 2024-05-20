import requests,random,os

def load_data(file_path):
    data_list = []
    with open(file_path, 'r') as file:
        for line in file:
            line_data = line.strip()
            data_list.append(line_data)
    return(data_list)

def get_img(img_url):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    img_bytes = requests.get(img_url).content  
    img_name = f'{random.randint(1, 1000)}.jpg'  
    full_path = output_dir+'/'+img_name
    with open(full_path, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded and saved in {output_dir}...')