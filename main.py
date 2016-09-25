import os,sys
from read_image import read_jpeg,blur_jpge,thumbnail_jpge

resource_path = 'C:/tmp/resource/'
jpg_name = 'tmp_001.jpg'

output_file_name = 'output_001.jpg'
tmp_file = resource_path + output_file_name

#tested suits
#read_jpeg(resource_path+jpg_name)
#blur_jpge(resource_path+jpg_name)
thumbnail_jpge(resource_path+jpg_name,tmp_file)