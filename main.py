import os,sys

#from image_process_fuctions import read_jpeg,blur_jpge,thumbnail_jpge,point_transform,bands_processing
from image_process_fuctions import *

resource_path = 'C:/tmp/resource/'
jpg_name = 'tmp001.jpg'
output_file_name = 'output_001.jpg'

org_file = resource_path+jpg_name
tmp_file = resource_path + output_file_name

#tested suits
print ("\t test list: \n 1: read_jpeg \n 2: blur_jpge \n 3: thumbnail_jpge \n "
       "4: point_transform \n 5: bands_processing \n 6: get_data_for_point")
test_index = int(input('Input a number'))

if test_index == 1:
    read_jpeg(org_file)
elif test_index == 2:
    blur_jpge(org_file)
elif test_index == 3:
    thumbnail_jpge(org_file,tmp_file)
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