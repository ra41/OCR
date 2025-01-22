import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# # load the image from the path
img1 = cv2.imread('img1.jpg')
# converted BGR to RGB(pytesseract acceptable)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

# detect text on the image and display it
print(pytesseract.image_to_string(img1))

# # for character recognition

# # Obtain the height and width for each image 3rd value is not needed
# h1Img, w1Img, none1 = img1.shape
# # print(img1.shape)
# #
# # # Convert images into bounding box values: x, y, width and height
# boxes = pytesseract.image_to_boxes(img1)
# # print(boxes)
# for b in boxes.splitlines():
#     # print(b)
#     b = b.split(' ')
#     # print(b)
#     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#     cv2.rectangle(img1, (x, h1Img-y), (w, h1Img-h), (0, 0, 255), 1)
#     # labels the detected character
#     cv2.putText(img1, b[0], (x, h1Img-y+25), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (50, 50, 255), 2)

# # # # display the image
# cv2.imshow('image 1', img1)

# # delay
# cv2.waitKey(0)

# words detection
h1Img, w1Img, none1 = img1.shape
boxes = pytesseract.image_to_data(img1)
# print(boxes)
for count, b in enumerate(boxes.splitlines()):

    if count != 0:
        b = b.split()
        print(b)
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img1, (x, y), (w+x, h+y), (0, 0, 255), 1)
            # # labels the detected character
            cv2.putText(img1, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (50, 50, 255), 2)

# display the image
cv2.imshow('image 1', img1)

# delay
cv2.waitKey(0)