import cv2
import pytesseract


img_cv = cv2.imread(r'img2.png')

img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
text = pytesseract.image_to_string(img_rgb)

print(repr(text))
result = text.split("\n")

f = open("list.txt", 'a')

for x in result:
    f.write(x)
    f.write("\n")

f.close()
