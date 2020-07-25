import numpy as np
import cv2 as cv
import autoCV


path = ("../resources/shapes.png")

originalImg = cv.imread(path)
originalImg = autoCV.resizeImg(originalImg, 720, 480)

img = cv.cvtColor(originalImg, cv.COLOR_BGR2GRAY)

img = cv.GaussianBlur(img, (3, 3), cv.BORDER_REPLICATE)

img = autoCV.autoCanny(img)

contours = autoCV.findAndDrawContours(img, originalImg, (255, 255, 255), 3, 1000)

cv.imshow("Image", contourImg)
cv.waitKey(0)
