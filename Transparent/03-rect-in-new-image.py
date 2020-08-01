import cv2
import numpy as np
from matplotlib import pyplot as plt


if __name__ == '__main__':
    img = cv2.imread('../resources/messi5.jpg')
    # img = cv2.imread('../resources/circle4.png')

    blk = np.full(img.shape, 255, np.uint8)

    # Draw rectangles
    cv2.rectangle(blk, (150, 50), (300, 175), (0, 0, 0), cv2.FILLED)
    cv2.imshow("blk", blk)
    cv2.waitKey()

    out = cv2.addWeighted(img, 1, blk, 0.5, 1)

    plt.subplot(1, 1, 1),
    plt.imshow(cv2.cvtColor(out, 4), 'gray')
    plt.show()
