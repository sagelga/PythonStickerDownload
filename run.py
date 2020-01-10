# Installing the libraries
import os
import requests

import PIL
from PIL import Image
from io import BytesIO

FIRST_ID = 0
STICKER_COUNT = 30
DEST_FOLDER = ''
FILE_PREFIX = 'sticker'
BASE_URL_PREFIX = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'
BASE_URL_SUFFIX = "/ANDROID/sticker.png"
PREFERENCE_SIZE = 512


def main():
    # Check for configuration error
    if (DEST_FOLDER != '') and (not os.path.exists(DEST_FOLDER)):
        raise Exception("Folder doesn't exist")

    # Retrieve sticker ID
    FIRST_ID = int(input('First Sticker ID : '))

    # Retrieve sticker count
    STICKER_COUNT = int(input('Sticker count in the pack : '))

    for i in range(STICKER_COUNT):
        stickerRetrieve(FIRST_ID + i)


def stickerRetrieve(id):
    id = str(id)

    url = BASE_URL_PREFIX + id + BASE_URL_SUFFIX
    print("-------------------------------------")
    print('Downloading from : '+url)

    try:
        # Retrive binaries
        img = requests.get(url, timeout=(10, 30))
        img.raise_for_status()
    except Timeout as identifier:
        # https://2.python-requests.org//en/master/user/quickstart/#timeouts
        print('Timeout')
    except TooManyRedirects:
        print('Too many redirects')
    except HTTPError:
        print('Unable to have HTTP connection')

    # Converts the image into a Telegram friendly size
    try:
        img = Image.open(BytesIO(img.content))
        print("Raw size :", str(img.size[0]) + " x " + str(img.size[1]))

        # Widest side will be sized 512px, and others will scale properly
        if max(img.size[0], img.size[1]) == img.size[1]:
            ratio = (PREFERENCE_SIZE / float(img.size[1]))
            wsize = int((float(img.size[0]) * float(ratio)))
            img = img.resize((wsize, PREFERENCE_SIZE), PIL.Image.ANTIALIAS)
        else:
            ratio = (PREFERENCE_SIZE / float(img.size[0]))
            wsize = int((float(img.size[1]) * float(ratio)))
            img = img.resize((PREFERENCE_SIZE, wsize), PIL.Image.ANTIALIAS)

        print("New size :", str(img.size[0]), "x", str(img.size[1]))

        # Save the file, where it should be
        img_dest = DEST_FOLDER + FILE_PREFIX + id + '.png'
        img.save(img_dest)
        print("Sticker destination : " + str(img_dest))

    except IOError as identifier:
        pass
    except KeyError as identifier:
        pass


main()
