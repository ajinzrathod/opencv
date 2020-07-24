import cv2
import numpy as np


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # iteraing through every contours
    for cnt in contours:
        area = cv2.contourArea(cnt)
        cv2.drawContours(imgContour, cnt, -1, (0, 255, 255), 3)

        # if area > 500:
        #     peri = cv2.arcLength(cnt, True)  # True for Closed Shapes
        #     approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        #     print(len(approx))
        #     objCorners = len(approx)
        #     x, y, width, height = cv2.boundingRect(approx)
        #     cv2.rectangle(imgContour, (x, y), (x + width, y + height), (255, 0, 0), 2)

        #     if objCorners == 3:
        #         objectType = "Triangle"
        #     elif objCorners == 4:
        #         aspRatio = width / float(height)

        #         if aspRatio > 0.80 and aspRatio < 1.20:
        #             objectType = "Square"
        #         else:
        #             objectType = "Rectangle"

        #     elif objCorners == 5:
        #         objectType = "Penta"
        #     elif objCorners > 5:
        #         objectType = "Circle"
        #     else:
        #         objectType = "None"
        #     cv2.putText(imgContour, objectType,
        #                 (x, y + 15), cv2.FONT_HERSHEY_COMPLEX, 0.7,
        #                 (255, 255, 255), 2)


path = 'resources/shapes.png'
originalImage = cv2.imread(path)
imgContour = originalImage.copy()
imgContour = cv2.resize(imgContour, (720, 480))

# Converting to Gray Scale
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

# Resizing Image
grayImage = cv2.resize(grayImage, (720, 480))

# Applying GaussianBlur removes noise from image.
# I have not done in this code

# Creating Canny Image
cannyImage = cv2.Canny(grayImage, 200, 200)
getContours(cannyImage)

# Showing Final Image
# cv2.imshow("Gray Image", cannyImage)
cv2.imshow("Contour Image", imgContour)

cv2.waitKey(0)
