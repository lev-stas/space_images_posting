import os
from PIL import Image
from instabot import Bot
from dotenv import load_dotenv
import argparse


image_dir = 'images'
edited_images_dir = 'resized'

if not os.path.exists (f'{image_dir}/{edited_images_dir}'):
    os.makedirs(f'{image_dir}/{edited_images_dir}')

# This function resizes images to 1080 px on long side
def edit_image(directory):
    images = os.listdir(image_dir)
    for image in images:
        if os.path.isfile(os.path.join(image_dir, image)):
            file_name = image.split('.')[0]
            picture = Image.open(f'{image_dir}/{image}')
            if picture.width > picture.height:
                proportion = picture.width / 1080
                height = picture.height / proportion
                picture.thumbnail((1080,height))
                # if the difference between sides is more than 16:9, we should crop the image
                if 1080 / height > 1.77:
                    true_width = int(height * 1.77)
                    ident = (1080 - true_width) / 2
                    coordinates = (ident,0,1080 - ident, height)
                    picture = picture.crop(coordinates)
            elif picture.width < picture.height:
                proportion = picture.height / 1080
                width = picture.width / proportion
                picture.thumbnail((width, 1080))
                # if the difference between sides is more than 16:9, we should crop the image
                if 1080 / width > 1.77:
                    true_height = int(width * 1.77)
                    ident = (1080 - true_height) / 2
                    picture = picture.crop (0, ident, width, 1080-ident)
            else:
                picture.thumbnail((1080,1080))
            rgb_picture = picture.convert('RGB')
        
            rgb_picture.save(f'{basic_folder}/{resized_folder}/{file_name}.jpg')
            print(f'{file_name} has been resized.')
            os.remove(f'{basic_folder}/{image}')
            print(f'{image} has been removed.')
        print ('All done.')

# this function posts images to instagram channel 
def insta_post_image(image_folder):
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    bot = Bot()
    bot.login(username=login, password=password)
    images = os.listdir(image_folder)
    for image in images:
        if os.path.isfile(os.path.join(image_folder, image)):
            bot.upload_photo(f'{image_folder}/{image}')
            os.remove(f'{image_folder}/{image}.REMOVE_ME')
    bot.logout()
    print('All done.')
    
        

if __name__ == '__main__':
    load_dotenv()

    parser = argparse.ArgumentParser(description='prepare and upload images to intsagram channel')
    parser.add_argument('basic_folder', help='Enter path to the directory where images are located')
    parser.add_argument('resized_folder', help='Enter the name of directory, where resized images will be saved')
    args = parser.parse_args()

    basic_folder = args.basic_folder
    resized_folder = args.resized_folder

    edit_image(basic_folder)
    insta_post_image(f'{basic_folder}/{resized_folder}')
