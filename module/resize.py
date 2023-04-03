import numpy as np
import cv2
from cv2 import imread

# read the image
img = imread('image_capture/captured_img.png')

# to resize 30x30
img = cv2.resize(img, (30, 30))

# resize to 90x90
img2 = cv2.resize(img, (90, 90))

# resize to 120x120
img3 = cv2.resize(img, (120, 120))

# show the image
cv2.imshow('RGB', img)
cv2.imshow('90x90', img2)
cv2.imshow('120x120', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()