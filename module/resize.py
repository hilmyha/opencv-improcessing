import numpy as np
import cv2
from cv2 import imread
import matplotlib.pyplot as plt

# read the image
img = imread('image_capture/captured_img.png')

# to resize 30x30
img1 = cv2.resize(img, (30, 30))

# resize to 90x90
img2 = cv2.resize(img, (90, 90))

# resize to 120x120
img3 = cv2.resize(img, (120, 120))

# show the image using matplotlib
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
plt.show()