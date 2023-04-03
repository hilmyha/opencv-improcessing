import numpy as np
import cv2
from cv2 import imread

# read the image
img = imread('image_capture/captured_img.png')

# rotate the image
rows, cols, ch = img.shape
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
dst = cv2.warpAffine(img, M, (cols, rows))

# show the image
cv2.imshow('RGB', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()