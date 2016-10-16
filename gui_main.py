from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd


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
        self.newWindow = DataOutWindow()

class DataInWindow:

    def __init__(self,parentWindow):
        self.root = Toplevel()
        self.parent = parentWindow
        self.root.title("Data In")
        self.reource_path = "C:/tmp/resource/"
        self.data_in_image_name = "datain.png"
        self.mainframe = ttk.Frame(self.root, padding="0 0 0 0")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.data_in_image = PhotoImage(file=self.reource_path + self.data_in_image_name)
        self.data_in_button = ttk.Button(self.mainframe, image=self.data_in_image, command=self.load_file).grid(
            column=1, row=1, sticky=W)
        self.input_text = Text(self.mainframe).grid(
            column=2, row=1, sticky=W)

        self.root.protocol('WM_DELETE_WINDOW', self.close_window)  # root is your root window

        self.execute_button = ttk.Button(self.mainframe, image=self.data_in_image, command=self.load_file).grid(
        column=3, row=1, sticky=W)

    def close_window(self):
        self.parent.deiconify()
        self.root.destroy()

    def load_file(self):
        fname = fd.askopenfilename(filetypes=(("Image Files", "*.png"),
                                              ("HTML files", "*.html;*.htm"),
                                              ("All files", "*.*")))

        if fname:
            try:
                self.data_in_image = PhotoImage(file=fname)
                self.data_in_button = ttk.Button(self.mainframe, image=self.data_in_image, command=self.load_file).grid(
            column=1, row=1, sticky=W)
            except:  # <- naked except is a bad idea
                print("Open Source File", "Failed to read file\n'%s'" % fname)
                self.parent.deiconify()

            return

class DataOutWindow:
    def a(self):
        c = 0