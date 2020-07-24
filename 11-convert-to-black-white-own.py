import numpy as np
import cv2


img = cv2.imread("resources/shapes.png")

val = (255 + 255 + 255) // 2
val = 200

img = cv2.resize(img, (480, 360))

a = -1
for x in img:
    a += 1
    b = -1
    for y in x:
        b += 1
        for z in y[:1]:
            tot = 0

            for c in range(3):
                # To int because img is numpy uint8(max val: 255)
                # And total might be > 255
                tot += int(img[a, b, c])

            if tot > val:
                for c in range(3):
                    img[a, b, c] = 255
            else:
                for c in range(3):
                    img[a, b, c] = 0

cv2.imshow("Image", img)
cv2.waitKey(0)
