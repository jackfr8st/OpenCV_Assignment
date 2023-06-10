from PIL import Image
import cv2
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'
im=Image.open('assignment3/cars/try4.jpg')
left = 511
top = 251
right = 1130
bottom = 460
im=im.rotate(-9)
im=im.crop((left,top,right,bottom))
im.save('assignment3/noplate/plate4.jpg')

# mser = cv2.MSER_create()
# kernel = np.ones((1, 1), np.uint8)
img=cv2.imread('assignment3/noplate/plate4.jpg')
imgg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,imgb=cv2.threshold(imgg,110,230,cv2.THRESH_BINARY)
# imgd=cv2.dilate(imgb, kernel, iterations=3)
# imge=cv2.erode(imgd, kernel, iterations=3)
# vis = img.copy()
# regions = mser.detectRegions(imgg)
# hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions[0]]
# cv2.polylines(vis, hulls, 1, (0,255,0)) 
# cv2.imshow("processed image",img)
# cv2.imshow("processed vis image",vis)

cv2.waitKey(0)
cv2.imwrite('assignment3/noplate/plate4.jpg',imgb)


def ocr_core(img):
    text=pytesseract.image_to_string(img)
    return text


print(ocr_core(imgb))