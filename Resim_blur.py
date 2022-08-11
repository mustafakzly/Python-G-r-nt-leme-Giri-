import cv2 
  

img = cv2.imread('merdiven.jpg')
cv2.imshow("resim",img)
#Resmi okuduk ve resmi gösterdik
blur = cv2.blur(img,(5,5))
#blur komutu resimi bulanıklaştırmak için kullanılır
cv2.imshow('blur',blur)
#Resmi gösterdik
gausBlur = cv2.GaussianBlur(img, (5,5),0) 
#GaussianBlur komutu resimi bulanıklaştırmak için kullanılır
cv2.imshow('Gaus blur', gausBlur)
#Resmi gösterdik
medBlur = cv2.medianBlur(img,5)
#medianBlur komutu resimi bulanıklaştırmak için kullanılır
cv2.imshow('Media blur', medBlur)
#Resmi gösterdik
cv2.waitKey(0)
#Ekranda kalması için waitKey(0) veriyoruz
cv2.destroyAllWindows()