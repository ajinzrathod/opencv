import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Reading Image in Grayscale Mode
img1 = cv.imread("../resources/1.jpg", 0)
img2 = cv.imread("../resources/6.jpg", 0)
img3 = cv.imread("../resources/cards.png", 0)
img4 = cv.imread("../resources/messi5.jpg", 0)
img5 = cv.imread("../resources/noisy2.png", 0)
img6 = cv.imread("../resources/noisy3.png", 0)
img7 = cv.imread("../resources/smarties.png", 0)
img8 = cv.imread("../resources/sudoku.png", 0)

img_list = [img1, img2, img3, img4, img5, img6, img7, img8]

cnt = 0
for img in img_list:
    cnt += 1

    # Applying GaussianBlur
    blurredImg = cv.GaussianBlur(img, (5, 5), cv.BORDER_REPLICATE)

    # Laplacian
    laplacian = cv.Laplacian(blurredImg, cv.CV_8U)
    # laplacian = cv.convertScaleAbs(laplacian)

    # Creating list of images and titles if those images
    images = [img, blurredImg, laplacian]
    titles = ["Img : " + str(cnt), "blurredImg : " + str(cnt), "Laplacian : " + str(cnt)]

    # Plotting images through pyplot
    for x in range(len(images)):
        plt.subplot(1, 3, x + 1), plt.imshow(images[x], 'gray')
        plt.title(titles[x])
        plt.xticks([]), plt.yticks([])

    # Displaying Plotted images
    plt.show()
