import cv2 as cv
from math import sqrt
import numpy as np


def fourSides(approx, wCenter, hCenter, realImg, w, h):
    # quadrant1, quadrant2, quadrant3, quadrant4 = ([] for i in range(4))
    quadrant1, quadrant2, quadrant3, quadrant4 = [], [], [], []
    textPts1, textPts2, textPts3, textPts4 = (None for i in range(4))

    for point in approx:
        pt = tuple(point[0])
        point = tuple(point.flatten())
        dist = sqrt(((point[0]-wCenter)**2) + ((point[1]-hCenter)**2))
        dist = round(dist, 2)

        if point[0] >= wCenter and point[1] <= hCenter:
            cv.circle(realImg, pt, 2, (255, 255, 255), 5)
            quadrant1.append(dist)
            textPts1 = (wCenter + w // 4 - 10 + 30, hCenter - h // 4)

        elif point[0] < wCenter and point[1] < hCenter:
            cv.circle(realImg, pt, 2, (0, 255, 255), 5)
            quadrant2.append(dist)
            textPts2 = (wCenter - w // 4 - 10, hCenter - h // 4 - 10)

        elif point[0] <= wCenter and point[1] >= hCenter:
            cv.circle(realImg, pt, 2, (255, 0, 255), 5)
            quadrant3.append(dist)
            textPts3 = (wCenter - w // 4 - 10, hCenter + h // 4 - 10)

        elif point[0] > wCenter and point[1] > hCenter:
            cv.circle(realImg, pt, 2, (255, 255, 0), 5)
            quadrant4.append(dist)
            textPts4 = (wCenter + w // 4 - 10 + 30, hCenter + h // 4 - 10)
    print(wCenter, hCenter, textPts1)

    std1 = round(np.std(quadrant1), 2)
    std2 = round(np.std(quadrant2), 2)
    std3 = round(np.std(quadrant3), 2)
    std4 = round(np.std(quadrant4), 2)

    allS = round(np.std([std1, std2, std3, std4]), 2)

    std1 = str(round(np.std(quadrant1), 2))
    std2 = str(round(np.std(quadrant2), 2))
    std3 = str(round(np.std(quadrant3), 2))
    std4 = str(round(np.std(quadrant4), 2))

    return textPts1, textPts2, textPts3, textPts4, std1, std2, std3, std4, allS
    # if textPts1 is not None:
    #     cv.putText(realImg, std1, textPts1, cv.FONT_HERSHEY_DUPLEX,
    #                .5, (0, 0, 0), 1)
    # if textPts2 is not None:
    #     cv.putText(realImg, std2 + ",", textPts2, cv.FONT_HERSHEY_DUPLEX,
    #                .5, (0, 0, 0), 1)
    # if textPts3 is not None:
    #     cv.putText(realImg, std3 + ",", textPts3, cv.FONT_HERSHEY_DUPLEX,
    #                .5, (0, 0, 0), 1)
    # if textPts4 is not None:
    #     cv.putText(realImg, std4, textPts4, cv.FONT_HERSHEY_DUPLEX,
    #                .5, (0, 0, 0), 1)

if __name__ == '__main__':
    approx = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
