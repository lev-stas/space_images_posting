import requests
import os
import argparse
from urllib3.exceptions import InsecureRequestWarning


dir_name = 'images'
hubble_image_url = 'http://hubblesite.org/api/v3/image'
hubble_collection_url = 'http://hubblesite.org/api/v3/images'

def hubble_image_downloader (image_id):
    
    response = requests.get(f'{hubble_image_url}/{image_id}')
    response.raise_for_status()

    if 'image_files' in response.json().keys():

        result = response.json()['image_files'][-1]
    

        link = result['file_url']
        width = result['width']
        height = result['height']
        resolution = result['file_url'].split('.')[-1]
        file_name = f'{image_id}_{width}_{height}.{resolution}'

        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        picture = requests.get('http:'+link, verify=False)
        picture.raise_for_status()

        if not os.path.exists (dir_name):
            os.makedirs (dir_name)

        with open (f'{dir_name}/{file_name}', 'wb') as file:
            file.write(picture.content)
        print (f'{file_name} has been downloaded')
    else:
        print('There is no such image id. Try lower')


def hubble_get_collection (collection):
    response = requests.get(f'{hubble_collection_url}/{collection}')
    response.raise_for_status()
    result = response.json()

    for image in result:
        hubble_image_downloader(image['id'])
    print ('All done.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='hubble image downloader')
    parser.add_argument('collection',help='name of images collection')
    args = parser.parse_args()

    img_collection = args.collection

   
    hubble_get_collection(img_collection)

    