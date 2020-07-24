import cv2
import numpy as np

img = cv2.imread("resources/cards.png")

# 335, 126
# 419, 127
# 334, 253
# 420, 251

width, height = 250, 350

pts1 = np.float32([[335, 126], [419, 127], [334, 253], [420, 251]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

croppedCard = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Card Image", croppedCard)

cv2.waitKey(0)
