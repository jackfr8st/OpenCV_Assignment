from PIL import Image
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'
im=Image.open('assignment3/cars/try3.jpg')
left = 333
top = 315
right = 570
bottom = 370
im=im.crop((left,top,right,bottom))
im.save('assignment3/noplate/plate3.jpg')

img=cv2.imread('assignment3/noplate/plate3.jpg')
imgg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,imgb=cv2.threshold(imgg,110,230,cv2.THRESH_BINARY)
cv2.imshow("processed image",imgb)
cv2.waitKey(0)
cv2.imwrite('assignment3/noplate/plate3.jpg',imgb)


def ocr_core(img):
    text=pytesseract.image_to_string(img)
    return text
print(ocr_core(imgb))