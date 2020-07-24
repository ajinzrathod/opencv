
# https://docs.opencv.org/4.4.0/dd/d49/tutorial_py_contour_features.html
import cv2 as cv
import numpy as np
from plotimages import plotImages as plImg
from grayBlurCanny import grayGBlurCanny as edges


if __name__ == '__main__':
    originalImg = cv.imread("../resources/shapes.png")
    img = edges(originalImg)

    contours, _ = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 100:
            (x, y), radius = cv.minEnclosingCircle(cnt)
            center = (int(x), int(y))
            radius = int(radius)
            cv.circle(originalImg, center, radius, (0, 255, 0), 2)

    images = [originalImg]
    titles = ["Image"]

    plImg(images, titles)
