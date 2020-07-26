import cv2 as cv
import autoCV


path = ("../resources/smarties.png")

realImg = cv.imread(path)

img = cv.cvtColor(realImg, cv.COLOR_BGR2GRAY)

img = cv.GaussianBlur(img, (5, 5), cv.BORDER_REPLICATE)

img = autoCV.autoCanny(img)

minArea = 50

# contours = autoCV.findAndDrawContours(img, realImg, (255, 255, 255), 3, minArea)

contours, _ = cv.findContours(img, 0, 1)

autoCV.detectObject.drawShapes(contours, realImg, (255, 255, 255), 2, minArea, True)

realImg = autoCV.resizeImg(realImg, 540, 480)

cv.imshow("Image2", realImg)
cv.waitKey(0)
