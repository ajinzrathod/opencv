# https://docs.opencv.org/4.4.0/dd/d49/tutorial_py_contour_features.html
import cv2 as cv
import numpy as np
from plotimages import plotImages as plImg
from grayBlurCanny import grayGBlurCanny as edges


if __name__ == '__main__':
    originalImg = cv.imread("../resources/noisy3.png")
    img = edges(originalImg)

    contours, _ = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 100:
            rows, cols = img.shape[:2]
            [vx, vy, x, y] = cv.fitLine(cnt, cv.DIST_L2, 0, 0.01, 0.01)
            lefty = int((-x * vy / vx) + y)
            righty = int(((cols - x) * vy / vx) + y)
            cv.line(originalImg, (cols - 1, righty), (0, lefty), (255, 255, 255), 2)

    images = [originalImg]
    titles = ["Image"]

    plImg(images, titles)
