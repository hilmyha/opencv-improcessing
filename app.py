from tkinter import *
from tkinter import ttk
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# to rgb module
def torgb():
    os.system('python module/toRGB.py')

# grayscale module
def grayscale():
    os.system('python module/grayscale.py')

# crop module
def crop():
    os.system('python module/crop_image.py')

# rotate module
def rotate():
    os.system('python module/rotating.py')

# translate module
def translate():
    os.system('python module/translation.py')

# flip module
def flip():
    os.system('python module/flipping.py')

# affine module
def affine():
    os.system('python module/affineTransform.py')

# perspective module
def perspective():
    os.system('python module/perspectiveTransform.py')

# padding module
def padding():
    os.system('python module/padding.py')

# split module
def split():
    os.system('python module/splitColorCh.py')

# resize module
def resize():
    os.system('python module/resize.py')

def cam():
    os.system('python cam.py')

root = Tk()
frm = ttk.Frame(root, padding=40)
root.title("IMAGE PROCESSING")
root.maxsize(800, 400)
frm.grid()
ttk.Label(frm, text="IMAGE PROCESSING\n").grid(columnspan=2, row=1)

ttk.Button(frm, text="TO RGB", command=torgb).grid(column=0, row=2, sticky='ew')
ttk.Button(frm, text="GRAYSCALE", command=grayscale).grid(column=1, row=2, sticky='ew')
ttk.Button(frm, text="CROP", command=crop).grid(column=0, row=3, sticky='ew')
ttk.Button(frm, text="ROTATE", command=rotate).grid(column=1, row=3, sticky='ew')
ttk.Button(frm, text="TRANSLATE", command=translate).grid(column=0, row=4, sticky='ew')
ttk.Button(frm, text="FLIP", command=flip).grid(column=1, row=4, sticky='ew')
ttk.Button(frm, text="AFFINE", command=affine).grid(column=0, row=5, sticky='ew')
ttk.Button(frm, text="PERSPECTIVE", command=perspective).grid(column=1, row=5, sticky='ew')
ttk.Button(frm, text="PADDING", command=padding).grid(column=0, row=6, sticky='ew')
ttk.Button(frm, text="SPLIT", command=split).grid(column=1, row=6, sticky='ew')
ttk.Button(frm, text="RESIZE", command=resize).grid(column=0, row=7, sticky='ew')

ttk.Label(frm, text="").grid(columnspan=3, row=9, sticky='ew')
ttk.Label(frm, text="Press 'space' to capture image").grid(columnspan=3, row=10, sticky='ew')
ttk.Label(frm, text="Press 'esc' to quit from cam").grid(columnspan=3, row=11, sticky='ew')
ttk.Label(frm, text="").grid(columnspan=3, row=12, sticky='ew')
ttk.Button(frm, text="CAM", command=cam).grid(columnspan=3, row=13, sticky='ew')
ttk.Button(frm, text="QUIT", command=root.destroy).grid(columnspan=3, row=14, sticky='ew')
root.mainloop()