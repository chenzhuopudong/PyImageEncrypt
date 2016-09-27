import os,sys
import numpy


from image_process_fuctions import *
from word_to_num import *

resource_path = 'C:/tmp/resource/'
jpg_name = 'png001.png'
output_file_name = 'output_001.png'

org_file = resource_path+jpg_name
tmp_file = resource_path + output_file_name

#tested suits
print ("\t test list with images: \n 1: read_image \n 2: blur_image \n 3: thumbnail_image \n "
       "4: point_transform \n 5: bands_processing \n 6: get_data_for_point")
test_index = int(input('Input a number'))

if test_index == 1:
    read_image(org_file)
elif test_index == 2:
    blur_image(org_file)
elif test_index == 3:
    thumbnail_image(org_file, tmp_file)
elif test_index == 4:
    for i in range(0,20,10):
        point_transform(org_file,tmp_file, i/10)
elif test_index == 5:
    bands_processing(org_file,tmp_file)
elif test_index == 6:
    for x in range(0,100):
        y = 100
        get_data_for_point(org_file,x,y)
else:
    print("No test defined yet")

# tested suits
print("\t test list with words: \n 1: read_words \n ")
test_index = int(input('Input a number'))

if test_index == 1:
    for input_word in ('你吃了吗？','Are you OK?'):
        read_words(input_word)
elif test_index == 2:
    for input_word in ('你吃了吗？', 'Are you OK?','我的名字叫michal：）1!!'):
        chinese_word_encode_decode(input_word)
else:
    print("No test defined yet")


