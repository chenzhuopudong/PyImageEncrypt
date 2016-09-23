import os,sys
from read_image import read_jpeg,blur_jpge,thumbnail_jpge

resource_path = 'C:/tmp/resource/'
jpg_name = 'tmp_001.jpg'

#tested suits
#read_jpeg(resource_path+jpg_name)
blur_jpge(resource_path+jpg_name)
#thumbnail_jpge(resource_path+jpg_name)