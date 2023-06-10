import cv2
from PIL import Image
import numpy as np

img=cv2.imread("Resources/lambo.png")
img2=cv2.imread("Resources/dog.png")
img3=cv2.imread("Resources/tree.png")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imblur=cv2.GaussianBlur(img_gray,(7,7),0)
imcanny=cv2.Canny(img,100,100)
kernel = np.ones((1, 1), np.uint8)
imgd=cv2.dilate(imcanny,kernel,iterations=1)
imge=cv2.erode(imgd, kernel, iterations=1)
imcrop=img[0:200,200:400]


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
cv2.imwrite("temp/assign2_Original image.png",img)

imresize1=cv2.resize(img,(250,200))
imresize2=cv2.resize(img2,(250,200))
imresize3=cv2.resize(img3,(250,200))

mergeimg=np.hstack((imresize1,imresize2,imresize3))
cv2.rectangle(img, (0, 0), (50, 100), (0,255,0), 3)

cv2.imshow("Rectangle image",img)
cv2.imshow("Merged image",mergeimg)
cv2.waitKey(0)

cv2.imwrite("temp/assign2_Gray image.png",img_gray)
cv2.imwrite("temp/assign2_Blur image.png",imblur)
cv2.imwrite("temp/assign2_Canny image.png",imcanny)
cv2.imwrite("temp/assign2_Dilation image.png",imgd)
cv2.imwrite("temp/assign2_Eroded image.png",imge)
cv2.imwrite("temp/assign2_Crop image.png",imcrop)
cv2.imwrite("temp/assign2_Small image.png",imresizesm)
cv2.imwrite("temp/assign2_Fullscreen image.png",imresizefs)
cv2.imwrite("temp/assign2_Rectangle image.png",img)
cv2.imwrite("temp/assign2_Merged image.png",mergeimg)