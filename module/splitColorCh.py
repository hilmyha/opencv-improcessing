import numpy as np
import cv2
from cv2 import imread
import matplotlib.pyplot as plt

# read the image
img = imread('image_capture/captured_img.png')

# split the image into color channels
b, g, r = cv2.split(img)

# visualize each color channel
zeros = np.zeros(img.shape[:2], dtype='uint8')

# show the split image using matplotlib
plt.subplot(221), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(cv2.merge([zeros, zeros, r])), plt.title('Blue')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(cv2.merge([zeros, g, zeros])), plt.title('Green')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(cv2.merge([b, zeros, zeros])), plt.title('Red')
plt.xticks([]), plt.yticks([])
plt.show()