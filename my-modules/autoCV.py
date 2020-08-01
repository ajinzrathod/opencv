"""
`Github: <https://github.com/ajinzrathod/>`
+--------------------------------+
| Make sure ``cv2`` is installed |
+--------------------------------+

Import Module::

  >>> import autoCV


`Resize Image`
Resize Image: autoCV.resizeImg(img, width, height)
-----------------------------------------------
Resize image with default Ratio::

  >>> img = autoCV.resizeImg(img)

Resize image with custom Ratio::

  >>> img = autoCV.resizeImg(img, width, height)


`Detect Objects`
To Detect Shapes: autoCV.detectObject.drawShapes(contours, realImg, name=False)
-------------------------------------------------------------------------------
Show Shapes::

  >>> autoCV.detectObject.drawShapes(contours, realImg)

Draw Shapes and Name Them::

  >>> autoCV.detectObject.drawShapes(contours, realImg, name=True)

Checking if contour is circle or not::

  >>> autoCV.detectObject.isCircle(cnt, realImg)


`Auto Canny Edges`
Find Edges using Canny: autoCV.autoCanny(img, sigma)
----------------------------------------------------
Find Edges::

  >>> img = autoCV.autoCanny(img)

Find edge with Sigma::

  >>> img = autoCV.autoCanny(img, sigma)


`Find And Draw Contours`
Find And Draw Contours: findAndDrawContours(edgedImg,
                                             originalImg
                                             color=(255, 255, 255
                                             thickness=2
                                             area=500):
-------------------------------------------------------
Drawing Contours::

  >>> img = autoCV.findAndDrawContours(edgedImg, originalImg)

Drawing Contours with custom settings::

  >>> img = autoCV.findAndDrawContours(edgedImg, originalImg,
                                      color, thickness, area)

"""

try:
    import cv2
    import numpy as np
    from math import sqrt
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


def autoCanny(image, sigma=0.33, retTh=False):
    """
    autoCanny(img, sigma=0.33) -> Image with Edges and threshold values
    |   @brief: Finds edges of Image
    |
    |
    |   Parameters Explained
    |   -------------------
    |   @param(1) image: inputs a image
    |   @param(2) sigma value (optional) [Default: 0.33]
    |   @param(3) Returns the value of threshold used in Canny if set True
    |             (optional)[Default: False]
    |
    |
    |   Return Value
    |   ------------
    |   Returns a edged Image and threshold values
    """

    # compute the median of the single channel pixel intensities
    v = np.median(image)
    std = np.std(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v) - (std * .75))
    upper = int(min(255, (1.0 + sigma) * v) + std)

    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    if retTh:
        return edged, lower, upper
    else:
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
                        area = 500) -> Contours of Img

    |   @brief: Draws Contours in Original Image and return Contours
    |
    |
    |   Parameters Explained
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

    # RETR_EXTERNAL = 0, CHAIN_APPROX_NONE = 1, CHAIN_APPROX_SIMPLE = 2

    contours, hierchy = cv2.findContours(edgedImg, 0, 2)  # Finding Contours

    for cnt in contours:
        if cv2.contourArea(cnt) > area:
            cv2.drawContours(originalImg, contours, -1, color, thickness)
    return contours


class detectObject:
    """
    This is a Class that detectObjects.
    To detect Shapes use::

      >>> autoCV.detectObject.drawShapes(contours, realImg,
                                         color=(255, 255, 255),
                                         thickness=4,
                                         minArea=500,
                                         name=False,
                                         fontScale=.75)

    To detect Circle use::

     >>> autoCV.detectObject.isCircle(cnt, realImg)

    """
    def __init__(self):
        print("Init called")

    def findShapes():
        print("Find Shapes called")

    def stdFourSides(approx, xCen, yCen, realImg, w, h):
        """
        stdFourSides(approx, wCen, hCen, realImg, w, h)
        -> Std Deviation of (Std Deviation of 4 Quadrants)

        |   @brief: Gives std of (std of 4 Quadrants)
        |
        |
        |   Parameters Explained
        |   --------------------
        |   @param(1): approx
        |           approximation found from ``approxPolyDP``
        |   @param(2): xCen
        |           x Co-ordinate of center of width
        |   @param(3): yCen
        |           y Co-ordinate of center of height
        |   @param(4): realImg
        |           Image on which we want to process
        |   @param(5): w
        |           width of current contour
        |   @param(6)
        |           height of current contour
        |
        |
        |   Return Value
        |   ------------
        |   Std Deviation of (Std Deviation of 4 Quadrants)
        """

        qd1, qd2, qd3, qd4 = [], [], [], []
        txtPt1, txtPt2, txtPt3, txtPt4 = (None for i in range(4))

        for point in approx:

            # Straightening Array and turning to Tuple
            point = tuple(point.ravel())

            # Calculating distance from center
            distance = sqrt(((point[0]-xCen)**2) + ((point[1]-yCen)**2))

            # Quadrant I
            if point[0] >= xCen and point[1] <= yCen:
                qd1.append(distance)

            # Quadrant II
            elif point[0] < xCen and point[1] < yCen:
                qd2.append(distance)

            # Quadrant III
            elif point[0] <= xCen and point[1] >= yCen:
                qd3.append(distance)

            # Quadrant IV
            elif point[0] > xCen and point[1] > yCen:
                qd4.append(distance)

        # Returning std of (std of all Quadrants)
        return np.std((np.std(qd1), np.std(qd2), np.std(qd3), np.std(qd4)))

    def isCircle(cnt, realImg):
        """
        ``NOTE: cnt is NOT list of contours, it is only one contour``

        isCircle(cnt, realImg) -> True if cnt is Circle else False

        |   @brief: Checks if contour is Circle or not
        |
        |
        |   Parameters Explained
        |   --------------------
        |   @param(1): cnt
        |           One contour
        |   @param(2): realImg
        |           Image on which we want to Detect
        |
        |
        |   Return Value
        |   ------------
        |   True if cnt is Detected as Circle, else False
        """

        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.002 * peri, True)

        # Finding x, y co-ordinate and width, height of each contour
        x, y, w, h = cv2.boundingRect(approx)

        # Calculating Center of each Contour
        xCen = int(x + (w / 2))
        yCen = int(y + (h / 2))
        center = (xCen, yCen)

        # Drawing a small circle at center
        # cv2.circle(realImg, center, 1, (255, 255, 255), 5)

        distFromCenter = []

        # Gives Std Deviation of (Std Deviation of 4 Quadrants)
        fourStd = detectObject.stdFourSides(approx, xCen, yCen, realImg, w, h)

        for point in approx:
            # Converting to Tuple because cv2.circle takes tuple
            point = tuple(point.flatten())

            # Calculating Distance from center points
            dist = sqrt(((point[0]-center[0])**2) + ((point[1]-center[1])**2))

            # Adding each distance in list
            distFromCenter.append(dist)

        # Finding Standard Deviation From Center
        stdFromCenter = float(np.std(distFromCenter))

        # Less Perfect Circle
        # if (stdFromCenter < 3 or fourStd < 1) and len(approx) > 20:

        # Perfect Circle
        if (stdFromCenter < 3 and fourStd < 1) and len(approx) > 25:
            return True
            # # To Check More Perfect Circle
            # if fourStd < 0.25:
            #     return True
            # else:
            #     return True

        return False

    def drawShapes(contours, realImg, minArea=500, name=False):
        """
        drawShapes(contours, realImg, minArea=500, name=False)

        |   @brief: Draws rectangle where any contour is Found
        |
        |
        |   Parameters Explained
        |   --------------------
        |   @param(1): contours
        |           Contours of the Image
        |   @param(2): realImg
        |           Image on which we will want to Draw
        |   @param(3): Name the object
        |           If set to True, name of the object will also be shown
        |           (optional) [Default: False]
        |
        |   Return Value
        |   ------------
        |   None
        """

        # Getting Shape of Real Image
        realH, realW, _ = realImg.shape

        thickness = realW // 275  # Setting Thickness
        fontScale = realH / 1000  # Setting fontScale

        if not contours:
            print("No Contours Found")
        for cnt in contours:
            cntArea = cv2.contourArea(cnt)  # Getting Area
            # i = -1
            # i += 1
            # color = (0, 255, 0)

            if cntArea < minArea:
                continue

            # Drawing contours
            # cv2.drawContours(realImg, [cnt], i, color, 3)

            # Finding Perimeters of each cnt
            peri = cv2.arcLength(cnt, True)  # True for Closed Shapes
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

            # Getting x, y co-ordinates and width, height of each cnt
            x, y, w, h = cv2.boundingRect(approx)

            # Making Black Rectangle around each contour
            cv2.rectangle(realImg,
                          (x - thickness, y - thickness),
                          (x + w + thickness, y + h + thickness),
                          (0, 0, 0), thickness)

            # Making White Rectangle around each contour
            cv2.rectangle(realImg, (x, y), (x + w, y + h),
                          (255, 255, 255), thickness // 2)

            if not name:
                continue

            corners = len(approx)  # Counting Corners
            objType = None

            if corners == 3:
                objType = "Triangle"

            elif corners == 4:
                aspRatio = w / float(h)
                if aspRatio > 0.9 and aspRatio < 1.1:
                    objType = "Square"
                else:
                    objType = "Rectangle"

            elif corners == 5:
                objType = "Pentagon"

            elif corners == 6:
                objType = "Hexagon"

            elif corners > 7:
                if detectObject.isCircle(cnt, realImg):
                    objType = "Circle"

            if objType is None:
                objType = "Not Found"

            if thickness == 1:
                thickness = 2

            # Setting FontFace
            fontFace = cv2.FONT_HERSHEY_DUPLEX

            # Getting Shape of Image
            h2, _, _ = realImg.shape

            # If Image Height is too Small, increase fontScale
            if h2 < 300:
                fontScale += 0.04
            elif h2 < 400:
                fontScale += 0.02

            textBgHeight = int(fontScale * 40)
            k = 0
            
            if h2 > 500:
                k = textBgHeight // 3

            # Copying the contents where we want to write text
            sub_img = realImg[y+h: y+h+textBgHeight+k, x:x+w]

            # Create a new black image with same shape
            rect = np.zeros(sub_img.shape, dtype=np.uint8)

            # Creating a new transparent image from
            # `copied image(sub_img)` and `black image`
            res = cv2.addWeighted(sub_img, .25, rect, .5, 1.0)

            # Replacing the part of realImg
            realImg[y+h: y+h+textBgHeight+k, x: x+w] = res

            # Putting White Text on Image
            cv2.putText(realImg, objType, (x, y + h + textBgHeight - 5),
                        fontFace, fontScale, (255, 255, 255), thickness * 2)

            # # Putting Black Text on Image
            cv2.putText(realImg, objType, (x, y + h + textBgHeight - 5),
                        fontFace, fontScale, (0, 0, 0), thickness // 2)

if __name__ == '__main__':
    pass
