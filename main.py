import os,sys
import numpy
from test_case import *
from image_operate import *
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


#tmp test section
tmp_info = InfoBody('abc我吃了defe511656很多')
#tmp_info.save_data_to_file('tmp003.bin')
#tmp_info.show_hex()
tmp_info.byte_to_4bit_tuple()