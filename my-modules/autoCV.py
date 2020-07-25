"""
`Github: <https://github.com/ajinzrathod/>`
+--------------------------------+
| Reshapes image using cv2       |
| Make sure ``cv2`` is installed |
+--------------------------------+

Import Module::

  >>> import autoCV


`Resize Image`
Resize Image -> ars.resizeImg(img, width, height)
-------------------------------------------------
Resize image with default Ratio::

  >>> img = autoCV.resizeImg(img)

Resize image with custom Ratio::

  >>> img = autoCV.resizeImg(img, width, height)


`Auto Canny Edges`
Find Edges using Canny -> autoCV.autoCanny(img, sigma)
------------------------------------------------------
Find Edges::

  >>> img = autoCV.autoCanny(img)

Resize image with Sigma::

  >>> img = autoCV.resizeImg(img, sigma)
"""

try:
    import cv2
    import numpy as np
except ModuleNotFoundError as e:
    print("ModuleNotFoundError:", e)
    # raise


def resizeImg(img, aspectW=480, aspectH=360):
    """
    resizeImg(img, aspectW=480, aspectH=360) -> A resized Image
    |   @brief: Resizes the image according to Best aspect Ratio
    |
    |
    |   Parameters Explained
    |   -------------------
    |   @param(1)     img: inputs a image
    |   @param(2) aspectW: sets width according to aspectW (optional)
    |   @param(3) aspectH: sets height according to aspectH (optional)
    |
    |   Default @param aspectW: 360
    |   Default @param aspectH: 480
    |
    |
    |   Return Value
    |   ------------
    |   Returns a resized image
    """

    # Finding width and height of original Image
    w, h = img.shape[0], img.shape[1]

    wScale = hScale = 1  # Default Vales

    # Changing only is size is more than aspect Range
    if w > aspectW or h > aspectH:
        wScale = w / aspectW
        hScale = h / aspectH

    # Finding max of widthScale and heightScale
    scale = int(max(wScale, hScale))

    # Resizing image that fits the Scale using cv2
    img = cv2.resize(img, (h // scale, w // scale))

    return img


def autoCanny(image, sigma=0.33):
    """
    autoCanny(img, sigma=0.33) -> Image with Edges
    |   @brief: Finds edges of Image
    |
    |
    |   Paramters Explained
    |   -------------------
    |   @param(1) image: inputs a image
    |   @param(2) sigma value (optional) [Default: 0.33]
    |
    |
    |   Return Value
    |   ------------
    |   Returns a edged Image
    """

    # compute the median of the single channel pixel intensities
    v = np.median(image)
    std = np.std(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v) - (std * .75))
    upper = int(min(255, (1.0 + sigma) * v) + std)

    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    return edged


def findAndDrawContours(edgedImg,
                        originalImg,
                        color=(255, 255, 255),
                        thickness=2,
                        area=500):
    """
    findAndDrawContours(edgedImg,
                        originalImg,
                        color=(255, 255, 255),
                        thickness=2,
                        area = 500) -> Contour Img

    |   @brief: Draws Contours in Original Image and return Contours
    |
    |
    |   Paramters Explained
    |   -------------------
    |   @param(1): edgedImg
    |           Inputs a Edged image
    |   @param(2): originalImg
    |           Inputs a image on which Contours to be drawn
    |   @param(3): color
    |           Color of Border
    |           (optional) [Default: White]
    |   @param(4): thickness
    |           Thickness of Border
    |           (optional) [Default: 2]
    |   @param(5): area
    |           Draw Contour if area greater than given area
    |           (optional)[Default: 500]
    |
    |
    |   Return Value
    |   ------------
    |   Returns Contours of Image
    """

    # RETR_EXTERNAL retrieves all contours without
    # any hierarchical relationships

    # RETR_EXTERNAL = 0, CHAIN_APPROX_NONE = 1

    contours, hierchy = cv2.findContours(edgedImg, 0, 1)  # Finding Contours

    for cnt in contours:
        if cv2.contourArea(cnt) > area:
            cv2.drawContours(originalImg, contours, -1, color, thickness)

    # returns contours of Image
    cv2.imshow("Imag", originalImg)
    cv2.waitKey(0)
    return contours


if __name__ == '__main__':
    pass
