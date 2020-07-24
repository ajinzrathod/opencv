import cv2
import numpy as np


kernel = np.ones((5, 5), np.uint8)

# Original Image
originalImage = cv2.imread("resources/1.jpg")
# cv2.imshow("Blazzer Image", originalImage)


# Converting to Gray Scale Image
# cvtColor is used to convert Image
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray Scale Image", grayImage)


# Blurred Image
blurImage = cv2.GaussianBlur(originalImage, (5, 5), cv2.BORDER_REPLICATE)
# cv2.imshow("Blured Image", blurImage)


# Canny Image
cannyImage = cv2.Canny(originalImage, 200, 200)
# cv2.imshow("Canny Image", cannyImage)


# Dilalate Image
dilate = cv2.dilate(originalImage, kernel, iterations=3)
cv2.imshow("Dilate Image", dilate)


# Erode Image
erode = cv2.erode(originalImage, kernel, iterations=1)
# cv2.imshow("Erode Image", erode)


cv2.waitKey(0)
