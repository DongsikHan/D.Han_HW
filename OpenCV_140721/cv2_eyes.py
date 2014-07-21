import cv2

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('faces.jpg')

eyes = eye_cascade.detectMultiScale(img, 1.2, 5)

for (x, y, w, h) in eyes:
	cv2.rectangle(img, (x,y), (x+h, y+h), (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
