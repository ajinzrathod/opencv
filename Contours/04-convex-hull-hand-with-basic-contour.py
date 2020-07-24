import cv2 as cv
import numpy as np
from plotimages import plotImages as plImg
from grayBlurCanny import grayGBlurCanny as edges


if __name__ == '__main__':
    # cap = cv.VideoCapture(0)
    # while True:
        # ret, originalImg = cap.read()

        originalImg = cv.imread("../resources/hand3.jpg")
        img = edges(originalImg)

        contours, hrchy = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        # Acc to opencv docs
        # https://docs.opencv.org/4.4.0/dd/d49/tutorial_py_contour_features.html
        # hull = cv.convexHull(points[, hull[, clockwise[, returnPoints]]
        hull = [cv.convexHull(c) for c in contours]
        for h in hull:
            # if cv.isContourConvex(h):
                print(cv.contourArea(h))
                final = cv.drawContours(originalImg, hull, -1, (0, 0, 0), 5)

        images = [img, originalImg]
        titles = ["Edged Image", "Original Image"]

        plImg(images, titles)
        # cv.imshow("Result", originalImg)

        # key = cv.waitKey(30)
        # if key == ord('q'):
        #     break

    # cv.destroyAllWindows()
