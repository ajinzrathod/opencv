import cv2 as cv
import face_recognition
from matplotlib import pyplot as plt


if __name__ == '__main__':
    ajinImg1 = face_recognition.load_image_file('../resources/1.jpg')
    # ajinImg1 = cv.cvtColor(ajinImg1, 4)

    faceLoc = face_recognition.face_locations(ajinImg1)[0]
    encodeAjin1 = face_recognition.face_encodings(ajinImg1)[0]
    cv.rectangle(ajinImg1, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]),
                 (255, 0, 255), 2)

    ajinImg2 = face_recognition.load_image_file('../resources/3.png')
    # ajinImg2 = cv.cvtColor(ajinImg2, 4)

    faceLoc = face_recognition.face_locations(ajinImg2)[0]
    encodeAjin2 = face_recognition.face_encodings(ajinImg2)[0]
    cv.rectangle(ajinImg2, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]),
                 (255, 0, 255), 2)

    results = face_recognition.compare_faces([encodeAjin1], encodeAjin2)
    faceDistance = face_recognition.face_distance([encodeAjin1], encodeAjin2)
    print(results, faceDistance)

    images = [ajinImg1, ajinImg2]

    for x in range(len(images)):
        plt.subplot(1, 2, x + 1), plt.imshow(images[x])
    plt.show()
