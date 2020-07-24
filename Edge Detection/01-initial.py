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

img_list = [img1, img2, img3, img4, img5, img6, img7]

cnt = 0
for img in img_list:
    cnt += 1
    # Applying GaussianBlur
    img = cv.GaussianBlur(img, (5, 5), cv.BORDER_REPLICATE)

    # Deciding Threshholds
    high_th, _ = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    # My Logic. Dont know true or not.  Just Worked on images of this folder
    if high_th > 200:
        high_th = 200
    elif high_th < 150:
        high_th += 100
    # My Logic Ends

    low_th = high_th * 0.5  # This logic is of Stack Overflow

    print(low_th, high_th)

    # Converting image to Canny
    default_canny = cv.Canny(img, 100, 200)

    # +50, +100 is my algo. Not of net,
    # Found better result if +50, +100
    auto_canny = cv.Canny(img, low_th, high_th)

    # Creating list of images and titles if those images
    images = [img, default_canny, auto_canny]
    titles = ["Img: " + str(cnt), "Th 100-200: " + str(cnt), "Auto Th: " + str(cnt)]

    # Plotting images through pyplot
    for x in range(len(images)):
        plt.subplot(1, 3, x + 1), plt.imshow(images[x], 'gray')
        plt.title(titles[x])
        plt.xticks([]), plt.yticks([])

    # Displaying Plotted images
    plt.show()
