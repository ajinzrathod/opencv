import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('resources/shapes.png', 1)

    # oldWidth, oldHeight = img.shape[0], img.shape[1]
    # print(oldWidth, oldHeight)

    # aspectedWidth = 360
    # aspectedHeight = 480

    # timesBigger = 1
    # if oldWidth > aspectedWidth:
    #     timesBigger = oldWidth // aspectedWidth

    # if oldHeight > aspectedHeight:
    #     timesBigger = oldHeight // aspectedHeight

    # newWidth = oldWidth // timesBigger
    # newHeight = oldHeight // timesBigger

    # img = cv2.resize(img, (newWidth, newHeight))
    # print(img.size)

    # img = cv2.resize(img, (360, 480))

    # cannyImage = cv2.Canny(img, 100, 100)
    # cv2.imshow("Real Image", cannyImage)
    cv2.imshow("Real Image", img)
    cv2.waitKey(0)
