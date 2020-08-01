import cv2 as cv
import autoCV
from matplotlib import pyplot as plt


if __name__ == '__main__':
    # Reading Image
    realImg = cv.imread("../resources/circle4.png")
    realImg = cv.imread("../resources/shapes.png")

    # Converting to GrayScale Mode
    grayImg = cv.cvtColor(realImg, 6)

    # Applying GaussianBlur To remove noise
    grayImg = cv.GaussianBlur(grayImg, (5, 5), 1)

    # Applying Canny Edge Detector
    grayImg = autoCV.autoCanny(grayImg)

    # RETR_EXTERNAL = 0, CHAIN_APPROX_SIMPLE = 2
    contours, _ = cv.findContours(grayImg, 0, 2)

    autoCV.detectObject.drawShapes(contours, realImg, name=True)

    # Convert 3 Channel image to RGB because plt reads in RGB
    realImg = cv.cvtColor(realImg, cv.COLOR_BGR2RGB)

    # Displaying Image
    plt.subplot(1, 1, 1), plt.imshow(realImg, 'gray')
    plt.show()
