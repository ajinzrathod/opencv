import numpy as np
import cv2


# path fo image
path = "../resources/1.jpg"

# Setting Font
font = cv2.FONT_HERSHEY_COMPLEX

# reading grayscale image
img = cv2.imread(path, 0)

# Threshold
# If value < 127, pixel is 0
# If value > 127, pixel is 200

# Thresh Binary
ret, thresh1 = cv2.threshold(img, 127, 200, cv2.THRESH_BINARY)
cv2.putText(thresh1, "Binary Image", (50, 50), font, 1.8, (127), 3)
# cv2.imshow("image1", thresh1)


# Thresh Binary Inverse
ret, thresh2 = cv2.threshold(img, 127, 200, cv2.THRESH_BINARY_INV)
cv2.putText(thresh2, "Binary Image Inv", (50, 50), font, 1.8, (127), 3)
# cv2.imshow("image2", thresh2)


# Thresh Binary Trunc
# Values less than 127 will not change,
# and values more than 127 will be 127
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
cv2.putText(thresh3, "Trunc", (50, 50), font, 1.8, (0), 3)
# cv2.imshow("image3", thresh3)


# thresh to zero INverse
# Values more than 127 will be 0
# and values less than 127 will be same
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
cv2.putText(thresh4, "To Zero", (50, 50), font, 1.8, (127), 3)
# cv2.imshow("image4", thresh4)


ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.putText(thresh5, "To Zero Inv", (50, 50), font, 1.8, (127), 3)
# cv2.imshow("image5", thresh5)

print(ret)

cv2.putText(img, "Original", (50, 50), font, 1.8, (127), 3)

hori1 = np.concatenate((img, thresh1, thresh2), axis=1)
hori2 = np.concatenate((thresh3, thresh4, thresh5), axis=1)
vertical = np.concatenate((hori1, hori2), axis=0)

cv2.namedWindow("Display Frame", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Display Frame", 1200, 800)
cv2.imshow("Display Frame", vertical)


# Saving Image
cv2.imwrite("Simple.jpg", vertical)

cv2.waitKey(0)
cv2.destroyAllWindows()
