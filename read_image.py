import os,sys
from PIL import Image,ImageFilter
import datetime

def read_jpeg(file_name):

    print("Read the image",file_name)
    jpgfile = Image.open(file_name)

    print("The details of",file_name)
    jpgfile.show()
    print (jpgfile.size)
    #jpgfile.thumbnail(128, 128)
    #thumbnail.show()
    print (jpgfile.bits, jpgfile.size, jpgfile.format, jpgfile.mode)


def blur_jpge(file_name):

    # Load an image from the hard drive
    original = Image.open(file_name)

    #print (datetime.datetime.now())
    datetime.datetime.now()
    # Blur the image
    blurred = original.filter(ImageFilter.GaussianBlur(radius=20))
    #print (datetime.datetime.now())
    # Display both images
    blurred.show()

    # save the new image
    #blurred.save("blurred.png")

def thumbnail_jpge(file_name):

    size = (128, 128)
    try:
        im = Image.open("Lenna.png")
    except:
        print
        "Unable to load image"

    im.thumbnail(size)
    im.save(saved)
    im.show()