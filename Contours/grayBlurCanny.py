import numpy as np
import cv2


def grayGBlurCanny(img, erode=False):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_REPLICATE)

    # Eroding Image
    if erode:
        kernel = np.ones((5, 5), np.uint8)
        img = cv2.erode(img, kernel, iterations=10)

    th, _ = cv2.threshold(img, 0, 255, 0 + cv2.THRESH_OTSU)
    # print(th)
    canny = cv2.Canny(img, 60, 150)

    return canny

if __name__ == '__main__':
    pass
