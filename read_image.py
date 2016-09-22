import os,sys
from PIL import Image

def read_jpeg(file_name):

    print("Read the image",file_name)
    jpgfile = Image.open(file_name)

    print("The details of",file_name)
    print (jpgfile.bits, jpgfile.size, jpgfile.format, jpgfile.mode)

