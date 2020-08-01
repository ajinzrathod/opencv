import cv2
import numpy as np
from matplotlib import pyplot as plt


if __name__ == '__main__':
    img1 = cv2.imread('../resources/shapes.png')

    x, y, w, h = 150, 50, 300, 175

    sub_img = img1[y:y + h, x: x + w]

    rect = np.zeros(sub_img.shape, dtype=np.uint8)

    # WHITE color is `important` data and BLACK color is `unwanted` data
    # So, BETA argument in `addWeighted` does NOT matter if background is BLACK

    # res = cv2.addWeighted(sub_img, .75, rect, .5, 1.0)  # For WHITE BG
    res = cv2.addWeighted(sub_img, .25, rect, .5, 1.0)  # For BLACK BG

    img1[y:y+h, x:x+w] = res

    plt.subplot(1, 1, 1),
    plt.imshow(cv2.cvtColor(img1, 4), 'gray')
    plt.show()
