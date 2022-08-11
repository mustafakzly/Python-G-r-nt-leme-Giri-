import cv2

img = cv2.imread('moon.jpg')
#Resmi okuduk
cols,rows, _ = img.shape
#Satır ve sütün sayısını bulduk
olcek = 50
#bir ölçek belirledik ne kadar oranda fotoğrafı küçülteceğinize göre değiştirebilirsiniz.
yukseklik = int(rows* olcek/100)
#yeni oluşacak resim için satır yani yükseklik belirledik
genislik = int(cols * olcek/100)
#yeni oluşacak resim için sütun yani genişlik belirledik
sonuc = (yukseklik,genislik)
#burada 2sinin sonucunu tek değere atıyoruz
resize = cv2.resize(img,sonuc,interpolation = cv2.INTER_AREA)
#Resmi resize ederek boyutlandırıyoruz
cv2.imshow("resim",img)
cv2.imshow("Resim", resize)
#resimleri gösteriyoruz
cv2.waitKey(0)
#Ekranda kalması için waitKey(0) veriyoruz
cv2.destroyAllWindows()
