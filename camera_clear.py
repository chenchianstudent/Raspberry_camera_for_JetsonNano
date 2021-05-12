import cv2
def getimageVar(imgpath):
    image = cv2.imread(imgpath)
    img2gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imwrite("CSICamera33.png", img2gray)
    imageVar = cv2.Laplacian(img2gray, cv2.CV_64F).var()
    #cv2.imwrite("CSICamera22.png", imageVar)
    return imageVar
image = getimageVar("aaa.jpg")
print(image)
