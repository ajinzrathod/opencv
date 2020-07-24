# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


#  Loading Image in Grayscale
img = cv.imread("../resources/shapes.png", 0)

# Converting image to GaussianBlur
gBlur = cv.GaussianBlur(img, (5, 5), cv.BORDER_REPLICATE)

# Finding Th Value
max_th, _ = cv.threshold(img, 0, 255, 0 + cv.THRESH_OTSU)
min_th = max_th * 0.5

# Applying Canny Edge Detection
cannyImage = cv.Canny(gBlur, min_th, max_th)

# Finding Contours
contours, hierchy = cv.findContours(cannyImage, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
cnt = contours[0]

M = cv.moments(cnt)

for key, values in M.items():
    print("{0:>10}{1:>25}".format(key, values))

area = cv.contourArea(cnt)

# Contour Perimiter
# It is also called arc length.
# It can be found out using cv2.arcLength() function.
# Second argument specify whether shape
# It is a closed contour (if passed True), or just a curve.

perimiter = cv.arcLength(cnt, True)
print(area, perimiter)

images = [img, gBlur, cannyImage]
titles = ["Original", "GBlurred", "Canny"]

for x in range(len(images)):
    plt.subplot(2, 2, x + 1), plt.imshow(images[x], 'gray')
    plt.title(titles[x])
    plt.xticks([]), plt.yticks([])

plt.show()
