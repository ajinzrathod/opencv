try:
    from fourSides import fourSides
    import cv2 as cv
    import numpy as np
    import math
    import autoCV
    from matplotlib import pyplot as plt
except ModuleNotFoundError as e:
    print(e)
    exit(1)

# realImg = cv.imread("../resources/shapes2.png")
# realImg = cv.imread("../resources/shapes5.png")
# realImg = cv.imread("../resources/circle4.png")
# realImg = cv.imread("../resources/smarties.png")
realImg = cv.imread("../resources/shapes.png")

if realImg is None:
    print("No such Image")
    exit(1)

imageW, _, _ = realImg.shape

img = cv.cvtColor(realImg, cv.COLOR_BGR2GRAY)
img = cv.GaussianBlur(img, (5, 5), 1)
# img = cv.cvtColor(realImg, 6)

# kernel = np.ones((5, 5), np.uint8)
# img = cv.dilate(img, kernel, iterations=1)

img = autoCV.autoCanny(img)

contours = autoCV.findAndDrawContours(img, realImg, (255, 255, 255), 1, 100)
# Iterating through each contour
for cnt in contours:
    # cv.imshow("d", realImg)
    # cv.waitKey()
    if cv.contourArea(cnt) > 100:
        # Calculating Perimeter
        peri = cv.arcLength(cnt, True)
        approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
        if len(approx) > 5:

            approx = cv.approxPolyDP(cnt, 0.002 * peri, True)

            # Finding x, y co-ordinate and width, height of each contour
            x, y, w, h = cv.boundingRect(approx)
            print("x, y, w, h, len: ", x, y, w, h, len(approx))

            # Drawing Rectangle on each contour
            color1 = (255, 255, 255)  # Outer Rectangle color
            color2 = (0, 0, 0)  # Inner Rectangle color

            cv.rectangle(realImg, (x, y), (x + w, y + h), color1, 3)
            cv.rectangle(realImg, (x - 2, y - 2), (x + w + 2, y + h + 2), color2, 2)

            # Calculating Center of each Contour
            wCenter = int(x + (w / 2))
            hCenter = int(y + (h / 2))
            center = (wCenter, hCenter)

            # Drawing a small circle at center
            cv.circle(realImg, center, 1, (255, 255, 255), 5)

            distFromCenter = []
            distFromNextContour = []
            i = 0
            prev = None

            # 4 Sides Quadrant Std

            textPoints1, textPoints2, textPoints3, textPoints4, std1, std2, std3, std4, allS = fourSides(approx, wCenter, hCenter, realImg, w, h)

            for point in approx:

                # Check if List is empty
                if i == 0:
                    pass
                else:
                    diff1 = point[0][0] - prev[0][0]
                    diff2 = point[0][1] - prev[0][1]
                    distFromNextContour.append((diff1, diff2))
                prev = point
                i += 1

                # Converting to Tuple because cv.circle takes tuple
                point = tuple(point.flatten())

                # PLotting Small circles in each shape
                cv.circle(realImg, point, 1, (255, 0, 0), 3)

                # Calculating Distance from center points
                dist = math.sqrt(((point[0]-center[0])**2) + ((point[1]-center[1])**2))

                # Adding each distance in list
                distFromCenter.append(dist)

            # Finding Standard Deviation From Center
            stdFromCenter = float(np.std(distFromCenter))
            stdFromCenterF = stdFromCenter

            # Finding Standard Deviation Between 2 close points
            stdBetween2Points = float(np.std(distFromNextContour))

            # Putting Std Dev Text on Image
            stdFromCenter = "Cen " + str(round(stdFromCenter, 2))
            stdBetween2Points = "Bet: " + str(round(stdBetween2Points, 2))

            cv.putText(realImg, stdFromCenter, (x, y + 20),
                       cv.FONT_HERSHEY_DUPLEX, 0.9, (255, 0, 0), 1)
            # cv.putText(realImg, stdBetween2Points, (x, y + h),
            #            cv.FONT_HERSHEY_DUPLEX, 0.8, (127, 127, 127), 1)

            # Black and White Image for Better Readability
            print(imageW / 800)

            perfect = "No Perf"

            # below line similar to cicle but not circle
            if (stdFromCenterF < 3 or allS < 1) and len(approx) > 20:
            # if (stdFromCenterF < 3 and allS < 1) and len(approx) > 25:  # More Accurate
                if allS < 0.25:
                    perfect = "Perfect"
                cv.putText(img, stdFromCenter, (x + w // 2, y + h + 20),
                           cv.FONT_HERSHEY_DUPLEX, .5, (127), 1)
                # cv.putText(img, stdBetween2Points, (x, y + h),
                #            cv.FONT_HERSHEY_DUPLEX, imageW / 800, (255), 2)

                if textPoints1 is not None:
                    cv.putText(realImg, std1, textPoints1, cv.FONT_HERSHEY_DUPLEX,
                               .5, (0, 0, 0), 1)
                if textPoints2 is not None:
                    cv.putText(realImg, std2 + ",", textPoints2, cv.FONT_HERSHEY_DUPLEX,
                               .5, (0, 0, 0), 1)
                if textPoints3 is not None:
                    cv.putText(realImg, std3 + ",", textPoints3, cv.FONT_HERSHEY_DUPLEX,
                               .5, (0, 0, 0), 1)
                if textPoints4 is not None:
                    cv.putText(realImg, std4, textPoints4, cv.FONT_HERSHEY_DUPLEX,
                               .5, (0, 0, 0), 1)

                cv.putText(realImg, str(allS) + perfect, (x + w // 4, y + h + 10), cv.FONT_HERSHEY_DUPLEX,
                           .5, (255, 255, 75), 1)
                print(" <CIRCLE FOUND>")
# gray = cv.cvtColor(realImg, cv.COLOR_BGR2RGB)
# plt.subplot(1, 1, 1), plt.imshow(img, 'gray')

realImg = cv.cvtColor(realImg, cv.COLOR_BGR2RGB)
plt.subplot(1, 1, 1), plt.imshow(realImg)

plt.show()
