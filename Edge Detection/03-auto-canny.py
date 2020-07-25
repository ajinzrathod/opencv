import numpy as np
import cv2 as cv

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
    pass
