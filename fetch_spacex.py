import requests
import os
import argparse

SPACEX_URL = 'https://api.spacexdata.com/v3/launches/'


def response_spacex_api (url):
    response = requests.get(url)
    response.raise_for_status()
    return response

def download_images(response):
    if response['links']['flickr_images']:
        for img_number, img in enumerate(response['links']['flickr_images']):
            file_name = f'spaceX_image_{response["flight_number"]}_{img_number+1}.jpeg'

            image_response = requests.get(img)
            image_response.raise_for_status()


            with open (f'{images_dir}/{file_name}', 'wb') as file:
                file.write(image_response.content)
            

                
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image downloader from SpaceX')
    parser.add_argument('-n','--flight_number', help='Type flight number', type=int)
    args = parser.parse_args()
    images_dir = 'images'
    os.makedirs(images_dir, exist_ok=True)

    if not args.flight_number:
        url = f'{SPACEX_URL}latest'
        response = response_spacex_api(url)
        answer = response.json()
    else:
        url = SPACEX_URL
        f_number = args.flight_number - 1
        response = response_spacex_api(url)
        try:
            answer = response.json()[f_number]
        except IndexError:
            exit()

    download_images(answer)

    
        
