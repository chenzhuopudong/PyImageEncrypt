import os,sys
import numpy
from test_case import *
from image_operate import *
from log import *

if (0):
    run_image_test()
    run_text_test()

# 0 init all the paths, files
resource_path = "C:/tmp/resource/"
input_file_name = "tmp001.png"
output_file_name = "out001.png"
input_file = resource_path + input_file_name
output_file = resource_path + output_file_name

operating_png = PNGimage(input_file,output_file)
#---------------------------------------------------------------------------------------
#             Sending side
#
#---------------------------------------------------------------------------------------
# 1 convert the data to byte and binar


sender_info = InfoBody('要不要发大财？:p')
# sender_info.save_data_to_file('tmp003.bin')
#sender_info.show_hex()
sender_info.write_length_to_head()
sender_info.bytes_to_4bit_tuple()


# 2 Use 'or' to embedded the data into LSB
operating_png.combine_LSB(sender_info.info_as_tuple)
operating_png.save_result()

#---------------------------------------------------------------------------------------
#             Receiving side
#
#---------------------------------------------------------------------------------------
#decode the information
result_png =PNGimage(output_file,output_file)
result_png.get_length()
result_png.get_LSB_by_length(result_png.info_length)
receiver_info = InfoBody('')
receiver_info.tuple_to_bytes(result_png.tumple_out)
receiver_info.hex_to_string()

#sender_info.read_info_back('tmp004.txt')
#read_png_points(output_file)

#note1, at first we needn't encrypt, and we don't need to have length at all, we just put
#data from the begining. And when we try to extract information, the data end can be found when
#all data starts to be 0.

#note2, at step 2 we can make all data with 'hole', like interweave, and keep all the other data unchanged


#tmp test section

