import cv2
import numpy as np


def nothing(x):
    pass

cv2.namedWindow("Trackbars")
cap = cv2.VideoCapture(0)

cap.set(3, 360)
cap.set(4, 480)

cv2.createTrackbar("Low-Hue", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("Low-Sat", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Low-Val", "Trackbars", 0, 255, nothing)

cv2.createTrackbar("High-Hue", "Trackbars", 255, 179, nothing)
cv2.createTrackbar("High-Sat", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("High-Val", "Trackbars", 255, 255, nothing)


while True:
    res, frame = cap.read()

    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_hue = cv2.getTrackbarPos("Low-Hue", "Trackbars")
    low_sat = cv2.getTrackbarPos("Low-Sat", "Trackbars")
    low_val = cv2.getTrackbarPos("Low-Val", "Trackbars")

    high_hue = cv2.getTrackbarPos("High-Hue", "Trackbars")
    high_sat = cv2.getTrackbarPos("High-Sat", "Trackbars")
    high_val = cv2.getTrackbarPos("High-Val", "Trackbars")

    lowerLimit = np.array([low_hue, low_sat, low_val])
    upperLimit = np.array([high_hue, high_sat, high_val])

    mask = cv2.inRange(hsvFrame, lowerLimit, upperLimit)

    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("Real frame", frame)
    cv2.imshow("Mask frame", mask)
    cv2.imshow("result", result)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
