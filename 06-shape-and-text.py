import cv2
import numpy as np


# Creating simple black image
img = np.zeros((512, 512, 3), np.uint8)

# Printing Shape
print(img.shape)

# Showing Image
# cv2.imshow("Black Image", img)

# Coloring Image
img[100: 200, 300: 400] = 0, 0, 255
# cv2.imshow("Colored Image", img)

# Drawing Line
cv2.line(img, (0, 0), (512, 512), (0, 255, 0), 3)
# cv2.imshow("Lined Image", img)

# Drawing Rectangle
cv2.rectangle(img, (0, 0), (img.shape[1], img.shape[0]), (255, 0, 0), 20)
cv2.rectangle(img, (300, 300), (img.shape[1], img.shape[0]), (255, 0, 0), cv2.FILLED)
# cv2.imshow("Rectangled Image", img)


# Drawing Circle
cv2.circle(img, (120, 300), 80, (200, 120, 34), 10)
# cv2.imshow("Rectangled Image", img)

# Writing on Images
cv2.putText(img, "Open CV2", (200, 200), cv2.FONT_HERSHEY_COMPLEX, 1.8, (200, 123, 221), 4)
cv2.imshow("Rectangled Image", img)

# Waiting
cv2.waitKey(0)
