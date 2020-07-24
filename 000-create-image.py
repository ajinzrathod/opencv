import cv2
import numpy as np


# default white Image
array = np.full((512, 512, 3), (255, 255, 255), np.uint8)

# NumPy 1.8 introduced np.full(),
# which is a more direct method than empty() followed by fill()
# for creating an array filled with a certain value:


cv2.imshow("My Image", array)
cv2.waitKey(0)


# default Black Image
array = np.zeros((512, 512, 3), np.uint8)
cv2.imshow("My Image", array)
cv2.waitKey(0)
