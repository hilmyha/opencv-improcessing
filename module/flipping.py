import numpy as np
import cv2
from cv2 import imread

# read the image
img = imread('image_capture/captured_img.png')

# flip the image
flip = cv2.flip(img, 1)

# show the image
cv2.imshow('RGB', flip)
cv2.waitKey(0)
cv2.destroyAllWindows()