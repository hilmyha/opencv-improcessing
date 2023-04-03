import numpy as np
import cv2
from cv2 import imread

# read the image
img = imread('image_capture/captured_img.png')

# affine transform
rows, cols, ch = img.shape
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))

# show the image
cv2.imshow('RGB', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()