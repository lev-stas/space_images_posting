## Space images posting
This is a project that will help you to download images from spacex and hubble APIs, prepare them for posting and post to your instagram account.

#### Dependences 
You need Python3 interpreter to use this script. All needed dependences are included in requirements.txt file. Use ```pip install -r requirements.txt``` to install them (use ```pip3``` instead ```pip```  if you have both python2 and python3 versions)

#### fetch_spacex.py
This script allows you to download images from spaceX launches. Run fetch_spacex.py without any arguments to download images from the last launch. If you need to load images from certain launch, give its number with the key -n ```python fetch_spacex.py -n XX```(use ```python3``` instead ```python```  if you have both python2 and python3 versions). After script comleted you will find "image" folder in the same directory where script fetch_spacex.py is located. All images will be in this "image" folder.

#### fetch_hubble.py
To download images from hubble telescope you should run script fetch_hubble.py and give images collection name to it as an argument ```python fetch_hunbble.py wallpaper``` (use ```python3``` instead ```python```  if you have both python2 and python3 versions). After script comleted you will find "image" folder in the same directory where script fetch_hubble.py is located. All images will be in this "image" folder.

#### image_posting.py
This script prepares your images for posting and posts them to your instagram account. If your image has more than 1080 p on its long side, the script will resize picture. If ratio between sides is more than 16:9, the image will be croped on its long side. You should have ```.env``` file in the same directory this script is located, and write LOGIN variable with your instagram username and PASSWORD variable with your instagram password. 
```LOGIN == 'your_insta_username'```
```PASSWORD == 'your_insta_password ```
Image_posting.py script needs two mandatory arguments. The first one is the path to the directory, where your images are located. The second one is the name of folder which will be created for resized images in the same directory, where original pictures are stored. 
```python images_posting.py images resized``` (use ```python3``` instead ```python```  if you have both python2 and python3 versions).
After uploading is finished all pictures will be deleted, both originals and resized copies. If you need to save original images, please make copies of them before you run this script.



#### Purpose of project
This script was performed as a part of API web-services cource by [Devman](https://dvmn.org/modules)
 