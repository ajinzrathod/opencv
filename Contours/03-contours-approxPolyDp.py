import cv2 as cv
import numpy as np
from plotimages import plotImages as plImg
from grayBlurCanny import grayGBlurCanny as edges

if __name__ == '__main__':
    originalImg = cv.imread("../resources/shapes.png")
    # originalImg = cv.imread("../resources/6.jpg")
    # originalImg = cv.imread("../resources/noisy3.png")
    # originalImg = cv.imread("../resources/imperfect_square2.png")
    img1 = edges(originalImg, False)
    img2 = edges(originalImg, True)  # True is for erode

    # for img in [img1, img2]:
    for img in [img1]:
        contours, hierchy = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        # cv.drawContours(originalImg, contours, -1, (0, 0, 255), 3)
        for cnt in contours:
            if cv.contourArea(cnt) > 1000:
                print(cv.contourArea(cnt))
                cv.drawContours(originalImg, cnt, -1, (0, 0, 255), 7)
                epsilon = 0.1 * cv.arcLength(cnt, True)
                approx = cv.approxPolyDP(cnt, epsilon, True)
                print(len(approx))

        images = [img, originalImg]
        titles = ["Edged Image", "Original Image"]

        plImg(images, titles)
