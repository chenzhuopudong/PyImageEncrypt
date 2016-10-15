from PIL import Image
from log import *

class PNGimage:


    new_data = []
    tumple_out = []
    module_log = logs(3)
    data_offset = 4
    def __init__(self,src_file,result_file):
        self.Im = Image.open(src_file)
        self.Im = self.Im.convert("RGBA")
        self.datas = self.Im.getdata()
        self.result_file = result_file
        self.info_length = 0

    def clean_LSB(self):
        self.new_data = []
        for item in self.datas:
            self.new_data.append((item[0] & 254, item[1] & 254, item[2] & 254, item[3] & 254))

    def combine_LSB(self, input_tuple_array):
        self.new_data = []

        for i in range(len(input_tuple_array)):
            tmp_tuple = self.datas[i]
            self.module_log.minor_log(tmp_tuple)
            self.module_log.minor_log(input_tuple_array[i])
            self.new_data.append((tmp_tuple[0] & 254 | input_tuple_array[i][0],
                                  tmp_tuple[1] & 254 | input_tuple_array[i][1],
                                  tmp_tuple[2] & 254 | input_tuple_array[i][2],
                                  tmp_tuple[3] & 254 | input_tuple_array[i][3]))
            self.module_log.minor_log((tmp_tuple[0] & 254 | input_tuple_array[i][0],
                                  tmp_tuple[1] & 254 | input_tuple_array[i][1],
                                  tmp_tuple[2] & 254 | input_tuple_array[i][2],
                                  tmp_tuple[3] & 254 | input_tuple_array[i][3]))


    def get_length(self):
        tmp_value = 0
        result = 0
        self.module_log.minor_log("******************")

        for i in range(0,4):
            tmp_value = 0
            for j in range(0,4):
                tmp_value +=(self.datas[i][j] & 1) << j
            tmp_value <<= (4*i)
            result += tmp_value
        self.module_log.debug_log('Length of data is:'+str(result))
        self.info_length = result

    def get_LSB_by_length(self, length):
        self.tumple_out = []
        for i in range(length):
            i += self.data_offset
            self.tumple_out.append((self.datas[i][0] & 1,
                                    self.datas[i][1] & 1,
                                    self.datas[i][2] & 1,
                                    self.datas[i][3] & 1))
            self.module_log.minor_log((self.datas[i][0] & 1,
                                    self.datas[i][1] & 1,
                                    self.datas[i][2] & 1,
                                    self.datas[i][3] & 1))

    def save_result(self):
        self.Im.putdata(self.new_data)
        self.Im.save(self.result_file, "PNG")

class InfoBody:

    file_folder='C:/tmp/resource/'
    module_log = logs(3)


    def __init__(self,info):
        self.info = info
        self.hex_for_file = bytes(info.encode())
        self.info_as_tuple =[]
        self.info_length = 0
        self.hex_out = []
        self.out_info = []

    def get_4bit_to_tumple_array(self,input_value):
        bit0_to_3 = [0, 0, 0, 0]
        for i in range(0, 4):
            bit0_to_3[i] = (input_value & (1 << i)) >> i
        tmp_tuple = (bit0_to_3[0], bit0_to_3[1], bit0_to_3[2], bit0_to_3[3])
        self.module_log.minor_log(tmp_tuple)
        self.info_as_tuple.append(tmp_tuple)


    def write_length_to_head(self):
        length_value = len(self.hex_for_file)*2 #Everybyte requires 2 points
        self.info_length = length_value
        print(self.info_length)

        for i in range(0, 4):
            self.get_4bit_to_tumple_array(length_value)
            length_value = length_value >> 4

        print(len(self.info_as_tuple))

    def show_hex(self):
        self.module_log.debug_log('Information is :',self.info)
        self.module_log.debug_log('length of data is:',len(self.hex_for_file))
        self.module_log.debug_log(self.hex_for_file)
        for i in range (len(self.hex_for_file)):
            self.module_log.minor_log(bin(self.hex_for_file[i]))
            self.module_log.minor_log(self.hex_for_file[i])


    def save_data_to_file(self, output_file):
        self.output_file = open(self.file_folder+output_file, 'wb')
        self.output_file.write(bytearray(self.hex_out))
        self.output_file.close()
        self.module_log.debug_log(((self.hex_out)))

        #def integer_to_4bit_tuple(self, eight_bit_value):
    def bytes_to_4bit_tuple(self):
        for i in range(len(self.hex_for_file)):
            tmp_value = self.hex_for_file[i]
            self.module_log.minor_log(bin(tmp_value))
            for j in range(0, 2):
                self.get_4bit_to_tumple_array(tmp_value)
                tmp_value = tmp_value >> 4
        self.module_log.minor_log(len(self.info_as_tuple))

    def tuple_to_bytes(self,input_tumple):
        tmp_count = 0
        tmp_offset = 0
        self.hex_out = []
        tmp_byte = 0
        self.module_log.minor_log("--------------------")

        for tmp_tumple in input_tumple:
            tmp_count = 1 - tmp_count
            self.module_log.minor_log(tmp_tumple)
            for i in range(0,4):
                tmp_byte += tmp_tumple[i]<<(i + tmp_offset)

            if tmp_count == 1 :
                tmp_offset = 4
            elif tmp_count == 0 :
                self.hex_out.append(tmp_byte)
                self.module_log.minor_log(tmp_byte)
                tmp_offset = 0
                tmp_byte = 0

    def hex_to_string(self):
        self.module_log.debug_log((bytes(self.hex_out).decode('utf-8')))















