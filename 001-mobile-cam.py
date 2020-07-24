import requests
import cv2
import numpy as np

url = "http://192.168.0.100:8080/video"

# cap.set(3, 640)  # width
# cap.set(4, 480)  # height
# cap.set(10, 50)  # brightness

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)

    img = cv2.imdecode(img_arr, -1)

    # cv2.set(3, 640)
    # cv2.set(4, 480)

    cv2.imshow("Android Camera", img)

    if cv2.waitKey(1) == 27:
        break
