import numpy as np
import cv2
from cv2 import imread

# read the image
img = imread('image_capture/captured_img.png')

# split the image into color channels
(b, g, r) = cv2.split(img)

# merge the image back together
merged = cv2.merge([b, g, r])

# concatenate the images along the x-axis
# (i.e., from left to right)
concatenated = np.concatenate([b, g, r], axis=1)

# show the image
cv2.imshow('Blue', concatenated)
cv2.imshow('Merged', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()