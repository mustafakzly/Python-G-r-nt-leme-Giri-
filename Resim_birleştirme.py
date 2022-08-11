import cv2
import numpy as np

img = cv2.imread('merdiven.jpg')
img2 = cv2.imread('moon.jpg')
#Resimleri Okuyoruz.
cv2.namedWindow('dikey',cv2.WINDOW_NORMAL)
cv2.namedWindow('yatay',cv2.WINDOW_NORMAL)
#Açıldığında boyutlanabilir olması için WINDOW_NORMAL yazıyoruz.
dikeyImg = np.vstack((img,img2))
#numpy kütüphanesinden vstack ile resimleri alt alta ekliyoruz.
yatayImg = np.hstack((img,img,img))
#numpy kütüphanesinden hstack ile resimleri yan yana ekliyoruz.
cv2.imshow('dikey', dikeyImg)
cv2.imshow('yatay', yatayImg)
#resimleri göstertiyoruz
cv2.waitKey(0)
#Ekranda kalması için waitKey(0) veriyoruz
cv2.destroyAllWindows()