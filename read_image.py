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

    resource_path = 'C:/Users/yuanlili/PycharmProjects/PyImageEncrypt/resource/'
    tmp_jpg_name = 'tmp_001.jpg'
    tmp_file=resource_path+tmp_jpg_name

    try:
        im = Image.open(file_name)
    except:
        print
        "Unable to load image"

    im.thumbnail(size)
    im.save(tmp_file)
    im = Image.open(tmp_file)
    im.show()