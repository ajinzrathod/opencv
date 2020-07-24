import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread("../resources/sudoku.png", 0)

blurredImg = cv.medianBlur(img, 5)
# blurredImg = cv.GaussianBlur(img, (5, 5), cv.BORDER_REPLICATE)

# Thresholding Images

# Global Threshold
ret, th_global = cv.threshold(blurredImg, 127, 255, cv.THRESH_BINARY)

# Adaptive Threshold

# 1. ADAPTIVE_THRESH_MEAN_C
th_adap_mean1 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                    cv.THRESH_BINARY, 11, 2)

th_adap_mean2 = cv.adaptiveThreshold(blurredImg, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                    cv.THRESH_BINARY, 11, 2)

# 1. ADAPTIVE_THRESH_GUASSIAN_C
th_adap_gaus1 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                    cv.THRESH_BINARY, 11, 2)

th_adap_gaus2 = cv.adaptiveThreshold(blurredImg, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                    cv.THRESH_BINARY, 11, 2)

ret, th_otsu1 = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

ret, th_otsu2 = cv.threshold(blurredImg, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)


titles = ["Img", "Adaptive Mean", "Adaptive Gaus", "Otsu", \
          "Blur", "Adaptive Mean Blur", "Adaptive Gaus Blur", "Otsu Blur"]

images = [img, th_adap_mean1, th_adap_gaus1, th_otsu1, \
          blurredImg, th_adap_mean2, th_adap_gaus2, th_otsu2]

length = len(titles)

for x in range(length):
    plt.subplot(2, length // 2, x + 1), plt.imshow(images[x], 'gray')
    plt.title(titles[x])
    plt.xticks([]), plt.yticks([])

plt.show()
