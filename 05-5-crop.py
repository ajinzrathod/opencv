import cv2


originalImage = cv2.imread("resources/1.jpg")

# Getting Shape of Image
print(originalImage.shape)

# Showing Original Image
cv2.imshow("Original Image", originalImage)

# Cropping Image
croppedImage = originalImage[0: 200, 200: 300]

# Showing Cropped Image
cv2.imshow("Cropped Image", croppedImage)

# Waiting for key press
cv2.waitKey(0)
