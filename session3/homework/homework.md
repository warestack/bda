**Homework**

The following script processes a single image by applying a `GaussianBlur` filter with a radius of 25 and resizing it to a thumbnail size of `3400x3400`. The processed image is then saved to a specified directory. 

```python
from PIL import Image, ImageFilter

# Name and location of the image to be processed
img_name = 'my_photo.jpg'
img_folder = 'photos/' + img_name

# Open the image file
img = Image.open(img_folder)

# Apply a Gaussian blur filter with a radius of 25
img = img.filter(ImageFilter.GaussianBlur(25))

# Resize the image to a thumbnail with a maximum size of 3400x3400 pixels
img.thumbnail((3400, 3400))

# Save the processed image to the 'processed' directory
img.save(f'processed/{img_name}')
```

> [!TIP]
>
> The script uses the [Pillow](https://pillow.readthedocs.io/en/stable/) ( `PIL`) library for image processing. This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.

**Task**

* Write a Python script to transform a set of images with `GaussianBlur 25` and resize them to thumbnail size `3400x3400`.

* Create the appropriate functions as needed.

* You can download the images from [here](https://www.dropbox.com/scl/fo/pfh3d3dcxdk8ivtext6oj/AMCTNa09cqw3P3ykxYFjzag?rlkey=pmb46i6a5amxk0m0uulgu8yju&dl=0). Store the downloaded images in the appropriate directories on your disk and manually create the necessary folders in your local file system. You can use the `os.makedirs('processed', exist_ok=True)` to create a directory within your Python scripts if they don't already exist. Alternatively, you have to create it manually.
* Compare and contrast the performance of serial and parallel processing.
* Compare and contrast the performance of  `ProcessPoolExecutor` and `Pool` classes.

**Supporting material**

Here are the file names of the photos.

```python
'photo-1516117172878-fd2c41f4a759.jpg'
'photo-1532009324734-20a7a5813719.jpg'
'photo-1524429656589-6633a470097c.jpg'
'photo-1530224264768-7ff8c1789d79.jpg'
'photo-1564135624576-c5c88640f235.jpg'
'photo-1541698444083-023c97d3f4b6.jpg'
'photo-1522364723953-452d3431c267.jpg'
'photo-1513938709626-033611b8cc03.jpg'
'photo-1507143550189-fed454f93097.jpg'
'photo-1493976040374-85c8e12f0c0e.jpg'
'photo-1504198453319-5ce911bafcde.jpg'
'photo-1530122037265-a5f1f91d3b99.jpg'
'photo-1516972810927-80185027ca84.jpg'
'photo-1550439062-609e1531270e.jpg'
'photo-1549692520-acc6669e2f0c.jpg'
```

