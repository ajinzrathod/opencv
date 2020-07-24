import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


# http://www.labbookpages.co.uk/software/imgProc/otsuThreshold.html
# https://docs.opencv.org/master/d7/d4d/tutorial_py_thresholding.html

img = cv.imread("../resources/noisy2.png", 0)

# Global thresholding by 127
ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# Otsu on Original Image
ret, th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

# Working with Noisy Image
blurredImg = cv.GaussianBlur(img, (5, 5), cv.BORDER_REPLICATE)
# 1. Global Threshold
ret, th3 = cv.threshold(blurredImg, 119, 255, cv.THRESH_BINARY)
# 1. Otsu Threshold
ret, th4 = cv.threshold(blurredImg, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

print(ret)

images = [img, th1, th2, blurredImg, th3, th4]
titles = ["Original Image", "Global Threshold", "Otsu Method", \
          "Blurred Image", "Global Threshold", "Otsu Method"]

for x in range(len(images)):
    plt.subplot(2, 3, x + 1), plt.imshow(images[x], 'gray')
    plt.title(titles[x])
    plt.xticks([]), plt.yticks([])

plt.show()
