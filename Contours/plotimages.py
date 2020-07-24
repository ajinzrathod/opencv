import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def plotImages(imagesList, titleList):
    length = len(imagesList)
    i = 2
    if length == 1:
        i = 1
        j = 1
    elif length == 2:
        i = 1
        j = 2
    else:
        j = length // 2

    for x in range(len(imagesList)):
        imagesList[x] = cv.cvtColor(imagesList[x], cv.COLOR_BGR2RGB)
        plt.subplot(i, j, x + 1), plt.imshow(imagesList[x], 'gray')
        plt.title(titleList[x])
        plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    pass
