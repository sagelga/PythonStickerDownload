# Installing the libraries
import urllib
import os, sys
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

		print("Downloading " + url + " to " + file_name)
		urllib.urlretrieve(url, file_name)

        pic_resizer()

def pic_resizer():
    img = Image.open(file_folder + )  # image extension *.png,*.jpg
    new_width = 200
    new_height = 300
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    img.save('output image name.png')  # format may what u want ,*.png,*jpg,*.gif

def main():
	if url == "" and count == 0:
		value_getter()
	pic_downloader(url, file_name, file_extension, count)

main()
