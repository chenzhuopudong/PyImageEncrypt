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

#note1, at first we needn't encrypt, and we don't need to have length at all, we just put
#data from the begining. And when we try to extract information, the data end can be found when
#all data starts to be 0.

#note2, at step 2 we can make all data with 'hole', like interweave, and keep all the other data unchanged


class PNGimage:


    new_data = []

    def __init__(self,src_file,result_file):
        self.Im = Image.open(src_file)
        self.Im = self.Im.convert("RGBA")
        self.datas = self.Im.getdata()
        self.result_file = result_file

    def clean_LSB(self):
        for item in self.datas:
            self.new_data.append((item[0] & 254, item[1] & 254, item[2] & 254, item[3] & 254))

    def save_result(self):
        self.Im.putdata(self.new_data)
        self.Im.save(self.result_file, "PNG")

class InfoBody:

    file_folder='C:/tmp/resource/'

    def __init__(self,info):
        self.hex_for_file = bytes(info.encode())

    def show_hex(self):
        print('length of data is:',len(self.hex_for_file))
        print(self.hex_for_file)
        for i in range (len(self.hex_for_file)):
            print(bin(self.hex_for_file[i]))

    def test_data(self,output_file):
        self.output_file = open(self.file_folder+output_file, 'wb')
        self.output_file.write(self.hex_for_file)
        self.output_file.close()

    def byte_to_4bit_tuple(self):


tmp_info = InfoBody('abc我吃了defe511656很多')
tmp_info.test_data('tmp003.bin')
tmp_info.show_hex()