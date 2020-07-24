import cv2
import numpy as np


imagePath = 'resources/smarties.png'

while True:
    img = cv2.imread(imagePath)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lowerLimits = np.array([110, 50, 50])
    upperLimits = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lowerLimits, upperLimits)

    cv2.imshow("Original Image", img)
    cv2.imshow("HSV Image", hsv)
    cv2.imshow("Mask Image", mask)

    key = cv2.waitKey(1)
    if key == 27 or key == ord('q'):
        break

cv2.destroyAllWindows()
