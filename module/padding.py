import numpy as np
import cv2
from cv2 import imread

# read the image
img = imread('image_capture/captured_img.png')

# padding
pad = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=[0, 0, 0])

# show the image
cv2.imshow('RGB', pad)
cv2.waitKey(0)
cv2.destroyAllWindows()