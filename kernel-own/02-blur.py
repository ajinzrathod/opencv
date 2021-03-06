from PIL import Image, ImageDraw
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

# Box Blur kernel
box_kernel = [[1 / 9, 1 / 9, 1 / 9],
              [1 / 9, 1 / 9, 1 / 9],
              [1 / 9, 1 / 9, 1 / 9]]

# Gaussian kernel
gaussian_kernel = [[1 / 256,  4 / 256,  6 / 256,  4 / 256, 1 / 256],
                   [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
                   [6 / 256, 24 / 256, 36 / 256, 24 / 256, 6 / 256],
                   [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
                   [1 / 256,  4 / 256,  6 / 256,  4 / 256, 1 / 256]]


# Select kernel here:
kernel = gaussian_kernel

# Middle of the kernel
offset = len(kernel) // 2

# Create output image
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

# Compute convolution between intensity and kernels
for x in range(offset, input_image.width - offset):
    for y in range(offset, input_image.height - offset):
        acc = [0, 0, 0]
        for a in range(len(kernel)):
            for b in range(len(kernel)):
                xn = x + a - offset
                yn = y + b - offset
                pixel = input_pixels[xn, yn]
                acc[0] += pixel[0] * kernel[a][b]
                acc[1] += pixel[1] * kernel[a][b]
                acc[2] += pixel[2] * kernel[a][b]

        draw.point((x, y), (int(acc[0]), int(acc[1]), int(acc[2])))


output_image.save("output.png")

img = cv.imread("output.png")

cv.namedWindow("output.png", cv.WINDOW_NORMAL)
cv.resizeWindow("output.png", 800, 800)

cv.imshow("output.png", img)
cv.waitKey(0)
