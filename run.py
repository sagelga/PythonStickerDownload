# Installing the libraries
import urllib
import os, sys

# sudo apt-get install python-imaging
import PIL
from PIL import Image

url = "https://stickershop.line-scdn.net/stickershop/v1/sticker/36146094/ANDROID/sticker.png"
file_header = "Pic"
file_extension = ".png"
file_folder = ""
count = 60

def value_getter():
    print("Please type in the URL")
    url = input()

    print("How many stickers are in that pack?")
    count = int(input())

    return url, count

def pic_downloader(url, file_extension, count):
    for i in range(count):
        # Editing a URL
        url = url.split('/')
        if (i == 0):
            int_url = int(url[6])
        else:
            int_url = int(url[6]) + 1
        url[6] = str(int_url)
        url = "/".join(url)
        file_name = file_folder + file_header + str(i) + file_extension

        print("Downloading " + str(int_url) + " to " + file_folder + file_name)
        urllib.urlretrieve(url, file_name)

        file_location = file_folder + file_name

		#pic_resizer(i, file_location)

def pic_resizer(i, file_location):

    img = Image.open(file_location)
    # Need to resize one of the following photo to the 512px

    old_height = img.size[0]
    old_width = img.size[1]

    print(old_height + " x " old_width)

    baseheight = 512

    hpercent = (baseheight / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))

    img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
    img.save(/)

def main():
    pic_downloader(url, file_extension, count)

main()
