import os,sys
from read_image import read_jpeg,blur_jpge

resource_path = 'C:/Users/yuanlili/PycharmProjects/PyImageEncrypt/resource/'
jpg_name = 'cz_001.jpg'

print("Read the file")
#read_jpeg(resource_path+jpg_name)
blur_jpge(resource_path+jpg_name)
