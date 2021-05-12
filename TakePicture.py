import cv2
webcam = cv2.VideoCapture(0)
return_value, image = webcam.read()
cv2.imwrite("Picture.png", image)
del(webcam)
