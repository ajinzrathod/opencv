import cv2 as cv
from matplotlib import pyplot as plt


# priority, crop || resize

img1 = cv.imread("../resources/shapes.png")
img2 = cv.imread("../resources/ajinkya.png")

# Checking for invalid Images
if img1 is None or img2 is None:
    print("Invalid Img")
    exit(1)

# Finding Shape of Image1
data1 = ()
data1 = img1.shape
pixels1 = data1[0] * data1[1]

# Finding Shape of Image1
data2 = ()
data2 = img2.shape
pixels2 = data2[0] * data2[1]

# Resizing the bigger image to smaller one
if pixels1 > pixels2:
    img1 = cv.resize(img1, (data2[0], data2[1]))
    if img1 != img2:
        img1 = cv.resize(img1, (data2[1], data2[0]))
    print("Resizing Image1")
elif pixels2 > pixels1:
    img2 = cv.resize(img2, (data1[0], data1[1]))
    if img1 != img2:
        img2 = cv.resize(img2, (data1[1], data1[0]))
    print("Resizing Image2")

# Finding New Shape
data1 = img1.shape
data2 = img2.shape

# Checking if Shape is same
if data1 != data2:
    print("Not Converted to same size")

# Adding Images
add = cv.add(img2, img1)

# Showing Images using plt
images = [img1, img2, add]
titles = ("img1", "img2", "add")

for x in range(len(images)):
    # 4 -> cv.COLOR_BGR2RGB
    images[x] = cv.cvtColor(images[x], 4)
    plt.subplot(2, 2, x + 1), plt.imshow(images[x], 'gray')
    plt.title(titles[x])
plt.show()
