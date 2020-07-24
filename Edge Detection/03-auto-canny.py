import numpy as np
import cv2 as cv
from autoreshape import *
from matplotlib import pyplot as plt
from scipy import stats


def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)
    std = np.std(image)
    print("{0:.2f}".format(std))

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v) + (std * .75))
    upper = int(min(255, (1.0 + sigma) * v) + std)

    print(lower, upper)
    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    return edged

if __name__ == '__main__':
    path = "../resources/1.jpg"
    path = "../resources/noisy3.png"
    print(path)
    img = cv.imread(path, 0)
    img = resizeImg(img)
    cv.imshow("asd", img)
    cv.waitKey(0)

    img = resizeImg(img)
    # print(img.shape[0], img.shape[1])

    # plt.hist(img.ravel(), 265, [0, 256])
    # plt.show()

    cv.imshow("Img", auto_canny(img))
    cv.waitKey(0)
