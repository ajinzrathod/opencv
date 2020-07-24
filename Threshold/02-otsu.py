import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("../resources/1.jpg", 0)

ret, thresh1 = cv2.threshold(img, 0, 200, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

ret, thresh2 = cv2.threshold(img, 0, 200, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

ret, thresh3 = cv2.threshold(img, 0, 255, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)

ret, thresh4 = cv2.threshold(img, 0, 255, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)

ret, thresh5 = cv2.threshold(img, 0, 255, cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU)

titles = ['Img', 'Binary', 'Binary Inv', 'Trunc', 'To Zero', 'To Zero Inv']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])


###########################################################
# plt.show() shows following error.

# UserWarning: Matplotlib is currently using agg,
# which is a non-GUI backend, so cannot show the figure

# To Remove this error,
#  ======= sudo apt-get install python3-tk =======

plt.show()
############################################################
