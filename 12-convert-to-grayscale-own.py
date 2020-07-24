import numpy as np
import cv2


if __name__ == '__main__':
    img = cv2.imread("resources/6.jpg")
    height, width, trash = img.shape

    grayImage = np.ones([height * width], np.uint8)

    count = 0
    i = 0
    for x in img.flatten():
        if count == 0:
            blue = x * 0.11
        elif count == 1:
            green = x * 0.59
        elif count == 2:
            red = x * 0.30

        if count == 2:
            grayImage[i] = blue + green + red
            count = -1

            i += 1

        count += 1

    grayImage = np.reshape(grayImage, [height, width, 1])

    cv2.imshow("GrayImage", grayImage)
    cv2.waitKey(0)
