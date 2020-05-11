__author__ = 'Pradyumn Vikram'

# Tkinter Imports
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
# Numpy import
import numpy as np
# Image Processing Imports
from PIL import Image, ImageTk
import cv2
import warnings

"""ImageE is an Image Editing Software with an easy to use GUI. ©Pradyumn Vikram"""


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):
        global button
        self.master.title("ImageE (GUI)")

        self.pack(fill=BOTH, expand=1)

        button = Button(self, text='Select An Image', command=self.upload_img)
        button.place(x=225, y=125)

        T = Label(root, text="Original")
        T.place(x=70, y=30)

        T1 = Label(root, text='Altered')
        T1.place(x=370, y=30)

        T2 = Label(root, text='©Pradyumn Vikram')
        T2.place(x=0, y=0)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        File = Menu(menu)
        File.add_command(label='Upload Image', command=self.upload_img)
        File.add_command(label='Preview Created Image', command=self.show_img)
        File.add_command(label='Download Created Image', command=self.download)
        File.add_command(label='Exit', command=self.exit)
        menu.add_cascade(label='File', menu=File)

        Scale = Menu(menu)
        Scale.add_command(label='Thermal', command=self.HSV)
        Scale.add_command(label='Grayscale', command=self.gray)
        Scale.add_command(label='Edge Map', command=self.edge)
        menu.add_cascade(label='Scale', menu=Scale)

        Rotate = Menu(menu)
        Rotate.add_command(label='Flip', command=self.r180c)
        Rotate.add_command(label='Rotate 90° Clockwise', command=self.r90c)
        Rotate.add_command(label='Rotate 90° Anti-Clockwise', command=self.r90a)
        menu.add_cascade(label='Rotate', menu=Rotate)

        Resize = Menu(menu)
        Resize.add_command(label='Passport Size(2x2 inches)', command=self.rspsimg)
        menu.add_cascade(label='Resize', menu=Resize)
        pass

    def exit(self):
        ans = mb.askyesno('Exit Confirmation', 'Do you want to exit?')
        warnings.simplefilter('ignore')
        if ans is True:
            exit(0)
            pass
        elif ans is False:
            pass
        pass

    # UPLOAD THE IMAGE
    def upload_img(self):
        global image, img, flag, button, smg

        global load
        flag = 0
        path = filedialog.askopenfilename()
        if len(path) > 0:
            image = cv2.imread(path)
            load = Image.open(path)
            render = ImageTk.PhotoImage(load)
            img = Label(self, image=render)
            img.image = render
            img.place(x=20, y=50)
            flag = flag+1
            if(flag > 0):
                button.destroy()
        pass

    # CHANGING IMAGE TO GRAY SCALE
    def gray(self):
        global graysc, image, img, smg
        graysc = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = graysc
        smg = graysc

    # CHANGING IMAGE TO HSV/THERMAL SCALE
    def HSV(self):
        global image, hsvsc, img, smg
        px1 = len(image.shape)
        if(px1 == 3):
            hsvsc = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            pass
        elif(px1 == 2):
            hsvsc = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
            hsvsc = cv2.cvtColor(hsvsc, cv2.COLOR_BGR2HSV)
            image = hsvsc
            smg = hsvsc
        pass
    # ROTATE 180

    def r180c(self):
        global r180r, image, img, smg
        (h, w) = image.shape[:2]
        center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, 180, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h))
        image = rotated
        smg = rotated
        pass
    # ROTATE 90 Clockwise

    def r90c(self):
        global r90c, image, img, smg
        (h1, w1) = image.shape[:2]
        center = (w1 / 2, h1 / 2)
        M1 = cv2.getRotationMatrix2D(center, -90, 1.0)
        rotated90c = cv2.warpAffine(image, M1, (w1, h1))
        image = rotated90c
        smg = rotated90c
        pass
    # ROTATE 90 Anti C

    def r90a(self):
        global r90a, image, img, smg
        (h2, w2) = image.shape[:2]
        center = (w2 / 2, h2 / 2)
        M2 = cv2.getRotationMatrix2D(center, 90, 1.0)
        rotated90a = cv2.warpAffine(image, M2, (w2, h2))
        image = rotated90a
        smg = rotated90a
        pass
    # CONVERT TO EDGE MAP

    def edge(self):
        global image, smg, img
        edge = cv2.Canny(image, 100, 200)
        image = edge
        smg = edge
        pass

    def rspsimg(self):
        global image, img, smg
        r = 413.0/image.shape[1]
        dim = (100, 100)
        rspsim = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        image = rspsim
        smg = rspsim
        pass

    def show_img(self):
        global image, im, imgtk
        global smg
        (h2, w2) = smg.shape[:2]
        px = len(smg.shape)
        if(px == 2):
            smg = cv2.cvtColor(smg, cv2.COLOR_GRAY2RGB)
            pass
        elif(px == 3):
            smg = cv2.cvtColor(smg, cv2.COLOR_BGR2RGB)
            pass
        im = Image.fromarray(smg)
        imgtk = ImageTk.PhotoImage(image=im)
        inimg = Label(root, image=imgtk)
        inimg.image = imgtk
        inimg.place(x=w2+175, y=50)
        pass

    def download(self):
        global image, img
        cv2.imwrite("Images/ImageE.jpg", image)
        mb.showinfo('Information', 'Image Downloaded')
        pass


root = Tk()
root.geometry("550x300")
app = Window(root)
root.mainloop()
