import os,sys
from PIL import Image,ImageFilter,ImageDraw
import datetime
def read_jpeg(input_file):

    try:
        im = Image.open(input_file)
    except:
        print
        "Unable to load image"

    print("The details of", input_file )
    im.show()
    print (im.size)
    print (im.bits, im.size, im.format, im.mode)


def blur_jpge(input_file):

    # Load an image from the hard drive
    try:
        im = Image.open(input_file)
    except:
        print
        "Unable to load image"

    #print (datetime.datetime.now())
    datetime.datetime.now()
    # Blur the image
    blurred = im.filter(ImageFilter.GaussianBlur(radius=20))
    #print (datetime.datetime.now())
    # Display both images
    blurred.show()

    # save the new image
    #blurred.save("blurred.png")

def thumbnail_jpge(input_file,output_file):

    size = (128, 128)

    try:
        im = Image.open(input_file)
    except:
        print
        "Unable to load image"

    im.thumbnail(size)
    im.save(output_file)
    im = Image.open(output_file)
    im.show()

def point_transform(input_file,output_file,coef):

    try:
        im = Image.open(input_file)
    except:
        print
        "Unable to load image"

    out = im.point( lambda i:i * coef)
    out.save(output_file)
    out.show()

def bands_processing(input_file,output_file):

    try:
        im = Image.open( input_file )
    except:
        print
        "Unable to load image"

    # split the image into individual bands
    source = im.split( )

    R, G, B = 0, 1, 2

    # select regions where red is less than 100
    mask = source[R].point( lambda i: i < 100 and 255 )

    # process the green band
    out = source[G].point( lambda i: i * 0.1 )

    # paste the processed band back, but only where red was < 100
    source[G].paste( out, None, mask )

    # build a new multiband image
    im = Image.merge( im.mode, source )
    im.save(output_file)
    im.show()

def get_data_for_point(input_file,pos_x,pos_y):

    try:
        im = Image.open( input_file )
    except:
        print
        "Unable to load image"


    position = (pos_x,pos_y)

    pixels = im.load()
    print (pixels[position])
