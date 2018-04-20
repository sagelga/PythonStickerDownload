# Installing the libraries
import urllib
import os, sys

# sudo apt-get install python-imaging
from PIL import Image
from resizeimage import resizeimage

url = "https://stickershop.line-scdn.net/stickershop/v1/sticker/36738878/ANDROID/sticker.png"
file_name = ""
file_extension = ".png"
file_folder = "/result"
count = 32

def value_getter():
	print("Please type in the URL")
	url = input()

	print("How many stickers are in that pack?")
	count = int(input())

	return url, count

def pic_downloader(url, file_name, file_extension, count):
	for i in range(count):
		# Editing a URL
		url = url.split('/')
		int_url = int(url[6]) + i
		url[6] = str(int_url)
		url = "/".join(url)
		file_name = file_folder + "Pic" + str(i) + file_extension

		print("Downloading " + url + " to " + file_folder + file_name)
		urllib.urlretrieve(url, file_name)

		file_location = file_folder + file_name
        pic_resizer(i, file_location)

def pic_resizer(i, file_location):

    img = Image.open(file_location)
    img_size = img.size

    # Need to resize one of the following photo to the 512px

    old_height = img_size[0]
    old_width = img_size[1]

    if old_height > old_width:
        scale = (old_height - old_width)/old_height
        new_height = 512
        new_width = old_width * scale
    else:
        scale = (old_width - old_height)/old_width
        new_width = 512
        new_height = old_height * scale

    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    img.save(file_location)

def main():
	if url == "" and count == 0:
		value_getter()
	pic_downloader(url, file_name, file_extension, count)

main()
