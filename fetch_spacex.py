import requests
import os
import argparse

base_url = 'https://api.spacexdata.com/v3/launches/'
dir_name = 'images'

def spacex_api_response (url):
    response = requests.get(url)
    response.raise_for_status()
    return response

def image_downloader(response):
    if not response['links']['flickr_images']:
        print ('No images of this flight. Try another flight number')
    else:
        for img_number, img in enumerate(response['links']['flickr_images']):
            file_name = f'spaceX_image_{response["flight_number"]}_{img_number+1}.jpeg'

            image_response = requests.get(img)
            image_response.raise_for_status()

            if not os.path.exists(dir_name):
                os.makedirs(dir_name)

            with open (f'{dir_name}/{file_name}', 'wb') as file:
                file.write(image_response.content)
            print(f'{file_name} has been downloaded.')
        print('All done.')

                
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image downloader from SpaceX')
    parser.add_argument('-n','--flight_number', help='Type flight number', type=int)
    args = parser.parse_args()

    if not args.flight_number:
        url = f'{base_url}latest'
        response = spacex_api_response(url)
        result = response.json()
    else:
        url = base_url
        f_number = args.flight_number - 1
        response = spacex_api_response(url)
        try:
            result = response.json()[f_number]
        except IndexError:
            print(f'There is not such flight number yet. The latest flight is {len(response.json())}.')
            exit()

    image_downloader(result)

    
        
