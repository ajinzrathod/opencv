import cv2 as cv
import face_recognition
import os


# Setting path of images
path = 'images/'
images = []
classNames = []
myList = os.listdir(path)

for cl in myList:
    currImg = cv.imread(f'{path}/{cl}')
    images.append(currImg)

    # Remove extension
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv.cvtColor(img, cv. COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncodings(images)
print(len(encodeListKnown))
