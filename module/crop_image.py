import numpy as np
import cv2
from cv2 import imread

# read the image
img = imread('image_capture/captured_img.png')

# to crop
y=0
x=0
h=400
w=400
crop = img[y:y+h, x:x+w]

# show the image
cv2.imshow('RGB', crop)
cv2.waitKey(0)
cv2.destroyAllWindows()