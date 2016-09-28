import os,sys
import numpy
from test_case import *
from PIL import Image

run_image_test()
run_text_test()

# 1 get the image, changing all pixel's LSB as b'0
# 2 convert the data to byte and binary
# 3 get the length of the array of byte
# 4 Use 'or' to embedded the data into LSB

class PNGimage:

    new_data = []

    def __init__(self,src_file):
        self.Im = Image.open(src_file)
        self.Im = self.Im.convert("RGBA")
        self.datas = self.Im.getdata()

    def clean_LSB(self):
        for item in datas:
            new_data.append((item[0] & 254, item[1] & 254, item[2] & 254, item[3] & 254))
