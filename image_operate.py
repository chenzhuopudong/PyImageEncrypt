
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
        self.info = info
        self.hex_for_file = bytes(info.encode())
        self.info_as_tuple =[]

    def show_hex(self):
        print('Information is :',self.info)
        print('length of data is:',len(self.hex_for_file))
        print(self.hex_for_file)
        for i in range (len(self.hex_for_file)):
            print(bin(self.hex_for_file[i]))

    def save_data_to_file(self, output_file):
        self.output_file = open(self.file_folder+output_file, 'wb')
        self.output_file.write(self.hex_for_file)
        self.output_file.close()

    def byte_to_4bit_tuple(self):
        index_for_tuple = 0
        tmp_array = [0,0,0,0]
        for i in range(len(self.hex_for_file)):
            tmp_value = self.hex_for_file[i]
            print(bin(tmp_value))
            for j in range (1,3):
                for k in range (0,4):
                    tmp_array[k] = (tmp_value&(1<<k))>>k
                self.info_as_tuple.append((tmp_array[0],tmp_array[1],tmp_array[2],tmp_array[3]))
                print(self.info_as_tuple[index_for_tuple])
                index_for_tuple+=1
                tmp_value = tmp_value>>4





