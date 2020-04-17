import requests
import os
import argparse
from urllib3.exceptions import InsecureRequestWarning



HUBBLE_IMAGE_URL = 'http://hubblesite.org/api/v3/image'
HUBBLE_COLLECTION_URL = 'http://hubblesite.org/api/v3/images'

def download_hubble_image (image_id):
    
    response = requests.get(f'{HUBBLE_IMAGE_URL}/{image_id}')
    response.raise_for_status()
    answer = response.json()

    if 'image_files' in answer:

        image = answer['image_files'][-1]
    

        link = image['file_url']
        width = image['width']
        height = image['height']
        resolution = image['file_url'].split('.')[-1]
        file_name = f'{image_id}_{width}_{height}.{resolution}'

        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        picture = requests.get('http:'+link, verify=False)
        picture.raise_for_status()

        with open (f'{images_dir}/{file_name}', 'wb') as file:
            file.write(picture.content)


def get_hubble_collection (collection):
    response = requests.get(f'{HUBBLE_COLLECTION_URL}/{collection}')
    response.raise_for_status()
    answer = response.json()

    for image in answer:
        download_hubble_image(image['id'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='hubble image downloader')
    parser.add_argument('collection',help='name of images collection')
    args = parser.parse_args()

    img_collection = args.collection

    images_dir = 'images'
    os.makedirs (images_dir, exist_ok=True)

   
    get_hubble_collection(img_collection)

    