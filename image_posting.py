import os
from PIL import Image
from instabot import Bot
from dotenv import load_dotenv
import argparse
import time 


def resize_images (directory):
    images = os.listdir(directory)
    max_resolution = 1080
    for image in images:
        if not os.path.isfile(os.path.join(directory, image)):
            continue
        file_name = image.split('.')[0]
        picture = Image.open(f'{directory}/{image}')
        if picture.width > picture.height:
            proportion = picture.width / max_resolution
            height = picture.height / proportion
            picture.thumbnail((max_resolution, height))
            picture = crop_image(picture)
            
        elif picture.width < picture.height:
            proportion = picture.height / max_resolution
            width = picture.width / proportion
            picture.thumbnail((width, max_resolution))
            picture = crop_image(picture)
            
        else:
            picture.thumbnail((max_resolution, max_resolution))
        picture = picture.convert('RGB')
        
        picture.save(f'{directory}/{resized_folder}/{file_name}.jpg')
        os.remove(f'{directory}/{image}')

def crop_image (image):
    max_ratio = 1.91
    min_ratio = 0.8
    width = image.width
    height = image.height
    image_ratio = image.width / image.height
    
    if image_ratio > max_ratio:
        limit_width = int(height * max_ratio)
        indent = (width - limit_width) // 2
        coordinates = (indent, 0, width-indent, height)
        image = image.crop(coordinates)
    elif image_ratio < min_ratio:
        limit_height = width // min_ratio
        indent = (height - limit_height) // 2
        coordinates = (0, indent, width, height - indent)
        image = image.crop(coordinates)
    return image


def post_images (image_folder):
    bot = Bot()
    bot.login(username=login, password=password)
    images = os.listdir(image_folder)
    for image in images:
        if not os.path.isfile(os.path.join(image_folder, image)):
            continue
        bot.upload_photo(f'{image_folder}/{image}')
        time.sleep(10)
        
    bot.logout()

    
        

if __name__ == '__main__':
    load_dotenv()

    parser = argparse.ArgumentParser(description='prepare and upload images to intsagram channel')
    parser.add_argument('basic_folder', help='Enter path to the directory where images are located')
    parser.add_argument('resized_folder', help='Enter the name of directory, where resized images will be saved')
    args = parser.parse_args()

    basic_folder = args.basic_folder
    resized_folder = args.resized_folder

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    os.makedirs(f'{basic_folder}/{resized_folder}', exist_ok=True)

    resize_images (basic_folder)
    post_images (f'{basic_folder}/{resized_folder}')
