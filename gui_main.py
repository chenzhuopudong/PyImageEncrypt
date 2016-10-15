from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd

class info_in_out:

    def __init__(self):
        self.root = Tk()
        self.root.title("Let's start to")
        self.reource_path = "C:/tmp/resource/"
        self.enter_image_name = "enter.png"
        self.getout_image_name = "getout.png"
    def mainframe_init(self):
        self.mainframe = ttk.Frame(self.root, padding="0 0 0 0")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
    def button_init(self):
        self.plus_image = PhotoImage(file=self.reource_path + self.enter_image_name)
        self.sub_image = PhotoImage(file=self.reource_path + self.getout_image_name)
        self.plus_button = ttk.Button(self.mainframe, image=self.plus_image, command=self.enter_button_fuc).grid(column=1, row=1, sticky=W)
        self.substract_button = ttk.Button(self.mainframe, image=self.sub_image, command=self.get_out_button_fuc).grid(column=2, row=1, sticky=W)
    def enter_button_fuc(self):
        i = 0

    def get_out_button_fuc(self):
        i = 1