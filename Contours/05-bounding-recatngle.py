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
            cv.drawContours(originalImg, cnt, -1, (255, 255, 255), 3)
            perimiter = cv.arcLength(cnt, True)  # True for closed contour
            eplison = 0.01 * cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, eplison, True)
            print(len(approx))

            x, y, w, h = cv.boundingRect(cnt)
            cv.rectangle(originalImg, (x, y), (x + w, y + h), (0, 0, 255), 3)

    images = [originalImg]
    titles = ["Image"]

    plImg(images, titles)
