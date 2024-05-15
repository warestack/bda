
from PIL import Image, ImageFilter

def process_image(img_name):
  img_folder='photos/'+img_name
  img = Image.open(img_folder)
  img = img.filter(ImageFilter.GaussianBlur(15))
  img.thumbnail((3400,3400))
  img.save(f'processed/{img_name}')
  return(f'{img_name} was processed...')
