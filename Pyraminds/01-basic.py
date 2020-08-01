import cv2 as cv
import imutils
from matplotlib import pyplot as plt


if __name__ == '__main__':
    img = cv.imread("../resources/1.jpg")

    img = imutils.resize(img, width=480)

    lower1 = cv.pyrDown(img)
    lower2 = cv.pyrDown(lower1)
    lower3 = cv.pyrDown(lower1)

    upper1 = cv.pyrUp(lower3)
    upper2 = cv.pyrUp(upper1)
    upper3 = cv.pyrUp(upper2)

    images = [lower1, lower2, lower3,
              upper1, upper2, upper3]

    titles = ["lower1", "lower2", "lower3",
              "upper1", "upper2", "upper3"]

    for x in range(len(images)):
        if x < 3:
            cv.imwrite('lower' + str(x) + '.jpg', images[x])
        else:
            cv.imwrite('upper' + str(x) + '.jpg', images[x])
        images[x] = cv.cvtColor(images[x], cv.COLOR_BGR2RGB)
        plt.subplot(2, 3, x + 1), plt.imshow(images[x], 'gray')
        plt.title(titles[x])

    plt.show()

    # for x in range(len(images)):
    #     cv.imshow(str(x), images[x])
    # cv.waitKey()
