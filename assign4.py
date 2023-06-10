import cv2
from PIL import Image
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img=cv2.imread("Resources/Group.jpeg.jpg")

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imblur=cv2.GaussianBlur(img_gray,(7,7),0)
imcanny=cv2.Canny(img,100,100)
kernel = np.ones((1, 1), np.uint8)
imgd=cv2.dilate(imcanny,kernel,iterations=1)
imge=cv2.erode(imgd, kernel, iterations=1)
imcrop=img[50:200,:400]


#Resize to smaller
imresizesm=cv2.resize(img,(150,100))
#Resize to screen size
imresizefs=cv2.resize(img,(1600,800))

cv2.imshow("Original image",img)
cv2.imshow("Gray image",img_gray)
cv2.imshow("Blur image",imblur)
cv2.imshow("Canny image",imcanny)
cv2.imshow("Dilation image",imgd)
cv2.imshow("Eroded image",imge)
cv2.imshow("Crop image",imcrop)
cv2.imshow("Small image",imresizesm)
cv2.imshow("Fullscreen image",imresizefs)
cv2.waitKey(0)


cv2.imwrite("temp/assign4_Original image.png",img)
cv2.imwrite("temp/assign4_Gray image.png",img_gray)
cv2.imwrite("temp/assign4_Blur image.png",imblur)
cv2.imwrite("temp/assign4_Canny image.png",imcanny)
cv2.imwrite("temp/assign4_Dilation image.png",imgd)
cv2.imwrite("temp/assign4_Eroded image.png",imge)
cv2.imwrite("temp/assign4_Crop image.png",imcrop)
cv2.imwrite("temp/assign4_Small image.png",imresizesm)
cv2.imwrite("temp/assign4_Fullscreen image.png",imresizefs)


faces=face_cascade.detectMultiScale(img_gray,1.01,33)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Detected Faces",img)
cv2.waitKey(0)

cv2.imwrite("temp/assign4_Detected image.png",img)