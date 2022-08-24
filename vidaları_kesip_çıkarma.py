import cv2
import os
import numpy as np

img = cv2.imread("vida.jpeg",0)

blur = cv2.medianBlur(img,5)

ret,thresh = cv2.threshold(blur,100,255,cv2.THRESH_BINARY)
matris = np.ones((5, 5), np.uint8)
thresh = cv2.dilate(thresh, matris , iterations = 2)
# cv2.imshow("threshold",thresh)

mask_inv = cv2.bitwise_not(thresh)

contours, hierarchy = cv2.findContours(mask_inv,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

dizi = []

for i in contours:
    
    x1,y1,w,h = cv2.boundingRect(i)
    x2 = x1+w
    y2 = y1+h
    # cv2.rectangle(img, (x1, y1), (x2, y2), (0,0,255),1)
    if w>40 and h>40:
        kes = img[y1:y2, x1:x2]
        dizi.append(kes)
        cv2.waitKey(0)
for j in range(1,len(dizi)):
    os.chdir("C:/Users/Mustafa/Desktop/Python/OpenCV/vida")
    #yeni yuz klasörü açtım ve orataya gittim
    
    cv2.imwrite(f"vida{j}.jpg",dizi[j])
    #yuz klasörünün içine yüzleri yazdırdım
image2 = cv2.imread("vida.jpeg")
img2 = image2[800:1027,1150:1377]
cv2.imshow("kes",img2)
cv2.waitKey(0)
cv2.drawContours(img, contours, -1,(255,0,0),1)  
cv2.destroyAllWindows()                                 