import sys 
import os
from PIL import Image

image_folder = sys.argv[1]
new_location = sys.argv[2]

if not os.path.exists(new_location):
    os.makedirs(new_location)

for file in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{file}')
    clear_img_name = os.path.splitext(file)[0]
    img.save(f'{new_location}{clear_img_name}.png', 'png')
    print('converted')     