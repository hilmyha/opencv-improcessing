import numpy as np
import cv2
from cv2 import imread

# read the image
img = imread('image_capture/captured_img.png')

# to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# show the image
cv2.imshow('RGB', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()