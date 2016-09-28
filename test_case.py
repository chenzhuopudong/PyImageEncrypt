from image_process_fuctions import *
from word_to_num import *

resource_path = 'C:/tmp/resource/'
image_name = 'png001.png'
output_file_name = 'output_001.png'
bin_file_name = 'tmp001.bin'

org_file = resource_path + image_name
tmp_file = resource_path + output_file_name

def run_image_test():
    #tested suits
    print ("\t test list with images: \n 1: read_image \n 2: blur_image \n 3: thumbnail_image \n "
           "4: point_transform \n 5: bands_processing \n 6: get_data_for_point \n 7: make white color transparent"
           "\n 8: process PNG image")
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
    elif test_index == 7:
        make_white_transparent(org_file, tmp_file)
    elif test_index == 8:
        process_png(org_file, tmp_file)
        for x in range(0, 100):
            y = 100
            get_data_for_point(org_file, x, y)

    else:
        print("No test defined yet")

def run_text_test():
    # tested suits
    print("\t test list with words: \n 1: read_words \n 2: try decode and encode \n 3: write to file ")
    test_index = int(input('Input a number'))

    if test_index == 1:
        for input_word in ('你吃了吗？','Are you OK?'):
            read_words(input_word)
    elif test_index == 2:
        for input_word in ('你吃了吗？', 'Are you OK?','我的名字叫michal：）1!!'):
            chinese_word_encode_decode(input_word)
    elif test_index == 3:
        write_into_file('你吃了吗？', resource_path + bin_file_name)
#        write_into_file('我的名字叫michal：）1!!',resource_path+bin_file_name)
    else:
        print("No test defined yet")

