# https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html

# Contours can be explained simply as a curve
# joining all the continuous points (along the boundary),
# having same color or intensity.
# The contours are a useful tool for
# shape analysis and object detection and recognition.


# For better accuracy, use binary images.
# So before finding contours, apply threshold or canny edge detection

#########################################################
# UnCommenting Laplacian code shows how slow Laplacian is
#########################################################


import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from laplacian_zero_crossing import Zero_crossing as Lap_zero

# Loading in Grayscale
originalImg1 = cv.imread("../resources/shapes.png")
# originalImg2 = originalImg1.copy() # For Laplacian

print(originalImg1.shape)

cv.resize(originalImg1, (50, 50))
# cv.resize(originalImg2, (50, 50)) # For Laplacian

img = cv.imread("../resources/shapes.png", 0)

# GaussianBlur
blurredImg = cv.GaussianBlur(img, (5, 5), cv.BORDER_REPLICATE)

# Otsu Threshold
ret, th = cv.threshold(img, 0, 255, 0 + cv.THRESH_OTSU)

# Laplacian
# laplacian = cv.Laplacian(blurredImg, cv.CV_8U)
# laplacian = Lap_zero(laplacian)

# Finding Contours
cntrs1, hierchy = cv.findContours(th, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# cntrs2, hierchy = cv.findContours(laplacian, cv.RETR_TREE, cv.CHAIN_APPROX_NONE) # For Laplacian

# Draw Contours
for cnt in cntrs1:
    cv.drawContours(originalImg1, cnt, -1, (255, 255, 255), 10)
# for cnt in cntrs2: # For Laplacian
#    cv.drawContours(originalImg2, cnt, -1, (255, 255, 255), 20)

# Showing Images with plt
images = [originalImg1, img, blurredImg, th]
titles = ["img", "gray image", "blurredImg", "Otsu"]

# images = [originalImg1, originalImg2, img, blurredImg, th, laplacian] # For Laplacian
# titles = ["img1", "img2", "gray image", "blurredImg", "Otsu", "Laplacian"] # For Laplacian

# images = [originalImg1, originalImg2]
# titles = ["img1", "img2"]

for x in range(len(images)):
    plt.subplot(2, 2, x + 1), plt.imshow(images[x], 'gray')
    plt.title(titles[x])
    plt.xticks([]), plt.yticks([])

plt.show()
