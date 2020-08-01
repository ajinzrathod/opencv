import cv2 as cv
import numpy as np
import autoCV


path = "../resources/too-many5.jpg"
src = realImg = cv.imread(path)

gray = cv.cvtColor(realImg, 6)

gray = cv.medianBlur(gray, 5)

gray, low, high = autoCV.autoCanny(gray, retTh=True)
print(low, high)

rows = gray.shape[0]
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 16,
                          param1=100, param2=50, minRadius=1, maxRadius=300)
# circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1,
#                           rows / 16, param1=400, param2=60)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for c in circles[0, :]:
        center = (c[0], c[1])
        cv.circle(realImg, center, 1, (0, 100, 100), 3)
        radius = c[2]
        cv.circle(realImg, center, radius, (0, 155, 0), 3)

realImg = autoCV.resizeImg(realImg)
cv.imshow("Image", realImg)
cv.waitKey(0)

