# Installing the libraries
import os
import urllib.request

# sudo apt-get install python-imaging
# or install Pillow (PIL) using pip `pip install Pillow`
import PIL
from PIL import Image

# URL example https://stickershop.line-scdn.net/stickershop/v1/sticker/169508422/ANDROID/sticker.png
url = ""

file_header = "Sticker"
file_extension = ".png"
file_folder = ""
count = 30


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
        if i:
            int_url = int(url[6]) + 1
        else:
            int_url = int(url[6])
        url[6] = str(int_url)
        url = "/".join(url)

        # Set file name
        file_name = file_folder + file_header + str(i + 1) + file_extension
        file_location = file_folder + file_name

        # Check if edited URL is valid
        if urllib.request.urlopen(url).getcode() >= 300:
            print("Invalid URL of", str(url) + ".\nSkipping....")

        else:
            print("-------------------------------------")
            print("Downloading ID : " + str(int_url) + " to " + file_location)
            urllib.request.urlretrieve(url, file_name)

        pic_resizer(file_location)


def pic_resizer(file_location):

    try:
        img = Image.open(file_location)

        # Checking the photo size
        print("Raw size :", str(img.size[0]) + " x " + str(img.size[1]))

        # Preferred new some side size
        PREFERENCE_SIZE = 512

        # Largest side will be main thing.
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
        img.save(file_location)
        print("File is saved at", str(file_location))

    except IOError:
        # Psudo throwing an exception (not throwing unacceptable error)
        print("Resizer cannot open file : " + file_location)


def main(test_count=0):
    if test_count >= 5:
        raise Exception('Reached maximum attempt')

# URL Validation
    if urllib.request.urlopen(url).getcode() > 400 or url == "":
        print("Lethal : URL you provide is unreachable...")
        value_getter()
        main(test_count=test_count+1)

    # Folder Validation
    if file_folder != "":
        if not os.path.exists(file_folder):
            raise Exception("Folder doesn't exist")

    pic_downloader(url, file_extension, count)


main()
