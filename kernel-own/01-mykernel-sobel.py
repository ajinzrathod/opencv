# CREDITS
# https://www.codingame.com/playgrounds/2524/basic-image-manipulation/filtering
from PIL import Image, ImageDraw
from math import sqrt
import cv2 as cv


# Load image:
input_image = Image.open("../resources/6.jpg")
width, height = input_image.size

# Resizing height
new_width = 360
new_height = int(new_width * height / width)

# Resizing width
new_height = 480
new_width = int(new_height * width / height)

# Resizing Image
input_image = input_image.resize((new_width, new_height), Image.ANTIALIAS)

# Loading Pixels
input_pixels = input_image.load()

# Calculate pixel intensity as the average of red, green and blue colors.
intensity = [[sum(input_pixels[x, y]) / 3 for y in range(input_image.height)] for x in range(input_image.width)]

# Sobel kernels
kernelx = [[-1, 0, 1],
           [-2, 0, 2],
           [-1, 0, 1]]

kernely = [[-1, -2, -1],
           [0, 0, 0],
           [1, 2, 1]]

# Create output image
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

# Compute convolution between intensity and kernels
for x in range(1, input_image.width - 1):
    for y in range(1, input_image.height - 1):
        magx, magy = 0, 0
        for a in range(3):
            for b in range(3):
                xn = x + a - 1
                yn = y + b - 1
                magx += intensity[xn][yn] * kernelx[a][b]
                magy += intensity[xn][yn] * kernely[a][b]

        # Draw in black and white the magnitude
        color = int(sqrt(magx**2 + magy**2))
        draw.point((x, y), (color, color, color))

output_image.save("output.png")
img = cv.imread("output.png")

cv.namedWindow("output.png", cv.WINDOW_NORMAL)
cv.resizeWindow("output.png", 800, 800)

cv.imshow("output.png", img)
cv.waitKey(0)
