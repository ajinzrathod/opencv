import cv2 as cv
import numpy as np


path = "../resources/shapes2.png"
src = realImg = cv.imread(path)

gray = cv.cvtColor(realImg, 6)

gray = cv.medianBlur(gray, 5)

rows = gray.shape[0]
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 16,
                          param1=255, param2=24, minRadius=1, maxRadius=300)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for c in circles[0, :]:
        center = (c[0], c[1])
        cv.circle(realImg, center, 1, (0, 100, 100), 3)
        radius = c[2]
        cv.circle(realImg, center, radius, (255, 0, 255), 3)

cv.imshow("Image", realImg)
cv.waitKey(0)
