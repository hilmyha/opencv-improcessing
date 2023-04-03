import numpy as np
import cv2
from cv2 import imread

# read the image
img = imread('image_capture/captured_img.png')

# translate the image
rows, cols, ch = img.shape
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))

# show the image
cv2.imshow('RGB', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()