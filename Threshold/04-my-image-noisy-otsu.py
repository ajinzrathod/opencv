import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img1 = cv.imread("../resources/noisy2.png", 0)
img2 = cv.imread("../resources/noisy3.png", 0)

_ = [img1, img2]

for img in _:

    # Global thresholding by 127
    ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

    # Otsu on Original Image
    ret, th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    # Working with Blurred Image
    blurredImg = cv.GaussianBlur(img, (5, 5), cv.BORDER_REPLICATE)
    # 1. Global Threshold
    ret, th3 = cv.threshold(blurredImg, 127, 255, cv.THRESH_BINARY)
    # 2. Otsu Threshold
    ret, th4 = cv.threshold(blurredImg, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    # 3. Adaptive Threshold
    th5 = cv.adaptiveThreshold(blurredImg, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, \
                               cv.THRESH_BINARY, 5, 7)
    th6 = cv.adaptiveThreshold(blurredImg, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, \
                               cv.THRESH_BINARY, 25, 3)

    print(ret)

    images = [img, th1, th2, blurredImg, th3, th4, th5, th6]
    titles = ["Original Image", "Global Threshold", "Otsu Method", \
              "Blurred Image", "Global Threshold", "Otsu Method", \
              "Adaptive1( on Blurred)", "Adaptive2( on Blurred)"]

    for x in range(len(images)):
        plt.subplot(3, 3, x + 1), plt.imshow(images[x], 'gray')
        plt.title(titles[x])

    plt.show()
