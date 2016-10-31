from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from image_operate import *


class InOutMainWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Let's start to")
        self.reource_path = "C:/tmp/resource/"
        self.enter_image_name = "enter.png"
        self.getout_image_name = "getout.png"
        self.mainframe = ttk.Frame(self.root, padding="0 0 0 0")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.plus_image = PhotoImage(file=self.reource_path + self.enter_image_name)
        self.sub_image = PhotoImage(file=self.reource_path + self.getout_image_name)
        self.plus_button = ttk.Button(self.mainframe, image=self.plus_image, command=self.enter_button_fuc).grid(
            column=1, row=1, sticky=W)
        self.substract_button = ttk.Button(self.mainframe, image=self.sub_image, command=self.get_out_button_fuc).grid(
            column=2, row=1, sticky=W)

    def enter_button_fuc(self):
        self.root.withdraw()
        self.newWindow = DataInWindow(self.root)

    def get_out_button_fuc(self):
        self.root.withdraw()
        self.newWindow = DataOutWindow(self.root)


class DataInWindow:
    def __init__(self, parentWindow):
        self.module_log = logs(5)
        self.root = Toplevel()
        self.parent = parentWindow
        self.root.title("Data In")
        self.reource_path = "C:/tmp/resource/"
        self.tmp_image_name = "tmp.png"
        self.data_in_image_name = "datain.png"
        self.combine_image_name = "combine.png"
        self.mainframe = ttk.Frame(self.root, padding="0 0 0 0")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.data_in_image = PhotoImage(file=self.reource_path + self.data_in_image_name)
        self.combine_image = PhotoImage(file=self.reource_path + self.combine_image_name)
        self.data_in_button = ttk.Button(self.mainframe, image=self.data_in_image, command=self.load_file).grid(
            column=1, row=1, sticky=W)
        self.fname = []
        # self.combine_button.config(state ="disabled")

        self.root.protocol('WM_DELETE_WINDOW', self.close_window)  # root is your root window

    def close_window(self):
        self.parent.deiconify()
        self.root.destroy()

    def load_file(self):
        self.fname = fd.askopenfilename(filetypes=(("Image Files", "*.png"),
                                              ("HTML files", "*.html;*.htm"),
                                              ("All files", "*.*")))

        if self.fname:
            try:
                self.data_in_image = PhotoImage(file=self.fname)
                self.data_in_button = ttk.Button(self.mainframe, image=self.data_in_image, command=self.load_file).grid(
                    column=1, row=1, sticky=W)
                self.add_text_box()
                self.add_combine_button()

            except:  # <- naked except is a bad idea
                print("Open Source File", "Failed to read file\n'%s'" % self.fname)
                self.parent.deiconify()

            return

    def add_text_box(self):
        self.input_text = Text(self.mainframe)
        self.input_text.bind("<Key>", self.text_input)
        self.input_text.grid(column=2, row=1, sticky=W)

    def text_input(self, key):
        self.combine_button.config(state=['!disabled'])

    def add_combine_button(self):
        self.combine_button = ttk.Button(self.mainframe, image=self.combine_image, command=self.combine_info)
        self.combine_button.grid(column=3, row=1, sticky=W)
        self.combine_button.config(state=['disabled'])

    def combine_info(self):
        info = self.input_text.get("1.0", END)
        self.module_log.debug_log(info)

        operating_png = PNGimage(self.fname, self.reource_path+self.tmp_image_name)
        info_to_be_send = InfoBody(info)
        info_to_be_send.write_length_to_head()
        info_to_be_send.bytes_to_4bit_tuple()
        operating_png.combine_LSB(info_to_be_send.info_as_tuple)
        operating_png.save_result()

        self.close_window()

class DataOutWindow:
    def __init__(self, parentWindow):
        self.module_log = logs(5)
        self.root = Toplevel()
        self.parent = parentWindow
        self.root.title("Data out")
        self.reource_path = "C:/tmp/resource/"
        self.data_out_image_name = "dataout.png"
        self.mainframe = ttk.Frame(self.root, padding="0 0 0 0")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.data_out_image = PhotoImage(file=self.reource_path + self.data_out_image_name)
        self.data_out_button = ttk.Button(self.mainframe, image=self.data_out_image, command=self.load_file).grid(
            column=1, row=1, sticky=W)
        self.fname = []
        # self.combine_button.config(state ="disabled")

        self.root.protocol('WM_DELETE_WINDOW', self.close_window)  # root is your root window

    def close_window(self):
        self.parent.deiconify()
        self.root.destroy()

    def load_file(self):
        self.fname = fd.askopenfilename(filetypes=(("Image Files", "*.png"),
                                              ("HTML files", "*.html;*.htm"),
                                              ("All files", "*.*")))

        if self.fname:
            try:
                self.data_out_image = PhotoImage(file=self.fname)
                self.data_out_button = ttk.Button(self.mainframe, image=self.data_out_image, command=self.load_file).grid(
                    column=1, row=1, sticky=W)
                self.add_text_box()

            except:  # <- naked except is a bad idea
                print("Open Source File", "Failed to read file\n'%s'" % self.fname)
                self.parent.deiconify()

            return

    def add_text_box(self):
        self.input_text = Text(self.mainframe)
        self.input_text.grid(column=2, row=1, sticky=W)
        self.get_data_out()


    def get_data_out(self):
        result_png = PNGimage(self.fname, self.fname)
        result_png.get_length()
        result_png.get_LSB_by_length(result_png.info_length)
        receiver_info = InfoBody('')
        receiver_info.tuple_to_bytes(result_png.tumple_out)
        receiver_info.hex_to_string()
        self.module_log.debug_log(receiver_info.info_body)
        self.input_text.insert(INSERT, receiver_info.info_body)
